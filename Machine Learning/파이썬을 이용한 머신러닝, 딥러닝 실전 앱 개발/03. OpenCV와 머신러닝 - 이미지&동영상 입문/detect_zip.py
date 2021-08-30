import cv2
import matplotlib.pyplot as plt

# 이미지로부터 우편번호 추출
def detect_zipno(fname):
    img = cv2.imread(fname)
    
    # 이미지 크기
    h, w = img.shape[:2]
    
    # 이미지의 오른쪽 윗부분만 추출
    img = img[:h//2, w//3:]
    
    # 이미지 이진화
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    im2 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]
    
    # 윤곽 검출
    cnts = cv2.findContours(im2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    # 윤곽 추출
    result = []
    for pt in cnts:
        x, y, w, h = cv2.boundingRect(pt)
        
        # 너무 작거나 큰 부분 제거
        if not (50 < w < 70): continue
        result.append([x, y, w, h])
    
    # 추출한 윤곽을 위치에 따라 정렬
    result = sorted(result, key=lambda x:x[0])
    
    # 추출한 윤곽이 너무 가까운 것들 제거
    result2 = []
    lastx = -100
    for x, y, w, h in result:
        if (x - lastx) < 10:continue
        result2.append([x, y, w, h])
        lastx = x
    
    # 테두리 출력
    for x, y, w, h in result2:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
    return result2, img

if __name__ == '__main__':
    cnts, img = detect_zipno('../datasets/hagaki1.png')
    
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
