import pandas as pd
from tabulate import tabulate

etf_data = pd.read_csv("data/etf_data_march_2021.csv")

def printTable(df):
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

# Gold ETF has no tracking error hence its enough to go by lowest expense ratio
def pickGoldETF():
    gold_etf = etf_data[etf_data["Sub-Sector"] == "Gold"]
    printTable(gold_etf[gold_etf["Expense Ratio"] == gold_etf["Expense Ratio"].min()])

# Large Cap ETF (consider tracking error where available)
def pickLargeCapETF():
    equity_etfs = etf_data[etf_data["Sub-Sector"] == "EQUITY"]


# Pick foreign ETF's (There's only one)
def pickForeignETF():
    return None
        

if __name__ == "__main__":
    print("Gold ETF Selection")
    pickGoldETF()
    print("NIFTY Large Cap ETF Selection")
    pickLargeCapETF()
    print("NIFTY MidCap ETF Selection")
    print("NIFTY GSec ETF Selection")
    print("Foreign ETF")