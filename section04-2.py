# section04-2 
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am a Boy."
str2 = "hello"
str3 = " "
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big pie\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

# 멀티라인
multi = \
""" 
문자열 

멀티라인

테스트

"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'baby'


# print(str_o1*100)
# print(str_o2+str_o3)
print('a' in str_o4)
print('z' in str_o4)
print('a' not in str_o4)

# 문자열 형 변환
print(str(77)+'a')
print(str(10.4)+'c')

# 문자열 함수

# a = 'jrich'
# b = 'red'

# print(a.islower())
# print(b.endswith('d'))
# print(a.capitalize())
# print(a.replace('jrich', 'jrich@'))
# print(list(reversed(b)))



a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:5])
print(b[0:len(a)])
print(a[:])
print(a[0:4:2])
print(b[1:-2])
print(b[::-1])


