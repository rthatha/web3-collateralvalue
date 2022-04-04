from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import datetime

from PIL import Image


"""
# Welcome to Collateral Value Calculator!

MetaStreet is a DeFi (Decentralized Finance) interest rate protocol that provides liquidity to NFT (non-fungible token) collateral via tranched capital pools, abstracting risk and yield away from individual NFTs. 
MetaStreet seeks to utilize financial constructs to scale the GDP of the Metaverse and emerging NFT economies.

In this project, an automatic “collateral value” calculator is built, using cryptopunks dataset, according to the formulation below.

"""
image = Image.open('CV_Formula.png')

st.image(image, caption='')
"""
For more details, checkout [Metastreet](https://metastreet.notion.site/Senior-Data-Scientist-Engineer-bad2e7e9a8e340d3a23ff77faa56548d) and [Data Career Jumpstart](https://www.datacareerjumpstart.com/).

### Exploratory Data Analysis:

The raw data provided is shown below in a table
"""

df = pd.read_csv('cryptopunks_01-14-2022_13-55-22_downloaded.csv')

st.dataframe(df)  # Same as st.write(df)


@st.cache(persist=True)
def fetch_and_clean_data(url):
     # Fetch data from URL here, and then clean it up.    
    return data


#d1 = fetch_and_clean_data(DATA_URL_1)

"""
We can see that we have all the data we need to build our calculator. 
The transaction date and the value in ETH / USD is all we need.

Choose a date below and the CV value will be calculated and displayed in both ETH and USD

"""

d = st.date_input(
     "Collateral Value on",
     datetime.date(2019, 7, 6))
st.write('is:', d)

