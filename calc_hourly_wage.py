# Names to represent regular hours and overtime pay
REG_HOURS = 40
OT_Mul = 1.5

# Get wage and amount of hours worked.
wage = float(input('Enter the wage: '))
hours = float(input('Enter the amount of hours worked: '))

if hours > REG_HOURS:
    # Number of OT hours worked.
    OT_hours = hours - REG_HOURS

    # Calculate weekly pay with overtime.
    OT_pay = OT_hours * wage * OT_Mul

    # Calculate weekly pay.
    Weekly_pay = REG_HOURS * wage + OT_pay

    # Calculate weekly pay without OT.
else:
    Weekly_pay = hours * wage

    # Display the weekly pay.
print('The total weekly pay is $', format(Weekly_pay,',.2f'), sep='')