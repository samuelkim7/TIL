### format ###
## .format
# print("나는 %d살이고 %s를 좋아합니다." % (15, "빨간색"))
# print("나는 {}살입니다.".format(30))

## f
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

## 퀴즈) format
# import random
# total = 0
# for i in range(1, 51):
#     time = random.randint(5, 50)
#     check = " "
#     if time >= 5 and time <= 15:
#         check = "O"
#         total += 1
#     print("[{}] {}번째 손님 (소요시간 : {}분)".format(check, i, time))
# print("총 탑승 승객 : {} 분".format(total))

## 퀴즈) 함수, format
# def std_weight(height, gender):
#     if gender == "남자":
#         return height ** 2 * 22
#     else:
#         return height ** 2 * 21
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height, gender, weight))


### 가변인자 ###
## *
# def profile(name, age, *language):
#     print("이름 : {}\t나이: {}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "python", "java", "C", "c++", "C#")
# profile("김태호", 25, "python", "java")


### 입출력 ###
## ljust, rjust
# scores = {"수학": 50, "영어": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

## zfill
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

## 오른쪽 정렬 및 총 10자리 확보, 부호 표시
# print("{0: >+10}".format(-500))
## 3자리 마다 , 찍기
# print("{0:,}".format(10000000))
## 소수점 3째자리까지 출력
# print("{0:.3f}".format(5/3))


### 파일 입출력 ###
# ex1) "w": 쓰기 모드, "a": 덧붙이기 모드
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

## "r": 읽기 모드, read(): 모두 읽기, readline(): 한 줄 읽고 다음줄로 이동
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

## 몇 줄인지 모를 경우 한줄씩 모두 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

## pickle, "wb": 쓰기 모드
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"a":100, "b":300}
# print(profile)
# pickle.dump(profile, profile_file) #profile 정보를 file에 저장
# profile_file.close()

## pickle, "rb": 읽기 모드
# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

## pickle, with
# import pickle
# with open("profile.pickle", "rb") as file:
#     print(pickle.load(file))

## with 읽기
# with open("study.txt", "w", encoding="utf-8") as file:
#     file.write("파이썬 열심히 공부 중")

## with 쓰기
# with open("study.txt", "r", encoding="utf-8") as file:
#     print(file.read())

## 퀴즈) 주간 보고 양식 만들기
# for i in range(1, 6):
#     with open("{}주차.txt".format(i), "w", encoding="utf-8") as file:
#         file.write("- {} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 :".format(i))