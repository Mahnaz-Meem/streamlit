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
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)
