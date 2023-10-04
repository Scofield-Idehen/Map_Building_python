import folium
import pandas


data =pandas.read_csv('Volcanoes.txt')
lat =list(data["LAT"])
lon =list(data["LON"])
ele = list(data["ELEV"])

def colour_marker(elevation):
    if elevation < 1000:
        return 'red'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'green'


map = folium.Map(location=[38.58, -99.08], zoom_start=6, tiles='OpenStreetMap')

f = folium.FeatureGroup(name="Volcanos")
for lt, ln, el in zip(lat, lon, ele):
    #this line adds a marker that enables he user to pinpoint the values
    #f.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=colour_marker(el))))
    f.add_child(folium.CircleMarker(location=[lt, ln], popup=el, radius=6, fill_color=colour_marker(el), color='grey', fill_opacity=0.7))

fg = folium.FeatureGroup(name="Population")

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'yellow'
if x['properties']['POP2005'] <10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'

}))

map.add_child(f)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")