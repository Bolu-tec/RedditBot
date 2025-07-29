import praw

# Replace the placeholders below with your Reddit API credentials before running the bot.
REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USERNAME = "YOUR_USERNAME"
REDDIT_PASSWORD = "YOUR_PASSWORD"
USER_AGENT = "bot by u/YOUR_USERNAME"



reddit_instance = praw.Reddit(
    client_id= REDDIT_CLIENT_ID,
    client_secret= REDDIT_CLIENT_SECRET,
    username= REDDIT_USERNAME,
    password= REDDIT_PASSWORD,
    user_agent= USER_AGENT
)

SUBREDDIT = "friendship"  # change this to the subreddit you want
KEYWORD = "hello"
REPLY_TEXT = "Hi there!  This is an automated reply."
def main():
    print(f"Bot is running on r/{SUBREDDIT}...")
    for comment in reddit_instance.subreddit(SUBREDDIT).stream.comments(skip_existing=True):
        if KEYWORD.lower() in comment.body.lower():
            try:
                print(f"Replying to comment: {comment.id}")
                comment.reply(REPLY_TEXT)
                print(f" Link: https://reddit.com{comment.permalink}")
            except Exception as e:
                print(f"Error replying: {e}")

if __name__ == "__main__":
    main()
