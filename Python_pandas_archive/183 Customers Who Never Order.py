#Write a solution to find all customers who never order anything.

#Return the result table in any order.

import pandas as pd

customer_data = [
                    [1, "Joe"],
                    [2, "Henry"],
                    [3, "Sam"],
                    [4, "Max"]
]
customers = pd.DataFrame(customer_data, columns=['id','name'])

orders_data = [[1,3],[2,1]]
orders = pd.DataFrame(orders_data, columns=['id','customerId'])

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    missing_ids = customers[~customers['id'].isin(orders['customerId'])]
    result = missing_ids[['name']].rename(columns={'name':'customers'})
    return result

output = find_customers(customers, orders)
print(output)

    