import json
from scraper.reddit_scraper import Scraper

cred_file = "creds.json"
submission_id = "qpp1nj"

def main():
    #get credentials from external file
    with open(cred_file) as f:
        creds = json.load(f)

    #Create a scraper object and connect to reddit
    scraper = Scraper(creds, submission_id)
    scraper.connect()

    #Get the comments to analyze
    comments = scraper.get_comments()

if __name__ == '__main__':
    main()
