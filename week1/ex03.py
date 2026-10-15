"""
ex03 成绩等级

要求：
    输入 0 到 100 之间的分数，输出等级：
        90 及以上 -> A
        80 及以上 -> B
        70 及以上 -> C
        60 及以上 -> D
        60 以下   -> F
    如果输入不在 0 到 100 之间，输出"分数不合法"。

示例：
    输入 95  ->  A
    输入 90  ->  A
    输入 59  ->  F
    输入 120 ->  分数不合法

提示：
    - 先判断合不合法，再判断等级
    - 用 if / elif / else 从上往下写，条件顺序会影响结果，想清楚再落笔

自测：90、89、60、59、0、100、-1、101 各测一遍
"""

score = int(input("请输入一个分数（0-100）:"))
if score < 0 or score > 100:
    print("分数不合法")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")