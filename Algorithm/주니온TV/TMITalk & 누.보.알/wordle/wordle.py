words = []
with open('./wordle/words_with_five_chars.txt', 'r') as f:
    reads = f.readlines()
    for word in reads:
        words.append(word.strip())


# 제외해야 하는 문자의 경우
def check_excludes(word, s):
    for c in s:
        if c in word:
            return False
    return True


# 포함해야 하는 문자의 경우
def check_includes(word, s):
    for c in s:
        if c not in word:
            return False
    return True


# 정확한 위치가 알려진 문자의 경우
def check_position(word, pmap:dict):
    for key in pmap:
        if word[key] != pmap[key]:
            return False
    return True


# 정확한 위치가 아닌 문자의 경우
def check_wrongpos(word, pmap):
    for key in pmap:
        if word[key] == pmap[key]:
            return False
    return True

# 조건에 맞는 단어 추천
includes = {0:'D', 1:'E'}
excludes = 'AT'
positions = {3:'L'}

recommend = []
for word in words:
    if not check_position(word, positions):
        continue
    if not check_includes(word, includes.values()):
        continue
    if not check_excludes(word, excludes):
        continue
    if not check_wrongpos(word, includes):
        continue
    recommend.append(word)

for word in recommend:
    print(word)