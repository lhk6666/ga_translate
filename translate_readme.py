import markdown
from bs4 import BeautifulSoup
import html2text
from openai import OpenAI
from langdetect import detect
import os

openai = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')
updating_model = "gpt-4o-mini"
history =[]

def truncate_history(history, max_history_length=5):
    if len(history) > max_history_length:
        history = history[-max_history_length:]
    return history

def gpt_translate(text):
    truncate_history(history)
    messages = [
        {"role": "system", "content": "You are a professional translator for the README.md file. Please overlook it when the contain is code or url or special name. Do not any prefix in your reply"},
        {"role": "system", "content": "Normally, Translate English to Japanese, Japanese to English"},
        {"role": "system", "content": f"Accord to the history: {history}. Keep the md file use one language"},
        {"role": "user", "content": f"Translate the following text to Japanese or English:\n\n{text}"},
    ]
    
    response = openai.chat.completions.create(
                model=updating_model,
                messages= messages,
                temperature = 0.1
            )
    
    translated_text = response.choices[0].message.content
    history.append(translated_text)
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

