import markdown
from bs4 import BeautifulSoup
from googletrans import Translator
import html2text  # HTML を Markdown に変換するために必要

# README.mdを読み込む
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

# MarkdownをHTMLに変換
html_content = markdown.markdown(readme_content)

# BeautifulSoupを使ってHTMLからテキストを抽出しつつ、タグは保持
soup = BeautifulSoup(html_content, 'html.parser')

# 翻訳インスタンスの生成
translator = Translator()

def translate_element(element):
    """タグ内のテキストを翻訳する"""
    if element.string and element.string.strip():  # None もしくは空白のみのテキストを除外
        translated = translator.translate(element.string, src='en', dest='ja').text
        element.string.replace_with(translated)

# HTMLの各要素を再帰的に翻訳
for elem in soup.find_all(text=True):
    if elem.parent.name not in ['code', 'pre']:  # コードブロックは翻訳しない
        translate_element(elem)

# BeautifulSoupオブジェクトをHTML文字列に変換
translated_html = str(soup)

# html2text を使ってHTMLをMarkdownに変換
markdown_converter = html2text.HTML2Text()
markdown_converter.ignore_links = False  # リンクを保持する
translated_markdown = markdown_converter.handle(translated_html)

# 翻訳結果をREADME.ja.mdとして保存
with open('README.ja.md', 'w', encoding='utf-8') as file:
    file.write(translated_markdown)
