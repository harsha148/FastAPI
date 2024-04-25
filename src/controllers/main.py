import time

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from Tweet import Tweet
from User import User

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hashtags")
async def get_hashtags():
    trending_hashtags = ['#Covid','#Corana','#Deepika','#Mahesh','#CSK']
    return trending_hashtags

@app.get('/recenttweets')
async def get_recent_tweets():
    tweets = [Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Musk', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open'])]
    return tweets

@app.get('/gettweetsbyuserid')
async def get_recent_tweets(user_id:str=''):
    tweets = [Tweet('Revanth', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Revanth', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Revanth', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('Revanth', 'Musk123', time.time(), 'I am asexual #Open', 10000, 100, ['#Open'])]
    return tweets


@app.get('/trendingtweets')
async def get_recent_tweets():
    tweets = [Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('NCB', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open'])]
    return tweets

@app.get('/trendingusers')
async def get_trending_users():
    return [
        User('Musk','@Musk123',True, 'Twitter Owner'),
        User('NCB','@NCB123',True,'AP Future CM'),
        User('Jagan','@Jagan123',True,'AP CM')
    ]


@app.get('/filterby')
async def get_filtered_tweets(search:str=''):
    if search[0]=='@':
        return [
            User('KCR','@Musk123',True, 'Twitter Owner'),
            User('KTR','@NCB123',True,'AP Future CM'),
            User('PK','@Jagan123',True,'AP CM')
        ]
    tweets = [Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open']),
              Tweet('KCR', 'NCB143', time.time(), 'I am asexual #Open', 10000, 100, ['#Open'])]
    return tweets

# Tweet object
    # user_name str
    # user_id str
    # created_at time
    # text str
    # retweet_count int
    # likes_count int
    # hashtags list

# Trending Hashtags
    # hastags list

#Trending tweets:
    # tweets

# Trending users:
    #list of users:
        # user_id: str
        # user_name: str
        # followers_count: int
        # following_count: int
        # tweets_count: int
        # description: str
        # verified: bool

# Search
    # request:
        # search_by
        # start_time
        # end_time

    # Response:
        # flag: USERS|TWEETS
        # tweets
        # users