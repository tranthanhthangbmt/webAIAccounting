import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. Cook Autos (EX 7.7)
cook_data = []
salespersons = ['Carlos', 'Arun', 'Shanice']
cars = ['SUV', 'Sedan', 'Sports']
targets = {
    'Carlos': {'SUV': 80, 'Sedan': 70, 'Sports': 10},
    'Arun': {'SUV': 67, 'Sedan': 70, 'Sports': 8},
    'Shanice': {'SUV': 75, 'Sedan': 50, 'Sports': 10}
}
actuals = {
    'Carlos': {'SUV': 60, 'Sedan': 67, 'Sports': 2},
    'Arun': {'SUV': 40, 'Sedan': 40, 'Sports': 38},
    'Shanice': {'SUV': 45, 'Sedan': 40, 'Sports': 30}
}
for sp in salespersons:
    for car in cars:
        cook_data.append([sp, car, targets[sp][car], actuals[sp][car]])
pd.DataFrame(cook_data, columns=['Salesperson', 'CarType', 'Target_Sales', 'Actual_Sales']).to_csv(os.path.join(out_dir, 'CookAutos_Sales.csv'), index=False)


# 2. Wok and Dumpling (EX 7.8)
start_date = datetime(2025, 1, 1)
wok_data = []
for i in range(90): # Q1 is 90 days
    current_date = start_date + timedelta(days=i)
    # Wok sales average around 20k, Dumpling average around 15k, with some variation
    wok_sales = random.randint(18000, 25000)
    dump_sales = random.randint(10000, 18000)
    wok_data.append([current_date.strftime('%m/%d/%Y'), 'Wok', wok_sales])
    wok_data.append([current_date.strftime('%m/%d/%Y'), 'Dumpling', dump_sales])
pd.DataFrame(wok_data, columns=['Date', 'Restaurant_Branch', 'Daily_Sales']).to_csv(os.path.join(out_dir, 'WokDumpling_Q1_Sales.csv'), index=False)


# 3. Santorini Group (EX 7.9)
santorini_data = []
employees = [fake.name() for _ in range(5)]
for emp in employees:
    hotel = random.choice(['Hilton', 'Marriott'])
    if hotel == 'Hilton':
        rate = random.randint(150, 250)
        dist = round(random.uniform(0.5, 3.0), 1)
    else:
        rate = random.randint(120, 200)
        dist = round(random.uniform(2.0, 6.0), 1)
    santorini_data.append([emp, hotel, rate, dist])
pd.DataFrame(santorini_data, columns=['EmployeeName', 'Hotel', 'NightlyRate', 'DistanceToSeminar_miles']).to_csv(os.path.join(out_dir, 'Santorini_Hotels.csv'), index=False)


# 4. Rainbow Hotel (EX 7.14)
# From book: 
# Website: Dirty room(4), Poor wifi(22), Unexpected fees(2), Unfriendly staff(14) = 42
# ratemyhotel: Dirty room(2), Poor wifi(4), Rodents(2), Unexpected fees(7), Unfriendly staff(60) = 75
# Call: Dirty room(2), Room temp(2), Unexpected fees(2), Unfriendly staff(16) = 22
# Mail: Unfriendly staff(90) = 90
rainbow_counts = {
    'Website': {'Dirty room': 4, 'Poor wifi': 22, 'Unexpected fees': 2, 'Unfriendly staff': 14},
    'ratemyhotel.com': {'Dirty room': 2, 'Poor wifi': 4, 'Rodents': 2, 'Unexpected fees': 7, 'Unfriendly staff': 60},
    'Call': {'Dirty room': 2, 'Room temp': 2, 'Unexpected fees': 2, 'Unfriendly staff': 16},
    'Mail': {'Unfriendly staff': 90}
}
rainbow_data = []
c_id = 1
for src, cats in rainbow_counts.items():
    for cat, count in cats.items():
        for _ in range(count):
            date = fake.date_between(start_date=datetime(2025,1,1), end_date=datetime(2025,1,31)).strftime('%m/%d/%Y')
            rainbow_data.append([f"C{c_id:04d}", date, src, cat])
            c_id += 1
pd.DataFrame(rainbow_data, columns=['Complaint_ID', 'Date', 'Source', 'Category']).to_csv(os.path.join(out_dir, 'RainbowHotel_Complaints.csv'), index=False)


# 5. Jumpers Grocery (EX 7.15)
jumpers_data = []
categories = ['Meat', 'Beverage', 'Vegetable and Fruit', 'Snacks', 'Freezer', 'Dairy', 'Other']
for year in range(2020, 2025):
    for store in ['NIndy', 'SIndy']:
        for cat in categories:
            sales = random.randint(50000, 200000)
            jumpers_data.append([year, store, cat, sales])
pd.DataFrame(jumpers_data, columns=['Year', 'Store', 'Category', 'SalesAmount']).to_csv(os.path.join(out_dir, 'Jumpers_5Year_Sales.csv'), index=False)


# 6. NoTable (PAC 7.2, 7.3, 7.4)
notable_prod = []
notable_sales = []
notable_cust = []
designers = [fake.name() for _ in range(5)]
states = ['NY', 'CA', 'TX', 'FL', 'NV', 'WA', 'IL']

# Generate Customers
customers = [f"CUST{i:03d}" for i in range(1, 21)]
for c in customers:
    notable_cust.append([c, fake.company(), random.choice(['A', 'B', 'C', 'D'])])
pd.DataFrame(notable_cust, columns=['CustomerID', 'CustomerName', 'CreditRating']).to_csv(os.path.join(out_dir, 'NoTable_Customers.csv'), index=False)

# Generate Production and Sales
for i in range(1, 101):
    order_id = f"ORD{i:04d}"
    designer = random.choice(designers)
    
    # Production
    est_labor = random.randint(500, 1500)
    est_mat = random.randint(300, 1000)
    # Create variances
    var_factor = random.uniform(0.8, 1.3) 
    act_labor = int(est_labor * var_factor)
    act_mat = int(est_mat * random.uniform(0.9, 1.1))
    notable_prod.append([order_id, designer, est_labor, act_labor, est_mat, act_mat])
    
    # Sales
    cust = random.choice(customers)
    amount = int((est_labor + est_mat) * 2.5) # Price
    order_date = fake.date_between(start_date="-6m", end_date="-1m")
    
    # Payment timing
    pay_scenario = random.choice(['early', 'on_time', 'late', 'unpaid'])
    if pay_scenario == 'early':
        pay_date = order_date + timedelta(days=random.randint(1, 14))
    elif pay_scenario == 'on_time':
        pay_date = order_date + timedelta(days=random.randint(16, 30))
    elif pay_scenario == 'late':
        pay_date = order_date + timedelta(days=random.randint(31, 60))
    else:
        pay_date = ""
        
    state = random.choice(states)
    notable_sales.append([
        order_id, cust, order_date.strftime('%m/%d/%Y'), 
        amount, 
        pay_date.strftime('%m/%d/%Y') if pay_date else "", 
        state
    ])

pd.DataFrame(notable_prod, columns=['OrderID', 'DesignerName', 'Est_LaborCost', 'Act_LaborCost', 'Est_MaterialCost', 'Act_MaterialCost']).to_csv(os.path.join(out_dir, 'NoTable_Production.csv'), index=False)
pd.DataFrame(notable_sales, columns=['OrderID', 'CustomerID', 'OrderDate', 'Amount', 'PaymentDate', 'DeliveryState']).to_csv(os.path.join(out_dir, 'NoTable_SalesOrders.csv'), index=False)

print("Chapter 7 datasets generated successfully!")
