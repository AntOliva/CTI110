# Oliva Anthony
# 3/15/2025
# P3HW2
# Determine OT pay, regular pay, and gross pay

employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
pay_rate = float(input("Enter pay rate: "))
print(f"Employee Name:{employee_name}")
#Determine if employee worked any overtime

if hours_worked > 40:
    OT_hours_worked = hours_worked - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT_hours_worked * OT_pay_rate
    reg_pay = 40 * pay_rate

# hours_worked <= 40
else: 
    OT_hours_worked = 0
    OT_pay = 0
    reg_pay = hours_worked * pay_rate

gross_pay = OT_pay + reg_pay

#Output the values


# Display the values in columns
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OT Hours': <20}{'Gross Pay':<20}")
print("-----" * 15)
print(f"{hours_worked:<20.2f}${pay_rate:<20.2f}{OT_hours_worked:<20.2f}${gross_pay:<20.2f}")





