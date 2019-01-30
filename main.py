from DataTables.datatables import TocaData
from DataTables.Box import Box

Data = TocaData()


if __name__ == "__main__":
   Data.GetElementsByCoords(5, 5, 1000, 2000)
   print(Data.table)
   print(Data.element_coords)
