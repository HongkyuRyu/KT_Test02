# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
result = int(data[0]) # 첫번쨰 문자

for i in range (1, len(data)):
    next_num = int(data[i])
    if next_num <= 1 or result <= 1:
        result += next_num
    else:
        result *= next_num
    

print(result)
