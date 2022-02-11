
list_of_numbers = []

for i in range(1, 1001):
  if i % 2 !=0:
    list_of_numbers.append(i**3)


def sum_digits(value):
    summ = 0
    while value != 0:
        summ += value % 10
        value //= 10
    return summ

result_summ_1 = 0
for i in list_of_numbers:
    if sum_digits(i) % 7 == 0:
        result_summ_1 += i


list_of_numbers_2 = []

for i in list_of_numbers:
    if i > 0:
        i += 17
    list_of_numbers_2.append(i)

result_summ_2 = 0
for i in list_of_numbers_2:
    if sum_digits(i) % 7 == 0:
        result_summ_2 += i

print(result_summ_1)
print(result_summ_2)


# for i in list_of_numbers:
#     summ = 0
#     while i != 0: #and i % == 0:
#         summ += i % 10
#         i = i // 10
#     if summ % 7 == 0:
#         summ = sum(summ)
#     print(summ)






# if i % 7 == 0:
#     sum(i, summ)
# # sum(i, summ)
# print(sum_result_1)




# if sum % 7 != 0:
# del list_of_numbers[i]


#
#      if sum = sum + i % 10:
#
#     print(i)
