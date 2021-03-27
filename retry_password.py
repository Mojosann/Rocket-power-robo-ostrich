# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出"登入成功!"
# 如果不正確 就印出"密碼錯誤! 還有__次機會!"

# default
password = 'a123456'
cont = 3

while True:
	user_pass = input('請輸入密碼: ')
	cont -= 1
	if user_pass == password:
		print('登入成功!')
		break
	elif cont > 0:
		print('密碼錯誤! 還有', cont, '次機會!')
	elif cont == 0:
		print('你沒機會了再見!')
		break