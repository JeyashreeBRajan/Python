# Write a solution to find all the classes that have at least five students.
#
# Return the result table in any order.

import pandas as pd

data =[['A','Math'],['B','English'],['C','Math'],['D','Biology'],['E','Math'],['F','Comp'],['G','Math'],['H','Math'],['I','Math']]
courses = pd.DataFrame(data, columns = ['student','class'])

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame()
    output = courses.groupby('class')['student'].count().reset_index()
    output.columns = ['class','cnt']
    filtered = (output['cnt'] >= 5)
    output_df = output.loc[filtered, ['class']]
    return output_df

output = find_classes(courses)
print(output)