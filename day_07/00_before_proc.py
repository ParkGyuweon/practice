# 절차지향 없이 len 구현하기

target = None
### 여기
if target is not None:
    length = 0
    for item in target:
        length += 1
    result = length
    ## GOTO: 저기

nums = list(map(int, input().split()))

# 이 시점에서 nums의 길이를 알고 싶다
target = nums
## GOTO: 여기
### 저기
print(result)