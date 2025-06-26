#Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
#Return the result table in any order.
import pandas as pd

data = [[1,1,0],[1,1,1],[1,1,2],[1,2,3],[1,2,4],[2,1,5],[2,1,6]]
actor_director = pd.DataFrame(data, columns = ['actor_id','director_id','timestamp'])
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director= actor_director.groupby(['actor_id','director_id'])['timestamp'].agg(list).reset_index()
    actor_director['count'] = actor_director['timestamp'].apply(lambda x: len(x))
    return actor_director[['actor_id','director_id']].where(actor_director['count'] >= 3).dropna()
print(actors_and_directors(actor_director))
    