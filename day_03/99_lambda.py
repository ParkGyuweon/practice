# 함수
def add(x, y):
    return x + y

print(add(1, 2))

l_add = lambda x, y: x + y
print(l_add(2, 3))

print((lambda x, y: x + y)(3, 4))

assigned_add = add
print(assigned_add(4, 5))

students = [
    ('지민', 25),
    ('서준', 20), 
    ('민우', 30)
]

# sorted의 key는 각 아이템의 크기의 기준을 찾아주는 함수를 인자로 전달해야 한다.
def get_age(student):
    return student[1]

print(sorted(students, key = get_age))
print(list(map(get_age, students)))

print(sorted(students, key=lambda student: -student[1]))