import pandas as pd
from geopandas.tools import geocode
import geopy

data = pd.read_csv("/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/Dataset/Day4.csv")

for index, row in data.iterrows():
    try:
        # print(row['Location'])
        info = geocode(str(row['Location']), provider='Nominatim')
        data.loc[int(index), 'Address'] = info['address'].loc[0]
        data.loc[int(index), 'Longitude'] = info['geometry'].loc[0].x
        data.loc[int(index), 'Latitude'] = info['geometry'].loc[0].y
    except BaseException:
        pass
data = data.dropna()
# print(data)
data.to_csv("/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/LocationInfo/loc4.csv")
