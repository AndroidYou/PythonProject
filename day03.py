"""
  数据类型转换
  1、隐式类型转换-自动完成
  2 显式类型转换 -需要使用类型函数来转换
  int(x [,base])

将x转换为一个整数  float(x)

将x转换到一个浮点数 complex(real [,imag])

创建一个复数  str(x)

将对象 x 转换为字符串  repr(x)

将对象 x 转换为表达式字符串  eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象  tuple(s)

将序列 s 转换为一个元组  list(s)

将序列 s 转换为一个列表  set(s)

转换为可变集合 dict(d)

创建一个字典。d 必须是一个 (key, value)元组序列。 frozenset(s)

转换为不可变集合 chr(x)

将一个整数转换为一个字符  ord(x)

将一个字符转换为它的整数值 hex(x)

将一个整数转换为一个十六进制字符串 oct(x)
"""
if __name__ == '__main__':
    num_int = 123
    num_flo = 12.3
    num_new = num_flo + num_int
    print(num_int, type(num_int))  # 123 <class 'int'>
    print(num_flo, type(num_flo))  # 12.3 <class 'float'>
    print(num_new, type(num_new))  # 135.3 <class 'float'>
    '''
      Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失。
    '''
    num_str = "3"

    # num_str + num_flo 报错
    x = int(1)
    print(x)  # 1
    y = float(2)
    print(y)  # 2.0
    z = str(3)
    print(z, type(z))  # "3" <class 'str'>
