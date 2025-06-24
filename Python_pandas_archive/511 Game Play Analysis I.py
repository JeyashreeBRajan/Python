# Write a solution to find the first login date for each player.
# 
# Return the result table in any order.
import pandas as pd

data = [[1,2,'2016-03-01',5],[1,2,'2016-05-02',6],[2,3,'2017-06-25',1],[3,1,'2016-03-02',0],[3,4,'2018-07-03',5]]
activity = pd.DataFrame(data, columns =['player_id','device_id','event_date','games_played'])

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    output = pd.DataFrame()
    output = activity.groupby('player_id')['event_date'].min().reset_index()
    output.columns = ['player_id','first_login']
    return output

output =game_analysis(activity)
print(output)