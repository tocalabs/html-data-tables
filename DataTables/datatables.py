import pandas as pd


class TocaData:

    def __init__(self):
        self.tables = []
        self.table = None
        self.json = None

    def GetTables(self, url):
        try:
            self.tables = pd.read_html(url)
        except Exception as ex:
            print(ex)

    def GetTable(self, index):
        try:
            self.table = self.tables[index]
        except Exception as ex:
            print(ex)

    def DescribeTable(self):
        try:
            table = self.table
            return table.describe()
        except Exception as ex:
            print(ex)

    def GetTableJson(self):
        try:
            self.json = self.table.to_json()
        except Exception as ex:
            print(ex)

