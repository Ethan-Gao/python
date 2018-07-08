# coding: utf-8
import math
import cmath

if __name__ == "__main__":
    # 数据处理
    print abs(-1.2), abs(4), abs(4.78)  # 取绝对值
    print math.floor(-1.23), math.floor(-3), math.floor(3.1), math.floor(4) # 下舍
    print math.ceil(1.23), math.ceil(-3.2), math.ceil(99)   # 上入
    print math.sqrt(4.7), math.sqrt(8), math.sqrt(0.1)  # math.sqrt仅能正数求平方根
    print cmath.sqrt(4.7), cmath.sqrt(8), cmath.sqrt(-18.1), cmath.sqrt(-9) # cmath.sqrt同时正数负数平方根
    print pow(2, 3), pow(2, 3, 4), pow(2, 3, 5) # pow(x, y[. z]) - 返回x的y次幂(所得结果对z取模)
    # 类型转换
    print int("123"), int(12.3), int(-1.23), int("-12")     # int("2.3")出错，若为字符串只能为整型
    print str(123), str("hello"), str("1hello0"), str(-1.23)
    print long(1.2), long(-12)
    # 用户输入
    print input("Numer: "), raw_input("Anything: ")
    # 打印结果
    print str(1000L), repr(1000L)
    print str("hello world"), repr("hello world")
    # 字符串处理
    print "c:\nowhere", r"c:\nowhere", "c:\\nowhere"
    print u"你好", "你好"
