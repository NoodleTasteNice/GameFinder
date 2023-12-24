import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv

#getting all game urls
games_url = []
#use 2000 games
for i in range(3):
    url = 'https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2023&page=' + str(i)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('a', class_='c-finderProductCard_container')
    for tag in tags:
        url = 'https://www.metacritic.com' + tag['href']
        print(url)
        games_url.append(url)

#getting the user score, meta score, genre, platform
game_data = []
for game_url in games_url:
    response = requests.get(game_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    #getting official game name
    name_div = soup.find('div', class_= 'c-productHero_title').find('div')
    title = name_div.text.strip()
    print(title)
    #getting user review scores
    user_score_div = soup.find('div', class_= 'c-siteReviewScore_user')
    user_score = user_score_div.find('span').text
    #getting meta scores
    meta_score_div = soup.find('div', class_= 'c-siteReviewScore')
    #divide by 10 to make it consistent with user scores
    meta_score = int(meta_score_div.find('span').text)/10
    #getting genre type
    genre_div = soup.find('a', class_='c-globalButton_container')
    genre = genre_div.find('span').text.strip()
    #get age rating
    age_div = soup.find('div', class_='c-productionDetailsGame_esrb_title')
    age = age_div.find('span').text.strip()
    
    #store information in a list
    game_data.append({'Title': title, 'User Score': user_score, 'Meta Score': meta_score, 'Genre': genre, 'Age Rating': age})

csv_file = 'game.csv'
with open(csv_file, mode='w', newline = '', encoding = 'utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'User Score', 'Meta Score', 'Genre', 'Age Rating'])
    writer.writeheader()
    for game in game_data:
        writer.writerow(game)

print('done')

