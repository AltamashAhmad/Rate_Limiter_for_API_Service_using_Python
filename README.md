# Rate_Limiter_for_API_Service
## 1. Rate-Limiting Strategy

### Rate-Limiting Algorithm
The API uses a token bucket algorithm for rate limiting. This method allows for a burst of requests up to a maximum limit and then refills tokens over time. The algorithm ensures fair usage across different tiers and handles high concurrency effectively.

### Rate Limits by Tier
- **Free Tier:**
  - Requests per minute: 10
  - Requests per hour: 100
- **Standard Tier:**
  - Requests per minute: 50
  - Requests per hour: 500
- **Premium Tier:**
  - Requests per minute: 200
  - Requests per hour: 2000

### Configuration Options
Rate limits are configured dynamically using environment variables. The following environment variables can be set to adjust the limits:
- `FREE_RATE_PER_MINUTE`
- `FREE_RATE_PER_HOUR`
- `STANDARD_RATE_PER_MINUTE`
- `STANDARD_RATE_PER_HOUR`
- `PREMIUM_RATE_PER_MINUTE`
- `PREMIUM_RATE_PER_HOUR`

## 2. Integration with API

### How It Works
- **Rate Limiting:** Each API request checks the user's tier and applies the corresponding rate limit using Redis. If the rate limit is exceeded, the API returns a 429 Too Many Requests status code with a `Retry-After` header indicating when the user can retry.

### Rate Limiting in Endpoints
- **Submit Data:** `POST /api/v1/analytics/submit`
- **Get Dashboard Data:** `GET /api/v1/analytics/dashboard`

## 3. Running the Service

### Setup Instructions
1. **Install Dependencies:**
# Activate the virtual environment
python3 -m venv venv
source venv/bin/activate  

   Ensure you have Python and Redis installed. Install required Python packages using:
   pip install -r requirements.txt
### Start Redis: Make sure Redis server is running. You can start Redis using
    redis-server
    brew services start redis    
   ### to restart redis 
    brew services restart redis
### Run the Application: Start the Flask application with:
    python app.py

### Dependencies
- `Flask: Web framework for Python.`
- `Flask-Cors: CORS support for Flask.
- `Redis: In-memory data structure store.`
- `RQ (Redis Queue): Library for background job processing.`
- `TextBlob: Text processing library (for sentiment analysis).`