import folium
from folium.plugins import FastMarkerCluster
from geopy.geocoders import Nominatim


def createMap(locations):
    # List of countries and cities
    # print(locations)
    # Create the Folium map
    folium_map = folium.Map(location=[0, 0],
                            zoom_start=2, tiles='CartoDB dark_matter')

    # Add the FastMarkerCluster layer to the map
    geolocator = Nominatim(user_agent="myGeocoder")
    for i in range(0, len(locations), 2):
        country = locations[i]
        city = locations[i+1]
        # Use a geocoding service to get the latitude and longitude for each city
        location = geolocator.geocode(f'{city}, {country}')
        if location:
            lat = location.latitude
            lon = location.longitude
            folium.Marker(location=[lat, lon], popup=f'{city}, {country}').add_to(folium_map)

    # Add the LayerControl to the map
    folium.LayerControl().add_to(folium_map)
    return(folium_map.get_root().render())
    # Save the map to an HTML file
    # folium_map.save('map.html')

