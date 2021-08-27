# TIL (Today I Learned)
>매일은 힘들어도 꾸준히는 하자

> 미래의 나를 위해 배운 것들을 잘 정리해두자

## 배운 것들
[git](./git)

Numpy

[Pandas](./Pandas)

[Statistics (Python)](Python%20Statistics)

[Database (MySQL)](SQL)

[Django](Django)

[Web (HTML, Crawling, Regular Expression)](Web)

[데이터 시각화](Visualization)

[OpenCV](OpenCV)

[Big Data Analysis (Preprocessing)](Big%20Data%20Analysis)

[Big Data Analysis (Machine Learning)](Big%20Data%20Analysis/Machine%20Learning)

[Big Data Analysis (Deep Learning)](Big%20Data%20Analysis/Deep%20Learning)

[애자일 프로젝트](Agile%20Project)



## 공부 중

> 오래 걸리더라도 끝까지!

크롤러, 스크레이핑

케라스 딥러닝



## 공부 끝

> 책의 내용 전체를 한 번 경험했을 뿐, 절대 끝이 아니다.

파이썬 통계분석 (21.06.11 ~ 21.06.20)

SQL 데이터 전처리 분석 (21.06.14 ~ 21.07.01)

Django (21.07.06 ~ 21.08.12)

파이썬 머신러닝 (21.07.21 ~ 21.08.27)



## 자주 쓰는 것

### 아나콘다 가상환경 설정(jupyter lab)

1. `conda create --name <name>`
2. `conda activate <name>`
3. `pip install ipykernel`
4. `python -m ipykernel install --user --name <name> --display-name "Python <name>"`
5. `conda install -c conda-forge jupyterlab`

- 삭제 : `conda remove --name <name> --all`

### Github

#### Github에 업로드된 파일이나 폴더 없애기

- `.gitignore에 파일/폴더 명 추가`
-  `git rm --cached -r .`
- `git add .`
- `git commit -m '.gitignore modified'`

