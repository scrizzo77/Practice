name = input("Enter employee name: ")
pay_rate = int(input("Enter hourly pay rate: "))
working_hours = []
for i in range(0,7):
    hours = int(input())
    working_hours.append(hours)

def total_pay(pay_rate,working_hours):
    weekdays = 0
    total_hours = 0
    for i in range(0,len(working_hours)):
        total_hours += working_hours[i]
    for i in range(0,5):
        weekdays += working_hours[i]
    weekdays = weekdays * pay_rate
    saturday = working_hours[5] * pay_rate * 1.5
    sunday = working_hours[6] * pay_rate * 2
    total = weekdays + saturday + sunday
    return total_hours, total

total_hours,total = total_pay(pay_rate,working_hours)
print(f"Name: {name}  Total hours worked: {total_hours}  Total pay: £{total}")
