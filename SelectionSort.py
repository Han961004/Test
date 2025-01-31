
def selection_sort(arr):
    
    # 마지막 요소는 자동 정렬되므로 n-1 까지 반복
    for i in range(len(arr) - 1):
        # 현재 인덱스를 최소값 위치로 설정
        min_idx = i
        
        # i+1 부터 끝까지 탐색하여 최소값 찾기
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 현재 i 번째 값과 최소값을 교환 swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)