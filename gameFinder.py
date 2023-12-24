import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('game.csv')

#fill nan values of 'None'
df.fillna('None', inplace=True)

#drop games with too little reviews
df = df.drop(df[df['User Score'] == 'tbd'].index)
df = df.drop(df[df['Meta Score'] == 'tbd'].index)
df = df.reset_index(drop=True)

#divide meta score by 10 to make it consistent with user scores
df['Meta Score'] = pd.to_numeric(df['Meta Score'])/10
df['User Score'] = pd.to_numeric(df['User Score'])

#calculate average score based on meta and user scores
df['Average Score'] = (df['User Score'] + df['Meta Score'])/2
df['Average Score'].round(1)
df['Average Score']

#one hot encode the genres and age ratings to transform to numerical values
one_hot = OneHotEncoder()
one_hot_df = one_hot.fit_transform(df[['Genre', 'Age Rating']]).toarray()
new_one_hot_df = pd.DataFrame(one_hot_df, columns=one_hot.get_feature_names_out(['Genre', 'Age Rating']))

#combine the two dataframes to form one that can be used for cosine similarity
new_df = pd.concat([df, new_one_hot_df], axis=1).drop(['Genre', 'Age Rating'], axis=1)

#compute cosine similarity
#drop the title column as it is not a feature
cosine_sim = cosine_similarity(new_df.drop('Title', axis=1))

#create function to recommend games
#elden ring is used as an example
game_title = "Elden Ring"
def main(game_title, cosine_sim=cosine_sim):
    #check if game exists in dataset
    if game_title not in df['Title'].values:
        print(f"{game_title} not found in dataset")
    else:
        #retrieve index of game in dataset
        index = df[df.Title == game_title].index[0]
        #get pairwise similarity scores then sort based on highest first
        sim_scores = list(enumerate(cosine_sim[index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        #get the top 10 similar games
        sim_scores = sim_scores[1:11]
        game_indices = [i[0] for i in sim_scores]
        print(df['Title'].iloc[game_indices])

main(game_title)