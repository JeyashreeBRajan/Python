# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
#
# Return the result table in any order.

import pandas as pd

data = [[1, '2020-11-28', 4, 32], [1, '2020-11-28', 55, 200], [1, '2020-12-03', 1, 42], [2, '2020-11-28', 3, 33],
        [2, '2020-12-09', 47, 74]]
employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time'])


def total_time(employees: pd.DataFrame):
    emp_time = pd.DataFrame(columns=['day','emp_id','total_time'])
    for index, row in employees.iterrows():
        emp_time.at[index, 'day'] = row['event_day']
        emp_time.at[index, 'emp_id'] = row['emp_id']
        emp_time.at[index, 'total_time'] = row['out_time'] - row['in_time']
    output = emp_time.groupby(['day','emp_id'])['total_time'].sum().reset_index()
    print(output)

total_time(employees)

