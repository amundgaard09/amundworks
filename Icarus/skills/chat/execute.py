
import os, dotenv
from openai import OpenAI, RateLimitError

SYS_INSTRCTN = """
You are ICARUS, an AI agent inspired by Tony Stark's JARVIS.
Your task is to help with STEM projects, like robots, advanced math, etc.
You will respond in a short, concise and natural way.
Your responses are to be streamed to a voice synthesiser, so avoid non-alphanumeric characters.
"""

dotenv.load_dotenv()
api_key = os.getenv("ICARUS_OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def execute(**kwargs):
    prompt = kwargs.get("prompt", "")
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {"role": "system", "content": SYS_INSTRCTN},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        text_output = []
        
        for item in getattr(response, "output", []):
            if isinstance(item, dict) and item.get("type") == "message":
                for content_piece in item.get("content", []):
                    if content_piece.get("type") == "output_text":
                        text_output.append(content_piece.get("text", ""))

        if text_output:
            return "".join(text_output).strip()

        return str(response)

    except RateLimitError:
        return f"ChatGPT Unavailable: Rate limit exceeded."
    except Exception as e:
        return f"An error occurred: {e}"