import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import plotly.express as px

# Load the dataset
data = pd.read_csv("final_job_list.csv")

# Sidebar filters
st.sidebar.title("Job Market Dashboard")
selected_location = st.sidebar.selectbox("Select Location", ["All"] + list(data['Location'].unique()))
selected_job_type = st.sidebar.selectbox("Select Job Type", ["All"] + list(data['Type of Positions'].unique()))
search_title = st.sidebar.text_input("Search Job Titles")

# Filter data based on selections
filtered_data = data.copy()
if selected_location != "All":
    filtered_data = filtered_data[filtered_data['Location'] == selected_location]
if selected_job_type != "All":
    filtered_data = filtered_data[filtered_data['Type of Positions'] == selected_job_type]
if search_title:
    filtered_data = filtered_data[filtered_data['Title'].str.contains(search_title, case=False)]

# Display key metrics
st.title("Job Market Analysis")
st.write(f"Total Jobs: {len(filtered_data)}")
st.write(f"Unique Titles: {filtered_data['Title'].nunique()}")
st.write(f"Average Salary: ${filtered_data['Salary'].mean():,.2f}")

# Top 10 Job Titles
st.subheader("Top 10 Job Titles")
top_jobs = filtered_data['Title'].value_counts().nlargest(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_jobs.index, y=top_jobs.values, ax=ax)
ax.set_title("Top 10 Most Common Job Titles")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Word Cloud for Most Common Skills
st.subheader("Most Common Skills")
all_skills = ' '.join(filtered_data['Identified_Skills'].dropna())
wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(all_skills)

fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Average Salary by Location
st.subheader("Average Salary by Location")
avg_salary_by_location = filtered_data.groupby('Location')['Salary'].mean().nlargest(10)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_salary_by_location.index, y=avg_salary_by_location.values, ax=ax)
ax.set_title("Top 10 Highest Paying Locations")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Skills Clustering
st.subheader("Skills Clustering")
vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
X = vectorizer.fit_transform(filtered_data['Identified_Skills'].dropna())
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)

# Add the cluster labels back to the data
filtered_data['Cluster'] = clusters
fig = px.scatter(filtered_data, x="Salary", y="Location", color="Cluster", hover_data=["Title", "Identified_Skills"], title="Job Clusters Based on Skills")
st.plotly_chart(fig)

st.write("Data Source: final_job_list.csv")