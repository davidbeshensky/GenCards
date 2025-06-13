from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define video-level context
video_title = ""
learning_goal = ""

def set_video_context(title: str, goal: str):
    global video_title, learning_goal
    video_title = title
    learning_goal = goal

def generate_flashcard(text_chunk: str) -> str:
    prompt = f"""You are creating flashcards to help someone deeply understand the material in a video titled: "{video_title}".

Their learning goal is: "{learning_goal}".

Only create flashcards that teach **concrete, valuable technical knowledge or conceptual insights** directly from the transcript.
⚠️ Do **not** generate flashcards that are vague, general, or about the speaker’s intent, opinions, or structure of the video.

Only include:
- Definitions
- Explanations of how something works
- Clear examples or mechanisms
- Step-by-step processes
- Comparisons or distinctions

Format:
Q: ...
A: ...

Transcript:
{text_chunk}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content
    return content.strip() if content else ""
