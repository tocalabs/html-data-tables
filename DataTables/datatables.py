import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyscreenshot as ImageGrab

from DataTables.Box import Box

options = Options()
options.headless = False


class TocaData:

    def __init__(self):
        self.table = None
        self.json = None
        self.element_coords = {}


    def DescribeTable(self):
        try:
            return self.table.describe()
        except Exception as ex:
            print(ex)

    def GetTableJson(self):
        try:
            self.json = self.table.to_json()
        except Exception as ex:
            print(ex)

    def GrabScreenshot(self, x, y, w, h):
        image = ImageGrab.grab(bbox=(x, y, w, h))
        image.save('screenshot.png')

    def GrabBox(self, x, y, w, h):
        drawn_box = Box(x, y, w, h)
        return drawn_box

    def GetElementsByCoords(self, x=0, y=0, w=0, h=0):
        try:
            driver = webdriver.Chrome(chrome_options=options)
            driver_rect = driver.get_window_rect()
            print(driver.execute_script("return window.pageYOffset"))
            inner_height = int(driver.execute_script("return innerHeight"))
            outer_height = int(driver.execute_script("return outerHeight"))
            height_difference = outer_height - inner_height

            user_box = Box(
                driver_rect['x'] + x, 
                driver_rect['y'] + y, 
                driver_rect['width'], 
                driver_rect['height']
                )

            driver.get("https://www.w3schools.com/html/html_tables.asp")

            content = driver.find_elements_by_tag_name('table')

            filtered_content = list(filter(lambda x : x.size['height'] != 0 and x.size['width'] != 0, content))

            for element in filtered_content:
                table_box = Box(
                    element.rect['x'] + height_difference, 
                    element.rect['y'], 
                    element.rect['width'],
                    element.rect['height']
                    )
                if user_box.intersection(table_box):
                    table_html = element.get_attribute('outerHTML')
                    self.table = pd.read_html(table_html)[0]
                    absolute_y = driver_rect['y'] + height_difference + int(element.rect['y'])
                    absolute_x = driver_rect['x'] + int(element.rect['x'])
                    self.element_coords = {
                        'top': absolute_y,
                        'left': absolute_x,
                        'width': element.rect['width'],
                        'height': element.rect['height'] 
                    }
                    print(driver_rect['y'])
                    print(height_difference)
                    print(element.rect['y'])
            driver.close()
            driver.quit()

        except Exception as ex:
            print("In Exception")
            print(ex)
