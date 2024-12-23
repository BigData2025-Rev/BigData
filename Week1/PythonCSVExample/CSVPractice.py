import csv

# with open('C:/Users/WilliamTerry/Desktop/BigData2025GitHub/PythonCSVExample/airport_codes.csv') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row) 

file = open('C:/Users/WilliamTerry/Desktop/BigData2025GitHub/PythonCSVExample/airport_codes.csv','r')
csv_reader = csv.reader(file)
rows = [row for row in csv_reader]
Airports = [airport for code, airport in rows]
print(Airports[1:])
Airports_Codes = [code for code, airport in rows]
print(Airports_Codes[1:])
file.close()

file2 = open('C:/Users/WilliamTerry/Desktop/BigData2025GitHub/PythonCSVExample/airport_codes2.csv','w',newline="")
csv_writer = csv.writer(file2)
rowsNoHeader = rows[1:]
for row in rowsNoHeader:
    csv_writer.writerow(row)
file2.close()
