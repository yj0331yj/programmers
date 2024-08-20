def solution(n, m):
    answer = []
    gcd = 0
    lcm = 0
    
    # 최대공약수
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd =i
            break
    
    # 최소공배수
    for j in range(max(n, m), (n*m)+1):
        if j % n == 0 and j % m == 0:
            lcm = j
            break
            
    answer = [i, j]
            
    return answer