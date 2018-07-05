# coding: utf-8

if __name__ == "__main__":
    # 强制转换
    print type(2.34), type("hello"), type(str(2.34))
    print 2.34, "hello", str(2.34)
    # 转义字符串
    print "hello", "\"world\"", "let\'s go"
    print "\"let\'s say \"hello world\"\""
    # 拼接字符串
    x, y = "hello", "worl"
    z = "d"
    print x, y, z
    print x + " " + y + z
    # str和repr
    print "hello", str("hello"), repr("hello")
    print 1000L, repr(1000L)
    print type(str(123)), type(123), type(123.456)
    # 长字符串
    print """hello
    world"""
    print "hello\
    world"
    print 1 + 2 + \
        3 + 4
    # 原始字符串
    print "c:\nowhere", "c:\\nowhere"
    print r"c:\nowhere", r"c:\nowhere\\", r"c:\nowhere" + "\\"
    # unicode字符串
    print u"친구야안녕", u"こんにちは", u"你好"
