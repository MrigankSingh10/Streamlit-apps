import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


add_selectbox1=st.sidebar.selectbox(
    'Choose the dataset',
    ('None','Students Performance','Titanic')
)
#adding a selectbox to sidebar
add_selectbox=st.sidebar.selectbox(
    'How would you like to contact me?',
    ('Email','Home Phone','Mobile Phone')
)

if add_selectbox=='Email':
    st.sidebar.markdown('mrigank2303239gmail.com') 
if add_selectbox=='Mobile Phone':
    st.sidebar.markdown('8340720530')
if add_selectbox=='Home Phone':
    st.sidebar.markdown('7274913161')


if add_selectbox1=='None':
    st.header('Welcome to my Data Visualisation page')
    st.write('Choose a dataset from the sidebar to get a detailed analysis')


if add_selectbox1=='Students Performance':
    st.header('Students Performance Data')
    @st.cache
    def load_data(path ='StudentsPerformance.csv'):
        df = pd.read_csv(path)
        df.gender[df.gender == 'male'] = 1
        df.gender[df.gender == 'female'] = 2
        df['test preparation course'][df['test preparation course']=='none']=0
        df['test preparation course'][df['test preparation course']=='completed']=1
    
        return df

    df = load_data()
    st.write(df)



    op = st.checkbox('show info')
    if op:
        st.write('1. For male and 2. For Female')
        st.write('1. For completed test prep course and 0 For not')

    st.markdown('## The distribution of maths marks on the dataset')
    df['math score'].plot(figsize=(10,5))
    st.pyplot()


    st.markdown('## The plot for reading and math scores')
    x=df['reading score']
    y=df['math score']
    fig=plt.scatter(x,y,)
    fig=plt.xlabel('Reading score')
    fig=plt.ylabel('math score')
    st.pyplot()
    st.write('The above plot shows that most students have their reading and math scores nearly equal')


    st.markdown('## The plot for reading and writing scores')
    y=df['reading score']
    x=df['writing score']
    fig=plt.scatter(x,y,)
    fig=plt.ylabel('Reading score')
    fig=plt.xlabel('writing score')
    st.pyplot()
    st.write('The above plot shows that the rreading and writing scores are also same for most students')

    st.markdown('## The plot for Reading, Writing and Math scores')
    fig = px.scatter_3d(data_frame=df,x='reading score',y='writing score', z='math score',color='test preparation course',width=600,height=600)
    st.plotly_chart(fig,use_container_width=True)
    st.write('This shows that students who completed the test prep course atleast got a decent marks and also were the top performers')

    st.markdown('## Conclusion')
    st.write('It is clear from the above graphs that the mostly the students lied in the average category of the marks and showed similar marks for all the three tests')
    st.write('Also we can state that the test helped some of the brilliant stdents to be on top performers list but for most of the students it was not much of help becaause the students mostly got an average marks even taking the test prep course.')

if add_selectbox1=='Titanic':
    st.header('Titanic Dataset')
    st.write('This dataset is a sample dataset for the passengers on the titanic when it hit an iceburg and submerged into the ocean')
    @st.cache
    def load_data(path ='titanic_train.csv'):
        df = pd.read_csv(path)
        return df

    df = load_data()
    st.write(df)

    st.markdown('## Male VS Female Passengers Who Survived')
    fig=sns.barplot(x="Sex", y="Survived", data=df)
    st.pyplot()
    fm=df["Survived"][df["Sex"] == 'male'].value_counts(normalize = True)[1]*100
    ml=df["Survived"][df["Sex"] == 'female'].value_counts(normalize = True)[1]*100
    st.write('The number of female passengers who survived:',fm)
    st.write('The number of male passengers who survived:',ml)

    st.markdown('## Survival in different Pclasses')
    sns.barplot(x="Pclass", y="Survived", data=df, hue='Sex')
    st.pyplot()
    p1=df["Survived"][df["Pclass"] == 1].value_counts(normalize = True)[1]*100
    p2=df["Survived"][df["Pclass"] == 2].value_counts(normalize = True)[1]*100
    p3=df["Survived"][df["Pclass"] == 1].value_counts(normalize = True)[1]*100
    st.write('The percetage of Pclass 1 people who survived', p1)
    st.write('The percetage of Pclass 2 people who survived', p2)
    st.write('The percetage of Pclass 3 people who survived', p3)


    st.markdown('## Survival VS Sibsp Bar Plot')
    sns.barplot(x="SibSp", y="Survived", data=df,palette='spring')
    st.pyplot()
    s0=df["Survived"][df["SibSp"] == 0].value_counts(normalize = True)[1]*100
    s1=df["Survived"][df["SibSp"] == 1].value_counts(normalize = True)[1]*100
    s2=df["Survived"][df["SibSp"] == 2].value_counts(normalize = True)[1]*100
    s3=df["Survived"][df["SibSp"] == 3].value_counts(normalize = True)[1]*100
    s4=df["Survived"][df["SibSp"] == 4].value_counts(normalize = True)[1]*100
    st.write('Percentage of SibSp = 0 who survived:',s0)
    st.write('Percentage of SibSp = 1 who survived:',s1)
    st.write('Percentage of SibSp = 2 who survived:',s2)
    st.write('Percentage of SibSp = 3 who survived:',s3)
    st.write('Percentage of SibSp = 4 who survived:',s4)

    #draw a bar plot for Parch vs. survival
    st.markdown('## Survival VS Parch Bar Plot')
    sns.barplot(x="Parch", y="Survived", data=df)
    st.pyplot()


    st.markdown('## Conclusion')
    st.write('The number of female passengers were more who survived the disaster. There were no direct effects of Pclass or Parch but definetely percentage of Subsp=1 were more for survival than the other Sibsp.')
