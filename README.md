# Matiks Content OS

**AI-native Content Operating System** for multi-channel Instagram management at scale.

One operator. 50 channels. 250 reels/day. Zero manual effort.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MATIKS CONTENT OS                        │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ 14 AI    │  │ Feedback │  │ Trend    │  │ Knowledge│     │
│  │ Agents   │──│ Loop     │──│ Intel    │──│ Graph    │     │ 
│  │          │  │ Engine   │  │ Engine   │  │          │     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│       │              │              │              │        │
│       ▼              ▼              ▼              ▼        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           Reel Generation Pipeline                   │   │
│  │  Trend → Script → Storyboard → Visual → Voice → Edit │   │
│  └──────────────────────────────────────────────────────┘   │ 
│                          │                                  │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │        Self-Improving Content Intelligence           │   │
│  │  Retention → Feedback → Strategy Adjustment → Agents │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Core Systems

### Multi-Agent Orchestration
14 specialized AI agents that communicate through orchestrated pipelines:

| Agent | Role |
|-------|------|
| Trend Hunter | Platform scanning, trend detection, viral hook identification |
| Competitor Intelligence | Competitor monitoring, gap analysis, pattern replication |
| Hook Generator | Scroll-stopping hooks using retention data and emotional triggers |
| Script Writer | High-retention scripts with viral pacing and emotional arcs |
| Viral Analyzer | Reverse-engineers viral content into reusable templates |
| Voiceover | AI voice generation with tone/emotion calibration |
| Scene Planner | Visual scene planning, shot composition, storyboards |
| Video Generator | AI video generation + FFmpeg assembly pipeline |
| Thumbnail Optimizer | A/B test thumbnails with attention heatmap predictions |
| Caption Generator | SEO-optimized captions with hashtag strategies |
| Posting Scheduler | Optimal timing using audience activity patterns |
| Analytics Feedback | Self-improvement engine — auto-adjusts all strategies |
| Content Memory | Niche-specific memory banks and cross-channel learning |
| Brand Consistency | Cross-channel brand voice and visual identity enforcement |

### Self-Improving Content Intelligence
The system continuously learns from:
- Retention curves and watch time
- Hook drop-off patterns
- Save, share, and comment ratios
- Competitor performance shifts
- Audience demographic changes
- Posting time effectiveness

Then automatically adjusts:
- Hook strength and duration
- Script pacing and narrative style
- Editing patterns and scene duration
- CTA style and placement
- Voice tone and speed
- Posting schedule
- Hashtag strategy

### Reel Generation Pipeline
6-stage autonomous pipeline:
1. **Trend Discovery** — Trend Hunter + Competitor Intel + Content Memory
2. **Content Strategy** — Analytics Feedback + Viral Analyzer
3. **Creative Generation** — Hook Generator + Script Writer
4. **Production** — Scene Planner + Voiceover + Brand Consistency
5. **Video Assembly** — Video Generator + Thumbnail Optimizer
6. **Publishing** — Caption Generator + Posting Scheduler

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 16, Tailwind CSS 4, Framer Motion, Recharts |
| Backend | FastAPI, SQLAlchemy 2.0, Pydantic v2 |
| Database | PostgreSQL 16, Weaviate (Vector DB) |
| Queue | Redis 7, Celery 5 |
| AI | OpenAI GPT-4, Anthropic Claude 3, Google Gemini |
| Voice | ElevenLabs Multilingual v2 |
| Video | Runway Gen-2, Pika, FFmpeg |
| Transcription | Whisper |
| Agent Framework | Custom multi-agent orchestrator |

---

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 20+
- Python 3.12+

### Option 1: Docker Compose
```bash
docker compose up
```
Frontend: http://localhost:3000
Backend: http://localhost:8000

### Option 2: Local Development

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Environment
Copy `.env.example` to `backend/.env` and fill in your API keys.

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/channels` | List all channels with metrics |
| `GET /api/channels/{id}/health` | Channel health diagnostics |
| `GET /api/trends` | All tracked trends |
| `GET /api/trends/emerging` | Emerging trend detection |
| `GET /api/trends/viral` | Currently viral trends |
| `GET /api/trends/radar` | Niche trend radar data |
| `GET /api/agents` | Agent registry with capabilities |
| `POST /api/agents/{type}/run` | Execute a single agent |
| `POST /api/pipeline/generate-reel` | Trigger full reel pipeline |
| `GET /api/pipeline/active` | Active pipeline monitoring |
| `POST /api/pipeline/feedback-loop` | Run self-improvement cycle |
| `GET /api/knowledge/graph` | Content knowledge graph |
| `GET /api/analytics/dashboard` | Full analytics dashboard |
| `GET /api/analytics/feedback-log` | AI adjustment history |

API docs available at http://localhost:8000/docs

---

## Project Structure

```
matiks/
├── backend/
│   ├── app/
│   │   ├── agents/          # 14 AI agents + orchestrator
│   │   ├── api/             # FastAPI route handlers
│   │   ├── models/          # SQLAlchemy data models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic services
│   │   ├── config.py        # Environment configuration
│   │   ├── database.py      # Database connection
│   │   └── main.py          # FastAPI application
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js app router
│   │   ├── lib/             # API client, utilities, mock data
│   │   └── components/      # React components
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Key Differentiators

1. **Self-Improving Intelligence** — The system doesn't just generate content. It learns from every metric and automatically optimizes all downstream generation.

2. **Multi-Agent Coordination** — 14 agents communicate through orchestrated pipelines, not isolated workflows. Each agent's output feeds the next stage with context.

3. **Viral Reverse Engineering** — Any viral reel can be deconstructed into a reusable template with hook structure, pacing, emotional triggers, and CTA strategy.

4. **Content Knowledge Graph** — Visual neural network of content relationships, viral clusters, hook families, audience segments, and winning formats.

5. **Operator Command Center** — Cinematic real-time dashboard showing pipeline status, agent activity, trend radar, feedback signals, and AI strategy adjustments.

---

## License

Proprietary — Internal use only.
