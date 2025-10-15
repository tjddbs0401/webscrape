# Webscrape Intern — Root README

This is the **main README** for the overall `webscrape` project.

---

## Overview

A full-stack demo that scrapes [BooksToScrape](https://books.toscrape.com/) using **Python** and visualizes the collected data with a **React + Vite** frontend.

---

## Structure

```
webscrape/
├── scraper/    # Python backend scraper
├── ui/         # React + Vite frontend
└── README.md   # (This file)
```

---

## Quick Start

### 1. Run the Scraper (Backend) - Refer Scraper Readme

```bash
cd webscrape
python -m scraper.src.main --max-pages=2 --delay-ms=700
```
This saves `items.jsonl` and automatically syncs it to the frontend.

### 2. Run the Frontend (UI)

```bash
cd ui
npm run dev
```

Then open:

```
http://localhost:5173
```

---

## Typical Workflow

1. Run scraper from root folder
2. Run UI in `ui/`
3. Refresh browser to view updated data

---

## File Roles

| Folder     | Description                                       |
| ---------- | ------------------------------------------------- |
| `scraper/` | Python crawler that scrapes books and saves data  |
| `ui/`      | React dashboard that reads data and visualizes it |
