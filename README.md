# data-analysis-practice
I'm updating my data analysis skills. This repo will track my "rough work"


## What I'm learning
- Pandas 3.0
- Plotly visualisations
- Building a portfolio

Started: 26.01.2026


## Week 3: NO2 Visualisations

Using data from the Umweltbundeamt (01.2016 - 02.2026), I analysed the Nitrogen Dioxide(NO2) levels across German states, focusing mainly on Hamburg traffic sensors.

**Interactive Visualisations**
1. [Time Series: NO2 Trends in Hamburg](https://mphengm.github.io/data-analysis-practice/01_no2_timeseries_hamburg.html) - Shows declining NO2 levels over 10 years
2. [Seasonal Patterns: Box Plot](https://mphengm.github.io/data-analysis-practice/02_no2_seasonal_boxplot_hamburg.html) - Reveals higher pollution in spring months
3. [Distribution: NO2 Histogram](https://mphengm.github.io/data-analysis-practice/03_no2_distribution_histogram_hamburg.html) - Shows typical NO2 concentration ranges for Hamburg traffic sensors
4. [Geographic Overview: Choropleth Map](https://mphengm.github.io/data-analysis-practice/04_average_no2_by_bundesland.html) - NO2 levels by German state, averaged out over the 10-year time period
5. [Timelapse Geographic Overview: Choropleth Map Timelapse](https://mphengm.github.io/data-analysis-practice/05_average_no2_by_bundesland_animated.html) - NO2 levels by German state from 01.2016 to 02.2026
6. [Correlation: Population Density vs NO2](https://mphengm.github.io/data-analysis-practice/06_population_density_vs_no2_scatter_germany.html) - Shows the relationship between population density and NO2 levels

**Key findings**
- NO2 levels have been steadily declining over the last decade
- Traffic sensors in Hamburg show unexpected seasonal variation (higher in spring than in late winter)
- Population denisty seems to correlate with NO2 very weakly in the 3 city states: Bremen, Hamburg, and Berlin

**Technical Stack:** Python, pandas, Plotly, Umweltbundesamt Data


## Interactive NO2 Air Quality Dashboard

**Live Dashboard:** https://data-analysis-practice-no2-analysis.streamlit.app/

Interactive analysis of 10 years of NO2 air quality data across all German states using Streamlit

**Features:**
- Regional filtering to specific areas
- Seasonal pattern analysis showing variation across months
- Timelapse choropleth map of geographic distribution

**Key-findings:** January shows unexpectedly low NO2 levels despite being a winter month

**tech stack:** Streamlit, Plotly, pandas, German environmental data (Umweltbundesamt)

## Week 4: Coastal News Visualisations
Rebuilt my CSIR project using modern Python tools. Interactive visualisations of ocean- and coasts-related news coverage (2014 - 2016)

**Live Dashboard:** https://coastal-news-classifier.streamlit.app/ 
**Tech Stack:** Streamlit, Plotly, pandas
