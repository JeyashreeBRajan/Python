#Write a solution to find for each date the number of different products sold and their names.

#The sold products names for each date should be sorted lexicographically.

#Return the result table ordered by sell_date.

import pandas as pd

data = [['2020-05-30','Headphone'],['2020-06-01','Pencil'],['2020-06-02','Mask'],['2020-05-30','Basketball'],['2020-06-01','Bible'],['2020-06-02','Mask'],['2020-05-30','T-Shirt']]
activities = pd.DataFrame(data,columns=['sell_date','product'])

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date')['product'].agg(list).reset_index()
    activities['products'] = activities['product'].apply(lambda x: dict.fromkeys(x))
    activities['products'] = activities['products'].apply(lambda x: sorted(x))
    activities['num_sold'] = activities['products'].apply(lambda x: len(x))
    activities['products'] = activities['products'].apply(lambda x: ','.join(x))
    activities = activities.sort_values(by='sell_date')
    activities = activities[['sell_date','num_sold','products']]
    return activities

print(categorize_products(activities))


    