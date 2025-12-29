import numpy as np
import pandas as pd

def clean_price(value):
    if pd.isna(value):
        return np.nan

    value = str(value).replace('â‚¹','').replace('₹','').replace(',','').strip()

    if 'Lakh' in value:
        num = float(re.findall(r'[\d\.]+',value)[0])
        return num*100000
    elif 'Crore' in value:
        num = float(re.findall(r'[\d\.]+',value)[0])
        return num*10000000
    else:
        try:
            return float(value)
        except:
            return np.nan
            
def clean_value(value):
    return float(re.findall(r'[\d\.]+',value)[0])

def clean_cc(value):
    return int(re.findall(r'[\d]+',value)[0])

def clean_kms(value):
    num = value.replace(',','')
    return int(re.findall(r'[\d\,]+',num)[0])
    
df_car = [your_dataframe].fillna({
    # 'registered_year':np.nan,
    'engine_capacity':'Not Specified',
    'insurance ':'Not Specified',
    'owner_type':'Not Specified'
})

df_car.drop_duplicates(inplace = True)
            
df_car['registered_year'] = pd.to_datetime(df_car['registered_year'], format = '%b-%y', errors = 'coerce').dt.year
df_car = df_car.dropna(subset=['registered_year'])
df_car['registered_year'] = df_car['registered_year'].astype(int)