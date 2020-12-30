### format ###
# ex1) .format
# print("나는 %d살이고 %s를 좋아합니다." % (15, "빨간색"))
# print("나는 {}살입니다.".format(30))

# ex2) f
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# ex3)
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

# ex4)
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
# ex1) *
# def profile(name, age, *language):
#     print("이름 : {}\t나이: {}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "C", "c++", "C#")
# profile("김태호", 25, "python", "java")


### 입출력 ###
# ex1) ljust, rjust
# scores = {"수학": 50, "영어": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# ex2) zfill
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# ex3)
## 오른쪽 정렬 및 총 10자리 확보, 부호 표시
# print("{0: >+10}".format(-500))
## 3자리 마다 , 찍기
# print("{0:,}".format(10000000))
## 소수점 3째자리까지 출력
# print("{0:.3f}".format(5/3))

