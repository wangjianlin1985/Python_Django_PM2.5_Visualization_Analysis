

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', charset="utf8")
cursor = conn.cursor()
cursor.execute("use db129")
#
# sql = """
# create table pm25(
#     id int not null primary key auto_increment,
#     times varchar(128),
#     jj varchar(128),
#     pm1 varchar(128),
#         pm2 varchar(128),
#     pm3 varchar(128),
#     pmpj varchar(128),
#     ld varchar(128),
#     xdsd varchar(128),
#     dqy varchar(128),
#     wd varchar(128),
#     fx varchar(128),
#     ljfs varchar(128),
#     xsjsl varchar(128),
#     ljjsl varchar(128),
#     city varchar(128)
#
#
# )default charset=utf8;
# """
# cursor.execute(sql)
# conn.commit()
#
# cursor.close()
# conn.close()
import csv
with open('北上广成沈五城市六年PM2.5数据汇总 1.csv', 'r',encoding='gbk') as f:
    reader = csv.reader(f)
    data_list = list(reader)

for i in data_list[1:]:
    print(i)
# da_list =['重庆', '少数民族预科班', '文史类', '少数民族预科班', '593', '590.5', '588', '2', '17年录取分数线']
    sql2 = "insert into pm25(times,jj,pm1,pm2,pm3,pmpj,ld,xdsd,dqy,wd,fx,ljfs,xsjsl,ljjsl,city) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15]
    )
    cursor.execute(sql2)
    conn.commit()
#
cursor.close()
conn.close()