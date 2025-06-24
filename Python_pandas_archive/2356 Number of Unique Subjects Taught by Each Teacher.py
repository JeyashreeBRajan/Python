# Write a solution to calculate the number of unique subjects each teacher teaches in the university.
#
# Return the result table in any order.

import pandas as pd

data =[[1,2,3],[1,2,4],[1,3,3],[2,1,1],[2,2,1],[2,3,1],[2,4,1]]
teacher = pd.DataFrame(data, columns=['teacher_id','subject_id','dept_id'])

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    output = pd.DataFrame()
    output = teacher.groupby('teacher_id')['subject_id'].unique().apply(len).reset_index()
    output.columns = ['teacher_id', 'cnt']
    return output

output = count_unique_subjects(teacher)
print(output)   