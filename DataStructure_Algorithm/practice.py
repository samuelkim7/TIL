def solution(arr1, arr2):
    print(arr1[0][0] + arr2[0][0])
    answer = [[0] * len(arr1[0])] * len(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

print(solution([[1,2], [1,2]], [[1,2], [3,3]]))