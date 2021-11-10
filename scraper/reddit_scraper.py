#!/bin/python3
import praw
from praw.models import MoreComments

class Scraper:
    def __init__(self, creds: dict):
        self.__creds = creds

    def connect(self):
        self.__reddit = praw.Reddit(client_id=self.__creds['client_id'],
                             client_secret=self.__creds['client_secret'],
                             user_agent=self.__creds['user_agent'])

    def get_comments(self, submission_id, replace_limit=0) -> list:
        '''
        Retrieves comments for specified post, returns them flat. Allows limiting number of comments retrieved for the sake of saving time

        '''
        self.__submission = self.__reddit.submission(id=submission_id)
        self.__submission.comments.replace_more(limit=replace_limit)
        return self.__submission.comments.list()
