#Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

import pandas as pd

data =[[1,100],[2,200],[3,400],[4,150]]
employee = pd.DataFrame(data, columns=['id','salary'])

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    output = pd.DataFrame()
    col = "SecondHighestSalary"
    distinct_salary = employee.sort_values(by= 'salary', ascending = False)
    distinct_salary = distinct_salary.drop_duplicates(subset= 'salary')

    if len(distinct_salary) < 2:
        output[col]= [pd.NA]
    else:
        output[col]= distinct_salary['salary'].iloc[[1]]
    return output

output = second_highest_salary(employee)
print(output)
    