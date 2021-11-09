import json
from random import shuffle
from scraper.reddit_scraper import Scraper
from nltk.sentiment import SentimentIntensityAnalyzer

cred_file = "creds.json"
submission_id = "qpp1nj"

def main():
    #get credentials from external file
    with open(cred_file) as f:
        creds = json.load(f)

    #Create a scraper object and connect to reddit
    scraper = Scraper(creds, submission_id)
    scraper.connect()

    #Get the top level comments to analyze
    comments = scraper.get_comments()

    #Analysis time!
    sia = SentimentIntensityAnalyzer()

    shuffle(comments)
    for c in comments[:10]:
        print(sia.polarity_scores(c)["compound"], ": ", c)

if __name__ == '__main__':
    main()
