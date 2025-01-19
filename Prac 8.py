from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.train

def insert():
    try:
        traincsvId = input('Enter traincsv Passenger Id:')
        traincsvName = input('Enter Name:')
        traincsvAge = input('Enter age:')
        traincsvFare = input('Enter Fare:')
        traincsvSex = input('Enter Sex:')
        traincsvTicket = input('Enter Ticket:')
        
        db.traincsv.insert_one({
            "PassengerId": traincsvId,
            "Name": traincsvName,
            "Age": traincsvAge,
            "Fare": traincsvFare,
            "Sex": traincsvSex,
            "Ticket": traincsvTicket,
        })
        
        print("\nInserted data successfully\n")
        
    except Exception as e:
        print(str(e))
        insert()

insert()

# --------------------------------------------------------------------

from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.train

def read():
    try:
        trainCol = db.traincsv.find()
        print("All data From database")
        for train in trainCol:
            print(train)
            
    except Exception as e:
        print(str(e))
        read()

read()

# -------------------------------------------------------------------------

from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.train

def update():
    try:
        traincsvId = input('Enter Passenger Id to update:')
        traincsvName = input('Enter Name to update:')
        traincsvAge = input('Enter age to update:')
        
        db.traincsv.insert_one({
            "PassengerId": traincsvId,
            "Name": traincsvName,
            "age": traincsvAge,
        })
        
        print("\nUpdated data successfully\n")
        
    except Exception as e:
        print(str(e))
        update()

update()
 
# -------------------------------------------------------------------

from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.train

def delete():
    try:
        criteria = input("Enter Name to delete:")
        db.traincsv.delete_one({"Name": criteria})
        print("\nDeleted data successfully\n")
        
    except Exception as e:
        print(str(e))
        delete()

delete()