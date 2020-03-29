import folium
import pandas as pd

locdata = pd.read_csv("new.csv")

# print(locdata)

m = folium.Map(tiles='OpenStreetMap', zoom_start=10)

for index, row in locdata.iterrows():
    if row['Polarity'] > 0:
        icon = folium.Icon(color='green')
    elif row['Polarity'] < 0:
        icon = folium.Icon(color='red')
    else:
        icon = folium.Icon(color='blue')
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Location'], icon=icon).add_to(m)

m.save('/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/LocationInfo/loc.html')
