import pandas as pd

pd.DataFrame()

class RailwayFrom:
    formType = " RailwayFrom"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayFrom()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
harrysApplication.printData()