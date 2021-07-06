import pandas as pd

def solution(df):
    avg = (df['math'] + df['science']) / 2
    df['avg'] = avg

    avg_high = (df['avg'] > 2.5)
    df['avg_high'] = avg_high
    return df


data = {'name':['A', 'B', 'C', 'D'],
        'math': [4.0, 2.1, 4.7, 2.6],
        'science':[3.8, 1.7, 0.7, 2.4]}
df = pd.DataFrame(data, columns=['name', 'math', 'science'])
print(solution(df))