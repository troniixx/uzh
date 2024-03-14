import praw, asyncio
import asyncpraw, json
from os.path import basename

ID = "Computational Science/ESC403/Course Project/API Tests/Reddit/clientid.txt"
SECRET = "Computational Science/ESC403/Course Project/API Tests/Reddit/clientsecret.txt"
SAVE_PATH = "Computational Science/ESC403/Course Project/API Tests/Reddit/reddit_test.json"

# Reddit API
with open(ID) as f:
    cid = f.read().strip()
    
with open(SECRET) as f:
    csec = f.read().strip()

async def get_comments_top_posts(reddit, subreddit_name, limit=5, comments_limit=5):
    subreddit = await reddit.subreddit(subreddit_name)
    comments = {}

    async for post in subreddit.new(limit=limit):
        post_title = post.title
        comments[post_title] = []

        # Check for comments before processing
        if post.comments is not None:
            try:
                await post.comments.replace_more(limit=0)
                count = 0
                for top_level_comment in post.comments:
                    if count >= comments_limit:
                        break
                    if isinstance(top_level_comment, asyncpraw.models.Comment):
                        comments[post_title].append(top_level_comment.body)
                        count += 1
            except Exception as e:
                print(f"Failed to process post {post_title}: {e}")
        else:
            # Handle case where post has no comments
            print(f"Post {post_title} has no comments or failed to retrieve comments.")

    return comments
    
async def main():
    reddit = asyncpraw.Reddit(
            client_id= cid,
            client_secret= csec,
            user_agent= "DataScience by /u/TroNiiXx https://www.github.com/TroNiiXx/uzh"
    )
    
    comments_data = {
        "header": {
            "format": "post_title: [comment1, comment2, ...]"},
        
        "data": await get_comments_top_posts(reddit, "learnprogramming", limit=5, comments_limit=5)
    }
    
    with open(SAVE_PATH, 'w', encoding='utf-8') as f:
        json.dump(comments_data, f, ensure_ascii=False, indent=4)
    
    print(f"Data saved to {basename(SAVE_PATH)}")
    await reddit.close()

if __name__ == "__main__":
    asyncio.run(main())
