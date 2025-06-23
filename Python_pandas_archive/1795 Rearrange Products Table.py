# Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
#
# Return the result table in any order.
import pandas as pd

data = [[0, 95, 100, 105], [1, 70,None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2','store3'])


def rearrange_products_table(products: pd.DataFrame):
    rearranged_df = pd.DataFrame(columns=['product_id','store','price'])
    rearranged_df = products.melt(id_vars='product_id',var_name='store', value_name='price')
    rearranged_df.dropna(subset='price', inplace=True)
    print(rearranged_df)

rearrange_products_table(products)



