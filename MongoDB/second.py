import pprint
from dbbase import DBBase
from my_csv_reader import readCSV
DBNAME = "Employee_Multiple_Data"
MONGOURL = "mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority"


dbobj = DBBase(MONGOURL)
db = dbobj.getDB(DBNAME)
csvobj = readCSV('emp.csv')

datalist = csvobj.process()
#
collobj = db["firstcoll"]

#<---------------SEARCH-------------------------------------->
# ot = collobj.find_one({"emp_name": "Aamir"})

# alldata = collobj.find()
# for data in alldata:
#     print(data)
# print("--------------------")
# print(ot)

#FIND ALL
# for i in collobj.find({'emp_name':"Aamir"}):
#     pprint.pprint(i)


#<---------------------INSERT---------------------------->
# dbobj.my_insert_many(collobj, datalist)

#<---------------------UPDATE--------------->
#update one
# prev={"emp_name":"Aqib"}
# nextt={"$set":{"Designation":"Engineer"}}
# pprint.pprint(collobj.update_one(prev,nextt))

# #update many
# prev={"emp_name":"Aqib"}
# nextt={"$set":{"Designation":"Engineer"}}
# pprint.pprint(collobj.update_many(prev,nextt))


#<----------DELETE---------->
# #Delete one
# rec={"emp_id":"108"}
# pprint.pprint(collobj.delete_one(rec))

# #Delete many
# rec={"emp_id":"108"}
# pprint.pprint(collobj.delete_many(rec))
#
# step 1 - we have csv file
# step 2 - in python read the csv file - how to
# step 3 - we make one datalist obj from that csv

