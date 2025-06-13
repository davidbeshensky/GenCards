from typing import List, Dict, Any
import whisper

def transcribe_audio(audio_path: str = 'output/audio.wav') -> List[Dict[str, Any]]:
    print("📝 Loading Whisper model…")
    model = whisper.load_model("base")
    print("📝 Transcribing (this may take a while)…")
    result: Dict[str, Any] = model.transcribe(audio_path)
    return result['segments']
