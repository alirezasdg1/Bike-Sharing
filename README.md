# Bike-Sharing
## Introduction:

Transportation congestion and air pollution are two major problems in most large cities. Using bikes instead of personal vehicles can be a practical solution to address these critical issues. As such, governments all around the world support companies that facilitate using bikes. Bike sharing system is a trending industry to encourage citizens to use bikes as their daily transportation mode. 

Successful adopting this technology highly depends on user experience (UX) and implementing appropriate policies. Monitoring bike systems enables us to make appropriate decisions to improve UX and corresponding policies. As such, in this study, I aim to explore data for a bike sharing system.

In terms of UX, it is essential to explore the daily and seasonal usage of bikes to make sure that there are sufficient bikes based on demands. In addition, understanding whether this technology is adopted for daily usage, it is important to explore bike usages in different weekdays. As such, the main goal of this study is to visualize and compare time usage of bikes for different seasons, weekdays, and day times.

## Methods:

To achieve the main goal of this study, I used three different dataset. The first dataset was for a bake share system( i.e., Bluebikes in Boston) [1]. Here, I only included data for year 2017. This dataset included more than 1,300,000 instances with the following attributes [2]:

	1. Trip Duration (seconds)
	2. Start Time and Date
	3. Stop Time and Date
	4. Start Station Name & ID
	5. End Station Name & ID
	6. Bike ID
	7. User Type (Casual = Single Trip or Day Pass user; Member = Annual or Monthly Member)
	8. Birth Year
	9. Gender

The second dataset [3] included Boston weather data for every days between 1/1/2013-4/8/18. Again, I only used dataset for year 2017. This dataset contains the following attributes:

	1. Averages of temperature
	2. Average of dew point
	3. Average of wind speeds
	4. sea level pressure
	5. precipitation levels

Finally, the last dataset [3] included 2017 official holidays for Boston.

To analyze data, I first had to join all of the data tables (e.g., biking system dataset, weather dataset, and holidays information. For this purpose, I first created three columns (i.e., year, month, and day) based on the “starttime” column data. I used these new columns as primary keys to merge the biking system dataset with the weather data table which had the same columns. Before merging the holiday data table to other dataset, I reshaped it to include the following columns: year, month, and day. By using these columns, I joined all of the three data tables. I also created ‘age’ and ‘season’ columns based on ‘birth year’ and ‘month’ column respectively. 

In this project, I was mainly interested in exploring the effects of different factors on the number of trips/day. To compute my main outcomes (# trips/day), I counted the number of the “starttime” for each day. To achieve the main goal of this study, I explored the effects of weather condition, season, gender, and age on the main outcome by visualizing several patterns and testing the following hypotheses:


	H1. Number of trips/day depends of weather conditions.
	H2. Number of trips/day is highly correlated with weather indexes (e.g., Avg temp, Avg Humidity, Avg Visibility, Avg Wind speed). 
	H3. Number of trips/day is higher during the warm seasons comparing with the cold seasons.
	H4. Number of registered users higher than casual users during weekdays.
	H3. Number of casual users are higher than registered users during off days.
	H4. Number of trips/day is higher during each weekday comparing to weekends.
	H5. Number of trips/day for females and males are similar.
	H6. Number of trips/day for young people are higher than other age groups.

In the following sections, I discussed the results of my analyses in details.

## The effects of weather on number of trips/day

<img src='src/figs/Weather_conditions.png'>


## References:

1. https://s3.amazonaws.com/hubway-data/index.html
2. https://www.bluebikes.com/system-data
2. https://www.kaggle.com/jqpeng/boston-weather-data-jan-2013-apr-2018
3. https://www.officeholidays.com/countries/usa/massachusetts/2017
