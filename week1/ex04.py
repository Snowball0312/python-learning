"""
ex04 累加求和

第一个任务：
    用循环算出 1 + 2 + ... + 100，输出结果。

第二个任务：
    改成让用户输入一个数 n，算 1 + 2 + ... + n。

示例：
    输入 10  ->  55
    输入 0   ->  0

提示：
    - 用一个变量存累加结果，初始值设为 0
    - 用 for 搭配 range()
    - 想一想 n 为 0 时，你的循环范围会不会出问题

自测：1、10、0 三个输入
"""

total = 0
for i in range(1,101):
    total += i                 
print(total)
n = int(input("请输入一个数 n:"))
total = 0
for i in range(1,n+1):
    total += i
print(total)
