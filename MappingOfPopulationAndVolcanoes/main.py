import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
# print(data.columns)
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
names = data["NAME"]

map = folium.Map(location=[38.0,-99],zoom_start=6, titles="mapBox")

def color_generation(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation < 3000:
        return "orange"
    else:
        return "red"

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
# https://www.google.com/search?q=%22Valles%20Caldera%22
# https://www.google.com/search?q=%22Dotsero%22

# map.add_child(folium.Marker(location=[38.0,-99],
#                 popup="Hi, I am a maker",
#                 icon = folium.Icon(color="green")))
fgv = folium.FeatureGroup(name="Volcano")


for lt,lo,el,name in zip(lat,lon,elev,names):
    # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # print(name)
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker([lt,lo],radius=6,popup=folium.Popup(iframe),
                    fill_color=color_generation(el),fill=True ,color = "grey",fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding = 'UTF-8-sig').read(),
style_function = lambda x :{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
