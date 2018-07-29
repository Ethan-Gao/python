# coding: utf-8
import string

if __name__ == "__main__":
    # 字符-%s
    print "hello %s" % "world"
    print "%s is %s" % ("more", "mehr")
    print "possibility  is %%%d" % 97
    # 浮点-%f
    print "pi is %.3f" % 3.14159
    # 整型-%d
    print "%d + %d = %d" % (1, 2, (1 + 2))
    # 16进制-%x
    print "%d is 0x%x" % (16, 16)
    # 模板字符串
    s1, s2 = string.Template("hello $x"), string.Template("It's ${x}tastic")
    print s1.substitute(x="world"), s2.substitute(x="fan")
