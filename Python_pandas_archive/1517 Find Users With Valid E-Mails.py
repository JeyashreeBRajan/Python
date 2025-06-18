#Write a solution to find the users who have valid emails.

#A valid e-mail has a prefix name and a domain where:

#The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
#Return the result table in any order.
#The domain is '@leetcode.com'.

import pandas as pd
import re as re

data =[[1,'Winston','winston@leetcode.com'],[2,'Jonathan','jonathanisgreat'],
        [3,'Annabelle','bella-@leetcode.com'],[4,'Sally','sally.come@leetcode.com'],
        [5,'Marwan','quarz#2020@leetcode.com'],[6,'David','david69@gmail.com'],
        [7,'Shapiro','.shapo@leetcode.com'],[8,'Ben','B@leetcode.com']]

users = pd.DataFrame(data,columns=['user_id','name','mail'])

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email=pd.DataFrame(columns=['user_id','prefix','domain'])
    email['user_id'] = users['user_id']
    email['prefix'] = users['mail'].str.split('@').str[0]
    email['domain'] = '@' + users['mail'].str.split('@').str[1]

    email['is_valid'] = False
    for index, row in email.iterrows():
        #is_prefix_valid = re.fullmatch(r'[a-zA-Z][\w\-\.]+', row['prefix']) is not None
        is_prefix_valid = re.fullmatch(r'[a-zA-Z][\w\-\.]*', row['prefix']) is not None
        is_domain_valid = row['domain']=='@leetcode.com'
        email.at[index,'is_valid'] = is_prefix_valid and is_domain_valid
    output = users[email['is_valid'] == True]
    return output
output = valid_emails(users)
print(output)

# re.fullmatch(r'[a-zA-Z][\w\-\.]+', row['prefix'])  # + means at least one *after* first letter
# Use * instead of + to allow zero or more characters after the first letter:
# re.fullmatch(r'[a-zA-Z][\w\-\.]*', row['prefix'])