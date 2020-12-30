### 클래스 ###
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{} : {}방향으로 이동합니다 [속도 {}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 다중상속
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

# wraith1 = FlyableAttackUnit("레이스", 50, 10, 10)
# wraith1.attack("1시")
# wraith1.fly(wraith1.name, "1시")


### 에러 ###
## 사용자 정의 에러
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     num = int(input("숫자 입력: "))
#     if num > 100:
#         raise BigNumberError("입력값: {}".format(num))
# except BigNumberError as err:
#     print("너무 큰 수입니다. ({})".format(err))


### 모듈 ###
## 모듈 위치 찾기
# import random
# import inspect
# print(inspect.getfile(random))

## 내장함수 (built-in functions)
## dir: 어떤 객체가 지닌 멤버 변수와 함수를 표시
# import random
# print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

## 외장함수 (modules)
## glob: 경로 내의 폴더, 파일 목록 조회
# import glob
# print(glob.glob("./basics/*.py"))

## os : 운영체제와 관련된 기본 기능 제공
# import os
# print(os.getcwd())  # 현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("존재하는 폴더")
#     os.rmdir(folder)
#     print(folder, "폴더 삭제")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더 생성")

## time, datetime 등등
