from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

from PIL import Image


"""
# Welcome to Collateral Value Calculator!

MetaStreet is a DeFi (Decentralized Finance) interest rate protocol that provides liquidity to NFT (non-fungible token) collateral via tranched capital pools, abstracting risk and yield away from individual NFTs. 
MetaStreet seeks to utilize financial constructs to scale the GDP of the Metaverse and emerging NFT economies.

image = Image.open('CV_Formula.png')

st.image(image, caption='Collateral Value Formula')

Checkout [Metastreet](https://metastreet.notion.site/Senior-Data-Scientist-Engineer-bad2e7e9a8e340d3a23ff77faa56548d) and [Data Career Jumpstart](https://www.datacareerjumpstart.com/).
"""


df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
