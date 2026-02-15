import json
from openai import AzureOpenAI
from core.prompts import SYSTEM_PROMPT, USER_PROMPT

class SentimentEngine:

    def __init__(self, settings):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )

        self.model = settings.AZURE_OPENAI_MODEL

    def analyze_batch(self, batch):

        prompt = USER_PROMPT.format(comments=json.dumps(batch, ensure_ascii=False))

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content.strip()

        start = result.find("[")
        end = result.rfind("]") + 1

        return json.loads(result[start:end])
