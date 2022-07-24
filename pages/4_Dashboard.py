from datetime import date, datetime
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def query_builder(Div,HS,AS,GR,dataf,decisions): 
    
    hs_min, hs_max = HS
    as_min, as_max = AS
    if decisions == [False,False,False,False]: #[Divcheck,HS_check,AW_check,GR_check] 1
        message = f"##### No parameters selected / Choose parameter(s)"
        
        
    # Division combinations
    elif decisions == [True,True,True,False]: #Done 2
        message = f'Only Division, Home Score and Away Score'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True))]
    
    elif decisions == [True,True,False, True]: #Done 3
        message = f'Only Division, Home Score and Game Result'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) &(dataf.Game_Result.isin(GR))]

    elif decisions == [True,False,True,True]: #Done 4
        message = f'Only Division, Away Score and Game Result'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True)) &(dataf.Game_Result.isin(GR))]

    elif decisions == [True,True,False,False]: #Done 5
        message = f'Only Division and Home Score'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Home_Score.between(hs_min,hs_max,inclusive=True))]

    elif decisions == [True,False,True,False]: #Done 6
        message = f'Only Division and Away Score'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True))]

    elif decisions == [True,False,False,True]: #Done 7
        message = f'Only Division and Game Result'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Game_Result.isin(GR))]

    elif decisions == [True,False,False,False]: #Done 8
        message = f" Only Division"
        returned_df =  dataf[dataf.Division.isin(Div)]

    # Home Score Combinations
    elif decisions == [False,True,True,True]: #Done 9
        message = f'Only Home Score, Away score and Game Result'
        returned_df = dataf[(dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True)) & (dataf.Game_Result.isin(GR))]

    elif decisions == [False,True,True,False]: #Done 10
        message = f'only home and away scores'
        returned_df = dataf[(dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True))]
    
    elif decisions == [False,True,False,True]: #Done 11
        message = f"Only Home Score and Game Result"
        returned_df = dataf[(dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) & (dataf.Game_Result.isin(GR))] 
    elif decisions == [False,True,False,False]: #Done 12
        message = f'Only Homescore'
        returned_df =  dataf[dataf.Home_Score.between(hs_min,hs_max,inclusive=True)]

    # Away Score Combinations

    elif decisions == [False,False,True,True]: #Done 13
        message = f'Only Away and Game Result'
        returned_df = dataf[(dataf.Away_Score.between(as_min,as_max,inclusive=True)) & (dataf.Game_Result.isin(GR))] 

    elif decisions == [False,False,True,False]: #Done 14
        message = f'Only Away Score'
        returned_df =  dataf[dataf.Away_Score.between(as_min,as_max,inclusive=True)]

    # Game Result Combinations

    elif decisions == [False,False,False,True]: #Done 15
        message = f'Only Game Result'
        returned_df = dataf[dataf.Game_Result.isin(GR)]

    else: #Done 16
        message = f'All Parameters'
        returned_df = dataf[(dataf.Division.isin(Div)) & (dataf.Home_Score.between(hs_min,hs_max,inclusive=True)) & (dataf.Away_Score.between(as_min,as_max,inclusive=True)) & (dataf.Game_Result.isin(GR))]
    
    return returned_df, message


st.set_page_config(page_title="Dashboard", page_icon=':bulb:',layout='wide')
season_df = pd.read_csv('pages/Data/BAFA_2019_complete.csv',index_col=False)

newmaster = pd.read_csv('pages/Data/BAFA_By_team_2019.csv',index_col=False)

season_df['Date'] = season_df['Game_Date']+" "+season_df['Game_Time']
season_df['Date'] = pd.to_datetime(season_df['Date'],infer_datetime_format=True)
season_df['Game_day'] = season_df['Date'].dt.date
season_df['Match'] = season_df['Home_Team']+' - '+season_df['Away_Team']

master = season_df[['Date','Game_day','Home_Team','Away_Team','Home_Score','Away_Score','Division','Game_Result','Total_Score','Temp_home','Cast_home','Match']]
divisions = tuple(pd.unique(master['Division']).tolist())
game_results = tuple(pd.unique(master['Game_Result']).tolist())

query_result = st.container()

with st.sidebar:

    st.markdown("### Select Parameter(s) to query information")

    by_division = st.container()
    by_homescore = st.container()
    by_awayscore = st.container()
    by_gameresult = st.container() 
    checkboxes = st.container()

    with by_division:
        choose_division = st.multiselect('Choose Division(s)',divisions)

    with by_homescore:
        choose_homescore = st.slider('Choose a range of scores for the home team',0,100,(0,40))

    with by_awayscore:
        choose_awayscore = st.slider('Choose a range of scores for the visiting team',0,100,(20,40))

    with by_gameresult:
        choose_game_result = st.multiselect('Choose game result(s)',game_results)
    
    with checkboxes:
        col1,col2, = st.columns([1,1,])
        with col1:
            Div_check = st.checkbox('Division')
        with col2:
            HS_check = st.checkbox('Home Score')
        col3,col4 = st.columns([1,1])
        with col3:
            AW_check = st.checkbox('Away Score')
        with col4:
            GR_check = st.checkbox('Game Result')


    query = st.button('Query')
    check_options = [Div_check,HS_check,AW_check,GR_check]

with st.expander('See Instructions'):
    st.markdown(
        """
        ##### One can query through the data in 3 simple steps by selecting different parameters on the left sidebar.
        ##### Steps:
        1. Select Parameter(s)
        2. Check the options the query is based on 
        3. Click the "Query" button

        ###### Some nomenclature to consider
        - HW -> refers to games where the local team won
        - AW -> refers to games where the visiting team won
        - T  -> refers to tied games 

        Final note:

        All queries are based on an 'and' operator

    """)

with query_result:
    if query:
        query_df, text = query_builder(choose_division,choose_homescore,choose_awayscore,choose_game_result,master,check_options)
        st.write(text)
        graphs, raw = st.tabs(['Graphs','Query Result'])
        with graphs:
            try:
                colcast, colscore = st.columns([2,2])
                with colcast:
                    figcountcast = plt.figure()
                    sns.countplot(x="Division", hue="Cast_home",data=query_df)
                    plt.xticks(rotation=90)

                    st.pyplot(figcountcast)
                with colscore:
                    grid_score = sns.catplot(x="Match", y="Home_Score",kind='bar', hue='Division',
                        data=query_df)
                    plt.xticks(rotation=89)
                    st.pyplot(grid_score)
                
                coltotscores, colsomething = st.columns([2,2])
                with coltotscores:
                    f, ax = plt.subplots(figsize=(6, 8))
                    sns.barplot(x='Total_Score',y='Match',data=query_df,label='Total Score',color='b')
                    sns.set_color_codes('muted')
                    sns.barplot(x='Home_Score',y='Match',data=query_df,label='Home Score',color='r')
                    ax.legend(ncol=2, loc="lower right", frameon=True)
                    sns.despine(left=True, bottom=True)
                    st.pyplot(f)
                
                with colsomething:
                    figcount = plt.figure()
                    sns.countplot(x="Division", hue="Game_Result",data=query_df)
                    plt.xticks(rotation=90)

                    st.pyplot(figcount)
            except ValueError:
                st.write('Query retrived no information')




        with raw:
            st.table(query_df[['Home_Team','Away_Team','Home_Score','Away_Score','Division','Game_Result']])

    

   

