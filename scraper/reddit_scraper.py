#!/bin/python3
import praw
from praw.models import MoreComments

class Scraper:
    def __init__(self, creds: dict, submission_id: str):
        self.__submission_id = submission_id
        self.__creds = creds

    def connect(self):
        self.__reddit = praw.Reddit(client_id=self.__creds['client_id'],
                             client_secret=self.__creds['client_secret'],
                             user_agent=self.__creds['user_agent'])

    def get_comments(self) -> list:
        self.__submission = self.__reddit.submission(id=self.__submission_id)
        self.__submission.comments.replace_more(limit=None)
        return [c.body for c in self.__submission.comments.list()]
