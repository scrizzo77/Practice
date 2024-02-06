power = int(input("Enter the power: "))
new_num_list = [1]
old_num_list = [1,1]
i = 0

print(new_num_list)
print(old_num_list)

while True:
    num1 = old_num_list[i]
    num2 = old_num_list[i+1]

    new_num_list.append(num1+num2)

    if len(new_num_list) < power:
        i += 1
        if i == len(old_num_list)-1:
            new_num_list.append(1)
            print(new_num_list)
            i = 0
            old_num_list.clear()
            old_num_list.extend(new_num_list)
            new_num_list.clear()
            new_num_list.append(1)
    else:
        new_num_list.append(1)
        print(new_num_list)
        break

        
        
        
        
