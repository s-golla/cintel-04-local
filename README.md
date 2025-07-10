
# Interactive Penguin Data Visualization App


## Overview

This project is an interactive data visualization app for the Palmer Penguins dataset, built with [Shiny for Python](https://shiny.posit.co/py/). It enables users to explore penguin data using dynamic filters and interactive charts, all within a modern web interface. The app is designed for data science demos and educational purposes.


## Features

- **Filter penguins** by species and island using sidebar controls
- **Interactive histograms** (Plotly and Seaborn) for bill length, bill depth, flipper length, and body mass
- **Scatterplot** of flipper length vs. body mass, colored by species and sex
- **Data table and data grid** views of the filtered dataset
- **Modern web UI** powered by Shiny for Python and Shinylive
- Built with Shiny for Python, Plotly, Seaborn, and PalmerPenguins


## Requirements

Install dependencies with:

```sh
pip install -r requirements.txt
```


## Running the App

To start the app locally, run:

```sh
shiny run --reload app.py
```

Then open the provided local URL in your browser (usually http://localhost:8000).

### Running in the Browser (Shinylive)

You can also run the app directly in the browser using Shinylive. Open `docs/index.html` in your browser to launch the interactive app without a Python backend.


## Project Structure

- `penguins/app.py` - Main Shiny app with UI and server logic
- `requirements.txt` - Python dependencies
- `docs/` - Static site for Shinylive (browser-based) version
- `README.md` - Project documentation


## References

- [Shiny for Python Documentation](https://shiny.posit.co/py/)
- [Shinylive Documentation](https://shinylive.io/)
- [Palmer Penguins Dataset](https://allisonhorst.github.io/palmerpenguins/)


---
*Created for interactive data science demos and browser-based visualization.*