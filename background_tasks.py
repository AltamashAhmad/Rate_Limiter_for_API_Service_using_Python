import re
import time
from textblob import TextBlob
from redis import Redis

# Initialize Redis connection
redis_conn = Redis()

def extract_hashtags(content):
    return re.findall(r"#(\w+)", content)

def calculate_sentiment(content):
    blob = TextBlob(content)
    return blob.sentiment.polarity  # Returns a float between -1.0 (negative) and 1.0 (positive)

def process_submission(platform, content, timestamp, analysis_id, user_id):
    print(f"Processing submission {analysis_id} for user {user_id}")
    time.sleep(2)  # Simulate a delay in processing

    # Extract hashtags 
    hashtags = extract_hashtags(content)

    # Calculate sentiment score
    sentiment_score = calculate_sentiment(content)

    # Store submission data in Redis (GET)
    submission_key = f"submission:{analysis_id}"
    redis_conn.hmset(submission_key, {
        'platform': platform,
        'content': content,
        'timestamp': timestamp,
        'hashtags': ",".join(hashtags),
        'sentiment_score': sentiment_score
    })

    # Convert timestamp to epoch for sorting
    epoch_time = int(time.mktime(time.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")))

    # Add submission ID to user's sorted set with timestamp as score
    user_submissions_key = f"user:{user_id}:submissions"
    redis_conn.zadd(user_submissions_key, {analysis_id: epoch_time})

    print(f"Submission {analysis_id} from {platform} processed and stored successfully.")
