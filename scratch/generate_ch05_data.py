import pandas as pd
import numpy as np
import os
import random
from faker import Faker

fake = Faker()
out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. Hikko (EX 5.7)
hikko_data = {
    'Region': ['US', 'EUROPE', 'ASIA'],
    '2022:Q1': [77265889, 53761998, 32188799],
    '2022:Q2': [57176758, 47848178, 27038591],
    '2022:Q3': [57748525, 51197551, 31094380],
    '2022:Q4': [78811207, 53224378, 32832575],
    '2023:Q1': [97265889, 65534311, 31777112],
    '2023:Q2': [71976758, 58325537, 23197292],
    '2023:Q3': [80613969, 67074367, 23661238],
    '2023:Q4': [94347912, 67500340, 32094883],
    '2024:Q1': [107467822, 73666129, 29778112],
    '2024:Q2': [78451510, 54512935, 22035803],
    '2024:Q3': [89434721, 54512935, 24239383],
    '2024:Q4': [102094431, 72929468, 28289206]
}
pd.DataFrame(hikko_data).to_csv(os.path.join(out_dir, 'Hikko_Revenue_Data.csv'), index=False)

# 2. Wilkinson (EX 5.8)
wilkinson_data = {
    'EmployeeID': ['ERF007', 'ERF008', 'ERF007', 'IR68', 'ERF008', 'ERF008', 'IR68', 'IR101'],
    'JobID': [3405, 3406, 3407, 3408, 4608, 4609, 4610, 4611],
    'WeekNo': [1, 1, 1, 1, 2, 2, 2, 2],
    'Thu_Hours': [4, 4, 4, 8, None, None, None, None],
    'Fri_Hours': [8, 8, 8, 4, None, None, None, None],
    'Sat_Hours': [4, 8, 0, 4, None, None, None, None],
    'Mon_Hours_W2': [None, None, None, None, 8, 8, 4, 6],
    'Tue_Hours_W2': [None, None, None, None, 8, 8, 8, 8],
    'Wed_Hours_W2': [None, None, None, None, 8, 4, 10, 8],
    'Thu_Hours_W2': [None, None, None, None, 8, 8, 8, 8],
    'Fri_Hours_W2': [None, None, None, None, 8, 8, 8, 8],
    'Sat_Hours_W2': [None, None, None, None, 4, 4, 4, 4]
}
# Transforming to a long format suitable for students to practice or just give them the raw messy format
# The raw format shown in book is more like a pivot. Let's provide a raw flat file so they can analyze it.
wilk_flat = []
for i in range(8):
    emp = wilkinson_data['EmployeeID'][i]
    job = wilkinson_data['JobID'][i]
    wk = wilkinson_data['WeekNo'][i]
    if wk == 1:
        wilk_flat.append([emp, job, wk, 'Thursday', '1/2/2025', wilkinson_data['Thu_Hours'][i]])
        wilk_flat.append([emp, job, wk, 'Friday', '1/3/2025', wilkinson_data['Fri_Hours'][i]])
        wilk_flat.append([emp, job, wk, 'Saturday', '1/4/2025', wilkinson_data['Sat_Hours'][i]])
    else:
        wilk_flat.append([emp, job, wk, 'Monday', '1/6/2025', wilkinson_data['Mon_Hours_W2'][i]])
        wilk_flat.append([emp, job, wk, 'Tuesday', '1/7/2025', wilkinson_data['Tue_Hours_W2'][i]])
        wilk_flat.append([emp, job, wk, 'Wednesday', '1/8/2025', wilkinson_data['Wed_Hours_W2'][i]])
        wilk_flat.append([emp, job, wk, 'Thursday', '1/9/2025', wilkinson_data['Thu_Hours_W2'][i]])
        wilk_flat.append([emp, job, wk, 'Friday', '1/10/2025', wilkinson_data['Fri_Hours_W2'][i]])
        wilk_flat.append([emp, job, wk, 'Saturday', '1/11/2025', wilkinson_data['Sat_Hours_W2'][i]])
pd.DataFrame(wilk_flat, columns=['EmployeeID', 'JobID', 'WeekNo', 'DayOfWeek', 'Date', 'HoursWorked']).to_csv(os.path.join(out_dir, 'Wilkinson_Timecards.csv'), index=False)

# 3. Vroomba (EX 5.11)
vroomba_data = []
distributors = ['Distributor A', 'Distributor B', 'Distributor C', 'UNAPPROVED DIST']
for i in range(100):
    vroomba_data.append([
        f"TXN{1000+i}",
        f"SP{random.randint(1,5):02d}",
        random.choice(distributors),
        random.randint(10, 200) if random.random() > 0.1 else random.randint(1000, 1500), # Some >1000 for bonus
        279 if random.random() > 0.05 else random.choice([250, 299, 0]), # Some invalid prices
        fake.date_between(start_date="-1y", end_date="today").strftime('%m/%d/%Y')
    ])
pd.DataFrame(vroomba_data, columns=['TransactionID', 'SalespersonID', 'DistributorName', 'UnitsSold', 'UnitPrice', 'SaleDate']).to_csv(os.path.join(out_dir, 'Vroomba_Sales.csv'), index=False)

# 4. Fluffy (PAC 5.1, 5.2, 5.3)
fluffy_sales = pd.DataFrame({
    'OrderNo': [1, 2, 3, 4, 5, 7, 9, 10, 11],
    'OrderDate': ['1/6/2025', '1/7/2025', '1/9/2025', '1/13/2025', '1/15/2025', '1/20/2025', '1/20/2025', '1/23/2025', '1/25/2025'],
    'OrderAmount': [838.46, 100.03, 245.67, 3632.16, 386.90, 753.15, 194.80, 611.00, 1496.72]
})
fluffy_receipts = pd.DataFrame({
    'ReceiptNo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'OrderNo': [1, 2, 3, 4, 5, 6, 10, 7, 9, 8, 11], # Some orders might not exist or partially paid
    'ReceiptDate': ['1/6/2025', '1/7/2025', '1/9/2025', '1/20/2025', '1/24/2025', '1/27/2025', '1/27/2025', '1/30/2025', '1/31/2025', '1/31/2025', '1/30/2025'],
    'Amount': [838.46, 100.3, 150.0, 350.0, 386.9, 200.0, 500.0, 194.8, 403.15, 95.67, 200.0],
    'PaymentType': ['Cash', 'Credit Card', 'Credit Card', 'Check', 'Cash', 'Check', 'Check', 'Check', 'Check', 'Check', 'Check']
})
fluffy_vendors = pd.DataFrame({
    'VendorID': range(1010, 1021),
    'VendorName': [fake.company() for _ in range(11)],
    'ServiceType': ['Manufacturing', 'StandardShipping', 'ExpressShipping', 'Packaging', 'Design', 'Inspection', 'Manufacturing', 'StandardShipping', 'ExpressShipping', 'Packaging', 'Design'],
    'StandardCost': [100, 0, 0, 25, 50, 0, 100, 0, 0, 25, 50],
    'ActualCost': [154, 252, 225, 150, 50, 125, 25, 250, 125, 10, 35]
})
fluffy_sales.to_csv(os.path.join(out_dir, 'Fluffy_SalesOrders.csv'), index=False)
fluffy_receipts.to_csv(os.path.join(out_dir, 'Fluffy_CashReceipts.csv'), index=False)
fluffy_vendors.to_csv(os.path.join(out_dir, 'Fluffy_Vendors.csv'), index=False)

# 5. Data Quality Issues (HomePrinter, Creighton)
hp_data = []
for i in range(50):
    hp_data.append([
        fake.ean(length=8),
        random.choice(['Laser', 'Inkjet', 'laser', 'INKJET', '']), # Case inconsistency, missing
        random.choice([199.99, 299.99, 49.99, -50.0, None]), # Negative, missing
        random.choice([10, 20, 5, 0, 1000])
    ])
pd.DataFrame(hp_data, columns=['PrinterModel', 'Type', 'Price', 'QtyPurchased']).to_csv(os.path.join(out_dir, 'HomePrinter_Data.csv'), index=False)

cr_data = []
for i in range(20):
    cr_data.append([
        fake.name(),
        random.choice(['Accounting', 'IT', 'HR', 'acct', 'h.r.']), # Inconsistent departments
        random.choice([50000, 60000, 70000, 1000000, None]), # Outlier, missing
        random.choice([1000, 2000, 0, 'N/A']) # Incorrect types
    ])
pd.DataFrame(cr_data, columns=['EmployeeName', 'Department', 'Salary', 'Bonus']).to_csv(os.path.join(out_dir, 'Creighton_Payroll.csv'), index=False)

print("Chapter 5 datasets generated successfully!")
