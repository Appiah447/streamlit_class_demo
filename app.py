import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit App Title
st.title("My Toy Streamlit App")

# Load the dataset
data = sns.load_dataset("penguins").dropna()  # Drop missing values for cleaner plots

# Sidebar for filtering options
st.sidebar.header('Filter Options')

# Category selection dropdown
species_options = ['All'] + list(data['species'].unique())  # Add "All" option
selected_category = st.sidebar.selectbox('Select Category', options=species_options)

# Filter the dataset based on selection
filtered_data = data if selected_category == 'All' else data[data['species'] == selected_category]

# 📌 Streamlit Scatter Chart
st.subheader("Streamlit Scatter Plot")
st.scatter_chart(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species')

# 📌 Add descriptive text
st.write("This interactive scatter chart allows you to filter penguin species and visualize their body mass against flipper length.")


# 📌 Seaborn Histogram 
st.subheader("Seaborn Histogram")
hist_col = st.selectbox("Select Column for Histogram", ["body_mass_g", "flipper_length_mm", "bill_length_mm"])
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.histplot(data=filtered_data, x=hist_col, color='blue', bins=20, kde=True, ax=ax1)
st.pyplot(fig1)


# 📌 Seaborn Scatter Plot
st.subheader("Seaborn Scatter Plot")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=filtered_data, x='flipper_length_mm', y='body_mass_g', hue='species', palette='viridis', s=100, ax=ax2)
st.pyplot(fig2)

# 📌 Bar Chart
st.subheader("Penguin Species Count - Bar Chart")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.countplot(data=filtered_data, x='species', palette='coolwarm', ax=ax3)
st.pyplot(fig3)


