import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. One Stop Shop (EX 8.14)
# Sales by quarter showing seasonality (Q4 is highest, Q1 is lowest)
oss_data = []
for year in range(2022, 2026):
    for q in range(1, 5):
        base_sales = 50000000 + (year - 2022) * 5000000 # general growth
        if q == 1:
            sales = base_sales * random.uniform(0.7, 0.9)
        elif q == 2:
            sales = base_sales * random.uniform(0.9, 1.1)
        elif q == 3:
            sales = base_sales * random.uniform(1.0, 1.2)
        else:
            sales = base_sales * random.uniform(2.0, 2.5) # Q4 spike
        oss_data.append([year, f"Q{q}", int(sales)])
pd.DataFrame(oss_data, columns=['Year', 'Quarter', 'SalesAmount']).to_csv(os.path.join(out_dir, 'OneStopShop_Sales.csv'), index=False)


# 2. U.S. Outdoor Adventures (EX 8.15, PR 8.1)
# Year, Priority, ShippingMode, ShipmentsCount, ShippingCost
us_outdoor_data = []
priorities = ['Critical', 'High', 'Medium', 'Low']
modes = ['First class', 'Same day', 'Second class', 'Standard class']
for year in range(2022, 2026):
    for p in priorities:
        for m in modes:
            # Random shipments count (mostly standard/medium)
            if m == 'Standard class' or p in ['Low', 'Medium']:
                count = random.randint(100, 500)
            else:
                count = random.randint(10, 100)
            
            # Shipping cost: increased dramatically over the years
            cost_per_shipment = 10 + (year - 2022) * 5
            if m == 'Same day':
                cost_per_shipment *= 3
            elif m == 'First class':
                cost_per_shipment *= 2
            
            total_cost = count * cost_per_shipment * random.uniform(0.9, 1.1)
            us_outdoor_data.append([year, p, m, count, round(total_cost, 2)])
pd.DataFrame(us_outdoor_data, columns=['Year', 'Priority', 'ShippingMode', 'ShipmentsCount', 'ShippingCost']).to_csv(os.path.join(out_dir, 'OutdoorAdventures_Shipping.csv'), index=False)


# 3. All Care Hospital (PR 8.2)
# 2000 hospitals data
hospital_data = []
for i in range(1, 2001):
    beds = random.randint(50, 1000)
    admissions = int(beds * random.uniform(30, 80)) # admissions per year
    staffing = int(beds * random.uniform(2.5, 4.5)) # staff per bed
    base_cost = admissions * 5000 + staffing * 70000
    total_cost = int(base_cost * random.uniform(0.9, 1.2)) # add noise
    hospital_data.append([f"HOSP_{i:04d}", admissions, beds, staffing, total_cost])
pd.DataFrame(hospital_data, columns=['HospitalID', 'Admissions', 'Beds', 'StaffingLevel', 'TotalOperatingCost']).to_csv(os.path.join(out_dir, 'AllCareHospital_Costs.csv'), index=False)


# 4. Ortho Inc. (PAC 8.2, 8.3)
# PAC 8.2: Purchase Orders vs Sales
ortho_purchasing = []
start_date = datetime(2022, 1, 1)
for i in range(48): # 4 years = 48 months
    current_month = start_date + timedelta(days=i*30)
    sales = random.randint(20000000, 100000000)
    # Purchasing might be much higher than sales occasionally or consistently growing faster
    purchasing = int(sales * random.uniform(1.0, 1.5)) # buying more than selling
    ortho_purchasing.append([current_month.strftime('%m/%Y'), sales, purchasing])
pd.DataFrame(ortho_purchasing, columns=['Date', 'SalesAmount', 'PurchaseOrdersAmount']).to_csv(os.path.join(out_dir, 'Ortho_Purchasing_Sales.csv'), index=False)

# PAC 8.3: Sales by State
ortho_states = []
states = ['CA', 'FL', 'IL', 'NY', 'TX']
# For 2024 and 2025
for year in [2024, 2025]:
    for state in states:
        # Based on textbook, ranges from 163M to 200M, but TX in 2024 was 913M (outlier in textbook?) Let's recreate
        if year == 2024 and state == 'TX':
            sales = random.randint(850000000, 950000000)
        elif year == 2024 and state == 'FL':
            sales = random.randint(800000000, 900000000)
        else:
            sales = random.randint(160000000, 200000000)
        ortho_states.append([year, state, sales])
pd.DataFrame(ortho_states, columns=['Year', 'State', 'SalesRevenue']).to_csv(os.path.join(out_dir, 'Ortho_Sales_By_State.csv'), index=False)

print("Chapter 8 datasets generated successfully!")
