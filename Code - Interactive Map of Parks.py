import pandas as pd
import folium

# Load the parks data CSV file
parks_file_path = 'parksdata.csv'  # Replace with your file path
parks_df = pd.read_csv(parks_file_path)

# Create a map centered around the average location of all parks in Belfast
map_center = [parks_df['LATITUDE'].mean(), parks_df['LONGITUDE'].mean()]
belfast_parks_map = folium.Map(location=map_center, zoom_start=13)

# Add park markers to the map
for _, park in parks_df.iterrows():
    folium.Marker(
        location=[park['LATITUDE'], park['LONGITUDE']],
        popup=park['NAME'],
        icon=folium.Icon(color='green', icon='tree')
    ).add_to(belfast_parks_map)

# Save the map to an HTML file
belfast_parks_map.save('belfast_parks_map.html')

print("Map saved as 'belfast_parks_map.html'")