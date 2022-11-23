import pandas as pd
from datetime import date, datetime
import os
import csv

def insert_index_data(df: pd.DataFrame, index_name: str):
    assert df["Date"].dtypes == "datetime64[ns]", "Invalid Date column"

    dir_path = os.path.join(os.getcwd(),"Database", "index_data")
    filename = f"{index_name.upper()}.csv"
    files = os.listdir(dir_path)

    if not filename in files:
        print(f"[ERROR] file {index_name.upper()}.csv does not exists.")
        return


    last_line = ""
    for line in open(os.path.join(dir_path, filename)).readlines():
        last_line = line

    last_date = datetime.strptime(last_line.split(",")[0], "%d-%m-%Y")
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df = df[df["Date"] > date(last_date.year, last_date.month, last_date.day)]
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].dt.strftime('%d-%m-%Y')

    data = df.values.tolist()
    print(data[:5])

    with open(filename, 'a', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerows(data[:5])
        # for val in data[:1]:
        #     # print(val)
        #     val = [str(x) for x in val]
        #     writer.writerow(val)

    
    

df = pd.read_csv("NSE_NIFTY_2022-11-22_1D.csv", parse_dates=["Date"])
# df["Date"] = pd.to_datetime(df["Date"]).dt.date

# df = df[df["Date"] > date(2022, 11, 1)]
# df["Date"] = pd.to_datetime(df["Date"])
# df["Date"] = df["Date"].dt.strftime('%d-%m-%Y')

# print(df["Date"].dtypes == "datetime64[ns]")

insert_index_data(df, "nifty 50")
