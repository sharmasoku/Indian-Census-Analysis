import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

# Loading the dataSet
df = pd.read_csv(r"C:\Users\sharm\Downloads\indian_census_2011.csv")
states= list(df['State'].unique())
states.insert(0,"All States")


# Streamlit

st.sidebar.title(':red[Indian] Census :red[Analysis]')
selected_states = st.sidebar.selectbox(' States', states)
primary_selected = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary_selected = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

# button⚠
plot = st.sidebar.button(':green[Plot]')

# Main

if plot:
    st.header(f':blue[Indian Census 2011:] {primary_selected} vs {secondary_selected}')

    if selected_states == "All States":
        st.caption(':red[NOTE]')
        st.caption(":orange[Sizes Indicates] " + str(primary_selected))
        st.caption(":orange[Colors Indicates] " + str(secondary_selected))
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary_selected, color=secondary_selected,color_continuous_scale=px.colors.cyclical.IceFire, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.caption(':red[NOTE]')
        st.caption(":orange[Sizes Indicates] " + str(primary_selected))
        st.caption(":orange[Colors Indicates] " + str(secondary_selected))
        state_df = df[df['State']==selected_states]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary_selected, color=secondary_selected,color_continuous_scale=px.colors.cyclical.IceFire, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)