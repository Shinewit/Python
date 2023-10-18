text = input("请输入一段话自动过滤敏感信息：")
datacase = ['操','bitch','fuck','nm']
for item in datacase:
    if item in text:
        text = text.replace(item,'*')
print(f'{text}')
