import streamlit as st
from utilities import load_css
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
)

st.header("Welcome! 👋")
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.')

load_css()

# Lottie
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_json = load_lottieurl(lottie_url)
with st.sidebar:
    st_lottie(lottie_json)
