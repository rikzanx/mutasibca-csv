import csv
import pandas as pd

datetahun="/2022"
csv_name = "agust2022.csv"
result = []
with open('agust.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if(row[4])
        newresult = ["","","","","",""]
        newresult[0] = row[0]+datetahun #tanggal
        row[1] = row[1].replace('\n'," ")
        newresult[5] = row[1] #note
        
        print(row[1])
        if(row[4] == "DB"):
            newresult[4] = "Pengeluaran"
            newresult[3] = "Pengeluaran"
            newresult[1] = 0
            newresult[2] = row[3]
        else:
            newresult[4] = "Pendapatan"
            newresult[3] = "Pendapatan"
            newresult[2] = 0
            newresult[1] = row[3]
        result.append(newresult)
    # print(f'Processed {line_count} lines.')

df = pd.DataFrame(result,columns=["date","amount","expense","category","category1","note"])
df.to_csv(csv_name,index=False,sep=";")