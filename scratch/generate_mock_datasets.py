import os
import random
import csv
from datetime import datetime, timedelta
try:
    import pandas as pd
    import numpy as np
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

DATASETS_DIR = "TaiLieu/Datasets"
os.makedirs(DATASETS_DIR, exist_ok=True)

# 1. Le Grind Sales Data
def generate_le_grind_data():
    filename = os.path.join(DATASETS_DIR, "LeGrind_Raw.csv")
    origins = ['Brazil', 'Colombia', 'Ethiopia', 'Vietnam', 'Guatemala', 'Costa Rica']
    categories = ['Retail', 'Wholesale', 'Online']
    states = ['CA', 'NY', 'TX', 'FL', 'IL', 'WA']
    
    start_date = datetime(2023, 1, 1)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['InvoiceID', 'Date', 'CustomerID', 'CustomerCategory', 'CustomerState', 'CoffeeOrigin', 'Quantity_lbs', 'UnitPrice', 'COGS_per_unit', 'Sales', 'TotalCOGS', 'GrossMargin'])
        
        for i in range(1, 5001):
            invoice_id = f"INV-{10000+i}"
            date = start_date + timedelta(days=random.randint(0, 365))
            cust_id = f"CUST-{random.randint(100, 999)}"
            category = random.choice(categories)
            state = random.choice(states)
            origin = random.choice(origins)
            
            qty = random.randint(10, 500) if category == 'Wholesale' else random.randint(1, 50)
            unit_price = round(random.uniform(15.0, 30.0), 2)
            cogs_unit = round(unit_price * random.uniform(0.4, 0.7), 2)
            
            sales = round(qty * unit_price, 2)
            total_cogs = round(qty * cogs_unit, 2)
            margin = round(sales - total_cogs, 2)
            
            writer.writerow([invoice_id, date.strftime('%Y-%m-%d'), cust_id, category, state, origin, qty, unit_price, cogs_unit, sales, total_cogs, margin])
            
    print(f"Generated {filename}")

# 2. Super Scooters Forecast
def generate_super_scooters():
    filename = os.path.join(DATASETS_DIR, "SuperScooters_Case.csv")
    models = ['EcoScooter', 'SpeedPro', 'CommuterMax']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Month', 'Model', 'Units_Sold', 'Unit_Price', 'Variable_Cost_per_Unit', 'Fixed_Costs', 'Revenue', 'Total_Variable_Cost', 'Operating_Income'])
        
        fixed_costs = 50000
        for month in months:
            for model in models:
                if model == 'EcoScooter':
                    units = random.randint(500, 1000)
                    price = 299
                    vc = 150
                elif model == 'SpeedPro':
                    units = random.randint(200, 500)
                    price = 799
                    vc = 450
                else:
                    units = random.randint(300, 700)
                    price = 499
                    vc = 250
                    
                revenue = units * price
                tvc = units * vc
                oi = revenue - tvc - fixed_costs/3 # allocate fixed costs
                
                writer.writerow([month, model, units, price, vc, fixed_costs/3, revenue, tvc, oi])

    print(f"Generated {filename}")

# 3. Dirty Data
def generate_dirty_data():
    if not PANDAS_AVAILABLE:
        print("Pandas not available. Generating CSV instead of XLSX for dirty data.")
    
    filename_csv = os.path.join(DATASETS_DIR, "Sales_DirtyData.csv")
    filename_xlsx = os.path.join(DATASETS_DIR, "Sales_DirtyData.xlsx")
    
    data = []
    # Create some clean rows
    for i in range(100):
        data.append({
            'OrderID': f"ORD-{1000+i}",
            'Order Date': (datetime(2023,1,1) + timedelta(days=random.randint(0,100))).strftime('%Y-%m-%d'),
            'Customer Name': f"Customer {i}",
            'Region': random.choice(['North', 'South', 'East', 'West']),
            'Revenue': random.randint(100, 5000)
        })
        
    # Inject dirty data
    data.append({
        'OrderID': "ORD-1001", # Duplicate
        'Order Date': "2023-01-05",
        'Customer Name': "Customer 1",
        'Region': "North",
        'Revenue': 500
    })
    
    data.append({
        'OrderID': "ORD-1100",
        'Order Date': "13-05-2023", # Wrong format
        'Customer Name': "  Customer X  ", # Leading/trailing spaces
        'Region': "Nort", # Typo
        'Revenue': "$1,500" # String instead of int
    })
    
    data.append({
        'OrderID': "", # Missing ID
        'Order Date': "Jan 5th 23",
        'Customer Name': "cUSTOMER y", # Case issue
        'Region': "", # Null
        'Revenue': "two thousand"
    })
    
    # Shuffle
    random.shuffle(data)
    
    if PANDAS_AVAILABLE:
        df = pd.DataFrame(data)
        df.to_excel(filename_xlsx, index=False)
        print(f"Generated {filename_xlsx}")
    else:
        with open(filename_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['OrderID', 'Order Date', 'Customer Name', 'Region', 'Revenue'])
            writer.writeheader()
            writer.writerows(data)
        print(f"Generated {filename_csv}")

if __name__ == "__main__":
    generate_le_grind_data()
    generate_super_scooters()
    generate_dirty_data()
