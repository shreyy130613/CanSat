# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import time
# from PIL import Image

# st.set_page_config(
#     page_title="Real-Time Data Science Dashboard",
#     page_icon="✅",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )
# st.sidebar.header("")
# st.title("Hi")
# placeholder = st.empty()
# data = pd.read_csv("CanSAT_TM.csv")
# st.map(data,zoom=None, use_container_width=True)

# import streamlit as st
# import folium
# import pandas as pd

# df = pd.read_csv('CanSAT_TM.csv')

# m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=13)

# for lat, lon in zip(df['latitude'], df['longitude']):
#     folium.Marker(location=[lat, lon]).add_to(m)

# st.write(m,element='map')
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Aether Ground Station",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.sidebar.header("")
st.title('GPS Map')

placeholder = st.empty()
# Load data from CSV file
df = pd.read_csv('gps_data.csv')

# Create a scatter mapbox plot
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", mapbox_style="carto-positron",color_discrete_sequence=['rgba(0,0,255,0.7)'],zoom=2,height=900)

# Use Streamlit to display the plot
st.plotly_chart(fig,use_container_width=True)
