# # list: 0개 이상의 데이터를 저장할 때
# alex = ['Alex', 'Rod', 'NYY']
# menus = ['Chicken', 'Pizza', 'Beer']
# print(menus)
# print(menus[0])
# print(menus[:2])
# print(menus[2:])
# print(menus[::-1])

# # mutable : 변경 가능
# menus[1] = 'Pepperoni Pizza'
# print(menus)

# # 중첩 가능 : list 안에 list를 넣을 수 있다.
# beers = ['Stella', 'Hoe', 'Cass', 'Terra']
# menus[2] = beers
# print(menus)

# menus = ['Chicken', 'Pizza', ['Stella', 'Hoe', 'Cass', 'Terra', 0]]
# print(menus[2][1][0])
# # print(menus[2][-1][0])

# tuple
jeeho = ('jeeho', 'Park', 0)
# immutable
# jeeho[0] = 'Jiho' # error

# tuple unpacking
first_name, last_name, age = jeeho

# swap
a = 2
b = 3
a, b = b, a # 오른쪽은 tuple
print(a, b)

# 다른 불쌍한 언어의 경우
a = 2
b = 3
temp = a
a = b
b = temp
print(a, b)

# warning
result = 100, # 정수가 아니고 tuple (끝의 쉼표가 한 개의 데이터를 가진 tuple을 만드는 행위)
print(type(result))
# print(result + 1) # error
print(result)


# range
print(range(10))
print(range(5, 10))
print(list(range(5, 0, -1)))
