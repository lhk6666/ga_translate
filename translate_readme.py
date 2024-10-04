import markdown
from bs4 import BeautifulSoup
import html2text
from openai import OpenAI
from langdetect import detect
import os

openai = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')
updating_model = "gpt-4"

def gpt_translate(text):
    messages = [
        {"role": "system", "content": "You are a professional translator for the README.md file. Please overlook it when the contain is code. Do not any prefix in your reply"},
        {"role": "system", "content": "Translate English to Japanese, Japanese to English"},
        {"role": "user", "content": f"Translate the following text to Japanese or English:\n\n{text}"},
    ]
    
    response = openai.chat.completions.create(
                model=updating_model,
                messages= messages,
                temperature = 0.1
            )
    
    translated_text = response.choices[0].message.content
    print(translated_text)
    return translated_text

with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

html_content = markdown.markdown(readme_content)

soup = BeautifulSoup(html_content, 'html.parser')

def translate_element(element):
    if element.string and element.string.strip():
        translated = gpt_translate(element.string)
        element.string.replace_with(translated)

for elem in soup.find_all(text=True):
    if elem.parent.name not in ['code', 'pre']:  
        translate_element(elem)

translated_html = str(soup)
markdown_converter = html2text.HTML2Text()
markdown_converter.ignore_links = False
translated_markdown = markdown_converter.handle(translated_html)

with open(f'README.{detect(translated_markdown)}.md', 'w', encoding='utf-8') as file:
    file.write(translated_markdown)

with open(f'README.{detect(readme_content)}.md', 'w', encoding='utf-8') as file:
    file.write(readme_content)

