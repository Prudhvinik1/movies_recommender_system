# Movie Recommender System

A lightweight Streamlit app that recommends movies using a precomputed similarity matrix.

**Status**: Example/demo. Contains large precomputed pickles (`similarity.pkl`) and a demo TMDB API key that has been removed from `app.py` — rotate any exposed keys before use.

## Contents
- `app.py` — Streamlit app entrypoint.
- `movie_dict.pkl` — pickled movie metadata used by the app.
- `similarity.pkl` — precomputed similarity matrix (large file).
- `movie-recommender-system.ipynb` — exploratory notebook used during development.

## Prerequisites
- Python 3.8+ recommended
- `streamlit`, `pandas`, `requests` (install with pip)

### Quick install (macOS / Linux)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit pandas requests
```

### Run the app

```bash
streamlit run app.py
```

## Notes
- The app fetches poster images from TMDB. The API key used by `app.py` is read from the environment variable `TMDB_API_KEY`.

- `similarity.pkl` is large (>100MB). If you plan to keep it in the repository, enable Git LFS and track the file:

```bash
brew install git-lfs    # macOS
git lfs install
git lfs track "similarity.pkl"
git add .gitattributes
git commit -m "Track similarity.pkl with Git LFS"
```

- If sensitive values (API keys, passwords) were pushed, rotate/revoke them immediately — treat them as compromised.

## Development tips
- If you accidentally committed sensitive files (for example `.env`), stop tracking them and optionally remove them from history. To stop tracking:

```bash
echo ".env" >> .gitignore
git rm --cached .env
git commit -m "Stop tracking .env"
git push origin main
```

- To remove a file from Git history (irreversible rewrite): use `git-filter-repo` or BFG. Back up branches before rewriting.

## Environment (local)
- Create a local `.env` to hold your TMDB API key securely. This repository ignores `.env` by default.
- Copy `.env.example` to `.env` and fill in your key, or create `.env` with an `export` line so you can `source` it:

```bash
# example using export in .env
export TMDB_API_KEY="your_real_api_key_here"

# then load it into your shell
source .env

# run the app
streamlit run app.py
```

- Alternative: export the variable directly in your shell:

```bash
export TMDB_API_KEY="your_real_api_key_here"
streamlit run app.py
```

- If you prefer automatic .env loading inside Python, install `python-dotenv` and add `from dotenv import load_dotenv; load_dotenv()` to the top of `app.py`.

## Contributing
- This repo is a personal/demo project. If you want to contribute, open an issue or a PR describing the change.

## License
- MIT-style: feel free to reuse for learning or demos.

