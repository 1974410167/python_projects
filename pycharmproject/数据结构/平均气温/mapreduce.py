

# 定义读取txt文件函数
def load_data():

    # with 上下文管理器，打开文件，并自动关闭
    with open('beijing.txt','r',encoding='utf-8') as f:
        list = f.readlines()

    # 返回列表，不带第一行
    return list[1:]

# 定义解析txt文件数据的函数
def mapper():

    #调用load_data函数

    list = load_data()

    # 把每天数据放入字典，格式为{'20160101':[-2,-3,-3,-4........],'20160102':[............]}
    dict = {}

    for i in list:

        # 把每一行数据按照','号分隔，返回一个列表
        s = i.split(',')

        # 排除脏数据
        if s[5] == 'N/A':
            continue

        if s[0] not in dict:
            dict[s[0]] = [int(s[5])]
        else:
            dict[s[0]].append(int(s[5]))

    return dict

# 定义计算月平均温度的函数
def reducer():

    # 调用mapper()函数
    dict = mapper()

    # 存放每月的所有温度，格式为{'201601':[..........六百多个数据]，'201602':[............六百多个数据]}
    dict1 = {}

    for i in dict:
        if i[0:6] not in dict1:
            dict1[i[0:6]] = dict[i]
        else:
            dict1[i[0:6]] += dict[i]


    # 计算平均温度，key为日期，value为平均温度，如{'201601':-3.81,'201602':1.68,..................}
    dict2 = {}

    for j in dict1:
        m = sum(dict1[j]) / len(dict1[j])
        dict2[j] = m

    return dict2
# 调用函数
if __name__ == '__main__':

    # 调用reducer()函数
    dict3 = reducer()
    for i in dict3:
        t = dict3[i]

        # 保留两位小数
        t = round(t,2)

        # 格式化输出
        print(i+' '+str(t))
