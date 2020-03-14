import csv
from textblob import TextBlob

if __name__ == '__main__':

    infile = 'Analysed Data/analysis_day1.csv'
    csvfile = open(infile, 'r')
    rows = csv.reader(csvfile)
    for row in rows:
        sentences = row[0]
        analysis = TextBlob(sentences)
        pol = analysis.sentiment.polarity
        if pol > 0:
            print('positive')
        elif pol < 0:
            print('negative')
        else:
            print('neutral')

            # postweets = [sentence for sentence in sentences if pol > 0]
            # # print(postweets)
            # print("Positive tweets percentage: {} %".format(100 * len(postweets) / len(sentences)))
            # negtweets = [sentence for sentence in sentences if pol < 0]
            # # print(negtweets)
            # print("Negative tweets percentage: {} %".format(100 * len(negtweets) / len(sentences)))
            # neutraltweets = [sentence for sentence in sentences if pol == 0]
            # print("Neutral tweets percentage: {} %".format(100 * len(neutraltweets) / len(sentences)))



