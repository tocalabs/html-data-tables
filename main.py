from DataTables.datatables import TocaData

Data = TocaData()

URL = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/risers-and-fallers/risers-fallers.html"

if __name__ == "__main__":
    Data.GetTables(URL)
    Data.GetTable(0)
    print(Data.DescribeTable())
    Data.GetTableJson()
    print(Data.json)
