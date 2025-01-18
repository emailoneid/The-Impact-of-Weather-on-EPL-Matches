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


Tables
Dimensions	Facts	StagingTable
dbo.dimBettingCompany	dbo.factBetting	dbo.Staging_DateInfo
dbo.dimDate	dbo.factLeague	
dbo.dimReferee	dbo.factMatch	
dbo.dimSeason	dbo.factWeather	
dbo.dimStadiumLocation		
dbo.dimTeam		
dbo.dimWeatherCondition		
dbo.dimWeatherStation		



ETL Process of dimBettingCompany, dimTeam, dimWeatherCondition
1.	Extract the source data
2.	Convert the data type
3.	Lookup for new data
4.	Check for null values
5.	Slowly Changing Dimension for changes
6.	Load


ETL Process of dimStadiumLocation, dimWeatherStation
1.	Extract the source data
2.	Convert the data type
3.	Lookup for new data
4.	Slowly Changing Dimension to update possible name (Stadium name, Weather Station name) changes
5.	Load


ETL Process of dimReferee
1.	Foreach Loop Container to loop through 5 csv files
2.	Extract the source
3.	Sort to remove duplicates
4.	Lookup for new data
5.	Slowly Changing Dimension for updates
6.	Load


ETL Process of dimSeason 
1.	Foreach Loop Container to loop through 5 csv files
2.	Extract the source
3.	Derive a column ‘DateValue’, database date (DT_DBDATE)
4.	Sort to remove duplicates
5.	Check for null values
6.	Load it to the Staging Table
7.	SQL Command to read the first record and last record of the Staging Table and update it to dimSeason
1.	09/08/2019 -> Start Date
2.	26/07/2020 -> End Date
3.	2019 -> Season Year
8.	Truncate the Staging Table


ETL Process of factLeague 
1.	Extract the source
2.	Convert the data type
3.	Lookup for Team_ID, Season_ID
4.	Lookup for new data
5.	Load


ETL Process of factWeather
1.	Foreach Loop Container for 13 csv files
2.	Separate Date and Time
3.	Lookup for Date_ID
4.	Covert null values to -9999
5.	Lookup for Weather_Condition_ID and Weather_Station_ID
6.	Lookup for new data
7.	Load


ETL Process of factMatch
1.	Foreach Loop Container for 5 csv files
2.	Derive columns Year, Date, Time
3.	Roundup minutes to the nearest hour (17:05 -> 17:00)
4.	Convert Team names (Man U -> Manchester United)
5.	Lookup for Home_Team_ID and Away_Team_ID
6.	Lookup for the Date_ID which matches with factWeather to get Weather_ID
7.	Lookup for new data
8.	Load


ETL Process of factBetting
1.	Same as factMatch
2.	Unpivot the betting columns to store Odds value
3.	Split betting types like "Market", "Closing “, "Home“ and handle empty company values as ‘unknown’
4.	Trim the names
5.	Convert the values as convert null odd values as 0
6.	Lookup tables for relevant IDs
7.	Aggregate to Group by for IDs and Maximum to avoid multiple entries for the same match
8.	Load


Data Visualization in PowerBI (League)
1.	Season selection
2.	Match related parameter
1.	Average Goals per Match
2.	Total Red Cards
3.	Total Fouls
4.	Total Goals
5.	Total Shots on Target
3.	Weather Condition parameter
1.	Clear
2.	Cloudy
3.	Fair
4.	etc

Data Visualization in PowerBI (Team)
1.	Season selection
2.	Match related parameter 
1.	Average Goals per Match
2.	Total Red Cards
3.	Total Fouls
4.	Total Goals
5.	Total Shots on Target
6.	etc
3.	Weather parameter
1.	Average temperature
2.	Snow Depth
3.	Wind Speed
4.	Total Precipitation
5.	etc
   
Data Visualization in PowerBI (Betting)
1.	Season selection
2.	Betting Type Selection
1.	Away Win Odds
2.	Home Win Odds
3.	Draw Win Odds 
4.	Over 2.5 Goals Odds
5.	Under 2.5 Goals Odds
3.	Weather Condition parameter
1.	Clear
2.	Cloudy
3.	Fair
4.	Etc
4.	Weather Parameter
1.	Average temperature
2.	Total Precipitation
3.	Win Speed
4.	Etc


Data Visualization in PowerBI (Comparison)
1.	Season selection
2.	Team selection 
1.	Relative Winning Percentages
2.	Total Winning Percentages
3.	Relative Match Scores
1.	Goals
2.	Shots
3.	Fouls
4.	Red Cards
3.	Relative Win, Loss, Draw by Weather Condition

Result
1.	Manchester City has maintained a winning percentage of 73% over the past five years. However, Arsenal has played under various weather conditions and tends to perform well across different weather conditions.
2.	West Ham United took the greatest number of shots on target when it was cloudy, with 390 shots. 
3.	Tottenham Hotspur has the highest average goals per match, with 6.50, when it rains. 
4.	Brighton & Hove Albion tends to commit more fouls than other teams, with 1,998 fouls, but its winning percentage is only 32%. 
5.	Higher odds for the away team indicate a stronger belief in the home team's likelihood of winning. However, the market’s Maximum Odds for a Home Win are higher during snowy conditions.


Difficulties Encountered
1.	Weather Data Collection 
1.	Many sources require paid API access. 
2.	Data for certain locations or dates may be unavailable. 
2.	Data Conversion Challenges 
1.	Date Conversion: Ensuring alignment between match times and weather data. 
2.	Granularity Issues: Weather data is recorded at different intervals, while match data varies in terms of timing and measurement units. Proper conversion is essential to maintain consistency.
3.	Understanding of Football and Weather Data Establishing proper relationships between football match data and weather conditions requires a solid understanding of both domains to ensure accurate analysis. 
4.	Further Analysis 
1.	Needs additional match data, including player information, more referee information would provide deeper insights. 
2.	Statistical modelling of weather and its impact on football performance remains a potential area for further exploration.


Weather_Fact_Table(factWeather)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Weather_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for factWeather 
2.FK 	Date_ID 	INT	 	 	Foreign Key for dimDate 
3.FK	Weather_Station_ID	INT			Foreign Key for dimWeather Station
4.FK 	Weather_Condition_ID (Foriegn Key) 	INT	 	 	Foreign Key for dimWeatherCondition 
5	Air_Temperature 	FLOAT 	 	 	Air Temperature (°C) 
6 	Dew_Point 	FLOAT 	 	 	Dew Point (°C) 
7 	Relative_Humidity 	FLOAT 	 	 	Relative Humidity (%) 
8 	Total_Precipitation 	FLOAT 	 	 	Total Precipitation (mm) 
9 	Snow_Depth 	FLOAT 	 	 	Snow Depth (mm) 
10 	Wind_Direction 	FLOAT 	 	 	Wind (from) Direction 
11 	Average_Wind_Speed 	FLOAT 	 	 	Average Wind Speed (km/h) 
12 	Wind_Peak_Gust 	FLOAT 	 	 	Wind Peak Gust (km/h) 
13 	Sea-Level_Air_Pressure 	FLOAT 	 	 	Sea-Level Air Pressure (hpa) 
14 	Total_Sunshine_Duration 	FLOAT 	 	 	Total Sunshine Duration (minutes) 


League_Fact_Table(factLeague)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	League_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for factFact 
2.FK	Team_ID	INT			Foreign Key for dimTeam
3.FK 	Season_ID 	INT	 	 	Foreign Key for dimSeason
4	Team_Rank	INT	 	 	Final team rank of the season
5 	Points	INT	 	 	Total points earned (Win = 3, Draw = 1, Lost = 0)
6 	Game_Played 	INT	 	 	The total number of games played
7 	Won 	INT	 	 	The total number of games won
8 	Drawn	INT	 	 	The total number of games drawn
9 	Lost 	INT	 	 	The total number of games lost
10 	Goals_For 	INT	 	 	The number of goals achieved
11 	Goals_Against 	INT	 	 	The number of goals lost
12 	Goals_Difference 	INT	 	 	Goals For – Goals Against
Match_Fact_Table(factMatch)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Match_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for factMatch
2.FK 	Season_ID (Foreign Key)	INT	 	 	Foreign Key for dimSeason 
3 .FK
	Date_ID (Foreign Key)	INT			Foreign Key for dimDate

4.FK 	Home_Team_ID (Foreign Key) 	INT	 	 	Foreign Key for dimTeam
5 FK	Away_Team_ID	INT			Foreign Key for dimTeam
6 .FK	Stadium_Location_ID (Foreign Key)	INT	 	 	Foreign Key for dimStadiumLocation
7 .FK	Weather_Condition_ID (Foreign Key)	INT	 	 	Foreign Key for dimWeatherCondition
8 .FK	Referee_ID	INT	 	 	Foreign Key for dimReferee
9	Full_Time_Home_Goals	INT	 	 	The number of goals scored by Home Team at full time
10	Full_Time_Away_Goals	INT	 	 	The number of goals scored by Away Team at full time
11	Full_Time_Result	VARCHAR(20)	 	 	Full Time Result (H = Home Win, D = Draw, A = Away Win)
12	Half_Time_Home_Team_Goals	INT	 	 	The number of goals scored by Home Team at half time
13	Half_Time_Away_Team_Goals	INT			The number of goals scored by Away Team at half time
14	Half_Time_Result	VARCHAR(20)			Half Time Result (H = Home Win, D = Draw, A = Away Win)
15	Home_Team_Shots	INT			Shots made by Home Team
16	Away_Team_Shots	INT			Shot made by Away Team
17	Home_Team_Shots_on_Target	INT			Shots on target made by Home Team
18	Away_Team_Shots_on_Target	INT			Shots on target made by Away Team
19	Home_Team_Fouls_Committed	INT			The number of fouls committed by Home Team
20	Away_Team_Fouls_Committed	INT			The number of fouls committed by Away Team
21	Home_Team_Corners	INT			The number of corners by Home Team
22	Away_Team_Corners	INT			The number of corners by Away Team
23	Home_Team_Yellow_Cards	INT			The number of yellow cards given to Home Team
24	Away_Team_Yellow_Cards	INT			The number of yellow cards given to Away Team
25	Home_Team Red_Cards	INT			The number of red cards given to Home Team
26	Away_Team_Red_Cards	INT			The number of red cards given to Away Team




Betting_Fact_Table (factBetting)
Key 	Name 	Data Type 	Null 	Attributes 	Description 	
1.PK 	Betting_ID (Primary Key)	 INT	 	IDENTITY 	Primary Key for factBetting 
2.	Match_ID	INT			
3.FK 	Date_ID (Foreign Key)	 INT	 	 	Foreign key for dimDate
4.FK 	Betting_Company_ID (Foreign Key)	 INT	 	 	Foreign key for dimBettingCompany
5 	Home_Win_Odds	FLOAT	 	 	The odds of home team winning 
6	Draw_Odds 	FLOAT	 	 	The odds of match ending in draw
7 	Away_Win_Odds	FLOAT	 	 	The odds of away team winning
8	Market_Maximum_Home_Win_Odds	FLOAT	 	 	Highest home win odds offered by any bookmaker
9	Market_Maximum_Away_Win_Odds	FLOAT	 	 	Highest away win odds offered by any bookmaker
10	Market_Maximum_Draw_Win_Odds	FLOAT	 	 	Highest draw odds offered by any bookmaker
11	Market_Average_Home_Win_Odds	FLOAT	 	 	Average odds of all bookmakers’ home wind odds
12	Market_Average_Away_Win_Odds	FLOAT	 	 	Average odds of all bookmakers’ away win odds
13	Market_Average_Draw_Win_Odds	FLOAT	 	 	Average odds of all bookmakers’ draw odds
14	Over_2_5_Goals_Odds 	FLOAT	 	 	Odds for total match goals exceeding 2.5
15	Under_2_5 Goals_Odds  	FLOAT			Odds for total match goals being 2.5 or fewer
16	Market_Maximum_Over_2.5_Goals	FLOAT			Highest odds for over 2.5 goals from any bookmaker
17	Market_Maximum_Under_2_5_Goals	FLOAT			Highest odds for under 2.5 goals from any bookmaker
18	Market_Average_Over_2_5_Goals	FLOAT			Average odds for over 2.5 goals across bookmakers
19	Market_Average_Under_2_5_Goals	FLOAT			Average odds for under 2.5 goals across bookmakers
20	Market_Size_of_Handicap_Home_Team	FLOAT			Betting spread of the handicap applied to the home team in a match (a negative value (e.g., -1.5) indicates that the home team is expected to perform better, a positive or zero value (e.g., +0.5 or 0) means the home team is less favoured, a bet on the home team wins only if they win by at least 2 goals.)
21	Asian_Handicap_Home_Odds 
	FLOAT			Odds adjusted for home team with an Asian Handicap
22	Asian_Handicap_Away_Odds 	FLOAT			Odds adjusted for away team with an Asian Handicap
23	Market_Maximum_Asian_Handicap_Home_Odds	FLOAT			Highest Asian Handicap Odds for the home team
24	Market_Maximum_Asian_Handicap_Away_Odds	FLOAT			Highest Asian Handicap odds for the away team
25	Market_Average_Asian_Handicap_Home_Odds	FLOAT			Average Asian Handicap odds for the home team
26	Market_Average_Asian_Handicap_Away_Odds	FLOAT			Average Asian Handicap odds for the away team
27	Closing_Home_Team_Win_Odds 	FLOAT			The final odds for the home team to win a match before the match starts
28	Closing_Away_Team_Win_Odds 	FLOAT			The final odds for the away team to win before the match starts
29	Closing_Draw_Win_Odds	FLOAT			The final odds for a draw before the match starts
30	Market_Maximum_Closing_Home_Win_Odds	FLOAT			The highest home win odds at closing time
31	Market_Maximum_Closing_Draw_Odds	FLOAT			The highest draw odds at closing time
32	Market_Maximum_Closing_Away_Team_Odds	FLOAT			The highest away win odds at closing time
33	Market_Average_Closing_Home_Team_Odds	FLOAT			Average home win odds at closing time 
34	Market_Average_Closing_Draw_Odds	FLOAT			Average draw odds at closing time 
35	Market_Average_Closing_Away_Team_Odds	FLOAT			Average away odds at closing time
36	Closing_Over_2_5_Goals	FLOAT			Final odds for over 2.5 goals before the match starts
37	Closing_Under_2_5_Goals 	FLOAT			Final odds for under 2.5 goals before the match starts
38	Market_Maximum_Closing_Over_2_5_Goals
	FLOAT			Highest odds for over 2.5 goals at closing time
39	Market_Maximum_Closing_Under_2_5_Goals	FLOAT			Highest odds for under 2.5 goals at closing time
40	Market_Average_Closing_Over_2_5_Goals	FLOAT			Average odds for over 2.5 goals at closing time
41	Market_Average_Closing_Under_2_5_Goals	FLOAT			Average odds for under 2.5 goals at closing time
42	Market_Size_of_Closing_Handicap_Home_Team	FLOAT			Betting spread of handicap applied to the home team at the closing time (a negative value (e.g., -1.5) indicates that the home team is expected to perform better, a positive or zero value (e.g., +0.5 or 0) means the home team is less favoured, a bet on the home team wins only if they win by at least 2 goals.)
43	Closing_Asian_Handicap_Home_Team_Odds	FLOAT			Final Asian Handicap odds for the home team before the match
44	Closing_Asian_Handicap_Away_Team_Odds
	FLOAT			Final Asian Handicap odds for the away team before the match
45	Market_Maximum_Closing_Asian_Handicap_Home_Team_Odds	FLOAT			Highest closing Asian Handicap odds for the home team
46	Market_Maximum_Closing_Asian_Handicap_Away_Team_Odds	FLOAT			Highest closing Asian Handicap odds for the away team
47	Market_Average_Closing_Asian_Handicap_Home_Team_Odds	FLOAT			Average closing Asian Handicap odds for the home team
48	Market_Average_Closing_Asian_Handicap_Away_Team_Odds	FLOAT			Average closing Asian Handicap odds for the away team




WeatherStationDimension(dimWeatherStation)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Weather_Station_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for dimStation
2.	Weather_Station_Name	VARCHAR(100)	 	 	Name of the weather station e.g. London Weather Centre
3.	Weather_Station_Code	INT			Weather Station Code “e.g. 03779” 
4.	Coordinates	INT	 	 	Map Coordinates e.g. 51.5085, -0.1257 


Weather_Condition_Dimension(dimWeatherCondition)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Weather_Condition_ID (Primary Key) 	 INT	 	IDENTITY 	Primary Key for dimWeatherCondition
2.	Weather_Condition	CHAR			Weather Condition e.g. Clear, Rain, Cloudy, etc.
3.	Weather_Condition_Code	 INT	 	 	Weather Condition Code e.g. 8 for Rain, 9 for Heavy Rain



Team_Dimension(dimTeam)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Team_ID (Primary Key) 	 INT	 	IDENTITY 	Primary Key for dimTeam
2.	Team_Name	 VARCHAR(50)	 	 	Team Name e.g.  Liverpool
Season_Dimension(dimSeason)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Season_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for dimSeason
2.	Season_Year	INT	 	 	Year of the EPL Season e.g. 2019, 2020
3.	Season_Start	DATE			Start Date of Season 
4.	Season_End
	DATE	 	 	End Date of Season


Date_Dimension(dimDate)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Date_ID (Primary Key) 	INT	 	IDENTITY 	Primary Key for dimDate
2.	Time	TIME	 	 	Time (0 = AM 12:00 / 16 = PM 04:00) 
3.	Date	DATETIME			YYYY-MM-DD(‘2018-08-23’)
4.	DayName	INT	 	 	Day in number.(‘28’)
5.	MonthNumber	INT			Month in number. (‘02’) 
6.	Year	INT	 	 	Year.(‘ 2018’)
7.	DateKey	INT			Datekey (20190101)
8	DayofMonth	INT			Day of the month
9	IsWeekend	BIT			Describes whether the match was played on a weekend or no




Betting_Company_Dimension(dimBettingCompany)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Betting_Company_ID (Primary Key) 	 INT	 	IDENTITY 	Betting_Company_ID Primary Key for dimBettingCompany
2.	Company_Name	 VARCHAR(50)	 	 	Betting company Name e.g. Bet365, VCBet, etc.

Staging_Table(dbo.Stagingdateinfo)
	Name	Data Type	Null	Attributes	Description
1	DateValue	Date			

Referee_Dimension(dimReferee)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Referee_ID (Primary Key) 	 INT	 	IDENTITY 	Primary Key for dimReferee
2.	Referee_Name	 VARCHAR(50)	 	 	Referee Name e.g.  M Oliver

Stadium_Location_Dimension(dimStadiumLocation)
Key 	Name 	Data Type 	Null 	Attributes 	Description 
1.PK 	Stadium_Location_ID (Primary Key) 	 INT	 	IDENTITY 	Primary Key for dimStadium
2.	Stadium _Name	 VARCHAR(50)	 	 	Stadium Name e.g.  Emirates Stadium
3.	Location	 VARCHAR(20)			Location Name e.g.  London
4.	Team_ID	INT			ID of each respective Teams Primary Key for dimTeam

