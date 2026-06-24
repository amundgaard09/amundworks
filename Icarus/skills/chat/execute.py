
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("ICARUS_OPENAI_API_KEY")
system_instruction = """
You are ICARUS, an AI agent inspired by Tony Stark's JARVIS.
You will respond in a short, concise and natural way.
Your responses are to be streamed to a voice synthesiser, so avoid non-alphanumeric characters.
"""

client = OpenAI(api_key=api_key)

def execute(**kwargs):
    prompt = kwargs.get("prompt", "")
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {"role": "system", "content": system_instruction},
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

    except Exception as e:
        return f"An error occurred: {e}"