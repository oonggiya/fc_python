# section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('hello Python!')
print("Hello Python!")
print("""heLLo Python!""")
print('''HeLlO Python!''')

print()

# Seperator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2020', '02', '15', sep='-')
print('oonggiya', 'gmail.com', sep='@')

# end 옵션사용
print('Welcome To the', end=' ')
print('J rich homepage')

# format 사용 [], {}, ()
print('{} and {}'.format('you', 'me'))
print("{0} and {1} and {0}".format('you', 'me'))
print("{a} are {b}".format(a="you", b="the best"))

print("%s's favorite number is %d" %('Joe', 1))  # %s : 문자, %d : 정수 , %f : 실수

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(775,6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=775,b=6534.123))

# Escape 코드
print('"you"')
print("'you'")
print('\'you\'')
print("""'you'""")
print('\\you\\\n\n\n')
print('\t\tJay')