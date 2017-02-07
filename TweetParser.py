# cell 0

# cell 1
# import Twython library
# Twython library information is available here
# https://twython.readthedocs.io/en/latest/

from twython import Twython

# cell 2
# setup a Twitter developer account and get API access settings
# define the parameters that are required 

api_key = "XXXX"
api_secret = "XXXX"
access_token_key = "XXXX"
access_token_secret = "XXXX"

# cell 3
# create an object named t of type Twython with the parameters
# that were previously defined


t = Twython(app_key=api_key, app_secret=api_secret, oauth_token=access_token_key,
            oauth_token_secret=access_token_secret)

# cell 4
# creat a variable called search
# assign search the results of a search done using the t object
# that was defined previously

# the example below will return 10 most recent tweets containing
# "bmw" in the tweet by creating a connection to Twitter APIs and
# executing the search

search_results = t.search(q='bmw', count=1)

# cell 5
#print(search_results)

# cell 6
# print out the data type for the search_results variable

#print(type(search_results))

# cell 7
# print out the search results

#print(search_results)

# cell 8
# create a new object called tweets
# and assign its value to be the 'statuses' value
# from the search_results

tweets = search_results['statuses']

# cell 9
# check the data type for tweets

print(type(tweets))

# cell 10
print(tweets)

# cell 11
for tweet in tweets:
    print("Tweet Text: ")
    print(tweet['text'])

# cell 12
# import csv library
# it is useful for reading and writing comma separated values data files
# additional information about the library is available here
# https://docs.python.org/3/library/csv.html

import csv

# cell 13
# Saving the tweets to the csv file

# we will also need the sys and codecs libraries
# to handle text encoding challenges

with open(r'H:\Download\work\recent_tweets_bmw.csv', 'w', newline='') as csvfile:
    wf = csv.writer(csvfile, delimiter=',',
                    quotechar='"')

    for tweet in tweets:
        wf.writerow(['bmw', tweet['text'].encode("utf-8")])

# cell 14


