# Installed Pillow to display image.
from PIL import Image
# install pandas from file > settings > projects > interpreter > + sign > pandas.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def intro():
    print("Kia Soul Car Sales Figures")
    print("from the years of 2009 to 2023")
    print("Many standard features are coherent")


#def greetings(name, lst_Name):
    #print("Hello " + name + " " + lst_Name)

def greetings(name):
    print("Hello " + name)


#===============================================================================

class car:
    def __init__(self, compny, modl):
        self.company = compny #instance attribute
        self.model = modl     #instance attribute

    def title(self):
        print(self.company + self.model)

class model(car):
    def __init__(self, compny, modl):
        super().__init__(compny, modl)

    #class decorator to declare this function as its own
    # firt argument must be cls
    @classmethod
    def standard_Features(cls):
        features = {"Engine Type": "2.0L 4-Cylinder Engine", "Engine Valve Train":"Dual Overhead Cam (DOHC), 16-valve",
                             "Fuel System":"Multi-Port Gasoline Injection (MPI)",
                             "Horsepower":"147 hp @ 6,200 rpm", "Safety": "Collision Avoidance-Assist with Pedestrian Detection",
                             "Warranty":"Kia 10-year/100,000-mile",
                             "Dimensions": {"Length":"165.2 in.", "Width":"70.9 in.", "Height":"63.0 in."}}

        series1 = pd.Series(features)
        print("Standard Features Across All Soul Trims")
        print(series1)

class sales(car):
    def __init__(self, compny, modl):
        super().__init__(compny, modl)


    @classmethod
    def two_Year_Sales(cls):
        # Nested Dictionary
        kia_sales = {"2010": {"Jan": 2145, "Feb": 3600, "Mar": 5106, "Apr": 5223, "May": 6134, "Jun": 6429, "Jul": 8020,
                              "Aug": 7021, "Sep": 5346, "Oct": 6137},
                     "2022": {"Jan": 3890, "Feb": 5059, "Mar": 5175, "Apr": 4414, "May": 4116, "Jun": 4954, "Jul": 5322,
                              "Aug": 5322, "Sep": 5113, "Oct": 4782}}
        # DataFrame() is a pandas method used to place data into columns
        print("2010 Vs. 2022 Sales")
        df = pd.DataFrame(kia_sales)
        print(df)
        #df.transpose().plot.bar()======================
        # .plot will plot a line graph only, but graph will only be visible if plt.show() is used.
        df.plot()
        # If show() is not used, only dataframe() will create columns in console. It won't show the visual graph unless show() is called.
        plt.show()


    @classmethod
    def two_Year_Sales2(cls):
        # Nested Dictionary
        kia_sales = {"2014": {"Jan": 8092, "Feb": 10584, "Mar":13992, "Apr":14403 , "May": 15606, "Jun":12322 , "Jul": 14709,
                              "Aug": 15069, "Sep": 10802, "Oct":10685},
                     "2022": {"Jan": 3890, "Feb": 5059, "Mar": 5175, "Apr": 4414, "May": 4116, "Jun": 4954, "Jul": 5322,
                              "Aug": 5322, "Sep": 5113, "Oct": 4782}}
        # DataFrame() is a pandas method used to place data into columns
        print("2014 Vs. 2022 Sales")
        df = pd.DataFrame(kia_sales)
        print(df)
        # df.transpose().plot.bar()======================
        # .plot will plot a line graph only, but graph will only be visible if plt.show() is used.
        df.plot()
        # If show() is not used, only dataframe() will create columns in console. It won't show the visual graph unless show() is called.
        plt.show()

    @classmethod
    def soul_vs_Seltos(cls):
        # using array [], arrays are changable can hold int, str, booleans at once.
        yAxisOfPie = np.array([56740, 44897, 124244])
        soul_Seltos = ["Kia Soul", "Kia Seltos", "Kia Sportage"]
        # pie char colors
        Colors = ["#FAEBD7", "y", "#E9967A"]
        plt.pie(yAxisOfPie, labels=soul_Seltos)
        # plt.pie(yAxisOfPie)
        plt.show()
        #print("2022 US Year Sales - Soul VS. Seltos VS. Sportage")


    @classmethod
    # Using open() & read() file methods
    def open_File(cls, Data):
        # Opening text file in read mode
        my_File_Handle = open(Data, "r")
        file_Content = my_File_Handle.read()
        return file_Content

#========================================================================================

# Function call to intro
# intro()

# Objects of class model
# d = model("Kia", "Soul")
# print(d.company, d.model)
# d.standard_Features()

# Objects of class sales
# t = sales("Kia", "Soul")
# t.two_Year_Sales()

# Get data from file
# kia_Data = "kia_Soul_Sales_Figure.txt"
# raw_Data = t.open_File(kia_Data)
# print(raw_Data)
#content_to_screen(c)

