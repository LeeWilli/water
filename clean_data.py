import pandas as pd

def delete_null_date(B2, date_name):
    B2 = B2[B2[date_name].notnull()]  # 删除日期存在缺失的数据
    return B2

def divide_table(B2, col, a, b):
    A = B2[B2[col]==a]
    B = B2[B2[col] == b]
    return A, B

def TimeTrains(ls):
    lis = ls
    if len(ls) == 8 and '/' not in ls:
        year = ls[0:4]
        month = ls[4:6]
        day = ls[6:]
        lis = year + '-' + month + '-' + day
    elif len(ls) == 8 and '/' in ls:
        lss = ls.split('/')
        lis = lss[0] + '-' + '0' + lss[1] + '-' + '0' + lss[2]
    elif len(ls) == 6:
        if ls[0:2] != '20':
            year = '20' + ls[0:2]
            month = ls[2:4]
            day = ls[4:]
            lis = year + '-' + month + '-' + day
    elif len(ls) == 10 and '/' not in ls:
        lss = ls.split('.')
        lis = lss[0] + '-' + lss[1] + '-' + lss[2]
    elif len(ls) == 10 and '/' in ls:
        lss = ls.split('/')
        lis = lss[0] + '-' + lss[1] + '-' + lss[2]
    elif len(ls) == 7:
        year = ls[0:4]
        month = ls[4:5]
        day = ls[5:]
        lis = year + '-' + '0' + month + '-' + day
    elif '.' in ls:
        lss = ls.split('.')
        lis = lss[0] + '-' + lss[1] + '-' + '0' + lss[2]
    elif len(ls) == 9 and '/' not in ls:
        year = ls[0:4]
        month = ls[5:7]
        day = ls[7:]
        lis = year + '-' + month + '-' + day
    elif len(ls) == 9 and '/' in ls:
        lss = ls.split('/')
        lis = lss[0] + '-' + '0' + lss[1] + '-' + lss[2]
    return lis


def convert_date(B2, column_name):
    lenlength = len(B2[column_name])
    cpB2 = []
    last_date = ''
    for d in B2[column_name]:
        try:
            cpB2.append(TimeTrains(d))
            last_date = TimeTrains(d)
        except TypeError:
            cpB2.append(last_date)
        except  KeyError:
            cpB2.append(last_date)

    print(len(cpB2))
    print(len(B2))
    B2.drop(column_name, axis=1, inplace=True)
    B2.insert(2, column_name, cpB2)
    return B2
