import pandas as pd
import numpy as np
import os
import random

out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. Water Sports, Inc. (EX 10.7)
products = ['Surfboards', 'Wetsuits', 'Snorkels', 'Fins', 'Kayaks', 'Paddleboards']
water_sports_data = []
for p in products:
    sales = random.randint(100000, 500000)
    cogs = int(sales * random.uniform(0.4, 0.6))
    sgna = int(sales * random.uniform(0.1, 0.25))
    water_sports_data.append([p, sales, cogs, sgna])
pd.DataFrame(water_sports_data, columns=['ProductLine', 'SalesRevenue', 'CostOfGoodsSold', 'SellingAndAdminExpenses']).to_csv(os.path.join(out_dir, 'WaterSports_Financials.csv'), index=False)


# 2. OneStopShop, Inc. (EX 10.8)
divisions = ['Floor cleaning', 'Lawn care', 'Pest control', 'Household cleaning', 'Corporate office cleaning', 'Plumbing products']
oss_div_data = []
for div in divisions:
    for year in [2024, 2025]:
        total_rev = random.randint(2000000, 8000000)
        net_income = int(total_rev * random.uniform(0.05, 0.2)) # Profit margin 5-20%
        avg_assets = int(total_rev * random.uniform(0.8, 1.5)) # Asset turnover ~0.6-1.25
        current_assets = int(avg_assets * random.uniform(0.3, 0.6))
        current_liabilities = int(current_assets * random.uniform(0.5, 1.5)) # Current ratio ~0.6-2.0
        oss_div_data.append([div, year, net_income, total_rev, avg_assets, current_assets, current_liabilities])
pd.DataFrame(oss_div_data, columns=['Division', 'Year', 'NetIncome', 'TotalRevenue', 'AverageTotalAssets', 'CurrentAssets', 'CurrentLiabilities']).to_csv(os.path.join(out_dir, 'OneStopShop_Divisions.csv'), index=False)


# 3. Computer Manufacturing Client Warranty (EX 10.12)
warranty_data = [
    ['32153', 'Warranty liability', 347954, 535849],
    ['23829', 'Warranty expense', 121784, 241132]
]
pd.DataFrame(warranty_data, columns=['AccountNumber', 'AccountDescription', 'Balance_2024', 'Balance_2025']).to_csv(os.path.join(out_dir, 'ComputerMfg_Warranty.csv'), index=False)

print("Chapter 10 datasets generated successfully!")
