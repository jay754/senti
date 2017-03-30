import json
from textblob import TextBlob
import pandas as pd

def load_json(name):
    with open(name) as json_data: d = json.load(json_data)
    return d

def mean(data):
    return float((sum(data))/(len(data)))

def main():
    scores = []
    results = [str(i) for i in load_json("results.json")]
    for tweet in results:
        testimonial = TextBlob(tweet)
        scores.append(testimonial.sentiment.polarity)

    print "The average of the sentiment of all tweets was " + str(mean(scores))

    data = pd.read_csv("HistoricalQuotes.csv")
    data.head()
    difference = data.open[1]-data.open[11]

    if difference > 0:
        print "Stock price of Apple rose " + str(difference)
    else:
        print "Stock price of Apple fell " + str(difference)

main()
