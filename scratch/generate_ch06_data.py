import pandas as pd
import numpy as np
import os
import random
from faker import Faker

fake = Faker()
out_dir = r"TaiLieu\textbookForPractice\Data"
os.makedirs(out_dir, exist_ok=True)

# 1. Ruppetware (EX 6.8)
ruppetware_data = []
# Need average of 2024 to be calculated. Let's make 2024 sales around 100k.
for i in range(20):
    sales_2024 = random.randint(80000, 120000)
    # 2025 sales: some fail, some pass by <5%, some by 5-10%, some by >10%
    # average 2024 is ~100k, target = 105k
    scenario = random.choice(['fail', 'low_bonus', 'med_bonus', 'high_bonus'])
    if scenario == 'fail':
        sales_2025 = random.randint(80000, 104000)
    elif scenario == 'low_bonus':
        sales_2025 = random.randint(106000, 109000)
    elif scenario == 'med_bonus':
        sales_2025 = random.randint(111000, 115000)
    else:
        sales_2025 = random.randint(116000, 150000)
    ruppetware_data.append([
        f"SP{101+i}",
        fake.name(),
        sales_2024,
        sales_2025
    ])
pd.DataFrame(ruppetware_data, columns=['SalespersonID', 'SalespersonName', 'SalesAmount_2024', 'SalesAmount_2025']).to_csv(os.path.join(out_dir, 'Ruppetware_Sales.csv'), index=False)

# 2. Leno Transportation Service (EX 6.9)
trucks = pd.DataFrame({
    'TruckID': [f"TRK{i:03d}" for i in range(1, 11)],
    'MaxCapacity_kg': [random.choice([5000, 8000, 10000]) for _ in range(10)]
})
pallets = pd.DataFrame({
    'PalletID': [f"PAL{i:04d}" for i in range(1, 51)],
    'Weight_kg': [random.randint(500, 2000) for _ in range(50)]
})
schedule = []
# Assign pallets to trucks, creating some over capacity and some under capacity (<75%)
assigned_pallets = list(pallets['PalletID'])
random.shuffle(assigned_pallets)

for truck in trucks.itertuples():
    truck_id = truck.TruckID
    cap = truck.MaxCapacity_kg
    # decide scenario
    scenario = random.choice(['under', 'over', 'normal'])
    assigned_weight = 0
    if scenario == 'under':
        target = cap * 0.6
    elif scenario == 'over':
        target = cap * 1.1
    else:
        target = cap * 0.9

    while assigned_weight < target and assigned_pallets:
        p_id = assigned_pallets.pop()
        w = pallets[pallets['PalletID'] == p_id]['Weight_kg'].values[0]
        schedule.append(['2/15/2025', truck_id, p_id])
        assigned_weight += w

pd.DataFrame(schedule, columns=['Date', 'TruckID', 'PalletID']).to_csv(os.path.join(out_dir, 'LTS_Schedule.csv'), index=False)
trucks.to_csv(os.path.join(out_dir, 'LTS_Trucks.csv'), index=False)
pallets.to_csv(os.path.join(out_dir, 'LTS_Pallets.csv'), index=False)

# 3. D*Tunes (PAC 6.1 - 6.3)
instructors = []
for i in range(1, 16):
    hrs = random.randint(100, 600)
    awards = random.randint(0, 5) if hrs > 250 else 0
    nat = random.choice(['Yes', 'No']) if awards >= 3 else 'No'
    instructors.append([
        f"INST{i:02d}",
        fake.name(),
        hrs,
        awards,
        nat
    ])
df_inst = pd.DataFrame(instructors, columns=['InstructorID', 'InstructorName', 'HoursTaught', 'AwardsWon', 'NationalRecognition'])

sessions = []
for i in range(1, 51):
    stype = random.choice(['Starter', 'Private', 'Group', 'Friday Party'])
    sessions.append([
        f"SESS{i:03d}",
        stype,
        random.choice(df_inst['InstructorID']),
        fake.date_between(start_date="-1m", end_date="today").strftime('%m/%d/%Y')
    ])
df_sess = pd.DataFrame(sessions, columns=['SessionID', 'SessionType', 'InstructorID', 'Date'])

registrations = []
students = [f"STU{i:03d}" for i in range(1, 101)]
for i in range(1, 151):
    student_id = random.choice(students)
    sess_id = random.choice(df_sess['SessionID'])
    # Check session type for fee
    stype = df_sess[df_sess['SessionID'] == sess_id]['SessionType'].values[0]
    fee = 0
    if stype == 'Starter':
        fee = 0
    elif stype == 'Friday Party':
        fee = 25
    elif stype == 'Group':
        fee = 40
    else:
        # Private depends on instructor level, but let's just make it a flat 100 for simplicity in the mock data, 
        # or calculate accurately based on rules: 
        # Apprentice (75), Intermediate (95), Advanced (115), Champion (140)
        # But students have to do the info modeling to find out, so we can just provide what they paid.
        fee = random.choice([75, 95, 115, 140]) 
    
    registrations.append([
        f"REG{i:04d}",
        student_id,
        fake.first_name(),
        sess_id,
        fee
    ])
# Force some fraud (multiple starters)
fraud_stu = "STU099"
registrations.append([f"REG9991", fraud_stu, "Fraud Student", df_sess[df_sess['SessionType']=='Starter']['SessionID'].values[0], 0])
registrations.append([f"REG9992", fraud_stu, "Fraud Student", df_sess[df_sess['SessionType']=='Starter']['SessionID'].values[1], 0])
registrations.append([f"REG9993", fraud_stu, "Fraud Student", df_sess[df_sess['SessionType']=='Starter']['SessionID'].values[2], 0])

pd.DataFrame(registrations, columns=['RegistrationID', 'StudentID', 'StudentName', 'SessionID', 'FeePaid']).to_csv(os.path.join(out_dir, 'DTunes_Registrations.csv'), index=False)
df_sess.to_csv(os.path.join(out_dir, 'DTunes_Sessions.csv'), index=False)
df_inst.to_csv(os.path.join(out_dir, 'DTunes_Instructors.csv'), index=False)

print("Chapter 6 datasets generated successfully!")
