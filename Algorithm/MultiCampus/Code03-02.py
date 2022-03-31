katok = ['삼색이', '야통이', '길막이']

def insert_data(position, friend):
    kLen = len(katok)
    if position > kLen:
        return
    
    katok.append(None)
    for i in range(kLen, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

insert_data(3, '무')
insert_data(6, '래기')
print(katok)