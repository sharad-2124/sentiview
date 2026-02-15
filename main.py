import json
from config.settings import Settings
from core.youtube_client import YouTubeClient
from core.sentiment_engine import SentimentEngine
from core.text_cleaner import TextCleaner
from services.analyzer_service import SentimentAnalyzerService

VIDEO_URL = "https://www.youtube.com/watch?v=5i2Hn8OG94o&t=18s"

def main():

    settings = Settings()

    yt = YouTubeClient(settings.YOUTUBE_API_KEY)
    engine = SentimentEngine(settings)
    service = SentimentAnalyzerService(engine, TextCleaner, settings)

    video_id = yt.extract_video_id(VIDEO_URL)
    comments = yt.fetch_comments(video_id)

    sentiments, counts = service.analyze(comments)

    output = {
        "video_url": VIDEO_URL,
        "total_comments": sum(counts.values()),
        "sentiment_distribution": sentiments,
        "raw_counts": dict(counts)
    }

    with open("data/sentiment_result.json", "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
