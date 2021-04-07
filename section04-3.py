name1 = 'lee'
name2 = 'park'

# section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서, 중복, 수정, 삭제 모두 가능 ***)
# 선언

a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'pen','banana', 'orange']
e = [10, 100, ['pen','banana', 'orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][0])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [10,100,1000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

del c[4]
print(c)

print()
print()
print()
print()
print()

# 리스트 함수

y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
print(y)
y.pop()
print(y) #LIFO

ex = [88,77]
y.extend(ex)
print(y)

# 삭제 :  del, remove, pop

# 튜플 (순서, 중복, 수정x ,삭제x)

a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c+d)
print()
print()
print()
print()
print()
print()

# 튜플 함수

z = (5,2,1,3,4,1)
print(z)
print(3 in z )
print(z.index(1))
print(z.count(1))