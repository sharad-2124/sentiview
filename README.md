
# 📊 Sentiview — AI-Powered YouTube Sentiment Analytics

Sentiview is an end-to-end AI system that analyzes YouTube video comments using **Azure OpenAI (GPT-4o)** and produces structured sentiment insights.

It automatically:

* Fetches all comments from a YouTube video
* Cleans and preprocesses text
* Batches comments for cost-efficient inference
* Uses GPT-4o for sentiment classification
* Aggregates results
* Produces percentage-based analytics

The system is designed with **production-style architecture**, including modular components, clean separation of concerns, and object-oriented design.

---

## 🚀 Features

✅ YouTube comment ingestion (YouTube Data API v3)

✅ Emoji + noise removal

✅ Batch GPT inference (cost optimized)

✅ Robust JSON parsing

✅ Sentiment aggregation

✅ Percentage analytics

✅ Modular class-based architecture

✅ Azure OpenAI integration

✅ Production-ready pipeline

Sentiment categories:

* Positive
* Neutral
* Negative

---

## 🧠 High-Level Architecture

```
YouTube Video
     ↓
YouTubeClient
     ↓
TextCleaner
     ↓
SentimentEngine (Azure GPT-4o)
     ↓
AnalyzerService
     ↓
sentiment_result.json
```

---

## 📁 Project Structure

```
sentiview/
│
├── core/
│   ├── youtube_client.py     # YouTube API integration
│   ├── sentiment_engine.py  # Azure GPT-4o wrapper
│   ├── text_cleaner.py      # Emoji + noise removal
│   └── prompts.py           # LLM system/user prompts
│
├── services/
│   └── analyzer_service.py  # Batching + aggregation logic
│
├── config/
│   └── settings.py          # Environment configuration
│
├── data/
│   └── sentiment_result.json  # Generated output
│
├── main.py                  # Application entry point
├── requirements.txt
└── config.env               # Environment variables (NOT committed)
```

---

## 🔐 Configuration

Create a file named:

```
config.env
```

Place it in the project root:

```
sentiview/config.env
```

### Example `config.env`

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=gpt-4o

YOUTUBE_API_KEY=your_youtube_api_key
```

⚠️ Never commit `config.env`.

It is ignored via `.gitignore`.

---

## 🛠 Installation

### 1. Create virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Open `main.py` and set your YouTube URL:

```python
VIDEO_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

Then run:

```bash
python main.py
```

---

## ✅ Output

Results are printed to console and saved to:

```
data/sentiment_result.json
```

### Example:

```json
{
  "video_url": "...",
  "total_comments": 214,
  "sentiment_distribution": {
    "Positive": 57.94,
    "Neutral": 29.91,
    "Negative": 12.15
  },
  "raw_counts": {
    "Positive": 124,
    "Neutral": 64,
    "Negative": 26
  }
}
```

---

## 🧩 Core Components

### YouTubeClient

Fetches all comments from a video using YouTube Data API v3.

---

### TextCleaner

Removes emojis and short/noisy comments.

---

### SentimentEngine

Wraps Azure OpenAI GPT-4o and performs batch sentiment classification.

---

### AnalyzerService

Handles:

* Chunking
* Rate limiting
* Aggregation
* Percentage computation

---

## 💡 Design Decisions

### Why batching?

Calling GPT once per comment is slow and expensive.

Sentiview batches 20 comments per request for:

* Lower cost
* Faster execution
* Reduced API overhead

---

### Why strict JSON prompts?

LLMs naturally return conversational output.

Sentiview enforces:

* JSON only
* No markdown
* No explanations

This guarantees machine-readable responses.

---

### Why robust JSON extraction?

Even with strict prompts, LLMs may add whitespace or invisible characters.

Sentiview safely extracts JSON using:

```
find("[") → find("]")
```

This makes the pipeline production-safe.

---

## 📈 Performance

Typical pipeline:

* ~200 comments
* ~11 GPT calls
* ~20–30 seconds runtime (depending on network)

---

## 🔒 Security

* API keys stored only in `config.env`
* Secrets excluded via `.gitignore`
* No credentials committed to Git

---

## 🛣 Roadmap (Optional Enhancements)

Future upgrades:

* FastAPI REST endpoint
* Async batching (5–10× faster)
* Token cost estimator
* React dashboard
* Chart visualization
* Azure Blob Storage
* Azure Functions deployment
* Per-comment sentiment export

---

## ⭐ Project Name

**Sentiview — AI Powered YouTube Sentiment Analytics**

---

## 🏁 Summary

Sentiview is a complete AI analytics backend demonstrating:

* Real API ingestion
* Large language model batching
* Robust parsing
* Aggregation logic
* Clean architecture

This mirrors how real-world NLP analytics systems are built.
