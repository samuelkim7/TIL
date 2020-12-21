# kth number
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

