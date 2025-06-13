import os

def extract_screenshots(video_path='output/video.mp4', output_dir='output/screenshots', interval=15):
    os.makedirs(output_dir, exist_ok=True)
    os.system(f"ffmpeg -i {video_path} -vf fps=1/{interval} {output_dir}/frame_%03d.jpg")
