import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/Mahnaz-Meem/streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWlieTY0ZTh1cDJtdDJsY3hnNms1b2x5bGJjN3dtOTg0a3d2bHNjdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UOdoMz3baCENO/giphy.gif"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
        after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
        m.split_map(
            left_layer=before, right_layer=after
        )
        

m.to_streamlit(height=700)
