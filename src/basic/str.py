# encoding: utf-8
# descripting 字符串代码演示
# date

# '' 字符
str = 'lovecws babymm'
print(str)

# "" 字符
str2 = "lovecws anans"
print(str2)

# """字符
str3 = """lovecws'a;s;s;'alslslsaa"""
print(str3)

# 字符串拼接
str = str + str2 + str3
print(str)

# 格式占位符 %s 非常类似于c语言的printf格式化输出
str = "lovecws babymm by %s " % ("ganliang")
print(str)

str = "love%s and %s by %s" % ("陈伟生", "甘子慕", "甘亮")
print(str)

# 更多字符串格式 10s代表该字段所占用的字符长度 如果字符不够这个长度 以空格代替 -10s 空格填充在右边 否则填充在左边
str = "love%-10s and %s by %10s" % ("陈伟生", "甘子慕", "甘亮")
print(str)

# 整数
print("lovecws %d" % 5211314)

# 浮点数 取几位小数点
print("lovecws %f" % 12.4444999)
print("lovecws %.2f" % 12.4444999)
print("lovecws %0.f" % 12.4444999)

# \n换行符 \t水平制表符
print("lovecws anana\n\tlalalsls\ton")

print(str.upper())
print(str.lower())

print(str.isupper())
print(not str.isupper())

print(True and True)
