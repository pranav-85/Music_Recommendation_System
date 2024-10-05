# Music Recommendation App

A simple music recommendation app that suggests similar songs based on user selection using **content-based filtering**. This approach uses the song lyrics and artist names to recommend songs that are similar in content.

## Features

- Select a song from a list of over 10,000 songs.
- Get recommendations for similar songs based on their tags (lyrics and artist).
- Visualize data or extend functionality with interactive capabilities via Streamlit.

## How It Works

The app uses **content-based filtering** to make song recommendations:

1. **Content-Based Filtering**: Each song is represented by a set of features, which include the song lyrics and artist name. These features are combined to form "tags" for each song.
2. A **Bag of Words** model is used to vectorize these tags.
3. **Cosine similarity** is then computed to find songs that have similar tags.
4. The top 5 most similar songs are recommended to the user.

## Prerequisites

- Python 3.x
- The following Python packages:
  - `streamlit`
  - `pandas`
  - `scikit-learn`

You can install these packages using the following command:

```bash
pip install streamlit pandas scikit-learn

```

## Installation

'''bash
git clone https://github.com/pranav-85/Music_Recommendation_System.git
cd Music_Recommendation_System
streamlit run app.py
```


