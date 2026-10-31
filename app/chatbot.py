from groq import Groq,APIConnectionError,RateLimitError,APIStatusError
from config import GROQ_API_KEY,GROQ_MODEL,MAX_TOKENS,TEMPERATURE


client = Groq(
    api_key=GROQ_API_KEY
)


def get_response(messages):
    try:
        
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages
        )
    except RateLimitError:
        return "Error: API RATE LIMIT EXCEEDED.\nPLEACE TRY AGAIN LATER"
    except APIConnectionError:
        return "ERROR: Unable to connect to Groq api."
    except APIStatusError as e :
        return f"ERROR: GROQ API returned status:{e.status_code}"
    except Exception:
        return "ERROR : Somethings went wrong c"
    return response.choices[0].message.content

def stream_response(messages):
    try:
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=True
        )

        full_response = ""

        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content,end="",flush=True)
                full_response += content

        print()
        return full_response
    except RateLimitError:
        return None
    except Exception:
        return None