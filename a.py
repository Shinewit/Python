#分支嵌套
#请输入一个正整数，判断是否能被2和3整除
num = int(input("请输入一个整数："))
if num %2 == 0:
    if num %3 == 0:
        print(f'这个数能被2和3整除')
    else:
        print("能被2整除不能被3整除")
else:
    print("这个数不能被2整除")