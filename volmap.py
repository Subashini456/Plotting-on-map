import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_range(elevate):
    if elevate < 2000:
        return "green"
    elif  2000 <= elevate < 3000:
        return "orange"
    else:
        return "red"       


map = folium.Map(location = [39.67,-99.86] ,zoom_start = 5 , tiles = "Stamen Terrain")
fgv = folium.FeatureGroup(name="volcanoes")

for lt,ln,ele in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location = [lt,ln], popup=str(ele) + " m" ,icon=folium.Icon(color=color_range(ele))))

fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read() ,
style_function = lambda x : {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] <= 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("volmap1.html")