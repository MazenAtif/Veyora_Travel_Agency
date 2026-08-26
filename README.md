# Veyora_Travel_Agency


## Setup

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env.example` to `.env` file with your Duffel sandbox key


3. Start Docker Desktop, then start the database:
```bash
cd docker
docker-compose up -d
```


4. Run the server:
```bash
uvicorn main:app --reload
```


## Endpoints

### POST `/search-flight`
Searches flights between two cities using Duffel API.


### POST `/best-destination`
Suggests the best travel destination based on weather, static ratings, flight price within budget, and AI ranking (Groq).

### POST `/create-booking`
Creates a pending booking, stores it in DB, sends confirmation email.

### GET `/booking/{email}/{confirmation_id}`
Returns one specific booking by email + confirmation ID.