def knapsack2(i, W, w, p):
    if (i <= 0 or W <= 0):
        return 0
    if (w[i] > W):
        value = knapsack2(i - 1, W, w, p)
        print(i - 1, W, value)
        return value
    else: # w[i] <= W
        left = knapsack2(i - 1, W, w, p)
        print(i - 1, W, left)
        right = knapsack2(i - 1, W - w[i], w, p)
        print(i - 1, W - w[i], right)
        return max(left, p[i] + right)
    
W = 20 # 배낭의 남은 무게
w = [0, 7, 10, 4, 20] # 다이아몬드 무게
p = [0, 90, 70, 60, 120] # 다이아몬드 가격
profit = knapsack2(len(w)-1, W, w, p)
print(profit)
