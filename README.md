# Sentiment Analyzer for Reddit
This project is inspired by the bipolar community that is [r/leafs](reddit.com/r/leafs). The goal of the project is to analyze the sentiment of comments left during the Game Day Threads (GDT) to get a grasp on the average opinions of leafs fans watching the game. 

## How It Works (Hopefully at some point)
- Comments from the GDT are retrieved via the Reddit API
	- Would like to do real-time analysis during the game, although I have to see what limitations I'm going to run into
- Comments will be processed using NLTK's VADER sentiment analysis tools [link](https://www.nltk.org/)
	- Going to start with this prebuild model. If I'm feeling ambitious I might try a custom model down the road
- Do some sort of analysis, make lots of pretty graphs with the findings
	- Honestly haven't thought this far. I'm sure I'll figure something out


## Resources (Because stealing is bad)
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
	Sentiment Analysis of Social Media Text. Eighth International Conference on
	Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014]

https://realpython.com/python-nltk-sentiment-analysis/
