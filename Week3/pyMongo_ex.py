from pymongo import MongoClient
import json

def main():
    # Connect to server
    client = MongoClient("mongodb://localhost:27017/")

    db = client.get_database("testdec30")
    empCollection = db.empDetails

    # Querying empDetails collection
    employees = empCollection.find()
    for employee in employees:
        print(employee['First_Name'])

    with open("orders.json") as f:
        orders_data = json.load(f)
    
    print(orders_data)
    new_order = {"customerName": "Gabriel", "amount": 150.0}
    db.orders.insert_one(new_order)

    db.orders.insert_many(orders_data)

    all_orders = db.orders.find({'customerName' : 'Leah'})
    for order in all_orders:
        print(order)

    



if __name__ == '__main__':
    main()