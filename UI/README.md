# Week 6 + Week 7 Combined: Impact Predictor UI Prototype

This prototype combines:
- Week 6: simple UI form for impact/risk prediction
- Week 7: edge-case testing and logic improvements

It uses the best-performing saved model from your previous evaluation run:
- `saved_models/gb_custom.pkl`

## Features
- Retro black-and-white UI theme
- Landing page and basic login flow (no authentication)
- Input validation + clamping for robust behavior
- Automatic `depth_mag_ratio` computation for consistent feature engineering
- Prediction outputs:
  - Predicted alert class (`green/yellow/orange/red`)
  - Impact score (0-100)
  - Risk level (`Low/Moderate/High/Severe`)
  - Class probability breakdown
- Predicted target class shown with its color badge
- Result panel shake intensity increases with risk level
- Built-in edge-case tests

## Run Locally (Flask)
From workspace root:

```powershell
python UI/app.py
```

Open:
- http://127.0.0.1:5000 (landing page)

Flow:
- Landing page: `/`
- Login page: `/login`
- Predictor app: `/app`

## Run Week 7 Edge-Case Tests

```powershell
python UI/app.py --run-tests
```

Or use endpoint:
- http://127.0.0.1:5000/tests

## Deploy on Vercel (Serverless Backend)

This repository now includes:
- Serverless Python endpoints in `UI/api/`
- Static frontend pages in `UI/public/`
- Vercel routing config in `vercel.json`
- Python dependencies in `requirements.txt`

### Serverless Endpoints
- `/api/health`
- `/api/predict` (POST JSON)
- `/api/tests`

### Deploy Steps
1. Push all changes to GitHub.
2. In Vercel, import the GitHub repository.
3. Keep project root as repository root (do not set it to `UI`).
4. Deploy.

After deploy, app pages are:
- `/`
- `/login`
- `/predictor`
