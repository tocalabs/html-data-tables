import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True


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

    def GetElementsByCoords(self, x=0, y=0, w=0, h=0):
        try:
            driver = webdriver.Chrome(chrome_options=options)
            driver.get("https://www.google.com/")
            content = driver.find_elements_by_xpath("//*")
            # filter content by height and width being similar to params
            # filter content by x/y coords not being too different to params
            # compare screenshots (potentially GPU acceleration?)
            for x in filter(lambda x : x.is_displayed, content):
                if(x.size['height'] != 0 and x.size['width'] != 0):
                    try:
                        screenshot = x.screenshot_as_base64
                        screenshot = "data:image/png;base64," + screenshot
                        
                    except Exception as error:
                        print(error)
            driver.close()
            driver.quit()
        except Exception as ex:
            print(ex)
