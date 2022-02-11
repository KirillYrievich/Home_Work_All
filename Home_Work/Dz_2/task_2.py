
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in range(len(original_list)):
    lines = original_list.pop(0)
    if lines.isdigit() == True:
       original_list.append(f'"{int(lines):02d}"')

    elif lines[0] == '+' and lines[1].isdigit() == True:
        original_list.append(f'"+{int(lines):02d}"')

    else: original_list.append(lines)

print(*original_list)



