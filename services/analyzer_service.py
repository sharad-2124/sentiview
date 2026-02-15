import time
from collections import Counter

class SentimentAnalyzerService:

    def __init__(self, engine, cleaner, settings):
        self.engine = engine
        self.cleaner = cleaner
        self.settings = settings

    def chunk(self, lst):
        for i in range(0, len(lst), self.settings.BATCH_SIZE):
            yield lst[i:i + self.settings.BATCH_SIZE]

    def analyze(self, comments):

        comments = self.cleaner.clean(comments)

        all_results = []

        for batch in self.chunk(comments):
            results = self.engine.analyze_batch(batch)
            all_results.extend(results)
            time.sleep(self.settings.SLEEP_SECONDS)

        counter = Counter(r["sentiment"] for r in all_results)

        total = sum(counter.values())

        percentages = {
            k: round(v * 100 / total, 2)
            for k, v in counter.items()
        }

        return percentages, counter
