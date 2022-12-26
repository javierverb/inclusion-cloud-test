# /usr/bin/python3.9/
import datetime
import json
from dataclasses import dataclass

"""
FinTech Settlement Project
Python Developer Test Questions
Question 1
Create a base class with:
    • Three properties initialized at construction
    • One empty classmethod
    • One empty instance method
"""


@dataclass
class Base:
    attr_1: str
    attr_2: int
    attr_3: float

    @classmethod
    def class_method(cls):
        pass

    def instance_method(self):
        pass


"""
Question 2
Create a derived class from the base class
    • Inherits all properties and methods from the base class
    • Initialize the properties differently from the base class
    • Add code to the empty methods
"""


@dataclass
class Derived(Base):
    @classmethod
    def class_method(cls):
        # Add code to the empty classmethod
        print("Class method called in Derived class")

    def instance_method(self):
        # Add code to the empty instance method
        print("Instance method called in Derived class")


derived = Derived("prop1 value", 42, 3.14)

"""
Question 3
Use list comprehension and a lambda function to extract all of the even integers out of a list of integers
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if (lambda x: x % 2 == 0)(n)]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

"""
Question 4
Use the next() function to find the first element in a list of dictionaries whose attribute 'x' = 5. 
Default to an empty dictionary if not found.
"""
data = [{"x": 3, "y": 1}, {"x": 5, "y": 2}, {"x": 7, "y": 3}, {"x": 9, "y": 4}]
result = next(filter(lambda d: d["x"] == 5, data), {})
print(result)  # Output: {'x': 5, 'y': 2}


"""
Question 5
Given the following JSON document:
{
    "claimId": "99999-100000",
    "payee": {
        "id": 9999,
        "role": "Payee"
    },
    "claimDateTime": 1634860244000,
    "invoiceCount": 7,
    "status": "LoadComplete",
    "invoiceIds": [
        "XXA15839",
        "XXA25829",
        "XXA35832",
        "XXA45830",
        "XXA55831",
        "XXA65833",
        "XXA75834"
    ],
    "jobNumber": 100000,
    "fileName": "XXXXXX20211021235044.xml",
    "fileId": 99999,
    "fileDateTime": 1634860244000,
    "receivedDateTime": 1634922275533,
    "process": "TRANSACT",
    "transmitterId": "XXX",
    "retailerId": "RETAILERID",
    "plantName": "XXX1",
    "totalStoreCount": 2,
    "totalOfferCount": 21,
    "totalRecordCount": 27,
    "totalCouponCount": 166,
    "totalFaceValueAmount": 445.58
}

    • Read in the document from a file
    • Find and print:
        ◦ The Payee ID value
        ◦ Any invoices that contain the text "583"
    • Change any date/time fields to text in the format '%Y-%m-%dT%H:%M:%S'
        ◦ Hint: The format of the date/time fields are integer timestamp.
        To create a datetime object from an integer timestamp, use the following:
datetime_obj = datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
    • Write the json document back out to a new file
"""

# Read in the JSON document from a file
with open("document.json", "r") as f:
    data = json.load(f)

# Find and print the Payee ID value
payee_id = data["payee"]["id"]
print(f"Payee ID: {payee_id}")

# Find and print any invoices that contain the text "583"
invoices = data["invoiceIds"]
filtered_invoices = [invoice for invoice in invoices if "583" in invoice]
print(f"Invoices containing '583': {filtered_invoices}")

# Change the date/time fields to text in the format '%Y-%m-%dT%H:%M:%S'
data["claimDateTime"] = datetime.datetime.fromtimestamp(data["claimDateTime"] / 1e3).strftime("%Y-%m-%dT%H:%M:%S")
data["fileDateTime"] = datetime.datetime.fromtimestamp(data["fileDateTime"] / 1e3).strftime("%Y-%m-%dT%H:%M:%S")
data["receivedDateTime"] = datetime.datetime.fromtimestamp(data["receivedDateTime"] / 1e3).strftime("%Y-%m-%dT%H:%M:%S")

# Write the JSON document back out to a new file
with open("new_document.json", "w") as f:
    json.dump(data, f, indent=4)
