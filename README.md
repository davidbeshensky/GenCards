# GenCards... Work in progess on the name

Today I was studying from a youtube video about how javascript works under the hood and I thought to myself, I should make some flashcards so I remember this. Shortly after I thought about how long that might take per video, and quickly rethought my plans. Insteaed I made GenCards which is a CLI tool for automatically generating flashcards from youtube videos and hopefully other media in the future.

## tech that I used
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — for downloading the YouTube video.
- **[ffmpeg](https://ffmpeg.org/)** — to extract audio and screenshots from the video.
- **[OpenAI GPT-4 API](https://platform.openai.com/)** — for generating useful Q&A flashcards from the transcript.
- **[OpenAI Whisper](https://github.com/openai/whisper)** — to transcribe speech to text.
- **[genanki](https://github.com/kerrickstaley/genanki)** — to generate `.apkg` files compatible with Anki.

## how does it work?
1. **you enter a youtube url + title** and specify what you'd like to learn from the video
2. the vide is **downloaded** with `yt-dlp`**.
3. **screenshots** are taken every 15 seconds of the video contents using ffmpeg
4. **audio** is then extracted  and transcribed using OpenAis whisper model.
5. the transcript is **split into chunks** and GPT4 is prompted to generate flashcards aligned with your learning goal.
6. flashcards are saved as:
  - `flashcards.json` - raw data
  - output_flashcards.apkg` - ready to import into Anki
7. all screenshots are saved and linked to each card for visual reinforcement.

## want to use it? here's how to get started:


```bash
### 1. Clone the repository
git clone https://github.com/your-username/GenCards.git
cd GenCards
### 2.set up a python virtual enviornment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Install ffmpeg (for macOS)
brew install ffmpeg
### 5. Add your own OpenAI key
#create a file named .env in the root directory of your project and add your own key with some seed money.
OPENAI_API_KEY=your-openai-api-key
###6. run the application
python main.py

#You'll be prompted to:

#🔗 Enter a YouTube URL

#🎯 Specify what you hope to learn from the video

#The script will then:

#Download the video

#Extract audio + screenshots

#Transcribe the speech

#Generate relevant flashcards using GPT-4

#Save them to output/flashcards.json and output/output_flashcards.apkg

###7. finally import the flashcards into Anki and get learning
```
