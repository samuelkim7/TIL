### Dominator
- Find an index of an array such that its value occurs at more than half of indices in the array.

- sorted() 이용 -> leader가 있다면 가운데 정렬된 수임 -> count()로 확인해서 반 이상인지 확인 -> 맞다면 index()로 return
- 만약 아니라면 return -1
- edge case 처리
- O(Nlog(N))

```python
def solution(A):
    if not A:
        return -1
    if len(A) == 1:
        return 0
    # sort
    A_sorted = sorted(A)

    # leader 확인
    leader = A_sorted[len(A) // 2]
    if A.count(leader) > len(A) // 2:
        return A.index(leader)
    # 없는 경우
    else:
        return -1
```

### MaxSliceSum
- Find a maximum sum of a compact subsequence of array elements.

- 해당 원소에서 끝나는 slice의 최댓값은 자기 자신과 이전까지의 최댓값에 자기 자신을 더한 것을 비교하여 결정된다.
- max_ending = max(a, max_ending + a)
- 이렇게 얻은 값들 중 최댓값을 max_slice에 저장함 
```python
def solution(A):
    if len(A) == 1:
        return A[0]

    max_ending = 0
    max_slice = -1000001
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice
```

## PrimeNumbers
### CountFactors
- Count factors of given number n.
- just count until square root of n
```python
def solution(N):
    i = 1
    result = 0
    while i*i < N:
        if N % i == 0:
            result += 2
        i += 1
    if i*i == N:
        result += 1
    return result
```
