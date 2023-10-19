print("请依次输入用户名、密码、邮箱，字符长度超过二十将会自动截去超出部分")
user = input("请输入用户名：")
password = input("请输入密码：")
mail = input("请输入邮箱（邮箱会自动添加后缀）：")
user = user[:20]
password = password[:20]
mail = mail[:20] + "@-mail"
a = "用户名"
b = "密码"
c = "邮箱"
print(f'{a:<25}{b:<25}{c:<25}')
print(f'{user:<25}{password:<25}{mail:<25}')