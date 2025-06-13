import yt_dlp

def download_video(url: str, output_path: str = "output/video.mp4") -> str:
    ydl_opts = {
        'format': 'best[ext=mp4][vcodec^=avc1]+bestaudio/best',
        'outtmpl': output_path,
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path
