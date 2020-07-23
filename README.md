# Bike-Sharing
# Introduction:

Transportation congestion and air pollution are two major problems in most large cities. Using bikes instead of personal vehicles can be a practical solution to address these critical issues. As such, governments all around the world support companies that facilitate using bikes. Bike sharing system is a trending industry to encourage citizens to use bikes as their daily transportation mode. 

Successful adopting this technology highly depends on user experience (UX) and implementing appropriate policies. Monitoring bike systems enables us to make appropriate decisions to improve UX and corresponding policies. As such, in this study, I aim to explore data for a bike sharing system.

In terms of UX, it is essential to explore the daily and seasonal usage of bikes to make sure that there are sufficient bikes based on demands. In addition, understanding whether this technology is adopted for daily usage, it is important to explore bike usages in different weekdays. As such, the main goal of this study is to visualize and compare time usage of bikes for different seasons, weekdays, and day times.

# Methods:

To achieve the main goal of this study, I use three diferent dataset. The first dataset is for a bake share system( i.e., bluebikes in Boston) for the year 2017 [1]. This dataset includes more than 1,000,000 instances with the following attributes [2]: 

* 1. Trip Duration (seconds), 2. Start Time and Date, 3. Stop Time and Date, 4. Start Station Name & ID, 5. End Station Name & ID, 6. Bike ID, 7. User Type (Casual = Single Trip or Day Pass user; Member = Annual or Monthly Member), 8. Birth Year, 9. Gender

The second dataset [3] includes boston whether data for every days between 1/1/2013-4/8/18. This dataset contains the following attributes:

1. averages of temperature, 2. dew point, 3. wind speeds, 4. sea level pressure, and 5. precipitation levels

Finally, the last dataset [3] includes official holidays for Boston in 2017. 


Here, after merging the mentioned datasets, I visualize the number of casual/registered users for different seasons, weekdays, weathers, and daytimes. I also test several hypotheses:

	H1. Number of bike users depends of weather conditions
	H2. Number of registered users higher than casual users during weekdays
	H3. Number of casual users are higher than registered users during holidays
	H4. Number of total users are higher during each weekday comparing to weekends
	H5. Number of users are higher during morning/evening rush hours comparing to afternoon during weekdays.

# References:

1. https://s3.amazonaws.com/hubway-data/index.html
2. https://www.bluebikes.com/system-data
2. https://www.kaggle.com/jqpeng/boston-weather-data-jan-2013-apr-2018
3. https://www.officeholidays.com/countries/usa/massachusetts/2017
