import tweepy

# Authenticate to Twitter
# should have api key
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

user = api.get_user("KMbappe")

print("User details:")
print(user.name)
print(user.description)
print(user.location)
print(len(user.followers()))

