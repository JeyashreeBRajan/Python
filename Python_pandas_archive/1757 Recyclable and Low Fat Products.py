#Write a solution to find the ids of products that are both low fat and recyclable.
#Return the result table in any order.

import pandas as pd

data =[
        [0,'Y','N'],
        [1,'Y','Y'],
        [2,'N','Y'],
        [3,'Y','Y'],
        [4,'N','N']
]

products = pd.DataFrame(data, columns=['product_id','low_fats','recyclable'])

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered = ((products['low_fats'] == 'Y') & (products['recyclable']=='Y'))
    result = products.loc[filtered, ['product_id']]
    return result

result = find_products(products)
print(result)
    