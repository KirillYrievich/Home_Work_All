
new_list_1 = []
new_list_2 = []
final_sum_1 = 0
final_sum_2 = 0

for i in range(1, 1001, 2):
    new_list_1.append(i**3)

def sum_digits(value):
    summ = 0
    while value != 0:
        summ += value % 10
        value //= 10
    return summ

for i in new_list_1:
    if sum_digits(i) % 7 == 0:
        final_sum_1 += i

for i in new_list_1:
    i += 17
    new_list_2.append(i)

for i in new_list_2:
    if sum_digits(i) % 7 == 0:
        final_sum_2 += i

print(final_sum_1)
print(final_sum_2)

