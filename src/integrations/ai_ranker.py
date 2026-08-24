from groq import Groq
from core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

async def rank_destinations(destinations: list[dict]):
    prompt = f"""Given this travel destination data (weather, rating):
{destinations}

Pick the best destination and explain why in 1-2 short sentences, friendly tone, suitable for a voice agent to speak aloud. Respond ONLY with plain text, no markdown."""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return completion.choices[0].message.content