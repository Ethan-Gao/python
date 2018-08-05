# coding: utf-8
from string import maketrans

if __name__ == "__main__":
    # find
    str = "Today is sunday"
    print str.find("is"), "hello world".find("h"), "hello world".find("jack")
    subject = "$$$ get rich now!!! $$$"
    print subject.find("$$$"), subject.find("$$$", 1), \
          subject.find("!!!"), subject.find("!!!", 0 , 16)
    # join
    val = "+"
    x, y = ["1", "2", "3", "4"], ("", "usr", "local", "bin")
    # z = [1, 2, 3, 4] 报错，join只能字符串
    print val.join(x), "/".join(y)
    # lower
    names, name = ["John", "Tom", "Ethan"], "ToM"
    print name.lower()
    if name.lower() in names: print "Found it"
    # replace
    print "This is a test", ";", "This is a test".replace("is", "ha")
    # split
    str1, x1 = "1+2+3+4", "+"
    str2, x2 = "/usr/local/bin", "/"
    str3 = "Using the default"
    print str1.split(x1), str2.split(x2), str3.split()
    # strip
    print "Hello world"
    print "   hello world ".strip()
    print "   hello world".strip()
    # translate
    table = maketrans("cs", "kz")
    print len(table), table[97:123] # 打印转换结果
    print "This is just test".translate(table)
