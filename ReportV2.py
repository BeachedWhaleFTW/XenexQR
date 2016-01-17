import pandas as pd
from functions import *
import numpy as np
import csv

filename_V2 = raw_input('Please enter the .CSV file name (extension included) for V2: ')
all_data_V2 = pd.read_csv(filename_V2)
days = input('Please enter the number of days in the Quarter: ')

accounts_V2 = list(set(all_data_V2.Customer))
accounts_V2 = accounts_V2[1::]
accounts_V2 = sorted(accounts_V2)

writer = pd.ExcelWriter('FinishedReportV2.xlsx', engine = 'xlsxwriter')
for account in accounts_V2:
	index_num = accounts_V2.index(account)
	data_account_fun_V2(account, all_data_V2, days).to_excel(writer, sheet_name=str(index_num))
	roomstate_account_fun_V2(account, all_data_V2).to_excel(writer, sheet_name = str(index_num), startrow = 0, startcol = 6)
	dates_account_fun_V2(account, all_data_V2).to_excel(writer, sheet_name=str(index_num), startrow = 0, startcol = 10)

index_key_V2 = [n for n in range(len(accounts_V2))]
key_V2 = [[index_key_V2],[accounts_V2]]
key_V2 = np.asarray(key_V2).T.tolist()
csvfile = 'KeyV2.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(key_V2)
