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
# #st.image('banner.png')
# placeholder = st.empty()
# st.title('Dashboard')
# st.write("")
# import streamlit as st

# col1, col2, col3,col4,col5,col6 = st.columns(6)
# col1.metric(":clock1: Mission Time", "17:25:31.26")
# col2.metric(":five: Packet Count", "106")
# col3.metric(":computer: Mode","Flight")
# col5.button('CAL')
# col6.button('ST')

# col1, col2, col3,col4,col5,col6 = st.columns(6)
# col1.metric(":thermometer: Temperature", "70 °C", "1.2 °C")
# col2.metric(":arrow_down: Pressure", "9 kPa", "-2 kPa")
# col3.metric(":arrow_up: Altitude","421 m","-20 m")
# col5.button('CX ON')
# col6.button('CX OFF')

# col1, col2, col3,col4,col5,col6 = st.columns(6)
# col1.metric("Tilt X", "1.9°", "1.2 °F")
# col2.metric("Tilt Y", "0.8°", "-8%")
# col3.metric(":bulb: Voltage","86 V","4 V")
# col5.button('Simulation Activate')
# col6.button('Simulation Enable')

# col1, col2, col3,col4,col5,col6 = st.columns(6)
# col1.metric(":satellite: Latitude", "19.022304°", "-0.000361°")
# col2.metric(":satellite: Longitude", "72.855946°", "0.000568°")
# col3.metric(":satellite: Satellites Detected","5","2")
# col5.button('Simulation Deactivate')

# col1,col2 = st.columns([2,1])
# with col2:
#     uploaded_file = st.file_uploader("Choose a csv file for simulation mode data")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
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

button_style = """
        <style>
        .stButton > button {
            color: white;
            background: '#0e1117';
            width: 180px;
            height: 50px;
            border: 2px solid #4CAF50;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)
st.sidebar.header("")
#st.image('banner.png')
placeholder = st.empty()

h1, h2 = st.columns([2,1])
with h1:
    st.title('Dashboard')
with h2:
    st.title('Commands')
st.write("")

col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric(":clock1: Mission Time", "17:25:31", "")
col2.metric(":1234: Packet Count", "106", "")
col3.metric(":computer: Mode","Flight", "")
col5.button('CAL')
col6.button('ST')
st.write("")


col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric(":thermometer: Temperature", "70 °C", "1.2 °C")
col2.metric(":arrow_down: Pressure", "9 kPa", "-2 kPa")
col3.metric(":arrow_up: Altitude","421 m","-20 m")
if col5.button('CX ON'):
    import time
    import serial

    ser = serial.Serial('COM5', 9600, timeout=1)
    ser.write(str.encode("Hello \n"))
    

if col6.button('CX OFF'):
    import time
    import serial
    ser = serial.Serial('COM5', 9600, timeout=1)
    ser.write(str.encode("Stopping \n"))
    

#Simulation Deactivate
#       CX OFF        
#       CX ON         
#        ST             
#        CAL
col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric("Tilt X", "1.9°", "1.2 °F")
col2.metric("Tilt Y", "0.8°", "-8%")
col3.metric(":bulb: Voltage","86 V","4 V")
col5.button(' Simulation Activate ')
col6.button('  Simulation Enable  ')

col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric(":satellite: Latitude", "19.022304°", "-0.000361°")
col2.metric(":satellite: Longitude", "72.855946°", "0.000568°")
col3.metric(":satellite: Satellites Detected","5","2")
col5.button('Simulation Deactivate')

st.write("")
st.write("")
uploaded_file = st.file_uploader("Choose a CSV File for Simulation Mode Data")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)