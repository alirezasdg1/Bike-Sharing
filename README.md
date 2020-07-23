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

### Weather indexes and the number of trips per day

I first explored whether there were any correlations between the number of trips and weather indexes. I found that the average temperatures and the number of trips for each day are highly correlated (Table 1 and Fig1). Though the number of trips and other indexes were not highly corelated, the effects of some these indexes on the output were significant. For example, the correlation between average wind speed and the outcome were significant (p-value <0.001).    

<center>
Table 1. Correlation between different weather indexes and the number of trips/day 

|       index       |Avg Temp (F)|Avg Humidity (%)|Avg Visibility (mi)|Avg Wind (mph)|Number of trips/day|
|-------------------|-----------:|---------------:|------------------:|-------------:|--------------:|
|Avg Temp (F)       |       1.000|           0.173|              0.130|        -0.226|          0.844|
|Avg Humidity (%)   |       0.173|           1.000|             -0.619|        -0.134|          0.000|
|Avg Visibility (mi)|       0.130|          -0.619|              1.000|        -0.102|          0.296|
|Avg Wind (mph)     |      -0.226|          -0.134|             -0.102|         1.000|         -0.319|
|Total_count_day    |       0.844|           0.000|              0.296|        -0.319|          1.000|
</center>


<p align="center">
<img src='src/figs/Weather_Indexes.png'>
<center>Fig 1. The correlation between different weather indexes and the outcome variables. </em>
</p>

### Weather conditions:

Here, I compared the number of trips/day for different weather conditions (i.e., clear, rainy, snowy, and both rainy and snowy weathers). Analyses of variance (ANOVAs) showed that the weather condition had significant effects on the outcome (p<0.001). I used the Tukey method for performing the paired comparisons. This method showed that the number of trips were significantly higher during clear and rainy weathers comparing with the snowy and both snowy and rainy weathers (Table2 and Fig 2). Surprisingly, there were not any significant differences between rainy and clear weather.

<p align="center">
Table 2. results of multiple comparison of means - Tukey HSD

|group1|group2|p-adj|reject|
|------|------|----:|------|
|Both  |None  |0.001|True  |
|Both  |Rain  |0.001|True  |
|Both  |Snow  |0.900|False |
|None  |Rain  |0.653|False |
|None  |Snow  |0.001|True  |
|Rain  |Snow  |0.001|True  |
</p>




<img src='src/figs/Weather_conditions.png'>
<center>Fig 2. It shows the mean of the number of trips/day for different weather conditions. Error bars indicate 95% confidence intervals. </em>


### Season effects

My results showed that seasons had significant effects on the outcome variable (Table 3). As you can see in Fig 3, the number of trips/day increased significantly during spring and summer comparing with winter and fall. It is also interesting that the difference between fall and winter is very large (Fig 3).


Table 3. results of multiple comparison of means - Tukey HSD

|group1|group2|p-adj|reject|
|-----:|-----:|----:|------|
|Winter|Spring|0.001|True  |
|Winter|Summer|0.001|True  |
|Winter|  Fall|0.001|True  |
|Spring|Summer|0.001|True  |
|Spring|Winter|0.002|True  |
|Summer|Winter|0.001|True  |



<img src='src/figs/Weather_seasons.png'>
<center>Fig 3. It shows the mean of the number of trips/day for different seasons. Error bars indicate 95% confidence intervals. </em>

## Registered users vs casual users

<img src='src/figs/BostonMap.png'>
<center>Fig 4. It shows start locations and number of trips/day for all of the biking trips in year 2017. The blue markers indicate registered customers and red markers show casual users. The markers sizes are proportional to the number of trips per day. </em>

## References:

1. https://s3.amazonaws.com/hubway-data/index.html
2. https://www.bluebikes.com/system-data
2. https://www.kaggle.com/jqpeng/boston-weather-data-jan-2013-apr-2018
3. https://www.officeholidays.com/countries/usa/massachusetts/2017
