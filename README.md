# TruVox

<<<<<<< HEAD
TruVox examines image, text, video, and audio evidence, records file custody,
and presents findings with clear uncertainty. It supports human review; it
does not decide what happened.

## Project structure

```text
TruVox/
├── backend/
│   ├── analysis/                 # Image, frame, voice, metadata, and caption analysis
│   ├── assistant/                # Case Assistant prompts and provider integration
│   ├── detection/                # Image, text, audio, and video detectors
│   ├── models/                   # Lazy model loading and download/test scripts
│   ├── routes/                   # Flask API endpoints
│   ├── services/                 # Upload, media, case, custody, and report services
│   ├── tests/
│   │   ├── samples/               # Generated smoke-test images
│   │   └── smoke_test.py          # Flask end-to-end smoke checks
│   ├── assets/logo.png
│   ├── .env.example
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   └── scoring.py
├── frontend/
│   ├── public/
│   │   ├── sample/                # Comparison-page example image
│   │   └── logo.png
│   ├── src/
│   │   ├── components/            # Evidence Room UI components
│   │   ├── pages/                 # Welcome, Dashboard, Analyze, Compare, guide
│   │   ├── services/api.js
│   │   ├── App.jsx
│   │   └── style.css
│   ├── index.html
│   ├── package.json
│   └── package-lock.json
├── .gitignore
└── README.md
```

Runtime-only folders such as `backend/uploads/`, `backend/cases/`,
`backend/reports/`, model downloads, `backend/venv/`, `frontend/node_modules/`,
and `frontend/dist/` are created locally and are intentionally not committed.

## Requirements

- Python 3.12
- Node.js and npm
- FFmpeg available on `PATH` for video audio extraction
- Hugging Face model downloads for model-backed analysis
- A Gemini or Anthropic API key for live Case Assistant answers

## Backend setup

Run these commands from the repository root in PowerShell:

```powershell
py -3.12 -m venv backend\venv
.\backend\venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
Copy-Item backend\.env.example backend\.env
```

Edit `backend\.env` locally and set `LLM_PROVIDER`, `LLM_MODEL`, and `API_KEY`
if you want the Case Assistant. Keep the key in this file; never add it to
frontend code or commit `backend/.env`.

Download configured Hugging Face models when needed:

```powershell
python -m backend.models.download_models
```

Start the Flask API from the repository root:

```powershell
python -m backend.app
```

The API listens on `http://127.0.0.1:5000`. Model loading is lazy; check model
availability at `http://127.0.0.1:5000/api/health/models`.

Text analysis accepts pasted text or `.txt`, `.pdf`, and `.docx` files through
`POST /api/analyze`. The text detector uses
`Hello-SimpleAI/chatgpt-detector-roberta`; download it with the other configured
models before using the backend offline. AI-writing probabilities and style
indicators are signals for review, not proof of authorship.

## Frontend setup

In a second PowerShell window:

```powershell
Set-Location frontend
npm install
npm run dev
```

Open the local address printed by Vite, usually `http://localhost:5173`.
Vite proxies `/api` requests to the Flask backend.

Create a production frontend bundle with:

```powershell
Set-Location frontend
npm run build
```

## Checks

Run the backend smoke suite from the repository root:

```powershell
python -m backend.tests.smoke_test
```

The smoke suite generates its sample images under `backend/tests/samples/` and
uses Flask's test client. It may load configured local models; the Case
Assistant provider check requires a valid API key and a live network
connection.

## Case Assistant providers

Supported providers are `gemini` and `anthropic`. Configure `LLM_PROVIDER`,
`LLM_MODEL`, and `API_KEY` in the ignored `backend/.env` file. The API key is
read only by Flask and is never sent to the React app. Case summaries and chat
messages are sent to the selected provider when a user asks the assistant a
question.

## Evidence and model limitations

Detector scores are indicators, not proof. Verify findings against original
sources and independent evidence. A SHA-256 custody fingerprint can show
whether an uploaded file has changed since TruVox recorded it; it cannot prove
the file was genuine before upload.
=======
Multimodal digital forensics web application for audio and video analysis.

## Structure
- `backend/`: Flask API, detection, analysis, scoring and reporting.
- `frontend/`: React + Vite interface.

See the source files for implementation TODOs.
>>>>>>> 6594e4f4bf835a460745065b64555124ce96106a
