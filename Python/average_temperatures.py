temps = []
for i in range(0,7):
    temp = int(input(f"Enter average temperature for day {i+1}: "))
    temps.append(temp)

def max_temp(temps):
    j = 0
    maxTemp = temps[0]
    maxTemp_index = 0
    for j in range(0,len(temps)):
        if temps[j] > maxTemp:
            maxTemp = temps[j]
            maxTemp_index = j
        

    return maxTemp, maxTemp_index+1

maxTemp,day = max_temp(temps)
print(maxTemp,day)
