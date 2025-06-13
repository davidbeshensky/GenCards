from urllib.parse import urlparse, parse_qs

def clean_url(url: str) -> str:
    if "youtu.be" in url:
        # Convert short link to full
        video_id = url.split("/")[-1].split("?")[0]
    else:
        # Extract v= parameter
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        video_id = query.get("v", [""])[0]

    return f"https://www.youtube.com/watch?v={video_id}"
