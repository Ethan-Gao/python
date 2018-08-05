# coding: utf-8
from math import pi

if __name__ == "__main__":
    ### 简单转换
    val1 = int(raw_input("int value: "))
    print val1, ", %d, %x, %o" % (val1, val1, val1)
    val2 = float(raw_input("float value: "))
    print val2, ", %e, %E, %f, %F" % (val2, val2, val2, val2)
    val3 = str(raw_input("string value: "))
    print val3, ", %s, %r" % (val3, val3)
    ### 完整版
    # 字段宽度与精度
    print "%10f" % pi   # 字段宽10
    print "%10.2f" % pi # 字段宽10，精度2
    print "%.2f" % pi   # 精度2
    print "%.5s" % "hello world", "%0.*s" % (5, "hello world")
    # 符号、对齐、0补充
    print "%f" % pi
    print "%010.2f" % pi    # 宽度不足10用0补充
    print "%-10.2f" % pi    # 左对齐，不足10位空格补齐
    print ("% 5d" % 10) + "\n" + ("% 5d" % -10)
    print ("%+5d" % 10) + "\n" + ("%+5d" % -10)
    # 字符串格式化实例
    width = input("Please enter width: ")
    price_width = 10
    item_width = width - price_width
    header_format, my_format = "%-*s%*s", "%-*s%*.2f"

    print "=" * width
    print header_format % (item_width, "Item", price_width, "Price")
    print "-" * width
    print my_format % (item_width, "Apples", price_width, 0.4)
    print my_format % (item_width, "Pears", price_width, 0.5)
    print my_format % (item_width, "Cantaloupes", price_width, 1.92)
    print my_format % (item_width, "Peach", price_width, 8)
    print my_format % (item_width, "Tomato", price_width, 12)
    print "=" * width
