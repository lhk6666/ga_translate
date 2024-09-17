from googletrans import Translator

with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

translator = Translator()
translated = translator.translate(readme_content, src='en', dest='ja').text

with open('README.ja.md', 'w', encoding='utf-8') as file:
    file.write(translated)
