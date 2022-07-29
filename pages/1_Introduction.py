import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="About BAFA", page_icon=":football:",layout="wide")
df = pd.read_csv('pages/Data/BAFA_2019_complete.csv',index_col=False)

df.rename(columns={'lat_d':'lat','lon_d':'lon'},inplace=True)


st.markdown("# About BAFA")
st.sidebar.header("BAFA Overview")
st.subheader('Introduction')
st.markdown('''##### BAFA is the abbreviation for the British American Football Association. It is the national governing body for the American Football in Great Britain. Currently, BAFA oversees two groups: Contact Football and Flag Fotball. Within contact football, there are different disciplines to accomodate different sectors of the population interested in the game.
''')
st.markdown("##### Contact Football:")
st.markdown('###### - Adult Contact')
st.markdown("###### - Women's Contact")
st.markdown("###### - Children's Contact")
st.markdown("###### - University Football (BUCS)")
st.markdown("###### - Wheelchair American Football")
st.markdown("######")
st.markdown('###### For more information about BAFA please visit :football: [BAFA](https://www.britishamericanfootball.org/):football:')
st.markdown("#####")
st.markdown("###### This analysis is carried out regarding the adult contact 2019 season")
st.markdown("###### Concerning American Football, adult contact is the most played discipline in the UK")

st.markdown('#### 2019 Adult Contact')
st.markdown(f"###### The League is made out of {(pd.unique(df['Division'])).size} divisions playing around the UK.")
st.markdown("###### The map shows the teams location of each division. Each red dot marks the place where games are played in the selected disvision")
st.markdown("**👈 Select Division(s) for you to check out!")
divisions = tuple(pd.unique(df['Division']).tolist())
with st.sidebar:
    option = st.multiselect('Choose Division to see its location:',divisions)

# st.markdown('###### Teams playing in Division: ' + option)
bydivision = df[df.Division.isin([option])]
byteams = bydivision.groupby('Home_Team').count()
teams = [byteams.iloc[i].name for i in range(len(byteams))]

cola, colb = st.columns([1,3])

with cola:
    for division in option:
        with st.expander('Teams in ' + division):
            bydivisiondf = df[df.Division == division]
            for team in bydivisiondf['Home_Team'].unique():
                st.write(':red_circle: '+ team)

with colb:
    st.map(df[df.Division.isin(option)])


       
st.write('---')


