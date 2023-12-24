
# Game Recommendation System

This Game Recommendation System project leverages user scores, Metacritic scores, genres, and age ratings to recommend video games. The system is built on Python and employs techniques such as cosine similarity and one-hot encoding for categorical data to find games with similar characteristics.

## How it Works

The recommendation system is a content-based filtering system. operates by first preprocessing the data such as one-hot encoding categorical data (genres and age ratings). It then calculates cosine similarity between games based on their features. Users can request game recommendations based on a specific title, and the system will suggest similar games.

## Getting Started

### Prerequisites

    1. Python 3.x
    2. libraries: Pandas, Scikit-learn

### Usage

To use the recommendation system, simply use your game title as the input for the main function.

Example:

main('Elden Ring')

## Data Sources

I wrote a python script to scrape information for [Metacritic's](https://www.metacritic.com/browse/game/) top ~1000 games of all time.

## Limitations and Considerations
    1. the quality of recommendations is highly dependent on the dataset used. The dataset used is currently quite limited with only around 925 games.
    2. Currently, the system does not account for user-specific preferences other than the game title.
    3. The system is designed for batch processing and does not support real-time recommendations

### Future Improvements
    1. Find a way to adapt the system for real-time recommendations.
    2. Use a larger dataset for more accurate results.
    3. Use more features to differentiate games, such as game descriptions, etc.
    4. Allow users to input preferences such as age ratings, games for specific platforms, etc.
    5. Incorporate both content-based and collaborative filtering to make the recommendation system more accurate.

