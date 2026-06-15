import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# ── Settings ─────────────────────────────────────────────────
n = 500  # number of leads
reps   = ['Ayesha K', 'Rohan M', 'Priya S', 'Dev T', 'Neha R']
stages = ['Lead', 'Qualified', 'Demo', 'Proposal', 'Closed Won', 'Closed Lost']
plans  = ['Starter', 'Growth', 'Enterprise']
plan_value = {'Starter': 499, 'Growth': 1299, 'Enterprise': 3999}

# ── Generate leads ────────────────────────────────────────────
start_date = datetime(2024, 1, 1)
records = []

for i in range(n):
    created  = start_date + timedelta(days=random.randint(0, 364))
    rep      = random.choice(reps)
    plan     = random.choices(plans, weights=[50, 35, 15])[0]
    stage    = random.choices(stages, weights=[30, 25, 20, 12, 8, 5])[0]
    revenue  = plan_value[plan] if stage == 'Closed Won' else 0
    days_in  = random.randint(1, 90)
    churned  = random.choices([0, 1], weights=[85, 15])[0] if stage == 'Closed Won' else 0

    records.append({
        'Lead_ID':       f'L{1000+i}',
        'Created_Date':  created.strftime('%Y-%m-%d'),
        'Month':         created.strftime('%B %Y'),
        'Rep':           rep,
        'Plan':          plan,
        'Stage':         stage,
        'Revenue':       revenue,
        'Days_In_Pipeline': days_in,
        'Churned':       churned
    })

df = pd.DataFrame(records)
df.to_csv('saas_sales_data.csv', index=False)
print(f"✅ Dataset created: {len(df)} rows")
print(df.head())
print("\nStage breakdown:")
print(df['Stage'].value_counts())
print(f"\nTotal Revenue: ${df['Revenue'].sum():,}")