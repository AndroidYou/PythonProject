"""
 输入和输出
 1.表达式语句
 2.print函数
 3.使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用
 4.使用 str.format() 函数来格式化输出值
 5.将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现

str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
rjust()：以将字符串靠右, 并在左边填充空格
 ljust() 和 center() 它们仅仅返回新的字符串。
  zfill(), 它会在数字的左边填充 0

  str.format() 的基本使用

 1. print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
  括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。

2.print('{0} 和 {1}'.format('Google', 'Runoob'))
如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:

可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi)) # 常量 PI 的值近似为 3.142。

旧式字符串格式化
% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串.
print('常量 PI 的值近似为：%5.3f。' % math.pi)

"""
if __name__ == '__main__':
    s = "hello ,world,android"
    print(str(s))  # hello ,world,android
    print(repr(s))  # 'hello ,world,android'
    for x in range(1, 11):  # rjust  返回长度-宽度右对齐的字符串。填充使用指定的填充字符（默认为空格）完成。
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
        print(repr(x * x * x).rjust(4))

    for i in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(i, i * i, i * i * i))

        """
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
        """
