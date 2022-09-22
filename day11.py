"""
 编程第一步

end 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
"""

if __name__ == '__main__':
    a, b = 0, 1
    while b < 10:
        print(b, end=",")
        a, b = b, a + b
