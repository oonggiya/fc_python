# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.

q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k in q1.keys():
    if k == "가을":
        print(q1[k])

for k,v in q1.items():
    if k == "여름":
        print(v)


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k,v in q2.items():
    if v == '딸기':
        print(k,v)

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

num = 10

if num >=81:
    print('num 등급 A', num)
elif num >= 61:
    print('num 등급 B', num)
elif num >= 41:
    print('num 등급 C', num)
elif num >= 21:
    print('num 등급 D', num)
else: 
    print('num D')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18

# ????????????????
# best = a

# if b > a:
#     best = b
# if c > b:
#     best = c
# print('highest : ', best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정",'진', '사']


show = [x for x in q3 if x != '사']
print(show)


for v in q3:
    if v == "정":
        continue
    else:
        print(v, end = "")

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

# List comprehension
q7 = [x for x in range(1,101) if x % 2 == 1 ]
print('q7: ', q7)


for n in range(1,101):
    if n % 2 == 0:
        print(n, end = ',')
    
print()


for n in range(1,101):
    if n % 2 == 1:
        print(n, end = ',')
    



# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for x in q4:
    if len(x) >= 5:
        print(x)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for x in q5:
    if x.islower():
        print(x)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print()
print()
print()



for x in q6:
    if x.isupper():
        print(x.lower())
    else:
        print(x.upper(), end= " ")



# List comprehension

# 일반적인 방법
numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

print()
print()
print()
print()
#========================

list_make = [x for x in range(1,101)]
print(list_make)