#Write a solution to find all the authors that viewed at least one of their own articles.

#Return the result table sorted by id in ascending order.

import pandas as pd

table = [
        [1,3,5,'2019-08-01'],
        [1,3,6,'2019-08-02'],
        [2,7,7,'2019-08-01'],
        [2,7,6,'2019-08-02'],
        [4,7,1,'2019-07-22'],
        [3,4,4,'2019-07-21'],
        [3,4,4,'2019-07-21']
]

views= pd.DataFrame(table, columns=['article_id','author_id','viewer_id','view_date'])

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['id'] = views.apply(lambda row: row['author_id'] if row['author_id'] == row['viewer_id'] else 0, axis=1 ).unique()
    filtered_output = (result['id'] != 0)
    output = result.loc[filtered_output]
    output = output.sort_values(by='id')
    return output

output = article_views(views)
print(output)

    