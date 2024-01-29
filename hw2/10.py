phone_number = input()
number_phone = phone_number.replace('-', '').replace(')', '').replace('(', '').replace(' ', '')
print(number_phone)