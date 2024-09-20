import uuid
import time
from redis import Redis

# Connect to Redis
redis_conn = Redis(host='localhost', port=6379, db=0)

# Example of adding a test submission
test_user_id = 'Altamash_free'
submission_id = str(uuid.uuid4())  # Generate a unique ID
timestamp = int(time.time())  # Use current time or a specific time

# Add the submission to the user's submissions
redis_conn.zadd(f"user:{test_user_id}:submissions", {submission_id: timestamp})

# Store the submission details
redis_conn.hmset(f"submission:{submission_id}", {
    'platform': 'twitter',
    'hashtags': '#test,#example',
    'sentiment_score': 0.5
})

print(f"Test submission added: ID={submission_id}, User={test_user_id}")
