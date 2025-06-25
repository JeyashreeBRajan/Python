#Write a solution to find the customer_number for the customer who has placed the largest number of orders.

#The test cases are generated so that exactly one customer will have placed more orders than any other customer.

import pandas as pd

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number'])


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame()
    output = orders['customer_number'].value_counts().reset_index()
    max_order = output['count'].max()
    output_df = output[output['count']== max_order][['customer_number']]
    return output_df


output = largest_orders(orders)
print(output)
