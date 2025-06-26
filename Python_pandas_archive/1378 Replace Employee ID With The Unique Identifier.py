#Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

#Return the result table in any order.

import pandas as pd
data_1 = [[1,'Alice'],[7,'Bob'],[11,'Meir'],[90,'Winston'],[3,'Jonathan']]
employees = pd.DataFrame(data_1, columns=['id','name'])

data_2 = [[3,1],[11,2],[90,3]]
employee_uni = pd.DataFrame(data_2, columns=['id','unique_id'])

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employee_uni, on='id', how='left')
    #employees['unique_id'] = employees['unique_id'].where(pd.notnull(employees['unique_id']), None)
    return employees[['unique_id','name']]