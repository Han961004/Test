'''
Space Complexity O(1)
Time Complexity O(n**2)

삽입 정렬은 기본적으로 정렬된 부분과 정렬되지 않은 부분을 나누어 진행하는 알고리즘이다.
'''
def insertion_sort(arr):
    
    if len(arr) <= 1:
        return 
    
    # 두 번째 요소부터 시작 (첫 번째 요소는 정렬된 상태)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # key 보다 큰 원소는 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # key를 올바른 위치에 삽입
        arr[j + 1] = key
        
    return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))