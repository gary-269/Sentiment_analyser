import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/Analysed Data/Merged.csv")
# print(data)

pos_tweets = [tweet for index, tweet in enumerate(data['Sentence']) if data['Polarity'][index] > 0]
neu_tweets = [tweet for index, tweet in enumerate(data['Sentence']) if data['Polarity'][index] == 0]
neg_tweets = [tweet for index, tweet in enumerate(data['Sentence']) if data['Polarity'][index] < 0]

pos_perc = len(pos_tweets) * 100 / len(data['Sentence'])
neg_perc = len(neg_tweets) * 100 / len(data['Sentence'])
neutral_perc = len(neu_tweets) * 100 / len(data['Sentence'])


K = ["Positive", "Negative", "Neutral"]
L = [pos_perc, neg_perc, neutral_perc ]

d = pd.DataFrame(K, columns=["Type"])
d["Percentage"] = L


d.plot(kind='bar',x='Type', y='Percentage')
plt.show()
