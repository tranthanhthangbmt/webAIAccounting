import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. SWI Inc. (EX 9.17)
swi_data = [
    ['Mary Ann Parola', 'Australia', 2, 88000],
    ['Mary Ann Parola', 'South America', 5, 98000],
    ['Hamish Rundan', 'North America', 122, 3000],
    ['Shonie Oscebono', 'European Union', 88, 8000]
]
pd.DataFrame(swi_data, columns=['SalesManager', 'Region', 'SalesApprovedCount', 'TotalRevenue']).to_csv(os.path.join(out_dir, 'SWI_SalesApprovals.csv'), index=False)


# 2. Super Scooters (EX 9.18)
scooter_data = []
for month in range(1, 13):
    # Base costs
    labor = 400000 + random.randint(-50000, 50000)
    material = 600000 + random.randint(-80000, 80000)
    overhead = 200000  # fixed cost behavior mostly
    total = labor + material + overhead
    scooter_data.append([month, labor, material, overhead, total])
pd.DataFrame(scooter_data, columns=['Month', 'Labor_Cost', 'Material_Cost', 'Overhead_Cost', 'TotalAllocated_Cost']).to_csv(os.path.join(out_dir, 'SuperScooters_Costs.csv'), index=False)


# 3. HEH, Inc. (EX 9.19)
heh_data = []
regions = ['North', 'South', 'East', 'West']
categories = ['Frames', 'Wheels', 'Drivetrain', 'Brakes', 'Accessories']
for i in range(500):
    date = fake.date_between(start_date="-1y", end_date="today").strftime('%m/%d/%Y')
    cust_id = f"CUST{random.randint(10, 99)}"
    cust_name = fake.company()
    cat = random.choice(categories)
    sales = random.randint(1000, 15000)
    reg = random.choice(regions)
    heh_data.append([date, cust_id, cust_name, cat, sales, reg])
pd.DataFrame(heh_data, columns=['Date', 'CustomerID', 'CustomerName', 'ProductCategory', 'SalesAmount', 'Region']).to_csv(os.path.join(out_dir, 'HEH_B2B_Sales.csv'), index=False)


# 4. One Stop Shop (EX 9.20)
oss_data = []
categories = ['Baby food', 'Beverages', 'Cereal', 'Clothes', 'Cosmetics', 'Fruits', 'Household', 'Meat', 'Office supplies', 'Personal care', 'Snacks', 'Vegetables']
# 2022 to 2025
sales_totals = {2022: 160, 2023: 175, 2024: 185, 2025: 195} # in millions
percentages = {
    2022: [9.4, 0.3, 0.4, 6.3, 13.8, 14.8, 3.8, 22.5, 0.4, 21.8, 4.3, 2.2],
    2023: [10.2, 0.4, 0.3, 5.5, 14.4, 15.2, 3.1, 23.0, 0.5, 20.1, 4.8, 2.5],
    2024: [13.3, 0.3, 0.4, 4.5, 15.0, 15.5, 2.3, 21.2, 0.4, 19.8, 4.9, 2.4],
    2025: [15.5, 0.4, 0.3, 4.0, 16.2, 14.8, 2.0, 19.5, 0.5, 18.2, 5.8, 2.8] # made up to complete 100%
}
# Normalize just in case
for year in percentages:
    s = sum(percentages[year])
    percentages[year] = [round((p/s)*100, 2) for p in percentages[year]]

for year in range(2022, 2026):
    for i, cat in enumerate(categories):
        pct = percentages[year][i]
        sales = round((pct / 100) * (sales_totals[year] * 1000000), 2)
        oss_data.append([year, cat, pct, sales])
pd.DataFrame(oss_data, columns=['Year', 'ProductCategory', 'SalesPercentage', 'TotalSalesAmount']).to_csv(os.path.join(out_dir, 'OneStopShop_ProductMix.csv'), index=False)


# 5. MPL Library System (PAC 9.1 - 9.4)
branches = ['Main Branch', 'North Branch', 'South Branch', 'East Branch', 'West Branch']

# PAC 9.1: Computer Usage
mpl_comp = []
for b in branches:
    comps = random.randint(10, 50)
    users = int(comps * random.uniform(2.5, 8.5)) # some branches highly used, some not
    mpl_comp.append([b, comps, users])
pd.DataFrame(mpl_comp, columns=['Branch', 'ComputersAvailable', 'DailyAvgUsers']).to_csv(os.path.join(out_dir, 'MPL_ComputerUsage.csv'), index=False)

# PAC 9.2: Payroll
mpl_payroll = []
positions = ['Librarian', 'Assistant', 'Clerk', 'Manager', 'Janitor']
for i in range(1, 101):
    b = random.choice(branches)
    pos = random.choice(positions)
    if pos == 'Manager': salary = random.randint(70000, 95000)
    elif pos == 'Librarian': salary = random.randint(50000, 75000)
    elif pos == 'Assistant': salary = random.randint(35000, 48000)
    elif pos == 'Clerk': salary = random.randint(30000, 40000)
    else: salary = random.randint(28000, 35000)
    mpl_payroll.append([f"EMP{i:03d}", fake.name(), b, pos, salary])
pd.DataFrame(mpl_payroll, columns=['EmployeeID', 'EmployeeName', 'Branch', 'Position', 'AnnualSalary']).to_csv(os.path.join(out_dir, 'MPL_Payroll.csv'), index=False)

# PAC 9.3: Financials 10Y
mpl_fin = []
for year in range(2016, 2026):
    rev = random.randint(5000000, 8000000)
    exp = int(rev * random.uniform(0.85, 1.1)) # sometimes deficit
    mpl_fin.append([year, rev, exp])
pd.DataFrame(mpl_fin, columns=['Year', 'TotalRevenue', 'TotalExpenses']).to_csv(os.path.join(out_dir, 'MPL_Financials_10Y.csv'), index=False)

# PAC 9.4: Performance Metrics
mpl_perf = []
for year in range(2024, 2026):
    for month in range(1, 13):
        ym = f"{year}-{month:02d}"
        for b in branches:
            books = random.randint(1000, 15000)
            visitors = int(books * random.uniform(0.5, 1.2))
            donations = random.randint(100, 5000)
            fines = random.randint(50, 1000)
            mpl_perf.append([ym, b, books, visitors, donations, fines])
pd.DataFrame(mpl_perf, columns=['YearMonth', 'Branch', 'BooksBorrowed', 'Visitors', 'DonationsReceived', 'FinesCollected']).to_csv(os.path.join(out_dir, 'MPL_PerformanceMetrics.csv'), index=False)

print("Chapter 9 datasets generated successfully!")
