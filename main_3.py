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
st.title("Telemetry Data CSV")
placeholder = st.empty()
while True:

    with placeholder.container():
        data = pd.read_csv("data - Copy.csv")
        st.dataframe(data,use_container_width=True,height=800)