import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
from shiny.express import ui, input, render
import plotly.express as px
from shiny import reactive
from shiny.render import plot as render_plot
from shinywidgets import render_plotly

# --- 1. Data Loading ---
penguins = load_penguins()

# --- 2. User Interface (UI) Definition ---
ui.page_opts(title="Interactive Penguin Data Visualizations", fillable=True)

with ui.sidebar(open="open"):
    ui.h2("Sidebar Filters")
    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
        inline=True,
    )
    # New: Add an island filter
    ui.input_checkbox_group(
        "selected_island_list",
        "Select Island",
        choices=["Torgersen", "Biscoe", "Dream"],
        selected=["Torgersen", "Biscoe", "Dream"],
        inline=True,
    )
    ui.hr()
    ui.h3("Histogram Options")
    ui.input_selectize(
        "selected_attribute",
        "Select Attribute for Histograms",
        choices=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
        selected="flipper_length_mm"
    )
    ui.input_numeric("plotly_bin_count", "Plotly Histogram Bins", 20)
    ui.input_slider("seaborn_bin_count", "Seaborn Histogram Bins", 0, 100, 20)

    ui.hr()
    ui.a("GitHub Repository", href="https://github.com/s-golla/cintel-03-reactive", target="_blank")

# --- 3. Server Logic and Output Definitions ---

# --- Data Tables and Grids ---
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Penguin Data Table (Filtered)")

        @render.data_frame
        def penguin_data_table():
            return render.DataTable(filtered_data())

    with ui.card(full_screen=True):
        ui.card_header("Penguin Data Grid (Filtered)")

        @render.data_frame
        def penguin_data_grid():
            return render.DataGrid(filtered_data())

# --- Histograms and Scatterplot ---
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Histogram (Combined and Filtered by Species)") # Updated title

        @render_plotly
        def plotly_histogram():
            selected_attribute = input.selected_attribute()
            return px.histogram(
                filtered_data(), # Data is already filtered by selected_species_list and island
                x=selected_attribute,
                nbins=input.plotly_bin_count(),
                title=f"Distribution of {selected_attribute} (Combined and Filtered)", # Updated title
                color="species", # Keep color to differentiate species within the combined histogram
                barmode="overlay", # Overlay bars for different species
                opacity=0.7 # Add some opacity to see overlapping bars
            )

    with ui.card(full_screen=True):
        ui.card_header("Seaborn Histogram (Filtered by Species and Island)") # Updated title

        @render_plot
        def seaborn_histogram():
            selected_attribute = input.selected_attribute()
            plt.figure(figsize=(8, 6))
            sns.histplot(
                data=filtered_data(),
                x=selected_attribute,
                bins=input.seaborn_bin_count(),
                kde=True,
                hue="species",
                multiple="stack",
            )
            plt.title(f"Distribution of {selected_attribute} (Filtered)")
            plt.xlabel(selected_attribute)
            plt.ylabel("Count")
            plt.legend(title="Species")
            plt.tight_layout()


    with ui.card(full_screen=True):
        ui.card_header("Plotly Scatterplot: Flipper Length vs Body Mass (Filtered by Species and Island)") # Updated title

        @render_plotly
        def plotly_scatterplot():
            return px.scatter(
                filtered_data(),
                x="flipper_length_mm",
                y="body_mass_g",
                color="species",
                symbol="sex",
                title="Penguin Flipper Length vs Body Mass by Species and Sex (Filtered)",
                labels={
                    "flipper_length_mm": "Flipper Length (mm)",
                    "body_mass_g": "Body Mass (g)",
                },
                hover_data=["island", "bill_length_mm", "bill_depth_mm"],
            )

# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Modified reactive calculation to filter the data by species AND island
@reactive.calc
def filtered_data():
    df = penguins.copy()

    # Filter by species
    if input.selected_species_list():
        df = df[df["species"].isin(input.selected_species_list())]
    else:
        return penguins.head(0) # Return empty if no species are selected

    # Filter by island
    if input.selected_island_list():
        df = df[df["island"].isin(input.selected_island_list())]
    else:
        # If no islands are selected, should we show nothing or all species for selected islands?
        # For this example, we'll return an empty DataFrame if no islands are selected.
        return penguins.head(0) # Return empty if no islands are selected


    return df
