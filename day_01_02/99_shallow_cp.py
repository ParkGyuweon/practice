a = [1, 2, 3]
b = a # a가 갖고 있던 주소를 b에 할당
a[0] = 4
print(b[0])


a = [1, 2, 3]
b = a[:] # 얕은 복사
a[0] = 4
print(b[0]) # 1

a = [1, 2, [3, 4, 5]]
b = a[:]
a[0] = 4
print(b[0]) # 1
a[2][0] = 6 
print(b[2][0])

from copy import deepcopy
a = [1, 2, [3, 4, 5]]
b = deepcopy(a)
a[0] = 4
print(b[0])
a[2][0] = 6
print(b[2][0])