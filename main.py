from utils.download import download_video
from utils.transcribe import transcribe_audio
from utils.screenshots import extract_screenshots
from utils.summarize import generate_flashcard, set_video_context
from utils.anki_builder import create_deck
from tqdm import tqdm
import json

import os

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    title = input("Enter the video title: ")
    goal = input("What do you hope to learn from this video? ")

    set_video_context(title, goal)

    os.makedirs("output", exist_ok=True)

    print("📥 Downloading video...")
    download_video(url)

    print("🎞️ Extracting screenshots...")
    extract_screenshots()

    print("🔊 Extracting audio...")
    os.system("ffmpeg -i output/video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 output/audio.wav")

    print("📝 Transcribing...")
    segments = transcribe_audio("output/audio.wav")

    flashcards = []
    for seg in tqdm(segments, desc="🔄 Generating flashcards"):
        qa = generate_flashcard(seg["text"])
        if "Q:" in qa and "A:" in qa:
            try:
                q = qa.split("Q:")[1].split("A:")[0].strip()
                a = qa.split("A:")[1].strip()
                img_idx = int(seg['start'] // 15) + 1
                img_path = f"output/screenshots/frame_{img_idx:03d}.jpg"
                flashcards.append({"q": q, "a": a, "img": img_path})
            except Exception as e:
                print(f"⚠️ Failed to parse QA: {qa[:60]}... | Error: {e}")

    if not flashcards:
        print("❌ No flashcards generated. Check transcription or summarization.")
        exit(1)

    # 💾 Save flashcards to JSON
    with open("output/flashcards.json", "w") as f:
        json.dump(flashcards, f, indent=2)

    print("🗃️ Flashcards saved to output/flashcards.json")
    print("📦 Creating Anki deck...")
    create_deck(flashcards)

    print("✅ Done! Flashcards saved to output/output_flashcards.apkg")
