# K번째 수
def solution(array, commands):
    # commands = i, j, k
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        # slicing
        temp = array[i - 1:j]
        temp.sort()
        # find kth number
        if k <= len(temp):
            answer.append(temp[k - 1])

    return answer

# 가장 큰 수
def solution(numbers):
    # 각 요소를 str으로 변환
    numbers = list(map(str, numbers))

    # str * 3을 통해 reverse 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 모든 요소를 str 합을 사용하여 반환
    return str(int(''.join(numbers)))


# 가장 큰 수 풀이2
import functools

def solution(numbers):
    numbers = [str(e) for e in numbers]
    numbers.sort(key = functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(numbers)))

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))