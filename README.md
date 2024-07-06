# Python for Nonprofits (Version 2)

By Kenneth Burchfiel

Released under the MIT License

In this project, I will demonstrate how nonprofits can use Python to retrieve, analyze, visualize, and share their data. This project is still in its early stages, but I plan to add a number of sections to it as time allows.

*Note*: This project is *not* meant to replace an introductory Python course or textbook. If you're new to Python, I suggest getting started with a resource like [Think Python, 3rd Edition](https://greenteapress.com/wp/think-python-3rd-edition/). (I found the 2nd edition of this book to be very helpful in my own studies.) Once you've finished reading Think Python or have a similar introductory background in the language, you should be in a great position to benefit from this project.

# Contents

Note: many of these sections have not yet been completed or even started; in addition, other sections may be added in later on. I'm working on this project in my free time (which, as a new dad, is not very abundant!), so it may be a while before I begin or finalize a given section.

## Part 1: Introduction

### Why Use Python (complete)

This essay explains why you should consider using Python at your nonprofit organization.

## Part 2: Retrieval

### Data Retrieval (Mostly Complete)

This section provides a brief overview of importing data into Python scripts from multiple sources.

### Data Prep (mostly complete)

This section shows how to clean and reformat data so that it can be incorporated into various analyses.

### Retrieving Census Data (Mostly Complete)

This section shows how to use Python to retrieve data from the US Census API, a great source of public-domain demographic data.

## Part 3: Analyses

### Descriptive Stats (not yet started)

In this section, you'll learn how to use Python to calculate a range of descriptive statistics.

### Regression Analyses (not yet started)

This section will show how to create linear regressions within Python. 

## Part 4: Visualizations

### Graphing (Not yet started)

Plotly is a powerful tool for creating both interactive and static charts. This section will demonstrate how to create bar, line, and scatter plots along with treemaps (an alternative to pie charts).

### Mapping (Initial draft complete)

This section demonstrates how to use Folium to create interactive choropleth maps. I may expand this section in the future to include additional map types (such as maps of points and routes).

Here are examples of the choropleth maps created within this section:

[Net migration rates by county](https://sites.google.com/view/pfn2-choropleth-maps/net-migration-by-county)

[Net migration rates by state](https://sites.google.com/view/pfn2-choropleth-maps/net-migration-by-state?authuser=0)

And here are static copies of these maps:

<img src="https://raw.githubusercontent.com/kburchfiel/pfn_2/main/Mapping/map_screenshots/net_migration_rate_county_2020-2023.png" width="500"/>

<img src="https://raw.githubusercontent.com/kburchfiel/pfn_2/main/Mapping/map_screenshots/net_migration_rate_state_2020-2023.png" width="500"/>

## Part 5: Publication

### Updating Online Spreadsheets (Not yet started)

This section will demonstrate how to use Python to export data to a Google Sheets workbook, thus enabling others to view that data.

### Online Visualizations (Not yet started)

In this section, you'll learn how to use the Dash and Plotly libraries to create interactive online dashboards.

# Part 6: Appendix

### NVCU Database Generation

This section contains a Jupyter Notebook that I used to construct a SQLite database with **fictional** data for an imaginary university. The tables in this dataset will play a role in many parts of Python for Nonprofits.