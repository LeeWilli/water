from clean_data import *

import pandas as pd
water = pd.read_csv('water.csv')
water = delete_null_date(water, 'Date')
water = convert_date(water, 'Date')
water.to_csv('water_a.csv', index = None)

parameter = pd.read_csv('parameter.csv', encoding="gb18030")

parameter = delete_null_date(parameter, 'Date')
parameter = delete_null_date(parameter, 'R4')
parameter = convert_date(parameter, 'Date')
parameter.to_csv('parameter_date.csv', index = None)
#water1 = convert_date(water, 'Date')
#water1.to_csv('water1.csv', index = None)
#parameter = delete_null_date(parameter, 'R4')
#parameter = delete_null_date(parameter, 'Date')
#parameter.to_csv('parameter_no_null.csv', index = None)

#parameter = convert_date(parameter, 'Date')
A, B = divide_table(parameter, 'L4', 'A组','B组')
A.to_csv('A.csv', index = None)

watera = pd.merge(water, parameter,  on=['Date'], how='left')
#watera = delete_null_date(watera, 'R4')
watera.to_csv('water_a.csv', index = None)

waterb = pd.merge(water, B,  on=['Date'], how='left')
#waterb = delete_null_date(waterb, 'R4')
waterb.to_csv('water_b.csv', index = None)