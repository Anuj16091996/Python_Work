###########################################################
###########################################################
#In computer programming, pandas is a software library written for the Python programming
# language for data manipulation and analysis. In particular, it offers data structures and
# operations for manipulating numerical tables and time series. It is free software released
# under the three-clause BSD license.


#The Pandas module mainly works with the tabular data, whereas the NumPy module works with
# the numerical data. The Pandas provides some sets of powerful tools like DataFrame and
# Series that mainly used for analyzing the data, whereas in NumPy module offers a
# powerful object called Array.
#he Pandas covered the broader application because it is mentioned in 73 company stacks and 46 developer stacks, whereas in NumPy, 62 company stacks and 32 developer stacks are being mentioned.
#The performance of NumPy is better than the Pandas for 50K rows or less.
#The performance of Pandas is better than the NumPy for 500K rows or more. Between 50K to 500K rows, performance depends on the kind of operation.
#NumPy library provides objects for multi-dimensional arrays, whereas Pandas is capable of offering an in-memory 2d table object called DataFrame.
#NumPy consumes less memory as compared to Pandas.
#Indexing of the Series objects is quite slow as compared to NumPy arrays.





# # install Pandas:
# # On cmd : pip install pandas   OR  pip3 install pandas
# #
# # install IPython:
# # an enhanced Python interactive shell called IPython.
# # On cmd : pip install ipython   OR  pip3 install ipython
#
#
# # Pandas and DataFrame !
# # a DataFrame is an object to store data in.
# # our df1 for example is a variable.
# # # lets make a DataFrame manually(usally with  passing in a file to it)
# #
# # #why??
# #launch ipython on cmd:
# #cmd :

# import ipython




#https://ipython.readthedocs.io/en/stable/interactive/tutorial.html
import pandas
# lst=[[2,4,6],[10,20,30]]
# print(type(lst))
# df1=pandas.DataFrame(lst)
# print(type(df1))
# print(df1)
# print('##################')
# df1=pandas.DataFrame(lst,columns=["price","age","value"])
# print(df1)
# print('##################')
# df1=pandas.DataFrame(lst,columns=["price","age","value"],index=["First","Second"])
# print(df1)
# print('##################')
#

# #example of list to dataframe
# myList = [{"Name":"Gabbar","Surname":"Singh"},{"Name":"Jack","Surname":"Kaur"}]
# print(type(myList))
# df2=pandas.DataFrame(myList)
# print(df2)
# #print('##################')
# #
# #example of tuple to dataframe
# myTuple = {"Name":"Gabbar","Surname":"Singh"},{"Name":"Jack","Surname":"Kaur"}
# print(type(myTuple))
# df2=pandas.DataFrame(myTuple)
# print(df2)
#print('##################')

# #example of dictionary to dataframe
# myDict = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
# print(type(myDict))
# df2=pandas.DataFrame(myDict)
# print(df2)
#print('##################')
#example of set to dataframe
mySet = {10,20,30,40}
print(type(mySet))
df2=pandas.DataFrame(mySet)
print(df2)
#print('##################')



# #Pandas DataFrame is two-dimensional size-mutable,
# #potentially heterogeneous tabular
# # data structure with labeled axes (rows and columns).
# #Pandas DataFrame consists of three principal components,
# #the data, rows, and columns.
#print(dir(df1))
#Pandas Series is a one-dimensional labeled array capable of holding data of any
#type (integer, string, float, python objects, etc.). The axis labels are collectively
# called index. Pandas Series is nothing but a
#column in an excel sheet. Labels need not be unique.


#now we enter the phase of data analysis meaning getting information
#out of our datastructure
#import pandas
#lst=[[2,4,6],[10,20,30]]
#df1=pandas.DataFrame(lst,columns=["price","age","value"],index=["First","Second"])
#print(df1)
#print('#######################')
#lets do the average of each column
#print(df1.mean())
#print(type(df1.mean()))  #type is pandas.Series
# #lets do the average of all
#print(df1.mean().mean())
#print('##################')

# print(df1)
# print('##################')
# print(df1.price)
# print(type(df1.price))
# print('##################')
# print(df1.price.mean())
# print(df1.price.max())



########################################################################
#######################################################################

########################################################################
#######################################################################
#Jupyter is a free, open-source, interactive web tool known as a computational notebook,
# which researchers can use to combine software code, computational output, explanatory text
# and multimedia resources in a single document.

#Jupyter Notebook provides you with an easy-to-use, interactive data science environment
# across many programming languages that doesn't only work as an IDE, but also as a
# presentation or education tool.




# Jupiter Notebook is a combination of python shell
# # and python editor and is browser based

#Jupyter !  jupyter.readthedocs.io/en/latest/install.html

#pip install jupyter

# then lets launch jupyter notebook
# cmd: cd workshop
# cmd: jupyter notebook
# if gives the following error
# 'jupyter' is not recognized as an internal or external command, operable program or batch file.
# cmd:python -m notebook
# and the browser should be launched and you could see whatever file you have in workshop folder.

import jupyter

#in the browser:
#New --> Python3
#opens a new Tab in the browser

#change the name of the notebook to testings

#a file with extention ipynb had been created in workshop directory

# print(1) - Enter
# print(2)   ctrl - Enter to execute

#for creating a new cell: alt - Enter

#for executing and creating a new cell : shift - enter

#for deleting a cell: Esc d d

#for shortcuts: help --> keyboard shortcuts


# print(1)
# print(2)
# shift - Enter

# import pandas
# shift - Enter

# df=pandas.read_csv("c:\\workshop\\thisIsaCSV.csv")
# df
# shift - Enter
#and you will see the table displayed


# to get a list of folder and files name you have in current directory
# import os
# os.listdir()
# shift -- Enter
#


#lets bring in a csv
# df1=pandas.read_csv("c:\\workshop\\supermarkets.csv")
# df1
# # shift -- Enter

#lets bring in a json file
# df2 = pandas.read_json("c:\\workshop\\supermarkets.json")
# df2
# # shift -- Enter

#then redo:
# df3 = pandas.read_excel("c:\\workshop\\supermarkets.xls",sheet_name=0)
# df3

# #for txt file separated by commas still we use read_csv:
# df4=pandas.read_csv("c:\\workshop\\supermarkets-commas.txt")
# df4



# #for txt file separated by semi-colons still we use read_csv:
# df5=pandas.read_csv("c:\\workshop\\supermarkets_semi-colons.txt",sep=";")
# df5
#Shift - Enter



############################################################################################


#import pandas

# set Header Row:
#
# df6=pandas.read_csv("c:\\workshop\\data.txt")
# df6
#
# #the problem is the first line becomes the header.
# #with following syntax, python will give you a default numeric header
#
# df6=pandas.read_csv("c:\\workshop\\data.txt",header= None)
# df6
#
#
# df6.columns = ["ID","Address","City","ZIP","Country","Name","Employees"]
# df6



# #indexing and slicing:
# #Set index columns:

# df7=df6.set_index("ID")
# df7
#
# now we want to take out a part of the DataFrame out:
# example:
# df7.loc[3:4,"City":"Country"]
#
# #and it display the portion we want.
#
# or :
#
# #will display usa:
# df7.loc[4,"Country"]
#
# #will display Country for all the rows:
# df7.loc[:,"Country"]
#
# #lets make a list of it:
# list(df7.loc[:,"Country"])


# #deleting columns and rows:
#
# #deletes on the fly "City" column
# df7.drop("City",1)
#
# #deletes on the fly row "ID" 4
# df7.drop(4,0)
#
#
# #if you wanted to be deleted for ever:
# df8=df7.drop(4,0)
# df8
#
# #if you want to go by range:
# df7.drop(df7.index[0:3],0)
#
# #or by range for columns would be:
# df7.drop(df7.columns[0:3],1)



# #adding and updating a column:
# df7["Continent"]=df7.shape[0]*["north America"]
# df7
# #and the column has been added.
#
# #or we could try updating:
# df7["Continent"]=df7["Country"]+ "," + "North America"
# df7



# #lets add a row to the DataFrame: first transpose the DataFrame
# df7_t=df7.T
# df7_t
#
# #then: add a column to it.
# df7_t["My ID"]=["My Address","My City","My ZIP","My Country","My Name", 400, "My Contient"]
#
# #then display it:
# df7_t
# #and you notice you have added a column to your DataFrame
#
# #then transpose the transposed df7
# df7=df7_t.T
# df7
# #and we get the row added to the DataFrame



##########################################################################

#in order to get latitude and longitude
#lets install geopy:
# pip install geopy
#
#
#
#import geopy

#in order to get a list of decoders:
#dir(geopy)

#what geocoder will do is getting your address
#and sending it to an online service which has
#all the informations.

# from geopy.geocoders import ArcGIS
#
# #creating an object ArcGIS (no more Nominatim)
# nom=ArcGIS()
#
# #applying the method geocode on the object variable "nom"
#
# nom.geocode("2000 rue Sainte-Catherine west, Montreal, Qc h3h 2t2")
# n=nom.geocode("2000 rue Sainte-Catherine west, Montreal, Qc h3h 2t2")
# print(n.latitude)
# print(n.longitude)
# print(type(n))


#############################################################################################


# #how about an entire column of a DataFrame:
#
# import pandas
# df=pandas.read_csv("c:\\workshop\\supermarkets.csv")
# print(df)
#
# # #we are adding a new column with the same format as geocoder:
# df["Address"]=df["Address"]+", " + df["City"] + ", " + df["State"]+ ", " + df["Country"]
# print(df)
# #
# # #and we get a complete column address in there.
# #
# # #we need to send that string of new column address:
# df["Coordinates"]=df["Address"].apply(nom.geocode)
# print(df)
# #
# # #its too long. you dont see it. then:
# print(df.Coordinates[0])
# print(df.Coordinates[0].latitude)
# #
# #
# # #Or
# #
# for i in range(6):
#     print(df.Coordinates[i][1])
#
