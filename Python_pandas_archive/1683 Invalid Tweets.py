#Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

#Return the result table in any order.

import pandas as pd

data = [[1,'Let us Code'],[2,'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns = ['tweet_id','content'])

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['tweet_id'] = tweets.apply(lambda row:row['tweet_id'] if len(row['content']) > 15 else 'valid_tweet', axis=1)
    filered = (result['tweet_id'] != 'valid_tweet')
    output = result.loc[filered, ['tweet_id']]
    return output

output = invalid_tweets(tweets)
print(output)
    