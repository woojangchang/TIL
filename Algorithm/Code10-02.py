def openBox():
    global count
    print('Open Box')
    count -= 1
    if count == 0:
        print('Input Ring')
        return
    
    openBox()
    print('Close Box')

count = 10
openBox()