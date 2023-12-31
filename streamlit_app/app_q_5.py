import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

st.title("Exploring the Finest: 3 Top Grape Varieties and Their 5 Best Wines")


df = pd.read_csv("/Users/andre/Documents/GitHub/Vivino_market_analysis/data/csv_streamlit/grape_wine.csv")


unique_grapes = df.grape.unique()
unique_wines = df.wines_names.unique()

json_df = df.to_json(orient="values")
dict_converted = json.loads(json_df)

nodes = []
edges = []
grapes = []
wines = []

for data in dict_converted:
    type_grape = data[4]
    wines_names = data[1]
    rank = data[2]
    
    if wines_names not in wines:
        nodes.append(Node(id=wines_names, label=str(rank), shape='CURVE_SMOOTH', color='#FDD00F'))
        wines.append(wines_names)
    
    if type_grape not in grapes:
        nodes.append(Node(id=type_grape, label=type_grape, shape='CURVE_SMOOTH', color='#07A7A6'))
        grapes.append(type_grape)
    
    edges.append(Edge(source=wines_names, target=type_grape))


config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6",
                collapsible=True,
                node={'labelProperty':'label'}
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)



data = df.sort_values(by=['grape', 'rank'])
def plot_bar_chart(data):
    plt.figure(figsize=(10, 6)) 
    
    for grape, group in data.groupby('grape'):
        plt.bar(group['rank'], group['wines_names'], label=grape, alpha=0.7)

    plt.xlabel('Rank')
    plt.ylabel('Wine Names')
    plt.title('Wine Rankings by Grape')
    plt.xticks(data['rank'])
    plt.legend()
    plt.tight_layout()

    return plt

st.title('Wine Rankings Visualization')
st.pyplot(plot_bar_chart(data))