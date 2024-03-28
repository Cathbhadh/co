import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data
unique_users = 44916
total_posts = 1838500
total_likes = 27603984
nsfw_posts = 1115367
nsfw_likes = 10943083
avg_likes_per_post = 15.01
date_most_posts = "2024-01-14"
avg_posts_per_day = 7924.57
likes_percentile = [3, 10, 58]

# Top 10 users data
top_users_data = {
    "profile_name": ["Yevhen S.", "Rukia Best Girl", "Zero zero", "Dario", "Catspaws", "AManApart", "Alan Smithee", "Teemuu", "AI MVP", "b4ai"],
    "user_uuid": ["8a33a752-0d4d-4304-9baa-e954db49a159", "5e32cee2-9697-4af7-9fc6-8d7221ba37b9", "1fadcdf9-b0b5-4c53-b272-adc5ad50a61d", "13f28181-c510-4b59-8252-250447cdba81", "737af57f-a026-4725-a1f3-fd9577491f8a", "473fa9e5-35ac-4112-9156-b49ee8224276", "d4be5799-1c43-4420-a3b2-2697eb99429f", "b9aae266-d509-42e5-be2b-d09195a35756", "07168cd3-f5ae-4b81-8171-dbb411b715e0", "492c6710-84f8-4d25-8173-4637745bbb40"],
    "post_count": [30084, 16041, 13490, 9132, 8407, 7227, 6638, 6197, 6037, 5548]
}
top_users_df = pd.DataFrame(top_users_data)

# Posts by day data
posts_by_day_data = {
    "date": ["2023-08-09", "2023-08-10", "2023-08-11"],  # Add more dates here
    "total_posts": [3426, 4600, 5349],  # Add more total posts here
    "nsfw_posts": [1934, 2743, 3199],  # Add more nsfw posts here
    "nsfw_percentage": [56.450671, 59.630435, 59.805571]  # Add more nsfw percentage here
}
posts_by_day_df = pd.DataFrame(posts_by_day_data)

# Posts by hour data
posts_by_hour_data = {
    "Hour": list(range(24)),
    "Post Count": [87555, 90077, 83852, 78812, 77059, 72662, 71416, 67774, 65058, 59996, 63106, 66863, 68479, 73217, 79746, 83824, 85581, 84407, 82931, 83693, 82518, 79105, 76382, 74387]
}
posts_by_hour_df = pd.DataFrame(posts_by_hour_data)

# Sidebar
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", ["Overview", "Top Users", "Posts by Day", "Posts by Hour"])

# Page content
st.title("YDStat")

if selected_page == "Overview":
    st.write(f"Unique Users: {unique_users}")
    st.write(f"Total Posts: {total_posts}")
    st.write(f"Total Likes: {total_likes}")
    st.write(f"NSFW Posts: {nsfw_posts} ({(nsfw_posts / total_posts) * 100:.2f}%)")
    st.write(f"NSFW Likes: {nsfw_likes} ({(nsfw_likes / total_likes) * 100:.2f}%)")
    st.write(f"Average Likes per Post: {avg_likes_per_post}")
    st.write(f"Date with Most Posts: {date_most_posts}")
    st.write(f"Average Posts per Day: {avg_posts_per_day}")
    st.write(f"Likes by Percentile: {likes_percentile}")

elif selected_page == "Top Users":
    st.subheader("Top 10 Users by Number of Posts")
    st.dataframe(top_users_df)

elif selected_page == "Posts by Day":
    st.subheader("Posts by Day")
    st.line_chart(posts_by_day_df.set_index("date")[["total_posts", "nsfw_posts"]])

elif selected_page == "Posts by Hour":
    st.subheader("Posts by Hour")
    st.bar_chart(posts_by_hour_df.set_index("Hour"))
