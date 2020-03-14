import csv
from textblob import TextBlob


def analysis_to_csv():
    infile = 'Dataset/Day6.csv'

    csvFile1 = open('Analysed Data/analysis_day6.csv', 'a')
    csvWriter = csv.writer(csvFile1)
    csvWriter.writerow(["Sentence", "Polarity", "Subjectivity"])
    csvfile = open(infile, 'r')
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[1]
        blob = TextBlob(sentence)
        # print(sentence)
        pol = blob.sentiment.polarity
        sub = blob.sentiment.subjectivity
        # print(pol,sub)
        csvWriter.writerow([sentence, pol, sub])
    csvFile1.close()


if __name__ == '__main__':
    analysis_to_csv()
