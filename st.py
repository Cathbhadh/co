import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data preprocessing
data = """Unique users: 44916
Total posts: 1838500
Total likes: 27603984
NSFW posts: 1115367 (60.67%)
NSFW likes: 10943083 (39.64%)
Average likes per post: 15.01
Date with most posts: 2024-01-14
Average posts per day: 7924.57
Likes by percentile: [3, 10, 58]

Top 10 users by number of posts:
profile_name                             user_uuid                                post_count
Yevhen S.                                8a33a752-0d4d-4304-9baa-e954db49a159          30084
Rukia Best Girl                          5e32cee2-9697-4af7-9fc6-8d7221ba37b9          16041
Zero zero                                1fadcdf9-b0b5-4c53-b272-adc5ad50a61d          13490
Dario                                    13f28181-c510-4b59-8252-250447cdba81           9132
Catspaws                                 737af57f-a026-4725-a1f3-fd9577491f8a           8407
AManApart                                473fa9e5-35ac-4112-9156-b49ee8224276           7227
Alan Smithee                             d4be5799-1c43-4420-a3b2-2697eb99429f           6638
Teemuu                                   b9aae266-d509-42e5-be2b-d09195a35756           6197
AI MVP                                   07168cd3-f5ae-4b81-8171-dbb411b715e0           6037
b4ai                                     492c6710-84f8-4d25-8173-4637745bbb40           5548

Posts by day:
date         total_posts  nsfw_posts   nsfw_percentage
2023-08-09   3426         1934         56.450671
... (data omitted for brevity) ...
2024-03-27   5633         3246         57.624712

Posts by hour:
Hour  Post Count
0     87555
1     90077
2     83852
3     78812
4     77059
5     72662
6     71416
7     67774
8     65058
9     59996
10    63106
11    66863
12    68479
13    73217
14    79746
15    83824
16    85581
17    84407
18    82931
19    83693
20    82518
21    79105
22    76382
23    74387"""

# Split the data into sections
sections = data.split('\n\n')

# Parse the summary statistics
summary_stats = sections[0].split('\n')
unique_users = int(summary_stats[0].split(': ')[1])
total_posts = int(summary_stats[1].split(': ')[1])
total_likes = int(summary_stats[2].split(': ')[1])
nsfw_posts = int(summary_stats[3].split(' ')[0])
nsfw_likes = int(summary_stats[4].split(' ')[0])
avg_likes_per_post = float(summary_stats[5].split(': ')[1])
date_most_posts = summary_stats[6].split(': ')[1]
avg_posts_per_day = float(summary_stats[7].split(': ')[1])
likes_percentiles = eval(summary_stats[8].split(': ')[1])

# Parse the top users data
top_users_data = sections[1].split('\n')[2:]
top_users = pd.DataFrame([row.split() for row in top_users_data], columns=['profile_name', 'user_uuid', 'post_count'])
top_users['post_count'] = top_users['post_count'].astype(int)

# Parse the posts by day data
posts_by_day_data = sections[2].split('\n')[1:]
posts_by_day = pd.DataFrame([row.split() for row in posts_by_day_data], columns=['date', 'total_posts', 'nsfw_posts', 'nsfw_percentage'])
posts_by_day['total_posts'] = posts_by_day['total_posts'].astype(int)
posts_by_day['nsfw_posts'] = posts_by_day['nsfw_posts'].astype(int)
posts_by_day['nsfw_percentage'] = posts_by_day['nsfw_percentage'].astype(float)

# Parse the posts by hour data
posts_by_hour_data = sections[3].split('\n')[1:]
posts_by_hour = pd.DataFrame([row.split() for row in posts_by_hour_data], columns=['Hour', 'Post Count'])
posts_by_hour['Post Count'] = posts_by_hour['Post Count'].astype(int)

# Streamlit app
st.title('Data Visualization')

# Summary statistics
st.header('Summary Statistics')
st.write(f'Unique users: {unique_users}')
st.write(f'Total posts: {total_posts}')
st.write(f'Total likes: {total_likes}')
st.write(f'NSFW posts: {nsfw_posts} ({(nsfw_posts / total_posts) * 100:.2f}%)')
st.write(f'NSFW likes: {nsfw_likes} ({(nsfw_likes / total_likes) * 100:.2f}%)')
st.write(f'Average likes per post: {avg_likes_per_post}')
st.write(f'Date with most posts: {date_most_posts}')
st.write(f'Average posts per day: {avg_posts_per_day}')
st.write(f'Likes by percentile: {likes_percentiles}')

# Top users
st.header('Top Users by Number of Posts')
st.write(top_users)

# Posts by day
st.header('Posts by Day')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='date', y='total_posts', data=posts_by_day, ax=ax, label='Total Posts')
sns.lineplot(x='date', y='nsfw_posts', data=posts_by_day, ax=ax, label='NSFW Posts')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Posts')
ax.set_title('Posts by Day')
st.pyplot(fig)

# Posts by hour
st.header('Posts by Hour')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='Hour', y='Post Count', data=posts_by_hour, ax=ax)
ax.set_xlabel('Hour')
ax.set_ylabel('Number of Posts')
ax.set_title('Posts by Hour')
st.pyplot(fig)
