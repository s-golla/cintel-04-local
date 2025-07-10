# Interactive data visualization app

## Overview

This project is an interactive data visualization app for the Palmer Penguins dataset, built with [Shiny for Python](https://shiny.posit.co/py/). It allows users to explore penguin data with dynamic filters and interactive charts.

## Features

- **Filter penguins** by species and island using sidebar controls
- **Interactive histograms** (Plotly and Seaborn) for bill length, bill depth, flipper length, and body mass
- **Scatterplot** of flipper length vs. body mass, colored by species and sex
- **Data table and data grid** views of the filtered dataset
- Built with Shiny for Python, Plotly, Seaborn, and PalmerPenguins

## Requirements

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Running the App

To start the app, run:

```sh
shiny run --reload app.py
```

Then open the provided local URL in your browser.

## Project Structure

- `app.py` - Main Shiny app with UI and server logic
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## References

- [Shiny for Python Documentation](https://shiny.posit.co/py/)
- [Palmer Penguins Dataset](https://allisonhorst.github.io/palmerpenguins/)

---
*Created for interactive data science demos.*