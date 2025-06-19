#Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

import pandas as pd

data = [[1,100],[2,200],[3,300],[4,150]]
employee = pd.DataFrame(data, columns=['id','salary'])

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    output = pd.DataFrame()
    col = f'getNthHighestSalary{"("}{N}{")"}'
    distinct_salary = employee.sort_values(by='salary', ascending = False)
    distinct_salary = distinct_salary.drop_duplicates(subset='salary')

    if N > len(distinct_salary) or N < 1:
        output[col] = [pd.NA]       
    else:
        output[col] = distinct_salary['salary'].iloc[[N - 1]]

    return output
        

N = 2
output = nth_highest_salary(employee, N)
print(output)