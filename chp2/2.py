# coding: utf-8

if __name__ == "__main__":
    # 索引
    x = "hello"
    print x[0], x[2], x[-1], x[-3], "world"[4]
    ###
    months = ['January', 'February', 'Mach', 'April', 'May', 'June',\
             'July', 'August', 'September', 'October', 'November', 'December']
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + \
              ['st', 'nd', 'rd'] + 7 * ['th'] + \
              ['st']
    year, month, day = raw_input("Year: "), raw_input("Month:(1-12) "), raw_input("Day:(1-31) ")
    month_number, day_number = int(month), int(day)
    print months[month_number - 1] + " " + day + endings[day_number - 1] + "," + year

    # 分片
    y = [1, 2, 3, 4, 5, 6, 7]
    print y[0:2], y[5:7], y[0:-1], y[-1:0]
    print y[-3:-1], y[-4:-2], y[-3:1]
    print y[:3], y[-2:], y[:]
    ###
    url = raw_input("URL: ")
    print "Domain name: " + url[11:-4]

    # 步长
    print y[0:2:1], y[0:3:2], y[7:5:-2]
    print y[::-5], y[0:10:-2], y[5::-3], y[:5:-3]

    # 相加
    print [1, 2, 3] + [4, 5, 6]
    print "hello" + " " + "world"

    # 相乘
    print "hello" * 5
    print [1, 2, 3] * 10
    print [[1, 2, 3], "hello"] * 3
    print [None] * 4
    ###
    sentence = raw_input("Sentence: ")
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) // 2
    print
    print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '| ' + sentence + ' |'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
    print

    # 成员资格
    x = "hello world"
    print 'h' in x, 'x' in x, "wor" in x
    ###
    database = [["albert", "1234"], ["dilbert", "4242"], ["smith", "7524"], ["Jones", "9843"]]
    username, pin = raw_input("Name: "), raw_input("Pin: ")
    if [username, pin] in database:
        print "Access granted"

    # 长度、最大、最小
    numbers = [1, -10, 200, 34, 587]
    print len(numbers), max(numbers), min(numbers)
    print max(10, -2, 100), min(-100, 1000, 1)
