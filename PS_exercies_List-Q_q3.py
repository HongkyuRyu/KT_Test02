# 리스트의 크기를 입력하세요.
num_size = int(input("리스트의 크기를 입력하세요."))

a = [False] * (num_size)

for i in range(len(arr)):
    a[i] = int(input(f'a[{i}]값을 입력하세요.: '))
print(f'현재 입력한 리스트: {a}')
a.sort()
print(f'이진 탐색 전 리스트: {a}')
def binary_search(arr, key):
    start = 0
    end = len(a)-1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
        

    return -1


target = int(input(f'검색할 값을 입력하세요.: '))
index = binary_search(a, target)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')
    
    
"""
<출력>
리스트의 크기를 입력하세요.5
a[0]값을 입력하세요.: 1
a[1]값을 입력하세요.: 2
a[2]값을 입력하세요.: 4
a[3]값을 입력하세요.: 3
a[4]값을 입력하세요.: 5
현재 입력한 리스트: [1, 2, 4, 3, 5]
이진 탐색 전 리스트: [1, 2, 3, 4, 5]
검색할 값을 입력하세요.: 3
검색값은 a[2]에 있습니다.

"""