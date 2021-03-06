# 01. 크롤러 설계 기본

- 목적과 대상에 따라서 필요한 기능만 갖춘 크롤러를 설계
- 어떤 사이트 전체를 내려받는 것이 목적이라면 wget만으로도 충분할 수 있음
  - 그러나 동적 페이지는 wget만으로 대응하기 어려움
- URL이 어느 정도의 계층을 갖고 있는 경우가 많으므로, 특정 계층만 크롤링하는 것이 효율적
  - 사이트맵에서 어떤 내용이 어떤 URL과 대응하는지 확인할 수 있음
  - 웹페이지에서 사이트맵을 제공하면 좋겠지만, 그렇지 않은 사이트들도 많음
    - 도메인 주소 + /sitemap.xml에 배치하여 XML 파일로 제공하는 사이트들도 있으나 XML 파일이 어디에 배치되는지는 정해져있지 않음
    - 또한 XML 파일이 제공되더라도 일부 페이지만 제공하는 경우도 많음
- 공식 아카이브를 제공하는 경우도 있음
  - 위키피디아의 [데이터베이스 아카이브 제공 페이지](https://dumps.wikimedia.org/kowiki/) 등
- 웹 API는 특정 URL에 정해진 매개 변수를 넣어 접근하면 XML 또는 JSON 등의 구조화된 데이터를 제공해주는 기능
- 크롤링을 통해 얻은 URL을 스크래이핑 후 다시 크롤링

# 02. 크롤러가 가지는 각각의 처리를 설계할 때의 주의 사항

### 크롤러의 각 처리 공정

- 수집 : 네트워크에 있는 데이터에 요청
- 분석 : 파싱, 텍스트 데이터를 구조화된 데이터로 변환
- 추출 : 필요한 데이터를 추출
- 가공 : 사용 형태에 맞게 데이터에서 노이즈 제거, 정규화, 이미지 처리 등
- 저장

### 네트워크 요청

- 간격 설정하기 : 사이트에 부하가 걸리기 때문에 적어도 1초에 1번 정도가 적당
- 타임아웃 : 요청한 사이트로부터 응답이 없는 경우(과부하 등), 타임아웃을 설정하여 N초간 응답이 없으면 수집을 종료
- 재시도 : 사이트가 큰 문제가 없음에도 오류가 나는 경우. 재시도 횟수는 1~3회 정도로 설정
  - 재시도 간격 : Exponential Backoff 방법을 사용하여 통신에 실패하는 횟수가 많아질수록 간격을 늘리는 알고리즘 (1초, 2초, 4초, 8초, ... 등 2의 n 제곱 간격으로 시도하는 등)

### 파싱(분석)

- 문자 코드 : 대부분 UTF-8로 작성돼 있으나 아닌 경우도 많음. EUC-KR로 작성된 페이지를 UTF-8로 읽으면 문자가 깨짐. 응답 헤더 내부의 Content-Encoding 헤더에 문자 코드가 나와있는 경우가 있으나 없는 경우도 있음
- HTML/XML 파싱 : 태그가 잘못 구성돼 있거나 하는 경우, HTML을 보완하기 위한 별도의 프로그램 사용 또는 파이썬 라이브러리 이용
  - [HTML Tidy](http://tidy.sourceforge.net/)
  - Beautiful Soup
  - lxml
- JSON 디코드 : JSON 디코더를 이용하여 프로그래밍 언어의 딕셔너리 자료형 형태로 데이터를 변환

### 스크레이핑과 정규 표현식

- URL 정규화 : 링크가 상대 경로인 경우, 프로토콜이나 호스트 이름을 포함한 절대 링크로 변환해야 함
- 테스트 : 일반적으로 여러 실패를 반복하면서 추출 처리를 수정하게 되며, 수정할 때마다 결과를 확인하는 것은 힘들기 때문에 테스트 코드를 사용하는 것이 좋음

### 데이터 저장소의 구조와 선택

#### 데이터 저장소 종류

- 파일
- 문서 데이터베이스(Document Database)
- 관계형 데이터베이스(Relational Database)
- 객체 데이터베이스(Object Database)
- 키-값 데이터베이스(Key-Value Database)

#### 파일

- 텍스트 파일로 저장하는 등
- 파일이 많은 경우 디렉터리를 나눠서 저장하거나(읽어들이는 속도 문제) 파일 이름으로 해시를 사용(중복되는 파일 명 방지)
- 다운 받은 파일이 어떤 페이지의 파일인가 하는 정보가 불필요하다면 SHA-1 형식 해싱하는 등

#### 데이터베이스

- MySQL 등의 관계형 데이터베이스를 사용하여 세부적인 부가 정보를 함께 기록
- 바이너리 데이터를 저장할 수 있는 BLOB 형식의 칼럼이 있기 때문에 디렉터리를 구분해서 저장할 필요가 없음
- MySQL의 단일 칼럼 인덱스의 최대 키 길이는 767바이트로 문자 길이가 191 이상인 URL에는 인덱스를 만들 수 없기 때문에 URL 해시를 만들고, 이 해시에 인덱스를 만드는 방법을 사용

# 03. 배치를 만들 때의 주의점

- **배치** : 정해진 일련의 처리를 한 번에 하는 프로그램
- **공정 분리하기** : 네트워크 요청과 스크레이핑 부분을 분리하여, 스크레이핑에 실패했을 때 네트워크 요청부터 다시 하는 경우가 없도록 함
- **중간 데이터 저장해두기** : 실패한 페이지에 대해서만 다시 요청해도 되도록 함
- **실행 시간 알아 두기** : 평소보다 시간이 오래 걸리는 경우 오류가 있음을 짐작
  - 현재 처리 중인 URL 등을 출력하여 경과 상태를 알 수 있게 하는 것이 좋음
- **중지 조건을 명확하게 하기** : 재귀적으로 링크를 추출하고 스크레이핑 할 때 정지 조건이 명확하지 않으면 무한 루프가 일어나기 때문에 크롤링하는 계층과 도메인을 한정하거나 내려받을 파일의 상한을 정하는 등 조건을 걸어줘야 함
- **함수의 매개 변수를 간단하게 하기** : 디버깅할 때 공정의 처리를 부분적으로 재현해야 하는 경우, 중간 데이터를 저장해두고 이를 매개변수로 사용하는 것이 좋음
- **날짜를 다룰 때의 주의 사항** : 데이터의 변경일을 저장할 때는 UTC로 통일하여 저장하는 것을 추천

