while True:
    num_str = input("请依次输入币值与符号(￥/$):")
    num = float(num_str[0:-1]) # 切片一串数据 左闭右开
    num_fu =num_str[-1] # 接受最后一个一串数据末尾的值
    if (num_fu == "￥"):
        M = num * 0.145
        print("您人民币转换为美币的金额为：%.5f$(结果保留五位小数)" % M)
        break
    elif (num_fu == "$"):
        D = num * 6.8833
        print("您美币转换为人民币的金额为：%5.5f￥(结果保留五位小数)" % D)
        break
    else:
        print("输入错误请重新尝试")
        continue