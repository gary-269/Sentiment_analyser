import csv

with open('/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/Analysed Data/analysis_day1.csv', 'r') as csvinput:
    with open('/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/LocationInfo/loc1.csv', 'w') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput, lineterminator='\n')


        all = []
        row = next(reader)
        row.append('Polarity')
        all.append(row)

        for row in reader:
            row.append(row[1])
            all.append(row)

        writer.writerows(all)