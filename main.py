import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("71QkNBHDbQtAwSMQ6Dl6bVhQm",
    "BKHAcscl3UhoHuX8Ief54fzLmnGONbTc2vQkj9WF8AXBaZxRu9")
auth.set_access_token("1462520428602212355-832IzxIn701Viz5UGXNePYItEhA2LM",
    "l9FcMShX4acS7RNg4fkBfrAj6uB0B6d0UIiExTS6xDkMH")

api = tweepy.API(auth)
api.verify_credentials()
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")