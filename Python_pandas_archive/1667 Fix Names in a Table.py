# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
#
# Return the result table ordered by user_id.

import pandas as pd

data = [[1,'aLice '],[2,'bOB'],[3,'kim Saram']]
users = pd.DataFrame(data, columns=['user_id','name'])

def fix_names(users: pd.DataFrame):
    #to capitalize both First and Last name
    #users['name'] = users['name'].str.title()
    users['name'] = users['name'].str.capitalize()
    users = users.sort_values(by='user_id')
    print(users)

fix_names(users)
