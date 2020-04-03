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

legend = '''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 110px; height: 120px; 
                            border:4px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp; Tweets <br>
                              &nbsp; Positive &nbsp; <i class="fa fa-map-marker fa-2x" style="color:green"></i><br>
                              &nbsp; Negative &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i><br>
                              &nbsp; Neutral &nbsp; <i class="fa fa-map-marker fa-2x" style="color:blue"></i>

                </div>
                '''

m.get_root().html.add_child(folium.Element(legend))
m.save('/Users/karanveersingh/PycharmProjects/Sentiment_analyser/Sentiment_analyser/LocationInfo/loc.html')
