#For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

#Return the result table in any order.

import pandas as pd

#data =[['2020-12-8','toyota',0,1],['2020-12-8','toyota',1,0],['2020-12-8','toyota',1,2],['2020-12-7','toyota',0,2],['2020-12-7','toyota',0,1],['2020-12-8','honda',1,2],['2020-12-8','honda',2,1],['2020-12-7','honda',0,1],['2020-12-7','honda',1,2],['2020-12-7','honda',2,1]]
#daily_sales = pd.DataFrame(data, columns=['date_id','make_name','lead_id','partner_id'])

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(['date_id','make_name']).nunique().reset_index()
    daily_sales.rename(columns = {'lead_id':'unique_leads', 'partner_id':'unique_partners'},inplace=True)
    return daily_sales
