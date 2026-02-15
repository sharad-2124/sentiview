import requests

class YouTubeClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def extract_video_id(self, url):
        return url.split("watch?v=")[1].split("&")[0]

    def fetch_comments(self, video_id):

        comments = []
        next_page = None

        while True:

            params = {
                "part": "snippet",
                "videoId": video_id,
                "maxResults": 100,
                "textFormat": "plainText",
                "key": self.api_key,
                "pageToken": next_page
            }

            r = requests.get(
                "https://www.googleapis.com/youtube/v3/commentThreads",
                params=params
            ).json()

            for item in r.get("items", []):
                comments.append(
                    item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                )

            next_page = r.get("nextPageToken")

            if not next_page:
                break

        return comments
