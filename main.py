from DataTables.datatables import TocaData

Data = TocaData()

URL = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/risers-and-fallers/risers-fallers.html"

if __name__ == "__main__":
    Data.GetElementsByCoords(0, 0, 0, 0)
