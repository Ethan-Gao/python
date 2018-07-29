# coding: utf-8

if __name__ == "__main__":
    website = "http://www.python.org"
    # 基本操作
    print website[:5], website[-3:], 3 * website, len(website), max(website), min(website)
    # 修改: 出错
    # website[1] = None
    # print website
