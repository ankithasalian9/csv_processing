import json
import numpy as np
import pandas as pd
import os
import csv
import numpy

input_columns = ["UID","Expense","UserInfo"]

df = pd.read_csv("./csv_1.csv")

result_data = dict()
for row in range(len(df)):
    userinfo = df["UserInfo"]
    exp = df["Expense"]

    uid = df["UID"]
    
    #print(uid[row], exp[row], userinfo[row])

    try:
        jsonUserinfo = json.loads(userinfo[row])

        fname = jsonUserinfo["name"]["fname"]
        lname = jsonUserinfo["name"]["lname"]
        add = jsonUserinfo["address"]
        pin = jsonUserinfo["pin"]
    except:
        fname = ""
        lname = ""
        add = ""
        pin = ""

    rowd ={"UID": uid[row], "Fname":fname, "Lname": lname, "Address":add, "pin":pin,"Total Expenses":exp[row]}
    if uid[row] in result_data:
        result_data[uid[row]]["Total Expenses"]+=exp[row]
    else:
        result_data[(uid[row])]=rowd   
    
    
#print(result_data)
with open("output.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["UID","Fname","Lname","Address","pin","Total Expenses"])
        writer.writeheader()
        for data in result_data.values():
            writer.writerow(data)