f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))

f.close()