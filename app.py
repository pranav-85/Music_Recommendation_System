import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def recommend_music(music, data):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(max_features=2000, min_df=1000, max_df=200000)

    vector = vectorizer.fit_transform(data['tags']).toarray()

    from sklearn.metrics.pairwise import cosine_similarity

    sim = cosine_similarity(vector[:10000])
    index = data[data['song'] == music].index[0]
    distances=sim[index]
    music_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    rec_list = []
    for i in music_list:
        rec_list.append(data.iloc[i[0]].song)

    return rec_list


st.write("""
# Music Recommendation App

""")

data = pd.read_csv('spotify_millsongdata.csv')

data = data.drop(['link'], axis=1)
data['text'] = data['text'].str.replace('\s',' ')
data['text'] = data['text'].str.replace('\n',' ')
data['text'] = data['text'].str.replace('\r',' ')
data['text'] = data['text'].str.replace(',',' ')
data['text'] = data['text'].str.replace('.',' ')
data['artist'] = data['artist'].str.replace(' ', '')

data['tags'] = data['text'] + ' ' + data['artist']
data['tags'] = data['tags'].str.lower()


option = st.selectbox('Select a song', data['song'][:10000], index=None, placeholder="Select a song...")

if option != None:
    music = recommend_music(option,data)

    for song in music:
        st.write(song)
