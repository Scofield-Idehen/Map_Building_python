
# Volcano Elevation Map with Folium

This Python script generates an interactive map using the Folium library to display the locations of volcanoes with varying elevations. The color of each volcano marker on the map is determined by its elevation, making it easy to visualize the distribution of volcanoes at different elevations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Sample Data](#sample-data)
- [License](#license)

## Prerequisites

Before running the code, ensure you have the following prerequisites installed:

- Python 3.x
- Folium library
- pandas library

You can install the required libraries using `pip`:

```
pip install folium pandas
```
Installation

Clone this repository to your local machine:

`git clone https://github.com/yourusername/volcano-elevation-map.git`

Navigate to the project directory:


`cd volcano-elevation-map`

Place your volcano data in a CSV file named Volcanoes.txt with columns "LAT," "LON," and "ELEV." You can use your own dataset or find one online.

Usage
Run the Python script to generate the volcano elevation map:


`python volcano_map.py`
The map will be saved as Map1.html in the project directory.

Code Explanation
The Python script volcano_map.py does the following:

Imports necessary libraries: folium for creating the map and pandas for reading volcano data from a CSV file.

Reads volcano data from the `Volcanoes.txt` CSV file, extracting latitude, longitude, and elevation.

Defines a function colour_marker to assign colors to volcano markers based on elevation. Red markers represent elevations below 1000 meters, orange markers represent elevations between 1000 and 3000 meters, and green markers represent elevations above 3000 meters.

Creates a Folium map centered at latitude 38.58 and longitude -99.08 with a zoom level of 6. It uses OpenStreetMap as the base tileset.

Initializes a FeatureGroup named "my map" to group the volcano markers.

Iterates through the volcano data, adding a CircleMarker for each volcano. The marker's color is determined by the colour_marker function, and the popup displays the volcano's elevation.

Adds a GeoJSON layer `(world.json)` to overlay country boundaries on the map. You should provide the GeoJSON file in the project directory.

Finally, the `FeatureGroup` is added to the map, and the map is saved as Map1.html.

Sample Data
You can find sample volcano data in the Volcanoes.txt file. Replace this file with your own volcano dataset in the same format if needed.

License
This project is licensed under the MIT License. See the LICENSE file for details.


This Markdown content can be saved as `README.md` in your GitHub repository to provide clear documentation for your project.