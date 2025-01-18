TOPIC: Analysing the impact of weather on EPL match outcomes

DATA SOURCE:
https://www.football-data.co.uk/englandm.php
The English Premier League match data, including daily updates on gambling odds, is available in CSV format. This dataset provides detailed match information, such as match times, participating teams, goals, shots on target, and fouls committed. 

https://www.premierleague.com/home
The league table, featuring daily updates on total games played, team standings, wins, and losses, is available on the official Premier League website under Premier League Tables. Leagues tables with goal scores, loss information will be web scrapped. 

https://meteostat.net/en/
Meteostat offers open access to weather and climate data, sourcing information from national weather services like NOAA and DWD. Hourly weather records include details such as temperature, wind speed, relative humidity, and overall weather conditions. The data was retrieved via API calls and exported in Excel format.

INTERESTING CHARACTERISTICS: 
This project focuses on exploring how weather conditions impact the outcomes of English Premier League (EPL) matches. By integrating detailed match statistics, hourly weather data, and betting odds from gambling companies, this analysis aims to uncover correlations between factors like temperature, precipitation, wind speed, and team performance. These insights could potentially reveal patterns that influence match outcomes, offering valuable predictions for betting strategies. With comprehensive data covering multiple perspectives, this dataset is well-suited for both predictive modelling and deeper statistical analysis and will be beneficial for those who gamble on matches.

SRUCTURE OF DATA SETS:
The dataset spans five seasons of the English Premier League, from 2019 to 2023, featuring 26 teams from 18 different cities. Hourly weather data is collected from the nearest weather station to each match location. The key attributes include: 
Club: Str, names of the club (e.g., Manchester United) 
Date: Datetime, date and time of the match kickoff (e.g., 2020-02-03 20:00) 
Goals: Int, number of goals scored 
FullTimeResult: Str, 'H' representing a home team win and 'A' for an away team win 
AwayTeamYellowCards: Int, number of yellow cards received by the away team 
HomeTeamOdds: Float, betting odds for the home team, provided by gambling companies
WeatherConditionCode: Int, numeric code representing the weather conditions during the match

PROPOSED KPI: 
1.	Win/Loss ratio of teams in different weather conditions (e.g., rain, snow, high wind).
2.	Correlation between the number of shots taken and weather conditions. 
3.	Average goals per match in varying weather conditions.
4.	Average fouls committed and cards received under varying weather conditions.
5.	Average betting odds for home versus away teams in adverse weather conditions.


<Result>
1.	Manchester City has maintained a winning percentage of 73% over the past five years. However, Arsenal has played under various weather conditions and tends to perform well across different weather conditions.
2.	West Ham United took the greatest number of shots on target when it was cloudy, with 390 shots. 
3.	Tottenham Hotspur has the highest average goals per match, with 6.50, when it rains. 
4.	Brighton & Hove Albion tends to commit more fouls than other teams, with 1,998 fouls, but its winning percentage is only 32%. 
5.	Higher odds for the away team indicate a stronger belief in the home team's likelihood of winning. However, the market’s Maximum Odds for a Home Win are higher during snowy conditions.

