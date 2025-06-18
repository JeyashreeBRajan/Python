#Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

#Return the result table ordered by employee_id.

import pandas as pd

data = [[2,'Meir',3000],[3,'Michael',3800],[7,'Addilyn',7400],[8,'Juan',6100],[9,'Kannon',7700]]

employees = pd.DataFrame(data, columns = ['employee_id','name','salary'])

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(columns = ['employee_id','bonus'])
    result['employee_id'] = employees['employee_id']
    result['bonus'] = employees.apply(lambda row:row['salary'] if (row['employee_id']%2 != 0 and row['name'][0] != 'M') else 0, axis =1)
    result = result.sort_values(by='employee_id')
    return result

output = calculate_special_bonus(employees)
print(output)