import asyncio
import asyncpraw, json
from os.path import basename
import asyncprawcore.exceptions

# Path to the client id, secret and path to save the data 
ID = "Computational Science/ESC403/Course Project/API Tests/Reddit/clientid.txt"
SECRET = "Computational Science/ESC403/Course Project/API Tests/Reddit/clientsecret.txt"
SAVE_PATH = "Computational Science/ESC403/Course Project/API Tests/Reddit/reddit_test.json"

# Read the client id and secret from the file and saving them in a constant
with open(ID) as f:
    cid = f.read().strip()
    
with open(SECRET) as f:
    csec = f.read().strip()

# Function to get the url of a reddit post
# This is later used to iterate through comments of the post icluding replies to comments 
# TODO: make sure only top level comments are included (maybe 1-2 replies max)
# TODO: change the code so that not only self posts are included
async def get_post_links(reddit, subreddit_name, limit=5):
    subreddit = await reddit.subreddit(subreddit_name)
    links = []
    
    async for post in subreddit.new(limit=limit):
        # Check if the post is a self-post
        if post.is_self:
            links.append(post.url)
        else:
            # For non-self posts, check if the URL points to Reddit
            if "reddit.com" in post.url:
                links.append(post.url)
    
    return links

# Function that gets the comments of a post and saves them inside a dictionary which then gets saved to a json file
async def get_comments_top_posts(reddit, subreddit_name, limit=5, comments_limit=5):
    # Check if the subreddit exists
    try:
        subreddit = await reddit.subreddit(subreddit_name, fetch=True)
    except asyncprawcore.exceptions.NotFound:
        print(f"Subreddit {subreddit_name} not found.")
        return {}

    # Get the links of the top posts
    links_list = await get_post_links(reddit, subreddit_name, limit)
    coms = {}

    # Iterate through the links and get the comments
    for link in links_list:
        try:
            submission = await reddit.submission(url=link)
            await submission.comments.replace_more(limit=0)
            comments = submission.comments.list()
            coms[submission.title] = [comment.body for comment in comments[:comments_limit]]
        
        # Error handling
        except asyncprawcore.exceptions.NotFound:
            print(f"Post not found: {link}")
            
        except Exception as e:
            print(f"Error processing post {link}: {e}")

    return coms

# Main function where reddit api gets called and then used for the rest of the script
async def main():
    reddit = asyncpraw.Reddit(
            client_id= cid,
            client_secret= csec,
            user_agent= "DataScience by /u/TroNiiXx https://www.github.com/TroNiiXx/uzh"
    )
    # header line
    comments_data = {
        "header": {
            "format": "post_title: [comment1, comment2, ...]"},
        
        "data": await get_comments_top_posts(reddit, "ethz", limit=10, comments_limit=10) # function call
    }
    
    # saving the data to a json file
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(comments_data, f, ensure_ascii=False, indent=4)
    
    # print the path to the file and close the reddit api
    print(f"Data saved to {basename(SAVE_PATH)}")
    await reddit.close()
    
# standart call to main
if __name__ == "__main__":
    asyncio.run(main())