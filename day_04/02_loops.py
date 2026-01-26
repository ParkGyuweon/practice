# for
foods = ['chicken', 'pizza', 'ramyeon']

# for <변수명> in <반복 가능한 객체> :
# 여러 데이터를 담고 있으면 반복 가능한 객체라고 볼 수 있음

for food in foods:
    print(food)
    
"""
food = foods[0]
print(food)
food = foods[1]
print(food)
food = foods[2]
print(food)
"""

# str 순회
word = 'fantastic'
print('|', end='')
for letter in word:
    print(letter, end = '|')

print()

# range를 활용한 순회
for i in range(10): # 0, 1, 2, ..., 9 (n - 1)
    print(i)

# list와 index를 조합했을 때
for i in range(len(foods)):
    print(foods[i])

# 2차원 리스트 순회
matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
]

for row in matrix:
    print(row)

row = [1, 2, 3]
for row in matrix:
    for col in row:
        print(col, end = ', ')
print()

# while -> if의 변형
# while <조건>:
loan = 1000
monthly = 50
# if랑 같은데 조건이 참인 동안 반복함 
while loan > 0:
    loan -= monthly    
    print(f'left: {loan}')
print('done!')