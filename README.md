# folio

Portfolio website. Minimal Flask app that renders a BabylonJS scene.

## Requirements

Python 3.15.0b3 (probably not required)
Flask 3.1.3

## Run

### With uv
```bash
uv sync
uv run python main.py
```

### Without uv 😡
```bash
python3 -m venv .venv

# linux
source .venv/bin/activate

# windows
.venv/Scripts/Activate.ps1

python3 -m pip install -r requirements.txt

python3 main.py
```