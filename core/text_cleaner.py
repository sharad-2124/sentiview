import re

class TextCleaner:

    @staticmethod
    def remove_emojis(text):
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub("", text)

    @classmethod
    def clean(cls, comments):
        cleaned = []

        for c in comments:
            c = cls.remove_emojis(c).strip()
            if len(c) > 5:
                cleaned.append(c)

        return cleaned
