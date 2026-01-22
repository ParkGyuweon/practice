numbers = [1, 2, 3, 4, 5]

print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

print(max(1, 2, 3))
print(min(44, 24, 10))

# map
raw_input = input()
num_list = map(int, raw_input.split()) # map(function, iteratable)
print(sum(num_list))
a= int('1') # 이건 함수 호출 / 위처럼 int는 그냥 함수임. 함수 호출을 하지 않음. 
# 여러 개의 데이터를 이 함수에 맵핑하겠다는 의미가 됨. 
# 중요한 차이점은 호출의 여부! 함수 자체를 전달하는 행위임. 
# map은 함수와 데이터를 매개변수로 받아서 각 데이터에 함수를 적용하는 것임.

def to_int_and_double_up(a):
    return int(a) * 2

print(to_int_and_double_up('1'))
num_list = map(to_int_and_double_up, raw_input.split())
print(sum(num_list))