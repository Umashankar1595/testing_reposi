from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class WebTable:
    def __init__(self, webtable):
        self.table = webtable

    def get_row_count(self):
        self.table.find_elements(By.TAG_NAME, "tr")
        return len(self.table.find_elements(By.TAG_NAME, "tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements(By.XPATH, "tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(), "columns": self.get_column_count()}

    def row_data(self, row_number):
        if (row_number == 0):
            raise Exception("Row number starts from 1")
        row_number = row_number + 1
        row = self.table.find_elements(By.XPATH, "//tr[" + str(row_number) + "]/td")
        rData = []
        for wedElement in row:
            rData.append(wedElement.text)
        return rData

    def column_data(self, column_number):
        col = self.table.find_elements(By.XPATH, "tr/td[" + str(column_number) + "]")
        rData = []
        for webElement in col:
            rData.append(webElement.text)
        return rData

    def get_all_data(self):
        noOfRows = len(self.table.find_elements(By.XPATH, "//tr")) - 1

        noOfColumns = len(self.table.find_elements(By.XPATH, "//tr[2]/td"))
        allData = []

        for i in range(2, noOfRows+2):
            ro = []
            for j in range(1, noOfColumns+1):
                print(i, j)
                ro.append(self.table.find_elements(By.XPATH, "tr[" + str(i) + "]/td[" + str(j) + "]").text)
            allData.append(ro)
        return allData


class Test(unittest.TestCase):
    def test_web_table(self):
        driver = webdriver.Chrome()
        driver.get("file:///C:/Users/R.K%20GOWDA/Desktop/table3.html")
        w = WebTable(driver.find_element(By.XPATH, "//table[@id='webtable']"))
        print("no of rows :", w.get_row_count())
        print("-------------------------")
        print("no of columns:", w.get_column_count())
        print("--------------------")
        print("table size:", w.get_table_size())
        print("------------------")
        print("first row data:", w.row_data(1))
        print("----------------------")
        print("first columm data:", w.column_data(1))
        print("----------------")
        print("get all data:", w.get_all_data)
        print("------------")

    if __name__ == "__main__":
        unittest.main()
