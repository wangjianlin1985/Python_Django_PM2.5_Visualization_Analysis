
import numpy
import csv

city_list = ['北京', '上海', '广州', '成都', '沈阳']

def a1():
    time_list = ['2010', '2011', '2012', '2013', '2014', '2015']
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)
        data_dict = {}
        for i in data_list:
            if '.' in i[5]:
                i[5] = i[5].split('.')[0]
            for times in time_list:
                if times in i[1] and not i[5] == '缺失':
                    if data_dict.get(times):
                        data_dict[times].append(int(i[5]))
                    else:
                        data_dict[times] = [int(i[5])]
                    break
        for c, i in data_dict.items():
            print(c, city, int(numpy.mean(i)))
            out = open('时间序列逐年数据.csv', 'a', newline='', encoding='utf-8-sig')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow([c, city, int(numpy.mean(i))])
            out.close()
def a2():
    time_list = ['春', '夏', '秋', '冬']
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        data_dict = {}
        for i in data_list:
            if '.' in i[5]:
                i[5] = i[5].split('.')[0]
            for times in time_list:
                if times in i[2] and not i[5] == '缺失':
                    if data_dict.get(times):
                        data_dict[times].append(int(i[5]))
                    else:
                        data_dict[times] = [int(i[5])]
                    break

        for c, i in data_dict.items():
            print(c, city, int(numpy.mean(i)))
            out = open('不同季度逐年数据.csv', 'a', newline='', encoding='utf-8-sig')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow([c, city, int(numpy.mean(i))])
            out.close()
def a3():
    time_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        data_dict = {}
        for i in data_list:
            if '.' in i[5]:
                i[5] = i[5].split('.')[0]
            i[1] = i[1].split('/')[1]
            for times in time_list:
                if times == i[1] and not i[5] == '缺失':
                    if data_dict.get(times):
                        data_dict[times].append(int(i[5]))
                    else:
                        data_dict[times] = [int(i[5])]
                    break

        for c, i in data_dict.items():
            print(c, city, int(numpy.mean(i)))
            out = open('一年中各个月份变化.csv', 'a', newline='', encoding='utf-8-sig')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow([c, city, int(numpy.mean(i))])
            out.close()
def a4():
    time_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23']

    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        data_dict = {}
        for i in data_list:
            if '.' in i[5]:
                i[5] = i[5].split('.')[0]
            i[1] = i[1].split(' ')[1].split(':')[0]
            # print(i)
            for times in time_list:
                if times == i[1] and not i[5] == '缺失':
                    if data_dict.get(times):
                        data_dict[times].append(int(i[5]))
                    else:
                        data_dict[times] = [int(i[5])]
                    break

        for c, i in data_dict.items():
            print(c, city, int(numpy.mean(i)))
            out = open('一天中不同时段.csv', 'a', newline='', encoding='utf-8-sig')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow([c, city, int(numpy.mean(i))])
            out.close()
def a6():
    time_list = ['东南风', '西南风', '西北风', '东北风']
    dara = {}
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        data_dict = {}
        for i in data_list:
            if '.' in i[5]:
                i[5] = i[5].split('.')[0]
            i[1] = i[1].split(' ')[1].split(':')[0]
            # print(i)
            for times in time_list:
                if times == i[11] and not i[5] == '缺失':
                    if data_dict.get(times):
                        data_dict[times].append(int(i[5]))
                    else:
                        data_dict[times] = [int(i[5])]
                    break

        for c, i in data_dict.items():
            print(c, city, int(numpy.mean(i)))
            out = open('与风向之间的关系.csv', 'a', newline='', encoding='utf-8-sig')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow([c, city, int(numpy.mean(i))])
            out.close()
def a7():
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        for item in data_list:
            print(item)
            # 先将pm2.5 和 露点进行数值转换
            if not item[6] == '缺失' and not item[7] == '缺失':
                item[6] = float(item[6])
                item[7] = float(item[7])
                print(city, item[6], item[7])
                out = open('pm2.5与露点之间的关系.csv', 'a', newline='', encoding='utf-8-sig')
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow([city, item[6], item[7]])
                out.close()
def a8():
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        for item in data_list:
            print(item)
            # 先将pm2.5 和 露点进行数值转换
            if not item[6] == '缺失' and not item[8] == '缺失':
                item[6] = float(item[6])
                item[8] = float(item[8])
                print(city, item[6], item[8])

                out = open('pm2.5与相对湿度之间的关系.csv', 'a', newline='', encoding='utf-8-sig')
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow([city, item[6], item[8]])
                out.close()
def a9():
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        for item in data_list:
            print(item)
            # 先将pm2.5 和 露点进行数值转换
            if not item[6] == '缺失' and not item[10] == '缺失':
                item[6] = float(item[6])
                item[10] = float(item[10])
                print(city, item[6], item[10])

                out = open('pm2.5与温度之间的关系.csv', 'a', newline='', encoding='utf-8-sig')
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow([city, item[6], item[10]])
                out.close()
def a10():
    for city in city_list:
        with open('%s.csv' % city, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        for item in data_list:
            print(item)
            # 先将pm2.5 和 露点进行数值转换
            if not item[6] == '缺失' and not item[9] == '缺失':
                item[6] = float(item[6])
                item[9] = float(item[9])
                print(city, item[6], item[9])

                out = open('pm2.5与大气压之间的关系.csv', 'a', newline='', encoding='utf-8-sig')
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow([city, item[6], item[9]])
                out.close()

if __name__ == '__main__':

    # a1()
    # a2()
    # a3()
    # a4()
    # a6()
    # a7()
    # a8()
    # a9()
    # a10()
    pass
