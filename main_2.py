import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from PIL import Image

st.set_page_config(
    page_title="Aether Ground Station",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.sidebar.header("")
#st.image('banner.png')

st.title('Real Time Telemetry Plotting')

placeholder = st.empty()
while True:

    with placeholder.container():
        data = pd.read_csv("CanSAT_TM.csv")

        # create two columns for charts
        fig_col1, fig_col2, fig_col3 = st.columns([1,1,1])
        with fig_col1:
            
            fig = px.line(data, x="Mission Time", y="Altitude",color_discrete_sequence=['orange'],title='Altitude Plot')
            #fig.update_traces(line=dict(color='firebrick'))
            st.plotly_chart(fig, use_container_width=True)
        with fig_col2:
            fig = px.line(data, x="Mission Time", y="Temperature",color_discrete_sequence=['white'],title='Temperature Plot')
            st.plotly_chart(fig, use_container_width=True)
        with fig_col3:
            fig = px.line(data, x="Mission Time", y="Pressure",color_discrete_sequence=['green'],title='Pressure Plot')
            st.plotly_chart(fig, use_container_width=True)

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            fig = px.line(data, x="Mission Time", y="Packet Count",color_discrete_sequence=['orange'],title='Packet Count Plot')
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.line(data, x="Mission Time", y="Voltage",color_discrete_sequence=['white'],title='Voltage Plot')
            st.plotly_chart(fig, use_container_width=True)
            
        with col3:
            fig = px.scatter(data, x="Longitude", y="Latitude",color_discrete_sequence=['green'],title='GPS Plot')
            st.plotly_chart(fig, use_container_width=True)