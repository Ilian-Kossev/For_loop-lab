n = int(input())
m = 2 * n
result_1 = 0
result_2 = 0
for number in range(1, 2 * n + 1):
    value = int(input())
    if number <= n:
        result_1 += value
    else:
        result_2 += value
difference = result_1 - result_2
if difference == 0:
    print(f"Yes, sum = {result_1}")
else:
    print(f"No, diff = {abs(difference)}")