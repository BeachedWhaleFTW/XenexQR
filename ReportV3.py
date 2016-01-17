import pandas as pd
from functions import *
import numpy as np
import csv

filename_V3 = raw_input('Please enter the .CSV file name (extension included) for V3: ')
all_data_V3 = pd.read_csv(filename_V3)
days = input('Please enter the number of days in the Quarter: ')

accounts_V3 = list(set(all_data_V3.HOSPITAL))
accounts_V3 = accounts_V3[1::]
accounts_V3 = sorted(accounts_V3)

writer = pd.ExcelWriter('FinishedReportV3.xlsx', engine = 'xlsxwriter')
for account in accounts_V3:
	index_num = accounts_V3.index(account)
	data_account_fun_V3(account, all_data_V3, days).to_excel(writer, sheet_name=str(index_num))
	roomstate_account_fun_V3(account, all_data_V3).to_excel(writer, sheet_name = str(index_num), startrow = 0, startcol = 6)
	dates_account_fun_V3(account, all_data_V3).to_excel(writer, sheet_name=str(index_num), startrow = 0, startcol = 10)

index_key_V3 = [n for n in range(len(accounts_V3))]
key_V3 = [[index_key_V3],[accounts_V3]]
key_V3 = np.asarray(key_V3).T.tolist()
csvfile = 'KeyV3.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(key_V3)
