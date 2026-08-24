# Veyora_Travel_Agency


## Setup

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env.example` to `.env` file with your Duffel sandbox key


3. Run the server:
```bash
uvicorn main:app --reload
```

## Endpoints

### POST `/search-flight`
Searches flights between two cities using Duffel API.


### POST `/best-destination`
Suggests the best travel destination based on weather, static ratings, flight price within budget, and AI ranking (Groq).