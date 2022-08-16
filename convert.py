import xdrlib
from re import sub
import re
from decimal import Decimal
from dateutil.parser import parse
import numpy as np
import pandas as pd
from datetime import datetime
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        # parse(string, fuzzy=fuzzy
        date_time_obj = datetime.strptime(string, '%d/%m')
        return True

    except:
        return False
datetahun="/2022"
f = open("aprjul2022.txt", "r")
csv_name = "aprjul2022.csv"
# print("{:.2f}".format(float("1573216.38")))
# print(f.readline(1))
# deleted = re.match(r'\d+(?:[.]\d{2})?$', '40.12')
result = []
resultindex = 0
for x in f:
    lines = x.split(' ')
    # print(lines)
    # print(len(lines[0]))
    # print(lines[0].find("/07"))
    # print(is_date(lines[0]))
    # print(": "+lines[0])
    # print(is_date(lines[0]))
    if(is_date(lines[0])):
        indexx= len(lines)-1
        x = lines[indexx].replace('\n', "", 1)
        # print(x)
        lines[indexx] = x
        deleteds=0
        for i in range(3):
            # print(lines[indexx-i])
            try:
                # deleted = Decimal(sub(r'[^\d.]', '',lines[indexx-i]))
                # print(deleted)
                # if(lines[indexx-i].find(",") != -1):
                stringcek = lines[indexx-i]
                sbstr = stringcek[len(stringcek) - 3]
                # print(sbstr)
                # print(lines[indexx-0])
                # deleted = re.match(r'\d+(?:[.]\d{2})?$', stringcek)
                # print(deleted)
                # stringcek="DB"
                # print(stringcek)
                # print(stringcek.find(".") == len(stringcek) - 3)
                if sbstr == "." and stringcek.find(".") == len(stringcek) - 3 and len(stringcek) >= 3:
                # print(deleted)
                    print(stringcek)
                    deleteds += 1
                # if deleted 
                # deleted = Decimal(sub(r'[^\d.]', '',lines[indexx-i]))
            except:
                deleteds -= 1
                # print("tidak bisa")
                # break
        # print(deleteds)
        if deleteds >= 2:
            lines.pop(indexx)
            indexx= len(lines)-1
        # print(lines)
        newresult = ["","","","","",""]
        newresult[0] = lines[0]+datetahun
        if lines[indexx] == "DB":
            # print("ini pengeluaran")
            lines.pop(indexx)
            indexx= len(lines)-1
            newresult[1] = 0  #ini pemasukan
            newresult[2] = lines[indexx]  #ini pengeluaran
            lines.pop(indexx)
            lines.pop(0)
            str = " ".join(lines)
            newresult[3] = "Pengeluaran"
            newresult[4] = "Pengeluaran"
            newresult[5] = str #ini pengeluaran
        else:
            # print("ini pemasukan")
            newresult[1] = lines[indexx]  #ini pemasukan
            newresult[2] = 0  #ini pengeluaran
            lines.pop(indexx)
            lines.pop(0)
            str = " ".join(lines)
            
            newresult[3] = "Pendapatan"
            newresult[4] = "Pendapatan"
            newresult[5] = str #ini pemasukan
        # print(newresult)
        result.append(newresult)
        resultindex += 1
        # print(len(lines))
        # print(lines[0])
    else: #tambahan
        # print(lines)
        indexx = len(lines) - 1
        lines[indexx] = lines[indexx].replace('\n', "", 1)
        str = " ".join(lines)
        resultindex = len(result) - 1
        indexresultitem = len(result[resultindex])-1
        result[resultindex][indexresultitem] += " " + str
        # print(str)
# print(result)
# print(len(result))
# print(result)
df = pd.DataFrame(result,columns=["date","amount","amountout","category","category1","catatan"])
df.to_csv(csv_name,index=False,sep=";")
# from tabula import read_pdf
# from tabulate import tabulate

# #reads table from pdf file
# df = read_pdf("foo.pdf",pages=1) #address of pdf file
# print(tabulate(df))