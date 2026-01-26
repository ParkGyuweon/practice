# 조건문 (conditional statement)

age = 20
# simple if
# if <조건>:
# <조건> : Boolean으로 평가될 수 있는 표현식
if age < 20:
    print('you shall not pass')

year = 2026
if year & 4 == 0:
    print('윤년 (2월 29일 존재)')

# is else
integer = 20
if integer % 2 == 0:
    print('is even')
else:
    print('is odd')

# if - elif - else
if age < 24:
    print('too young')
elif age > 30:
    print('too old')
else:
    print('welcome')

# is - elif의 경우 앞쪽의 조건이 참이 될 경우 뒤쪽 조건을 확인하지 않음
dust = 10

if dust < 10:
    print('Good')
elif dust >= 10 and dust < 30:
    print('Soso')
elif dust >= 30 and dust < 50:
    print('Bad')
elif dust >= 50:
    print('Very Bad')

dust = 10
if dust < 10:
    print('Good')
elif dust < 30:
    print('soso')
elif dust < 50:
    print('Bad')
else:
    print('Very Bad')

a = 10
b = 0
if b == 0:
    print('Cannot divide by zero')
else:
    print(a / b)