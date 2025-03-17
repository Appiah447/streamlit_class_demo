import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("My Toy Streamlit App")

# Load dataset
data = sns.load_dataset("penguins").dropna()

# Sidebar filtering options
st.sidebar.header('Filter Options')
species_options = ['All'] + list(data['species'].unique())
selected_category = st.sidebar.selectbox('Select Category', options=species_options)

# Filter dataset
filtered_data = data if selected_category == 'All' else data[data['species'] == selected_category]

# Streamlit Scatter Chart
st.subheader("Streamlit Scatter Plot")
st.scatter_chart(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species')

# Area Chart
st.subheader("Area Chart: Flipper Length vs. Body Mass")
st.area_chart(filtered_data[['flipper_length_mm', 'body_mass_g']])

# Multi-Dimensional Bar Chart
st.subheader("Multi-Dimensional Chart: Flipper Length, Body Mass, and Bill Length")

# Restructure data for proper visualization
multi_dim_data = filtered_data[['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']]
multi_dim_data = multi_dim_data.set_index('species')  # Ensure species is the index

# Debugging step: Check if data is properly formatted
st.write("Debugging: Multi-Dimensional Data Preview:", multi_dim_data.head())

# Plot multi-dimensional data
st.bar_chart(multi_dim_data)

# Seaborn Histogram
st.subheader("Seaborn Histogram")
hist_col = st.selectbox("Select Column for Histogram", ["body_mass_g", "flipper_length_mm", "bill_length_mm"])
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.histplot(data=filtered_data, x=hist_col, color='blue', bins=20, kde=True, ax=ax1)
st.pyplot(fig1)

# Seaborn Scatter Plot
st.subheader("Seaborn Scatter Plot")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=filtered_data, x='flipper_length_mm', y='body_mass_g', hue='species', palette='viridis', s=100, ax=ax2)
st.pyplot(fig2)

# Bar Chart
st.subheader("Penguin Species Count - Bar Chart")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.countplot(data=filtered_data, x='species', palette='coolwarm', ax=ax3)
st.pyplot(fig3)

