first_number = float(input('Enter the first number: '))
second_number = float (input('Enter the second number: '))
if first_number < second_number:
    print(f'{first_number} is smallest then {second_number}')
elif first_number > second_number:
    print(f'{first_number} greater then {second_number}')
else:
    print('The numbers are equals')

