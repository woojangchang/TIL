# RE

- https://docs.python.org/3/library/re.html
- https://en.wikipedia.org/wiki/Regular_expression
- `import re`



## Characters

###  `.`

- 한 개의 임의의 문자
- 반드시 하나의 문자가 있어야 매치가 된다.

```python
r = re.compile("a.c")

r.search("abc")
# <re.Match object; span=(0, 3), match='abc'>

r.search("kkk")
# 아무런 결과도 출력되지 않는다.

r.search('ac')
# 아무런 결과도 출력되지 않는다.
```



### `?`

- `?` 앞의 문자가 없거나, 한 번만 나오는 경우 표현

```python
r = re.compile("ab?c") # ? 앞의 b가 있어도, 없어도 됨

r.search("abbc")
# 아무런 결과도 출력되지 않는다.

r.search("abc")
# <re.Match object; span=(0, 3), match='abc'>

r.search("ac")
# <re.Match object; span=(0, 2), match='ac'>
```



### `*`

- `*` 앞의 문자가 0번 이상 나오는 경우 표현

```python
r = re.compile("ab*c")

r.search("abcc")
# 아무런 결과도 출력되지 않는다.

print(r.search("ac"))      # b가 0 개
print(r.search("abc"))     # b가 1 개
print(r.search("abbbbc"))  # b가 4 개
'''
<re.Match object; span=(0, 2), match='ac'>
<re.Match object; span=(0, 3), match='abc'>
<re.Match object; span=(0, 6), match='abbbbc'>
'''
```



### `+`

- `+` 앞의 문자가 1번 이상 나오는 경우 표현

```python
r = re.compile("ab+c")

r.search("ac")
# 아무런 결과도 출력되지 않는다.

print(r.search("abc"))     # b가 1 개
print(r.search("abbbbc"))  # b가 4 개
'''
<re.Match object; span=(0, 3), match='abc'>
<re.Match object; span=(0, 6), match='abbbbc'>
'''
```



### `^`

- `^` 뒤의 문자로 시작되는 경우 표현
- 여러 문자열 포함

```python
r = re.compile("^a")

r.search("ab")
# <re.Match object; span=(0, 1), match='a'>

r.search("d a")
# 아무런 결과도 출력되지 않는다.
```

```python
r = re.compile('^abc')

print(r.search('aabc'))
print(r.search('abc'))
'''
None
<re.Match object; span=(0, 3), match='abc'>
'''
```



### `{num}`

- `{num}` 앞의 문자가 정확히 num 만큼 반복되는 경우 표현

```python
r = re.compile("ab{2}c")

print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbbbc"))
'''
None
None
<re.Match object; span=(0, 4), match='abbc'>
None
'''
```



### `{num1, num2}`

- `{num1, num2}` 앞의 문자가 num1 이상, num2 이하 반복되는 경우 표현

```python
r = re.compile("ab{2,8}c")

r.search("ac")
# 아무런 결과도 출력되지 않는다.

r.search("ac")
# 아무런 결과도 출력되지 않는다.

r.search("abc")
# 아무런 결과도 출력되지 않는다.

print(r.search("abbc"))        # b가 2개
print(r.search("abbbbbbbbc"))  # b가 8개
'''
<re.Match object; span=(0, 4), match='abbc'>
<re.Match object; span=(0, 10), match='abbbbbbbbc'>
'''

r.search("abbbbbbbbbc")
# 아무런 결과도 출력되지 않는다.
```

- num2가 생략되는 num1 이상 표현이 된다.



### `[]`

- `[]` 안에 문자를 넣으면, 그 문자 중 어떤 하나와 매치

```python
r  = re.compile("[abc]")

print(r.search("a"))
print(r.search("aaaaaaa"))
print(r.search("baac"))
print(r.search("cbaa"))
print(r.search("aBC"))
print(r.search("111"))
'''
<re.Match object; span=(0, 1), match='a'>
<re.Match object; span=(0, 1), match='a'>
<re.Match object; span=(0, 1), match='b'>
<re.Match object; span=(0, 1), match='c'>
<re.Match object; span=(0, 1), match='a'>
None
'''
```



### `[^chr]`

- `^` 뒤의 문자가 제외된 문자 매치

```python
r = re.compile("[^abc]")

r.search("a")
# 아무런 결과도 출력되지 않는다.

r.search("ab")
# 아무런 결과도 출력되지 않는다.

r.search("b")
# 아무런 결과도 출력되지 않는다.

print(r.search("d"))
print(r.search("1"))
print(r.search("X"))
'''
<re.Match object; span=(0, 1), match='d'>
<re.Match object; span=(0, 1), match='1'>
<re.Match object; span=(0, 1), match='X'>
'''
```



### `\d`

- 임의의 숫자 매치, `[0-9]`와 같음
  - `\d+` : 숫자 1개 이상

### `\D`

- 숫자를 제외한 문자 매치, `[^0-9]`와 같음



## Function

### `re.split()`

- `re.split(expression, text)` : expression을 기준으로 문자열을 나눈다.
- python 내장 함수 `text.split()`보다 강력하다.

```python
t = '1. 사과, 2. 딸기, 3. 수박'
list(map(lambda x:x.strip(', '), re.split('\d+\. ', t)))
# ['', '사과', '딸기', '수박']
```



### `re.findall()`

- `re.findall(expression, text)`  : expression을 text에서 찾아 list로 반환
  - 찾지 못했으면 빈 list 반환

```python
text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""

re.findall("\d+",text)
# ['010', '1234', '1234', '30']
```



### `re.sub()`

- `re.sub(expression, replace, text)` : expression을 text에서 찾아 replace로 대체

```python
text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."

re.sub('[^a-zA-Z]',' ',text)
'Regular expression   A regular expression  regex or regexp     sometimes called a rational expression        is  in theoretical computer science and formal language theory  a sequence of characters that define a search pattern '
```

- 또는 미리 정규식을 compile한 뒤 아래와 같이 사용

```python
p = re.compile("(내|나의|네꺼)")

p.sub("그의", "나의 물건에 손대지 마시오.")
'그의 물건에 손대지 마시오.'
```

- `|` : or



# nltk

- `pip install nltk`
- 정규 표현식을 사용하여 단어 토큰화를 수행

```python
import nltk
from nltk.tokenize import RegexpTokenizer

text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"

tokenizer=RegexpTokenizer("[\w]+")
print(tokenizer.tokenize(text))
'''
['Don', 't', 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', 'Mr', 'Jone', 's', 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop']
'''
```

```python
tokenizer=RegexpTokenizer("[\s]+", gaps=True)
print(tokenizer.tokenize(text))
'''
["Don't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name,', 'Mr.', "Jone's", 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop']
'''
```

