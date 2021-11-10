#!/bin/python3
from scraper.reddit_scraper import Scraper
import datetime
import time
import json
import sys
import re

start = time.time()
cred_file = "creds.json"
submission_id = ["q095nt" if len(sys.argv) < 2 else sys.argv[1]][0]

# Load credentials
print("Loading credentials from file...")
with open(cred_file) as f:
    creds = json.load(f)

# Create a scraper object and connect to reddit
print("Connecting to Reddit...")
scraper = Scraper(creds)
scraper.connect()

# retrieve the comments
print("Querying comments for submission", submission_id)
comments = {'comments': scraper.get_comments(submission_id, replace_limit=None),
            'time': datetime.datetime.utcnow(),
            'submission_id': submission_id}

# Save the data as a json
print("Formatting data to dictionary...")
i=0
length = len(comments['comments'])

comment_json = {}
for comment in [w for w in comments['comments'] if w.author is not None]:
    print("comment", i, "of", length, "(%.2f%%)"%(i/length*100))
    comment_json[comment.id] = {"author": comment.author.id,
                             "body": comment.body,
                             "score": comment.score,
                             "time": comment.created_utc}
    i += 1

# Generate filename in the format id_datetime.json
print("Writing to file...")
filename =  "./data/" + \
            comments['submission_id'] + "_" + \
            re.sub('[-:. ]', '', str(comments['time'])) + \
            ".json"

f = open(filename, 'w')
f.write(json.dumps(comment_json))
f.close()

print("Success(?)")
