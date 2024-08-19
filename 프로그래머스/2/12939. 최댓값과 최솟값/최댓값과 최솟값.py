def solution(s):
    nums = list(map(int, s.split()))
    min_num = min(nums)
    max_num = max(nums)
    return f"{min_num} {max_num}"