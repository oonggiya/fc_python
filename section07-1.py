# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#   # 함수
#   # 함수
#   # 함수


# 예제 1

class UserInfo:
  def __init__(self, name):
    self.name = name
  def user_info_p(self):
    print('name : ', self.name)


user1 = UserInfo()
