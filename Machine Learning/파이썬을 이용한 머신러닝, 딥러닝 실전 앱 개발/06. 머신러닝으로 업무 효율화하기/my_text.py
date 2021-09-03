import pickle, tfidf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import model_from_json

# 텍스트
text1 = '''
대통령이 북한과 관련된 이야기로 한미 정상회담을 준비하고 있습니다.
'''

text2 = '''
아이폰과 아이패드 모두 가지고 다니므로 USB를 2개 연결할 수 있는 휴대용 배터리를 선호합니다.
'''

text3 = '''
이번 주에는 미세먼지가 많을 것으로 예상되므로 노약자는 외출을 자제하는 것이 좋습니다.
'''

# TF-IDF 사전 읽어 들이기
tfidf.load_dic('../datasets/text/genre-tfidf.dic')

# Keras 모델 정의, 가중치 데이터 읽기
n_classes = 4
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(37414, )))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(n_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy',
             optimizer=RMSprop(), metrics=['accuracy'])
model.load_weights('../models/genre_model.hdf5')

# 텍스트 지정해서 판별
def check_genre(text):
    # 레이블 정의
    LABELS = ['정치', '경제', '생활', 'IT/과학']
    # TF-IDF 벡터 변환
    data = tfidf.calc_text(text)
    # MLP로 예측
    pre = model.predict(np.array([data]))[0]
    n = pre.argmax()
    print(LABELS[n], '(', pre[n], ')')
    return LABELS[n], float(pre[n]), int(n)


if __name__ == '__main__':
    check_genre(text1)
    check_genre(text2)
    check_genre(text3)
