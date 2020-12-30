from pathlib import Path
import os
import csv
import pandas


# with open(str(Path('c://') / 'find' / 'weather_data.csv')) as cvs_open:
#     cvs_data_list = cvs_open.readlines()
# print(cvs_data_list)

# with open(str(Path('c://') / 'find' / 'weather_data.csv')) as cvs_open:
#     csv_object = csv.reader(cvs_open)
#     list_temp = []
#     for row in csv_object:
#         print(row)
#         if row[1].isnumeric():
#             list_temp.append(int(row[1]))
#     print(list_temp)


data_csv = pandas.read_csv(str(Path('c://') / 'find' / 'census.csv'))
os.system('cls')
# print(type(data_csv))
# temp_list = data_csv['temp'].max()
# print(temp_list)
# print(data_csv[data_csv.temp == temp_list])

# monday = data_csv[data_csv.day == 'Monday']
# print(monday.condition)
# # f=(c*1.8)+32
# print((monday.temp*1.8)+32)

# a = pandas.DataFrame(monday)
# a.to_csv('a.csv')
# gray = 
print(data_csv['Fur_Color'].count())