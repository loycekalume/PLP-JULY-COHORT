
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# App title
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Slider for year range
year_range = st.slider("Select Year Range", 2015, 2023, (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show summary
st.write(f"Showing {filtered.shape[0]} papers")

# Plot publications per year
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Show sample data
st.write(filtered.sample(10))
