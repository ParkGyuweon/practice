
def make_sum(x, y):
    result = x + y
    return result

print(make_sum(1, 2)) # 같은 code를 여러 번 작성하지 않도록 모아두는 곳이 함수 (재사용 가능)
print(make_sum(3, 4))

def add_interest(money, rate):
    money += money * (rate / 100)
    return money

print(add_interest(100, 4.2))
print(100 + (100 * (4.2 / 100)))
print(add_interest(25000, 4.11))
print(25000 + (25000 * (4.11 / 100)))

a = add_interest(100, 4.2) # 콘솔에는 안 나타나도 결과는 존재하는 상황 -> 콘솔에 나타나게 하려면 print가 필요
print(add_interest(100, 4.2)) # print는 스스로 데이터를 갖지 않음, 그냥 보여주는 역할만 함! -> 터미널에 출력하는 것 자체가 일.

# 화면에 출력하는 함수
def pring_greeting(name):
    print(f'Hello, {name}!!!') # None return

# 호출한 곳으로 값을 변환하는 함수
def make_greeting(name):
    return f'Hi, {name}!!!'

print(pring_greeting('Jeeho'))
print(make_greeting('Jeeho'))