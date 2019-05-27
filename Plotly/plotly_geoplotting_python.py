"""
Geoplotting and Choropleth Maps - Python, Plotly Data Visualization
--------------------------------------------------------------------------------
Gianluca Capraro
Created: May 2019
--------------------------------------------------------------------------------
This script will demonstrate the use of Plotly along with Python to create
geographical plots. This script will utilize data from the following .csv files:
- 2011_US_AGRI_Exports.csv
- 2012_Election_data.csv
- 2014_World_GDP.csv
- 2014_World_Power_Consumption.csv

This public data will be used to demonstrate plotly's visualization capabilities, 
specifically, those related to geoplotting on the national and international scale.

IMPORTANT: If you intend to view each type of plot within this script, you will
need to comment out the sections of code that do not involve the desired plot.
If this script is run as is, it will plot everything at once and you will only
be able to interact with the last plot demonstrated (2012 Election Data). 

Each section is designed to run on its own.

For all method parameters, refer to Plotly official documentation.
--------------------------------------------------------------------------------------------------------------------------------
"""

#import plotly and necessary libraries for offline plotting
import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#import pandas for data manipulation
import pandas as pd

"""
--------------------------------------------------------------------------------------------------------------------------------
Simple Choropleth US Map Example
--------------------------------------------------------------------------------------------------------------------------------
- creating a map figure requires two parameters:
	- data (a dictionary containing map detail information)
	- layout (a dictionary containing the type of map)
- this section of code will demonstrate a simple example of plotting the US
	- will show 3 states, California, New York, Colorado
	- give each a different z value and text field
--------------------------------------------------------------------------------------------------------------------------------
"""

#create the map data dictionary
map_data = dict(type = 'choropleth', locations = ['CA','NY','CO'], locationmode = 'USA-states', colorscale = 'Portland', text = ['Sunshine State','Never Sleeps','Mile High'], z = [1,2,3], colorbar = {'title':'State Z Value'})

#create the layout dictionary for the US
map_layout = dict(geo = {'scope':'usa'})

#create an instance of the map
choropleth_map = go.Figure(data=[map_data],layout=map_layout)

#call plotly to create the plot (opens browser)
print('\nOpened Browser: Simple Plotly US Map...')
plot(choropleth_map)
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Create a Map Showing Agricultural Exports by State
--------------------------------------------------------------------------------------------------------------------------------
- Read in data from 2011_US_AGRI_EXPORTS
- Create a US Map that shows each state's Agricultural exports in Millions USD
- Format the data dictionary to more easily understand parameters
- Change the layout to show lakes on the map, define lake color
--------------------------------------------------------------------------------------------------------------------------------
"""

#read in the csv file
agri_exports = pd.read_csv('2011_US_AGRI_EXPORTS.csv')

#print the head of the data to understand contents
print('Showing 2011 Agricultural Exports Head:')
print(agri_exports.head())
print('\n')

#define the map data
agri_data = dict(type='choropleth',
            colorscale = 'Rainbow',
            locations = agri_exports['code'],  		#use the state code data 
            z = agri_exports['total exports'], 		#color by amount of exports
            locationmode = 'USA-states',
            text = agri_exports['text'],				#use the text column data
            colorbar = {'title':"Millions USD"}
            ) 

#define the map layout
agri_layout = dict(
		title = '2011 US Agriculture Exports by State',
        geo = dict(
            scope='usa',
            showlakes = True,
            lakecolor = 'rgb(85,173,240)')
        )

#create the agricultural exports map object
agri_choromap = go.Figure(data = [agri_data], layout = agri_layout)

#display the geomap
print('\nOpened Browser: 2011 US Agriculture Exports by State...')
plot(agri_choromap)
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Create a World Map to Visualize Countries and their GDP
--------------------------------------------------------------------------------------------------------------------------------
- Read in data from 2014_World_GDP
- Create a World Map that shows country GDP data
- Change the layout to a Mercator style - an interactive globe
	You can click and drag to move around globe
--------------------------------------------------------------------------------------------------------------------------------
"""

#read in the csv file
world_gdp_data = pd.read_csv('2014_World_GDP.csv')

#print the head of the data to understand contents
print('Showing World GDP Data Head:')
print(world_gdp_data.head())
print('\n')

#define the world map data
world_map_data = dict(
        type = 'choropleth',
        locations = world_gdp_data['CODE'],
        z = world_gdp_data['GDP (BILLIONS)'],
        text = world_gdp_data['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      ) 

#define the world map layout
world_map_layout = dict(
    	title = '2014 World GDP',
    	geo = dict(
        	showframe = True,
        	projection = {'type':'mercator'}
    )
)

#create the agricultural exports map object
world_gdp_choromap = go.Figure(data = [world_map_data], layout = world_map_layout)

#display the geomap
print('\nOpened Browser: 2014 World GDP...')
plot(world_gdp_choromap)
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Create a World Map to Visualize Global Power Consumption
--------------------------------------------------------------------------------------------------------------------------------
- Read in data from 2014_World_Power_Consumption
- Create a World Map that shows country power consumption data
- Add a custom colorscale
- Reverse the scale of the colormap
--------------------------------------------------------------------------------------------------------------------------------
"""

#read in the csv file
world_consumption_data = pd.read_csv('2014_World_Power_Consumption.csv')

#print the head of the data to understand contents
print('Showing World Power Consumption Data Head:')
print(world_consumption_data.head())
print('\n')

#define the world map data
world_map_data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = world_consumption_data['Country'],
        locationmode = "country names",
        z = world_consumption_data['Power Consumption KWH'],
        text = world_consumption_data['Country'],
        colorbar = {'title' : 'Power Consumption in KWH'}
      ) 


#define the world map layout
world_map_layout = dict(
		title = '2014 Power Consumption in KWH',
        geo = dict(
        	showframe = False,
        	projection = {'type':'mercator'})
      )


#create the agricultural exports map object
world_power_choromap = go.Figure(data = [world_map_data], layout = world_map_layout)

#display the geomap
print('\nOpened Browser: 2014 World Power Consumption...')
plot(world_power_choromap)
print('\n')



"""
--------------------------------------------------------------------------------------------------------------------------------
Create a US Map to Visualize Election Data by State
--------------------------------------------------------------------------------------------------------------------------------
- Read in data from 2012_Election_Data
- Create a US Map that shows voting-age population (VAP) per state
	- For exploration with other data columns, consider the data type
	- VAP works nicely because it is already a float value
	- Add formatted markers
--------------------------------------------------------------------------------------------------------------------------------
"""
#read in the csv file
election_data = pd.read_csv('2012_Election_Data.csv')

#print the head of the data to understand contents
print('Showing 2012 Election Data Head:')
print(election_data.head())
print('\n')

#define the US map data
map_data = dict(
			type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = election_data['State Abv'],
            z = election_data['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = election_data['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            )


#define the US map layout
map_layout = dict(
			title = '2012 Election Voting Data',
            geo = dict(
            	scope='usa',
                showlakes = True,
                lakecolor = 'rgb(85,173,240)')
             )


#create the agricultural exports map object
election_choromap = go.Figure(data = [map_data], layout = map_layout)

#display the geomap
print('\nOpened Browser: 2012 Election, Voting Age Population by State...')
plot(election_choromap)
print('\n')




