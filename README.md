# movies_recommender_system
# Movie Recommender System

A lightweight Streamlit app that recommends movies using a precomputed similarity matrix.

**Status**: Example/demo. Contains large precomputed pickles (`similarity.pkl`) and a demo TMDB API key in `app.py` — rotate any exposed keys before use.

**Contents**
- `app.py` — Streamlit app entrypoint.
- `movie_dict.pkl` — pickled movie metadata used by the app.
- `similarity.pkl` — precomputed similarity matrix (large file).
- `movie-recommender-system.ipynb` — exploratory notebook used during development.

**Prerequisites**
- Python 3.8+ recommended
- `streamlit`, `pandas`, `requests` (install with pip)

Quick install (macOS / Linux)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit pandas requests
```

Run the app

```bash
streamlit run app.py
```

Notes
- The app fetches poster images from TMDB. The API key is currently set inside `app.py`. Move the key into an environment variable for security, for example:

```bash
export TMDB_API_KEY="your_api_key_here"
# then modify app.py to read from os.environ
```

- `similarity.pkl` is large (>100MB). If you plan to keep it in the repository, enable Git LFS and track the file:

```bash
brew install git-lfs    # macOS
git lfs install
git lfs track "similarity.pkl"
git add .gitattributes
git commit -m "Track similarity.pkl with Git LFS"
```

- If sensitive values (API keys, passwords) were pushed, rotate/revoke them immediately — treat them as compromised.

Development tips
- If you accidentally committed sensitive files (for example `.env`), stop tracking them and optionally remove them from history. To stop tracking:

```bash
echo ".env" >> .gitignore
git rm --cached .env
git commit -m "Stop tracking .env"
git push origin main
```

- To remove a file from Git history (irreversible rewrite): use `git-filter-repo` or BFG. Back up branches before rewriting.

Contributing
- This repo is a personal/demo project. If you want to contribute, open an issue or a PR describing the change.

License
- MIT-style: feel free to reuse for learning or demos.
