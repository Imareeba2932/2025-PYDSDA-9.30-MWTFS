import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is the Dashboard Page")  

df = sns.load_dataset("titanic")
st.dataframe(df)

#gender filter
gender = st.sidebar.multiselect('Gender',
                                 options = df['sex'].unique(),
                                 default = df['sex'].unique())

#pclass filter
pclass = st.sidebar.multiselect('Passenger Class',
                                options=df['pclass'].unique(),
                                default=df['pclass'].unique())

filtered_df = df[
    (df['sex'].isin(gender)) & #to check whether the gender filter has the data of sex column of df
    (df['pclass'].isin(pclass)) #to check whether the pclass filter has the data of pclass column of df
]

fig = px.sunburst(filtered_df, path=['pclass','sex','survived'],values='age',
            title='Survival by class and gender', width=500, height=500,
                template='plotly_dark', color='age', color_continuous_scale='RdBu',)
st.plotly_chart(fig)
st.markdown("This graph shows the survival rate of passengers by their class and gender")

survived_counts = filtered_df['survived'].value_counts()
fig = px.pie(names=survived_counts.index, values=survived_counts.values,
       title = 'Survival Rate', template='plotly_dark',
       width=500, height=500,)
st.plotly_chart(fig)

