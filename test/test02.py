# def reverseWords(input):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#
#     return output
#
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)