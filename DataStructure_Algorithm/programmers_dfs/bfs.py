answer = 0


def dfs(i, numbers, target, value):
    global answer
    if i == len(numbers) and target == value:
        answer += 1
        return
    if i == len(numbers):
        return

    dfs(i + 1, numbers, target, value + numbers[i])
    dfs(i + 1, numbers, target, value - numbers[i])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer