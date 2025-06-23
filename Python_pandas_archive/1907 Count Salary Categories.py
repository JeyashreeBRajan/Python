# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
#
# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.
#
# Return the result table in any order.
import pandas as pd

data =[[3,108939],[2,12747],[8,87709],[6,91796]]
accounts = pd.DataFrame(data, columns=['account_id','income'])

def count_salary_categories(accounts: pd.DataFrame):
    output =pd.DataFrame()
    expected_category = ['Low Salary', 'Average Salary', 'High Salary']
    for index, row in accounts.iterrows():
        if row['income'] < 20000:
            accounts.at[index, 'category'] = 'Low Salary'
        elif row['income'] >= 20000 and row['income'] <= 50000:
            accounts.at[index,'category'] = 'Average Salary'
        elif row['income'] > 50000:
            accounts.at[index,'category'] = 'High Salary'
    category_count = accounts['category'].value_counts().reindex(expected_category, fill_value=0)

    output = category_count.reset_index()
    output.columns=['category','accounts_count']
    print(output)

count_salary_categories(accounts)
