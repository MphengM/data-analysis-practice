'''My first attempt at using data to create a table'''

import streamlit as st
import pandas as pd
import glob
import plotly.express as px
import json


st.title("NO2 levels Dashboard")
st.write("Analysis of Nitrogen Dioxide levels in German states (2015 - 2026)")

# Load annual data

df_long_verkehr = pd.read_csv('no2_annual_traffic.csv')


# Get unique regions and sort alphabetically
gemeinde = sorted(df_long_verkehr['Gemeinde'].unique())

# Time series selector
selected_region = st.selectbox(
    "Select a region:",
    options=gemeinde,
    index=0
)
# Time series plot  

df_verkehr_filtered = df_long_verkehr[df_long_verkehr['Gemeinde'] == selected_region]


fig = px.line(df_verkehr_filtered, x='Jahr', y='NO2', color='Stationsname',
             title=f'NO2 levels in {selected_region} (2015 - 2025)',
             labels={'Jahr':'Year', 'NO2':'NO2 (µg/m³)', 'Stationsname':'Station Name'})

#fig.show() 

with st.container():
    st.subheader("NO2 Trends Over Time")
    st.plotly_chart(fig, width='content')

# Load monthly data

df_monthly = pd.read_csv('no2_monthly_data.csv')

#Convert Datum to datetime
df_monthly['Datum'] = pd.to_datetime(df_monthly['Datum'], dayfirst=True)

#Create the Month Column
df_monthly['Monat'] = df_monthly['Datum'].dt.month

#Convert Messwert to numeric and it back to the column
df_monthly['Messwert'] = pd.to_numeric(df_monthly['Messwert'], errors='coerce')

#Create 'Year' column for the animated choropleth
df_monthly['Jahr'] = df_monthly['Datum'].dt.year

df_monthly_verkehr = df_monthly.loc[df_monthly['Art der Station'] == 'Verkehr']
df_monthly_verkehr = df_monthly_verkehr.dropna(subset=['Messwert'])

# Get unique regions and sort alphabetically
bundesland = sorted(df_monthly_verkehr['Bundesland / Messnetz'].unique())

# Dropdown selector - first region by default
selected_messnetz = st.selectbox(
    "Select a region:",
    options=bundesland,
    index=0
)

df_monthly_verkehr_filtered = df_monthly_verkehr[df_monthly_verkehr['Bundesland / Messnetz'] == selected_messnetz]

# Box plot

fig2 = px.box(df_monthly_verkehr_filtered,
             x='Monat',
             y='Messwert',
             title=f'NO2 Seasonal Variation in {selected_messnetz}(Traffic Sensors)',
             labels={'Monat':'Month', 'Messwert':'NO2 (µg/m³)'})

#fig2.show()

with st.container():
    st.subheader("Seasonal Variation")
    st.plotly_chart(fig2, width='content')

#Load GeoJSON
with open('4_niedrig.geo.json') as f:
    geojson = json.load(f)

df_monthly_verkehr = df_monthly.loc[df_monthly['Art der Station'] == 'Verkehr']
df_choropleth_yearly = df_monthly_verkehr.groupby(['Bundesland / Messnetz', 'Jahr'])['Messwert'].mean().reset_index()

# Animated choropleth
fig4_animated = px.choropleth(df_choropleth_yearly,
                             geojson=geojson,
                             locations='Bundesland / Messnetz',
                             featureidkey='properties.name',
                             color='Messwert',
                             animation_frame='Jahr',
                             scope='europe',
                             title='Average NO2 Levels by German State (2016 - 2026)',
                             labels={'Messwert':'NO2 (µg/m³)', 'Jahr':'Year'},
                             color_continuous_scale='Reds',
                             range_color=[0, 50])

fig4_animated.update_geos(fitbounds='locations', visible=False)


with st.container():
    st.subheader("NO2 levels by German state (timelapse)")
    st.plotly_chart(fig4_animated, width='content')

