# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print('yes')

# 예2
if False:
    print('No')
# 예3
if False:
    print('No')
else:
    print('Yes2')

# 관계연산자
# >, >=, <, <=, ==같다, !=같지않다

# a = 10
# b = 0
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)

# 참 거짓 종류 ( True, False )
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""

if city:
    print('True')

else:
    print('False!!')

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and:', a > b and b > c)
print('or: ', a > b or c > b)
print(not True)
print(not False)


# 산술, 관계 논리 연사자
# 산술 > 관계 > 논리 순서로 적용
print('ex1: ', 5+10 > 0 and not 7+3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('합격하셨습니다.')
else:
    print('불합격')

# 다중조건문
num = 75

if num >=90:
    print('num 등급 A', num)
elif num >= 80:
    print('num 등급 B', num)
elif num >= 70:
    print('num 등급 C', num)
else: 
    print('num D')


# 중첩조건문

age = 17
height = 170

if age >= 20:
    if height >= 170:
        print('A')
    elif height >= 160:
        print('B')
    else:
        print('키제한')

else:
    print('나이제한')