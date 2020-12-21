# bubble_sort
def bubble_sort(List):
    for i in range(0, len(List) - 1):
        for j in range(0, len(List) - 1 - i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List


# merge_sort
def merge_split(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = merge_split(A[:middle])
    right = merge_split(A[middle:])
    return merge(left, right)

def merge(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1

    while j < len(right):
        sorted.append(right[j])
        j += 1
    return sorted


# quick_sort
def qsort(data):
    if len(data) <= 1:
        return data

    left, right = [], []
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right)

# def quick_sort(A, lo, hi):
#     def partition(lo, hi):
#         pivot = A[hi]
#         left = lo
#         for right in range(lo, hi):
#             if A[right] < pivot:
#                 A[left], A[right] = A[right], A[left]
#                 left += 1
#         A[left], A[hi] = A[hi], A[left]
#         return left
#
#     if lo < hi:
#         pivot = partition(lo, hi)
#         quick_sort(A, lo, pivot - 1)
#         quick_sort(A, pivot + 1, hi)
