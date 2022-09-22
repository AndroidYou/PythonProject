"""
 条件控制

 if 语句

 if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3


1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
"""
if __name__ == '__main__':
    a = 1
    while a < 7:
        if a % 2 == 0:
            print(a, "is Even")
        else:
            print(a, "is odd")
        a += 1

    """
1 is odd
2 is Even
3 is odd
4 is Even
5 is odd
6 is Even
    """
