import markdown
from bs4 import BeautifulSoup
import html2text
from openai import OpenAI
from langdetect import detect
import os

openai = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')
updating_model = "gpt-4o"
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
        {"role": "system", "content": f"This is the contains you already translated: {history}. Keep the md file use one language"},
        {"role": "system", "content": "However, if this text I ask you to translate is same as the language used in the previous contains, you can keep the original text"},
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

def gpt_detect_language(text):
    messages = [
        {"role": "system", "content": "You are a professional linguist."},
        {"role": "system", "content": "Your output could be: en or ja. Do not include extra text"},
        {"role": "user", "content": f"Please identify the primary language of the following text:\n\n{text}"}
    ]
    
    response = openai.chat.completions.create(
                model=updating_model,
                messages= messages,
                temperature = 0.1
            )
    
    detected_language = response.choices[0].message.content
    return detected_language

with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.readlines()

translated_content = []

for line in readme_content:
    if line.strip() and line.strip('```').strip():  
        translated_line = gpt_translate(line)
        translated_content.append(translated_line)
    else:
        translated_content.append(line) 

detected_language = gpt_detect_language(translated_content)
with open(f'README.{detected_language}.md', 'w', encoding='utf-8') as file:
    file.write("\n".join(translated_content))

detected_language = gpt_detect_language(readme_content)
with open(f'README.{detected_language}.md', 'w', encoding='utf-8') as file:
    file.write(''.join(readme_content))

