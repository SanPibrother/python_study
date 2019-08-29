
def read():
    my_file = open("F:/test.txt")
    line = my_file.readline()
    my_dict = dict()
    index = 0
    while line:
        if "zte" in line:
            location = find_location(line)
            print(location)
            if location == 0:
                index = 0
            elif location == 7:
                index = 1
            elif location == 10:
                index = 2
            result = "com" + get_str_btw(line, "com", ":jar")

            my_dict.update({result: index})
        line = my_file.readline()
    print(my_dict)


# 取出字符串中间的部分
def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]


def find_location(str1):
    if str1.find("+") != -1:
        return str1.find("+")
    elif str1.find("\\") != -1:
        return str1.find("\\")
    else:
        return 0

read()

