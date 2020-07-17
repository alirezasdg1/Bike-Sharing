# Bike-Sharing
# Introduction:

Transportation and pollutions are two major problems in most large cities. Using bikes instead of personal vehicles can be a practical solution to address these critical issues. As such, governments all around the world support companies that facilitate using bikes. Bike sharing system is a trending industry to encourage citizens to use bikes for their daily transportations. 

Successful adopting this technology highly depends on user experience (UX) and implementing appropriate policies. Monitoring bike systems enable us to make appropriate decisions to improve UX and corresponding policies. As such, in this study, I aim to explore data for a bike sharing system. 

In terms of UX, it is essential to explore time usage of bikes each day and season to make sure that there are sufficient bikes based on demands. In addition, to understand whether this technology is adopted for daily usage, it is important to explore bike usages in different weekdays. As such, the main goal of this study is to visualize and compare time usage of bikes for different seasons, weekdays, and day times.

# Methods:

To achieve the main goal of this study, I use a bike share dataset [1]. The dataset includes more than 17000 instances with the following attributes: 

1. instance, 2. Date, 3. Year, 4. Month, 5. Hour, 6. Holidays, 7. Weekday, 8. Working days, 9. Weather conditions, 10. Temperature, 11. Normalized humidity, 12. Windspeed, 13. Count of casual users for each hour, 14. Count of registered users for each hours 


Here, I visualize number of casual/registered users for different seasons, weekdays, weathers, and daytimes. I also test several hypotheses:

	H1. Number of bike users depends of whether conditions
	H2. Number of registered users higher than casual users during weekdays
	H3. Number of casual users are higher than registered users during holidays
  H4. Number of total users are higher during each weekday comparing to weekends
  H5. Number of users are higher during morning/evening comparing to afternoon during weekdays.

1. https://archive.ics.uci.edu/ml/machine-learning-databases/00275/
