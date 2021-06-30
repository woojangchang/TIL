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
- `pip install PyMuPDF==1.18.14`
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

# Unix

- https://replit.com
  - Bash(Linux 환경)를 웹에서 사용 가능

- `!!` : 전에 실행했던 cmd를 실행
- `^a^b` : 전에 실행했던 cmd에서 a를 b로 대체
- `grep <패턴> <파일이름>` : 패턴에 맞는 폴더/파일 목록 출력

```bash
# 예시
# 디렉토리 내 폴더/파일 목록 출력
ls -l

# 디렉토리 내 wiki라는 단어가 포함된 폴더/파일 목록 출력
!! | grep wiki

# 디렉토리 내 python 단어가 포함된 폴더/파일 목록 출력
^wiki^python
```

- `sed <옵션> <명령어> <파일 이름>` : 문자열의 특정 내용을 변경하거나 줄단위 데이터를 추출할 때
  - 명령어 `s/a/b/` : a 표현을 b로 바꾼다.
  - 파일 이름 `file1 > file2` : file1을 수정하여 file2로 저장한다. (`> file2`를 쓰지 않으면 단순 출력)

# Log

- `pip install logging`
- `pip install colorlog`

