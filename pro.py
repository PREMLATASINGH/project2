import numpy as np
import pandas as pd
data = {
    'customer_id': [1, 2, 3, 4, 5], 
    'purchase_amount': [100, 200, 150, 300, 250],
    'purchase_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'product_category': ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
}
df = pd.DataFrame(data)
print(df)