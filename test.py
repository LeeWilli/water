from clean_data import *

import pandas as pd
water = pd.read_csv('water_a.csv')
parameter = pd.read_csv('parameter_date.csv', encoding="gb18030")

watera = pd.merge(water, parameter,  on=['Date'], how='left')
#watera = delete_null_date(watera, 'R4')
watera.to_csv('water_p.csv', index = None)

