# Beautiful Soup

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

```python
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
```



# Camelot

PDF 파일로부터 표 추출하기

- `pip install camelot-py==0.9.0`
- ``pip install PyMuPDF==1.18.14`
- https://www.ghostscript.com/download/gsdnld.html

```python
import camelot

# pdf 파일로부터 표 추출하기
tables = camelot.read_pdf('example.pdf', pages='1, 2, 3') # 1~3페이지만
# 테이블 출력
tables[0].df
```

```python
# 엑셀파일로 저장
tables[0].to_excel('table0.xlsx')
```

