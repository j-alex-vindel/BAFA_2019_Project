import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="Data-Collection-Integration", page_icon=':computer:',layout='wide')
df = pd.read_csv('pages/Data/BAFA_2019_Full.csv',index_col=False)
venues = pd.read_csv('pages/Data/BAFA_2019_Team_Venues.csv')

st.markdown("# DATA Collection")
st.sidebar.header("Data Collection - Integration - Questions")

ab_data = st.container()
questions = st.container()

with ab_data:
    st.subheader('About the Data')
    st.markdown("###### Information about the season can be found here: [BAFA](https://bafanle.leaguerepublic.com/index.html). The site provides date & time, home team, away team and the final score for each game in a division.")
    st.markdown("###### From here: [BAFA Venues](https://bafanle.leaguerepublic.com/venues.html) one can accces, by name, the adress where teams have registered the location for their home games.")

    col1,col2 = st.tabs(['Table 1','Table 2'])
    with col1:
        st.markdown("##### The information about games is organized into a dataframe (table1)")
        st.table(df[['Game_Date','Game_Time','Home_Team','Away_Team','Home_Score','Away_Score','Division']].head(5))
    with col2:
        st.markdown("##### The information about the venues is compiled into a dataframe (table2)")
        st.table(venues[['Team_name','PostCode']].head(5))
    st.write(f'* These tables  only show a limited amount of the total rows.')
    st.markdown("##### The location where a game was played can be accessed by relating the Home_Team and the Team_name in both tables. Moreover, under the assumption that every team gathers in their home base before a game, information about where a team starts their journey when away can be accessed too.")
    st.markdown("##### Information about the distance between two postcodes can be found here [Postcode Distance](http://www.postcode-distance.com/distance-between-postcodes). Estimations on travel distance for each game is now accesible.")

    with st.expander('Some Data Findings regarding the names'):
        st.markdown('###### Postcode information  about Carslile Sentinels, Furness Phantoms, Maidstone Pumas, Bristol Apache and Cornish Sharks does not appear in [BAFA Venues](https://bafanle.leaguerepublic.com/venues.html). However, information about these teams was located through different means some from [Here](https://www.american-football.com/teams/carlisle-sentinels-1026) or directly from their social media. Bristol Apache shares the same postcode with other Bristol team.')
    with st.expander('Some Data Findings regarding the Game Scores'):
        st.markdown("###### It was found that some game scores are not recorded as nuumber rather with the letters 'H - W' and 'A - W'. The coding refers to home walkover or away walkover. Essentially, this is for game cancellations where the team recieving the walkover win were not notified correctly by the opposing team.")
        st.table(df[['Home_Team','Away_Team','Home_Score','Away_Score']][df['Home_Score'].isin(['A','H'])])
        st.markdown("###### It was suggested to consider the walkover score to 50 - 0.A-W then is changed to 0-50 and H-W to 50-0. Now a complete numerical analysis  can be performed for scores.")

    st.subheader('More Information')
    st.markdown("###### The PostCode is also useful to get more precise geolocation information (lattitude and longitude) by using the API [Here]('https://api.getthedata.com/postcode/').")
    st.table(venues[['Team_name','Lat','Long']].head(5))
    st.markdown('###### Following the same idea relating Home_Team and Team_name from tables 1,2. Geoinformation is now available. Combining geoinformation with time and date can lead to more interesting information.')
    st.markdown("###### Historical weather information can be accesed in the [API-weather](https://weather.visualcrossing.com). Now, an overall weather information about each game is available. This can be helpful to draw more information about the circumstances each game was played in.")
    st.table(df[['Game_Date','Game_Time','Home_Team','Away_Team','Temp','Humidity','Windspeed','Visibility','Precipitation','Cast']].head(5))
    st.markdown('###### The weather information is selected as these weather features can have an impact on the game performance. The units are as follows temperature: F, windspeed: miles/hour, visibility: miles, precipitation:inches, humidity: %.')
    st.markdown("###### Unfortunately, information about game stats are not available. Passing yards, rushing yards, total_allowed_yards, number of 1st and ten, passing attempts, pass completion, rush attempts, etc. would've made this analysis more robust.")

with questions:
    st.write('---')
    st.write(' The crawlers and web scrapers used to collect the data can be looked [here](https://github.com/j-alex-vindel/DATA_BAFA) ')
    st.write('---')
    st.subheader('Questions')
    st.markdown('###### The idea is to be able to answer some questions such as:')
    st.markdown('- Does a Team score most points at home or away?')
    st.markdown('- Which Division travels the most (km)?')
    st.markdown('- Which Division scores the most overall?')
    st.markdown("- What's the difference between the most scoring team in each division?")
    st.markdown("- Is there a relationship with the weather, travel distance and the points scored?")
    st.markdown('- What are the average weather conditions for the games?')
    st.markdown('- Can a predictive model be build? and How accurate it is considering the limitiations?' )




