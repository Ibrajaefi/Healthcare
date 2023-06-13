import streamlit as st
import pandas as pd
import plotly.express as px
import random
import plotly.graph_objects as go
import plotly.io as pio
import hydralit_components as hc


# Datasets
data0 = pd.read_csv("master.csv")
data1 = pd.read_csv("suicide-rate-by-country-2023.csv")
data2 = pd.read_csv("number-with-each-mental-illness-country.csv")
data3 = pd.read_csv("psychiatrists-working-in-the-mental-health-sector.csv")
data4 = pd.read_csv("real-gdp-per-capita-PennWT.csv")
data5 = pd.read_csv("GDP_Suicide.csv")


########################
def gender():

    st.write("""
        The number of males that have commited suicides have exceeded that of the
        females by a very large margin. Difference in the male and female population might
        have a slight contribution to this. But still, the difference is huge
    """)
    malecount = data0.groupby('sex').get_group('male')['suicides_no'].sum()
    femalecount = data0.groupby('sex').get_group('female')['suicides_no'].sum()
    fig = px.bar(x=['Male','Female'],y=[malecount,femalecount],color=[malecount,femalecount],color_continuous_scale='Brwnyl')
    fig.update_layout(
        title='Gender vs Suicides',
        xaxis_title='Gender',
        yaxis_title='Number of Suicides'
    )
    st.plotly_chart(fig,use_container_width=True)


def generations():
    st.write("""
        The Boomer Generation has suffered the most from this problem, followed by the Silent
        Generation.
    """)
    fig = px.pie(data0,values='suicides_no',names='generation',color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig.update_layout(
        title='Distribution of deaths over different generations'   
    )
    st.plotly_chart(fig, use_container_width=True)

def age():
    st.write("""
        In terms of age groups, 35-54 years old individuals represent the majority of suicide cases followed by 55-74 years old group. 
    """)
    fig = px.pie(data0,values='suicides_no',names='age',color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig.update_layout(
        title='Distribution of deaths over different age groups'
    )
    st.plotly_chart(fig, use_container_width=True)
########################



# Group the data by country to calculate the total number of suicide cases
grouped_data = data0.groupby(["country"]).sum().reset_index()

# Create the interactive map
fig = px.choropleth(
    grouped_data,
    locations="country",
    locationmode="country names",
    color="suicides_no",
    hover_name="country",
    hover_data=["suicides_no"],
    color_continuous_scale=px.colors.sequential.Brwnyl,
    template="plotly_dark"  # Choose a template that suits your app's style
)

# Configure the map layout
fig.update_geos(
    showcountries=True, countrycolor="darkgray", showcoastlines=True, coastlinecolor="darkgray"
)
fig.update_layout(height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.set_page_config(layout='wide') 
####################################
# recommendations function 
def recommendations():
    st.title("What should be done about suicide?")
    st.subheader("Select to Expand")

    bullet_points = [
        "**Improve data collection and reporting**",
        "**Address stigma and cultural factors**",
        "**Strengthen healthcare infrastructure**",
        "**Targeted interventions for high-risk groups**",
        "**Increase the availability of mental health professionals**",
        "**Foster collaboration and knowledge sharing**"
    ]

    for bullet_point in bullet_points:
        if st.checkbox(bullet_point, key=bullet_point):
            if bullet_point == "**Improve data collection and reporting**":
                st.write("To address the lack of reliable data in developing countries, it is crucial to invest in building robust reporting systems for suicide cases. This can involve training healthcare professionals, implementing standardized reporting protocols, and raising awareness about the importance of accurate data collection.")
            elif bullet_point == "**Address stigma and cultural factors**":
                st.write("Stigma surrounding mental health and suicide can prevent individuals from seeking help and hinder accurate reporting. It is important to implement comprehensive awareness campaigns to combat stigma, educate communities about mental health, and promote open conversations about suicide.")
            elif bullet_point == "**Strengthen healthcare infrastructure**":
                st.write("Developing countries often face challenges with their healthcare infrastructure, which can impact the availability and accessibility of mental health services. Governments and organizations should prioritize investing in mental health infrastructure, including increasing the number of mental health professionals, establishing counseling centers, and integrating mental health services into primary healthcare systems.")
            elif bullet_point == "**Targeted interventions for high-risk groups**":
                st.write("Since men consistently have higher rates of suicide, it is essential to develop targeted interventions and support systems for men. This can involve promoting mental health awareness specifically tailored to men, providing accessible counseling services, and addressing the societal pressures and expectations that contribute to male suicide rates.")
            elif bullet_point == "**Increase the availability of mental health professionals**":
                st.write("The low number of psychiatrists in developing countries highlights the need to improve accessibility to mental health services. This can be done by training more mental health professionals, incentivizing psychiatrists to work in underserved areas, and utilizing technology-based solutions such as telemedicine to reach remote regions.")
            elif bullet_point == "**Foster collaboration and knowledge sharing**":
                st.write("International collaboration and knowledge sharing between countries can play a significant role in addressing the global issue of suicide. Sharing best practices, research findings, and successful intervention strategies can help countries learn from each other's experiences and implement effective suicide prevention measures.")
############################

import hydralit_components as hc

# Define menu data
menu_data = [
    {"label": "Introduction"},
    {"label": "Deeper Overview"},
    {"label": "Suicide & GDP/Capita"},
    {"label": "Mental Disorders"},
    {"label": "Recommendations"}
]


# Create navigation bar
menu_id = hc.nav_bar(menu_definition=menu_data, sticky_mode='sticky')


# Define page contents
if menu_id == "Introduction":
    st.title("Introduction")
    st.subheader('Suicide')
    st.write("""
        Suicide is a significant global concern, and early identification and intervention are crucial for its prevention. 
        According to the World Health Organization (WHO), 703,000 suicides globally were recorded in 2019, making it the 
        17th leading cause of death worldwide and the fourth leading cause of death among young people aged 15-29. 
        Furthermore, COVID-19 pandemic has exacerbated several risk factors associated with suicidal attempts and ideation. 
        By early April 2020, countries worldwide had put strict restrictions on the 
        movement of citizens to prevent the spread of the virus, with estimates indicating that one third of the global 
        population was affected by these measures. Due to pandemic economic and social toll,
        people around the world have been suffering from the impacts of the financial crisis but most significantly the mental 
        health issues linked to the overwhelming sense of loneliness and isolation.
    """)
    st.subheader('The Data')
    st.write("""
        The main dataset used in this analysis application is retrived from Kaggle https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016. 
        It is compiled dataset pulled from four other datasets linked by time and place, and was built to find signals correlated to
        increased suicide rates among different cohorts globally, across the socio-economic spectrum covering the time period between 1985 and 2016. 
        Additionally, several dataset related to suicide and mental illness have been used in this analysis. These datasets are mainly retrieved https://ourworldindata.org/ 
        & https://worldpopulationreview.com/
    """)
    st.subheader('Total Suicides by Country 1985-2016')
    st.write("""
        The map below shows the total number of suicide cases per country during the peirod of 1985 to 2016. The map shows no data for most developing 
        and third-world countries, indicating lack of data recording practices for suicide cases.
    """)
     
    st.plotly_chart(fig, use_container_width=True)


elif menu_id == "Suicide & GDP/Capita":
    st.title("Suicide Rates and GDP/Capita Analysis")
    st.subheader('Suicide Rates per 100K Indivisuals for the Year 2019')
    st.write("""
        Perhaps surprisingly, many of the most troubled nations in the world have comparatively low suicide rates. Afghanistan has 4.1 
        suicides per 100k; Iraq has 3.6, and Syria has just 2.0. It is not clear if the suicide statistics for these countries reflect
        suicides committed due to mental health problems and terminal illnesses(which are the primary reasons for suicide in most of the world) 
        or include suicides committed as part of the ongoing conflicts in these countries.
    """)
    def create_scatter_plot(data1, rate_column):
        fig = px.scatter(data1, x=rate_column, y="country", color="country",
                        labels={"country": "Country", rate_column: "Suicide Rate"},
                        template="plotly_dark")
        fig.update_layout(height=800, margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.update_traces(showlegend=False)
        # Increase dot size
        fig.update_traces(marker=dict(size=10))

    # Add jitter to separate overlapping dots
        jitter_amount = 0.2 
        random.seed(42)  
        for trace in fig.data:
            if trace.type == "scatter":
                trace.x = [x + random.uniform(-jitter_amount, jitter_amount) for x in trace.x]
        return fig
    

    # Create the dropdown menu for rate selection
    rate_options = ['both sexes', 'male', 'female']
    selected_rate = st.selectbox('Select Rate', rate_options)
    
    # Filter the data based on the selected rate
    filtered_data = data1[['country', selected_rate]]
    
    # Create the scatter plot
    fig = create_scatter_plot(filtered_data, selected_rate)
    st.plotly_chart(fig, use_container_width=True)


    st.subheader('GDP per Capita for the Year 2019')
    # Create a scatter plot using plotly
    fig10 = px.scatter(data5, x='GDP per capita', y='Suicide_Rate', title='GDP per capita vs. Suicide Rate',
                 labels={'GDP per capita': 'GDP per capita', 'Suicide_Rate': 'Suicide Rate'},
                 hover_data=['Country'] , color='GDP per capita', color_continuous_scale=px.colors.sequential.Burg)
    fig10.update_traces(marker=dict(size=8))
    st.plotly_chart(fig10, use_container_width=True)


elif menu_id == "Deeper Overview":
    st.title("Deeper Overview")
# Scatter Plot
    st.subheader("Sucide Rate per Country Each Year")
    # plot
    fig1 = px.scatter(data0,x='country',y='suicides/100k pop',animation_frame='year',size='suicides/100k pop',color='country')
    fig1.update_layout(
        xaxis={
            'showticklabels':False,
            'showgrid':False
        },
        yaxis_title='Number of Suicides per 100k'
    )
    st.plotly_chart(fig1, use_container_width=True)
# Timeseries
    st.subheader("Number of Suicides over the Years")
    grouped_data1 = data0[data0['year'] != 2016].groupby("year")['suicides_no'].sum().reset_index()
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=grouped_data1['year'],y=grouped_data1['suicides_no'],marker={'color':'#ede5cf'},mode='lines+markers',hovertext=grouped_data1['year'],hoverinfo='text'))
    fig2.update_layout(
        xaxis_title='Year',
        yaxis_title='Suicides',
        title='Suicides over the Years',
        yaxis=dict(
            range=[0, grouped_data1['suicides_no'].max()+50000],  # Set the y-axis range from 0 to the maximum value + 50,000
            tick0=0,  # Start the y-axis ticks at 0
            dtick=50000,  # Set the interval between ticks to 50,000
    )
    )
    st.plotly_chart(fig2,use_container_width=True)

    opt1 = st.selectbox(
        "Analyse Suicide Rate with ?",
        ('Gender',"Generations","Age")
    )   

    if opt1 == "Gender":
        gender()
    elif opt1 == "Generations":
        generations()
    elif opt1 == "Age":
        age()
    
elif menu_id == "Mental Disorders":
    st.title("Mental Disorders & Suicide")
    st.write("""
    We can see that total number of suicides (refer to Deeper View) and the number of people with mental illnesses are showing an upward trend over the 
    period 1990-2016 (the period common between the two). 
    This correlation is expected considering the direct link between suicidal ideation and mental disorders, especially anxiety and depression.
    """)

    # Create a list of available mental disorders, including "All"
    disorders = ['All', 'Anxiety', 'Depression', 'Schizophrenia', 'Bipolar', 'Eating_disorders']

    # Allow the user to select the mental disorder to display
    selected_disorder = st.selectbox('Select a mental disorder:', disorders)

    if selected_disorder == 'All':
        # Filter the data for all disorders and the country 'World'
        filtered_data = data2.loc[data2['Entity'] == 'World', ['Year'] + disorders[1:]]  # Exclude 'All' from the selected disorders

        # Group the filtered data by year and sum the values for all disorders
        grouped_data = filtered_data.groupby('Year')[disorders[1:]].sum().reset_index()

        # Create the line chart for all disorders
        line_chart = px.line(data_frame=grouped_data, x='Year', y=disorders[1:], labels={'value': 'Number of People'})

        # Display the chart
        st.plotly_chart(line_chart, use_container_width=True)

    else:
        # Filter the data based on the selected disorder and the country 'World'
        filtered_data = data2.loc[(data2['Entity'] == 'World') & (data2[selected_disorder].notnull()), ['Year', selected_disorder]]

        # Group the filtered data by year and sum the values for the selected disorder
        grouped_data = filtered_data.groupby('Year')[selected_disorder].sum().reset_index()

        # Create the line chart for the selected disorder
        line_chart = px.line(data_frame=grouped_data, x='Year', y=selected_disorder)

        # Display the chart
        st.plotly_chart(line_chart, use_container_width=True)
    st.subheader("Number of Psychiatrists per 100k Population")
    st.write("""
        It is evident that developing countries have the lowest number of psychiatrists, for example, 
        Yemen has 0.2 psychiatrists for every 100k population compared to 10.54 in the U.S. This can be seen as an indicator 
        of the level of accessibility to mental health services as well as the awareness of the importance of mental well-being. 
    """)
    fig6 = px.choropleth(data3,
                    locations="Country",
                    locationmode="country names",
                    color="Psychiatrists per 100k",
                    hover_name="Country",
                    hover_data=["Psychiatrists per 100k"],
                    color_continuous_scale=px.colors.sequential.Brwnyl,
                    template="plotly_dark")

    # Configure the map layout
    fig6.update_geos(showcountries=True,
                countrycolor="darkgray",
                showcoastlines=True,
                coastlinecolor="darkgray")
    fig6.update_layout(height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig6, use_container_width=True)

    # Add contents for page 3
elif menu_id == "Recommendations":
   recommendations()








    