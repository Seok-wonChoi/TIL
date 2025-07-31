
# # 함수명 snake_case
# # 클래스명 PascalCase

# class SetMenu:
#     # 생성자 메서드
#     def __init__(self):
#         self.potato = 100 # 인스턴스 변수(속성), 필드
#         self.hambug = 300


#     # 메서드
#     # append(), pop() ---> 호출할 수 있는 이유 : built-in scope기 때문
#     def eat(self):
#         print('햄버거 세트 맛있다.')
#         print(f'음 {self.potato + self.hambug}불이 들었네')


# # 클래스 호출 (변수 = 클래스명())
# # 인스턴스 생성
# sanghai = SetMenu()

# # 메서드 호출
# sanghai.eat()

# a = 3  # 할당
# b = [1, 2, 3, 4, 5]         # 할당
 
# c = SetMenu()   # 할당
# a = 15          # 할당
# b[3] = 2     # 할당 X
# a = SetMenu() # 재할당


# # Q) c에 할당된 Setmenu와 a에 할당된 SetMenu 는 서로 같은 객체?
# # A) 서로 다른 객체.
# # Q) 할당 횟수?
# # A) 5번
# # Q) 객체는 총 몇 개?
# # A) 11개

###################################################################

# class Zergling:
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50
    
#     def run(self):
#         print('뛴다')
#         self.hp -= 1
#         self.mana += 1
    
#     def show_status(self):
#         print(f'hp : {self.hp}, mana : {self.mana}')

    
# z1 = Zergling()
# z2 = Zergling()

# z1.run()
# z1.show_status()

# for i in range(5):
#     z2.run()
# z2.show_status()


#######################################################
'''
class Calculator:
    pi = 3.141592 # 클래스 변수

    # 생성자
    def __init__(self, name):
        self.name = name # 인스턴스 변수

    # 메서드
    def add(self, a, b):
        return a + b
    
    # 매직 메서드 --> 객체를 문자열로 표현할 때 호출됨
    def __str__(self):
        return f'Calculator name : {self.name}'
    
    # 클래스 메서드 --> 클래스 자체를 첫번째 인자로 받는다
    @classmethod
    def get_pi(cls):
        return f'파이 값은 {cls.pi}'
    
    # 스태틱 메서드 --> self나 cls가 없음
    @staticmethod
    def multiply(a, b):
        return a * b



# 인스턴스 생성
calc = Calculator("공학용계산기")
# 메서드 호출
print(calc.add(2,3))
# 매직 메서드 호출
print(calc)
# 클래스 메서드 호출 - 클래스로 직접 호출
print(Calculator.get_pi())
# 스태틱 메서드 호출 - 클래스로 호출도 가능, 인스턴스로 호출도 가능
print(Calculator.multiply(4,5))
print(calc.multiply(4,5))
'''



# # 상속 으로 할 수 있는 것 2가지 (부모메서드 교체, 새로운 메서드 추가)
# # 1. 오버라이딩

# # 부모클래스
# class Person:
#     def walk(self):
#         print('사람이 걷는다')

# class SuperMan(Person):
#     def fly(self):
#         print('슈퍼맨이 난다')

#     def walk(self):       # 오버라이딩 == 메서드를 재정의 한다.
#         print('슈퍼맨이 뚜벅뚜벅 걷는다.')

# a = SuperMan()  # 인스턴스 생성 (자식클래스의 )
# # 자식클래스의 인스턴스를 생성해도 부모클래스의 메서드 호출이 가능
# a.walk() # 메서드 호출
# a.fly()



# EAFP(tru - except 구조)
# - IndexError

# def get_v(arr, idx):
#     try:
#         return arr[idx]
#     except IndexError:
#         print()



# # LBYL (if - else 구조)
# def get_v(arr, idx):
#     if 0 <= idx <= len(arr) -1:
#         return arr[idx]
#     return -1

# arr = [1, 2, 3]
# result = get_v(arr,5)
# print(result)


# 아래 클래스를 수정하시오.
# class StringRepeater:
#     def __init__(self, c, s):
#         self.c = c
#         self.s = s

#     def repeat_string(self):
#         for i in range(self.c):
#             print(self.s)

# repeater1 = StringRepeater(3, "Hello")
# repeater1.repeat_string()

# 아래 클래스를 수정하시오.
# class Person:
#     number_of_people = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
#         Person.number_of_people += 1
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)




# 아래 함수를 수정하시오.
# def check_number():
#     try:
#         num = int(input('숫자를 입력하세요 : '))
#         if num > 0:
#             print('양수입니다.')
#         elif num == 0:
#             print('0입니다.')
#         elif num < 0:
#             print('음수입니다.')
#     except ValueError:
#         print('잘못된 입력입니다.')


# check_number()



# 아래 클래스를 수정하시오.
# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

#     def get_user_info(self):
#         name = input("이름을 입력하세요: ")
#         age = input("나이를 입력하세요: ")
#         if age.isdigit():
#             self.user_data["name"] = name
#             self.user_data["age"] = age
#         else:
#             print("나이는 숫자로 입력해야 합니다.")
#             self.user_data.clear()

#     def display_user_info(self):
#         if "name" in self.user_data and "age" in self.user_data:
#             print('사용자 정보 : ')
#             print(f'이름 : {self.user_data["name"]}')
#             print(f'나이 : {self.user_data["age"]}')
#         else:
#             print('사용자 정보가 입력되지 않았습니다.')
# user = UserInfo()
# user.get_user_info()
# user.display_user_info()





# def restructure_word(word, arr):

#     for i in word:
#         if i.isdecimal():
#             for _ in range(int(i)):
#                 if arr:
#                     arr.pop()
#         else:
#             if i in arr:
#                 arr.remove(i)
#     return arr

# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []
# arr.extend(original_word)

# result = restructure_word(word, arr)
# print(result)           
# print(''.join(result))  



# # 아래에 코드를 작성하시오.
# my_lsit = [1, 2, 3]
# my_dict = {'A': 1, 'B': 2, 'C': 3}
# print(dir(my_lsit))
# print(dir(my_dict))

# help(my_lsit)
# help(my_dict)



# class Myth:
#     type_of_myth = 0
#     def __init__(self,name):
#         self.name = name

#         Myth.type_of_myth += 1


#     @staticmethod
#     def description():
#         print("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘라싼 이야기를 뜻한다")
    
# myth1 = Myth("dangun")
# myth2 = Myth("greek & rome")
# print(myth1.name)
# print(myth2.name)
# print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth} ')

# Myth.description()





# data = {'name': '홍길동'}

# try:
#     print(data['age'])
# except:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)
# # 아래에 코드를 작성하시오.
    

# arr = ['반갑', '하세요', '안녕']
# try:
#     for i in range(4):
#         print(arr.pop())

# # 아래에 코드를 작성하시오.
# except:
#     print(arr)
#     print('더 이상 pop 할 수 없습니다')


# word = '3.15'
# try:
#     print(int(word))
# # 아래에 코드를 작성하시오.
# except:
#     print('정수로 변환 가능한 값을 입력해 주세요.')



class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author

class Other(BaseModel):
    TYPE = 'Other Model'
    def __init__(self, data_type, title, content, created_at, updated_at):
     super().__init__(data_type, title, content, created_at, updated_at)

hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
print(hong.PK)
print(chun.PK)
hong.save()
chun.save()
print(hong.author)
print(chun.author)
print('---')

company = Other('회사', '회사명', '회사 설명', 2000, 2023)
print('Other 모델 인스턴스의 PK와 save 메서드')
print(company.PK)
company.save()

print('---')
print('모델 별 타입')
print(Novel.TYPE)
print(Other.TYPE)


# while True:
#     a, b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     elif a <= b:
#         print('No')6
#     else:
#         print('Yes')