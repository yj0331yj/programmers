def solution(price, money, count):
    # 등차수열 합 공식 : n * (n + 1) / 2 
    price = price * count * (count+1) /2
    answer = price - money
    
    if answer > 0:
        return answer
    else:
        return 0