import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns


airbnb = pd.read_csv('listings.csv')
print(airbnb.head())

#View the data types in the data set
print(airbnb.dtypes)

#View each unique neighbourhood group variable
print(airbnb['neighbourhood_group'].unique())

#View each unique room type variable
print(airbnb['room_type'].unique())

#Clean the dataset
airbnb.isnull().sum()

#Remove redundant variables
airbnb.drop(['id','host_name','last_review'],axis=1,inplace=True)
airbnb.head()

#Replace missing variables
airbnb['reviews_per_month'].fillna(0,inplace=True)

#Assign minimum nights >= 90 column
airbnb['min_night_90_days'] = np.where(airbnb['minimum_nights'] >= 90, '90 nights and above', 'Below 90 nights')


#Bar Chart displaying Host IDs with highest number of listings
top_host_id = airbnb['host_id'].value_counts().head(10)
sns.set(rc={'figure.figsize':(10,8)})
viz_bar = top_host_id.plot(kind='bar')
viz_bar.set_title('Hosts with the most listings in Singapore')
viz_bar.set_xlabel('Host IDs')
viz_bar.set_ylabel('Count of listings')
viz_bar.set_xticklabels(viz_bar.get_xticklabels(), rotation=45)

plt.show()

#Pie Chart displaying neighbourhood groups
labels = airbnb.neighbourhood_group.value_counts().index
colors = ['#008fd5','#fc4f30','#e5ae38','#6d904f','#8b8b8b']
explode = (0.1,0,0,0,0)
shape = airbnb.neighbourhood_group.value_counts().values
plt.figure(figsize=(12,12))
plt.pie(shape, explode = explode, labels=shape, colors= colors, autopct = '%1.1f%%', startangle=90)
plt.legend(labels)
plt.title('Neighbourhood Group')
plt.show()

#Pie chart for listings above 90 nights
labels = list(airbnb['min_night_90_days'].unique())
sizes = list(airbnb.groupby('min_night_90_days').count()['neighbourhood'])
sizes.sort()
#colors
colors = ['#66b3ff','#ff9999']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90)
#draw circle
centre_circle = plt.Circle((0,0),0.69,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
#Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.show()

#Top Planning Area
airbnb.neighbourhood.value_counts().head(10)

#Review distribution by minimum nights
plt.figure(figsize=(10,6))
sns.scatterplot(x='minimum_nights', y='number_of_reviews', data=airbnb)
plt.title("Distribution of reviews by minimum nights")
plt.show()

#Check values to map
coord = airbnb.loc[:,['longitude','latitude']]
coord.describe()

#Plotting Latitude and Longitude of AirBnB properties
plt.figure(figsize=(18,12))
plt.style.use('fivethirtyeight')
BBox = (103.5935, 104.0625, 1.1775, 1.5050)
sg_map = plt.imread('map.gif')
plt.imshow(sg_map,zorder=0,extent=BBox)
ax = plt.gca()
groups = airbnb.groupby('neighbourhood_group')
for name,group in groups :
    plt.scatter(group['longitude'],group['latitude'],label=name,alpha=0.5, edgecolors='k')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

