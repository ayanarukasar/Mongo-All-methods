import pymongo
client = pymongo.MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
DBNAME = "Employee_Data"
#db = client.DBNAME  #process 1 in this db always DBNAME
db = client[DBNAME] #process 2  in this we can use the variable
data = {"emp_name": "Ayana", "emp_id": 46152931,"Designation":"Associate-I Engineer"}
# connect with collection name
#db["firstcoll"].insert_one(data)


datalist = [{"emp_name": "Aamir", "emp_id": 63152931,"Designation":"Technology Analyst"},
            {"emp_name": "Sanobar", "emp_id": 19052931,"Designation":"Project Engineer"},
            ]
#
db["firstcoll"].insert_many(datalist)
#
# db["mycoll"].insert_many(datalist)



