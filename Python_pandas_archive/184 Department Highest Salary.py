# id is the primary key (column with unique values) for this table.
# departmentId is a foreign key (reference columns) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
# Write a solution to find employees who have the highest salary in each of the departments.
# 
# Return the result table in any order.

import pandas as pd

data_1 = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2],
          [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data_1, columns=['id', 'name', 'salary', 'departmentId'])

data_2 = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data_2, columns=['id', 'name'])


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame):
    df = pd.DataFrame()
    merge_df = pd.merge(employee, department, left_on='departmentId',right_on='id' )
    df = merge_df.sort_values(by=['salary','departmentId'], ascending=[False, True])
    df['rank'] = df.groupby('departmentId')['salary'].rank(ascending=False)
    top_salary = df[df['rank'] <2 ]#.sort_values(by=['departmentId', 'rank'])

    output = pd.DataFrame(columns=['Department','Employee','Salary'])
    output['Department'] = top_salary['name_y']
    output['Employee'] = top_salary['name_x']
    output['Salary'] = top_salary['salary']

    print(output)

output= department_highest_salary(employee, department)
print(output)
