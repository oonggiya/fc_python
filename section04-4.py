# section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) :  순서x, 중복x, 수정0, 삭제0

# Key, Value (Json) -> MongoDB

# 선언

a = {'name' : 'JOE', 'Phone': '010-111-2222', 'bitrh' : 581121}
b = {0:'Hello Python', 1: 'hey bro'}
c = {'arr': [1,2,3,4,5]}

print(type(a))

# 출력

print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3)
print(a)

#keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(2 in b)
print('name' in a)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b) #형 변환
print(t)
l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))


# 추가 & 제거
s3 = set([7,8,10,15])
s3.add(18)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))