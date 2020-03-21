from os import chdir
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt


def merge(indir="/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/Analysed Data",
          out_file="Merged.csv"):
    chdir(indir)
    file_list = glob("*.csv")
    df_list = []
    for filename in file_list:
        print(filename)
        df = pd.read_csv(filename)
        df_list.append(df)
    concatenated_df = pd.concat(df_list, axis=0)
    concatenated_df.to_csv(out_file, index=None)


def visualise():
    data = pd.read_csv(
        "/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/Analysed Data/Merged.csv",
        usecols=['Polarity'])
    # print(data)
    fig, ax = plt.subplots(figsize=(8, 6))
    data.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
              ax=ax,
              color="Maroon")

    plt.title("Sentiments from Tweets on CAA and NRC")
    plt.show()


if __name__ == '__main__':
    visualise()
