katok = ['삼색이', '야통이', '길막이', '무', '래기']

def delete_data(position):
    kLen = len(katok)

    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

delete_data(3)
print(katok)