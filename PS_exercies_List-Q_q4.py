# 리스트의 크기를 입력하세요.
num_size = int(input("리스트의 크기를 입력하세요."))

a = [False] * (num_size)

for i in range(len(a)):
    a[i] = int(input(f'a[{i}]값을 입력하세요.: '))
print(f'현재 입력한 리스트: {a}')


def find_max(arr):
    i = 0
    while True:
        if i == len(arr):
            return MAX_value[1]
        
        MAX_value = [arr[0], 0]
        if arr[i] > MAX_value[0]:
            MAX_value[0] = arr[i]
            MAX_value[1] = i
        i += 1 
        
def find_min(arr):
    i = 0
    while True:
        if i == len(arr):
            return Min_value[1]
        Min_value = [arr[0], 0]
        if arr[i] < Min_value[0]:
            Min_value[0] = arr[i]
            Min_value[1] = i
        i += 1
    
print(find_max(a))
print(find_min(a))
"""
    
리스트의 크기를 입력하세요.3
a[0]값을 입력하세요.: 1
a[1]값을 입력하세요.: 2
a[2]값을 입력하세요.: 3
현재 입력한 리스트: [1, 2, 3]
2
0
"""