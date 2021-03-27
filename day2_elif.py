'''x = 5
print(x)
#宣告 declare 有創作意味
x = 10'''

# else if 另外如果
age = input('請輸入年齡: ')
age = int(age)
if age < 13:
	print('國小')
elif 13 <= age < 18: #age >=13 and age <18
	print('國高中')
elif age >= 18 and age < 22:
	print('大學')
else:
	print('社會')