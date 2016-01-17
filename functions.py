def data_account_fun_V2(account, all_data, days):
	account_data = all_data[all_data.Customer == account]
	data_account = account_data.pivot_table(values = ['# Rooms(Disinfections)', 'Total Run (Sec.)',
		'Sum Num Flashes'], index = 'Customer', aggfunc = sum)
	data_account['RPD'] = data_account['# Rooms(Disinfections)']/days
	data_account['Total Run Time (Hours)'] = data_account['Total Run (Sec.)']/(60*60)
	data_account = data_account[['# Rooms(Disinfections)', 'RPD','Total Run Time (Hours)', 'Sum Num Flashes']]
	
	return data_account

def roomstate_account_fun_V2(account, all_data):
	account_data = all_data[all_data.Customer == account]
	roomstate_account = account_data.pivot_table(values = ['# Rooms(Disinfections)', 'Sum Num Flashes'], index = 'Room State', aggfunc = sum)

	return roomstate_account

def dates_account_fun_V2(account, all_data):
	account_data = all_data[all_data.Customer == account]
	dates_account = account_data.pivot_table(values= ['# Rooms(Disinfections)', 'Sum Num Flashes'], index = 'Date Start', aggfunc = sum)

	return dates_account

def data_account_fun_V3(account, all_data, days):
	account_data = all_data[all_data.HOSPITAL == account]
	data_account = account_data.pivot_table(values = ['ROOMS DISINFECTED', 'TOTAL RUN SECS', 'SUM NUM FLASHES'], index = 'HOSPITAL', aggfunc = sum)
	data_account['RPD'] = data_account['ROOMS DISINFECTED']/days
	data_account['Total Run Time (Hours)'] = data_account['TOTAL RUN SECS']/(60*60)
	data_account = data_account[['ROOMS DISINFECTED', 'RPD', 'Total Run Time (Hours)', 'SUM NUM FLASHES']]

	return data_account

def roomstate_account_fun_V3(account, all_data):
	account_data = all_data[all_data.HOSPITAL == account]
	roomstate_account = account_data.pivot_table(values = ['ROOMS DISINFECTED', 'SUM NUM FLASHES'], index = 'ROOM STATE', aggfunc = sum)

	return roomstate_account

def dates_account_fun_V3(account, all_data):
	account_data = all_data[all_data.HOSPITAL == account]
	dates_account = account_data.pivot_table(values = ['ROOMS DISINFECTED', 'SUM NUM FLASHES'], index = 'START DATE', aggfunc = sum)

	return dates_account