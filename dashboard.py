import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit.logger import DEFAULT_LOG_MESSAGE

# st.markdown(
#         f"""
# <style>
#     .reportview-container .main .block-container{{
#         max-width: 80%;
#         padding-right: 5rem;
#         padding-left: 20rem;
#     }}
#     .reportview-container .main {{
        
#     }}
# </style>
# """,
#         unsafe_allow_html=True,
#     )

st.set_page_config(layout="wide")

def df_read(select):
    reg_30="dashboard_export/India/last30DaysRegistration.csv"
    global df_reg30,df_cov,df_rurban,df_aefi,df_age,df_byage,df_detail,df_dose
    df_reg30 = pd.read_csv(reg_30)
    
    cov="dashboard_export/{}/DistrictWiseVaccinationCoverage.csv".format(select)
    df_cov = pd.read_csv(cov)

    rurban="dashboard_export/{}/VaccinationByCategory.csv".format(select)
    df_rurban = pd.read_csv(rurban)

    aefi="dashboard_export/{}/last30DaysAefiReported.csv".format(select)
    df_aefi = pd.read_csv(aefi)

    age="dashboard_export/{}/vaccinationByAge.csv".format(select)
    df_age = pd.read_csv(age)
    
    byage="dashboard_export/{}/weeklyAgeWiseVaccination.csv".format(select)
    df_byage = pd.read_csv(byage)

    detail="dashboard_export/{}/DistrictWiseVaccination.csv".format(select)
    df_detail = pd.read_csv(detail)

    dose="dashboard_export/{}/WeeklyVaccination.csv".format(select)
    df_dose = pd.read_csv(dose)



st.title("Covid Vaccination Dashboard")
st.sidebar.title("Covid Vaccination Dashboard")
st.markdown("This application is a Covid Vaccination dashboard to visualize the statistics of Innoculations being carried out throughout the country")
st.sidebar.markdown("This application is a Covid Vaccination dashboard to visualize the statistics of Innoculations being carried out throughout the country")

#st.sidebar.title("States")
select = st.sidebar.selectbox('State', ['India', 'Punjab', 'Haryana', 'Chandigarh' ], key='1')
selectlabels=['India','Punjab', 'Haryana', 'Chandigarh']

if not st.sidebar.checkbox("Hide", False, key='1'):
    if select in selectlabels:

        df_read(select)
        title_1="State Data for {}".format(select)
        st.title(title_1)


        if not st.checkbox("Hide", False, key='107'):
                                    
            st.header("Vaccination Trends")
            
            if select == 'India':
                bylabel=["By Age","By Doses"]
                byradio=st.radio('',bylabel)
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                if byradio == 'By Age':
                    df=df_byage
                    set1 = { 'x': df.label, 'y': df.total, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'cyan','shape': 'spline',  'smoothing': 1.3 },'name': 'total','fill':'tonexty'}
                    set2 = { 'x': df.label, 'y': df.vac_18_45, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'seagreen','shape': 'spline',  'smoothing': 1.3 },'name': '18-44','fill':'tonexty'}
                    set3 = { 'x': df.label, 'y': df.vac_45_60, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'yellow','shape': 'spline',  'smoothing': 1.3 },'name': '45-60','fill':'tonexty'}
                    set4 = { 'x': df.label, 'y': df.vac_60_above, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'red','shape': 'spline',  'smoothing': 1.3 },'name': '60 Above','fill':'tonexty'}
                    data = [set4, set3, set2, set1]
                    fig = go.Figure(data=data)
                    st.plotly_chart(fig)
                
                
                elif byradio == 'By Doses':
                    df=df_dose
                    set1 = { 'x': df.label, 'y': df.total, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'cyan','shape': 'spline',  'smoothing': 1.3 },'name': 'Total Doses','fill':'tonexty'}
                    set2 = { 'x': df.label, 'y': df.dose1, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'seagreen','shape': 'spline',  'smoothing': 1.3 },'name': 'Dose 1','fill':'tonexty'}
                    set3 = { 'x': df.label, 'y': df.dose2, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'yellow','shape': 'spline',  'smoothing': 1.3 },'name': 'Dose 2','fill':'tonexty'}                
                    data = [set3, set2, set1]
                    fig = go.Figure(data=data)
                    st.plotly_chart(fig)
            else:
                txt1="Cummulative Vaccination Data for {}".format(select)
                st.header(txt1)
                df=df_dose
                set1 = { 'x': df.label, 'y': df.total, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'cyan','shape': 'spline',  'smoothing': 1.3 },'name': 'Total Doses','fill':'tonexty'}
                set2 = { 'x': df.label, 'y': df.dose1, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'seagreen','shape': 'spline',  'smoothing': 1.3 },'name': 'Dose 1','fill':'tonexty'}
                set3 = { 'x': df.label, 'y': df.dose2, 'type': 'scatter', 'mode': 'lines+markers', 'line': { 'width': 1, 'color': 'yellow','shape': 'spline',  'smoothing': 1.3 },'name': 'Dose 2','fill':'tonexty'}                
                data = [set3, set2, set1]
                fig = go.Figure(data=data)
                st.plotly_chart(fig)

        # if not st.checkbox("Hide", False, key='106'):                        
        #     st.header("Vaccination - Category")

        if not st.checkbox("Hide", False, key='105'):                        
            st.header("Vaccination by Age")
            df=df_age
            labels=["18-44","45-60","Above 60"]
            values=[df.iat[0,0],df.iat[0,1],df.iat[0,2]]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values)])                 
            st.plotly_chart(fig)


        if not st.checkbox("Hide", False, key='110'):                        
            st.header("Vaccination by States/Districts")
            df=df_detail
            st.dataframe(df)

        if not st.checkbox("Hide", False, key='104'):                        
            st.header("Reported AEFI")
            df=df_aefi
            set1 = { 'x': df.vaccine_date, 'y': df.aefi, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' ,'shape': 'spline',  'smoothing': 1.3},'name': 'Total','fill':'tonexty'}
            data = [set1]
            fig = go.Figure(data=data)
            st.plotly_chart(fig)   

            
        if not st.checkbox("Hide", False, key='103'):                        
            st.header("Rural Vs Urban Trend")
            df=df_rurban
            set1 = { 'x': df.vaccine_date, 'y': df.rural, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' ,'shape': 'spline',  'smoothing': 1.3},'name': 'Rural','fill':'tonexty'}
            set2 = { 'x': df.vaccine_date, 'y': df.urban, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green','shape': 'spline',  'smoothing': 1.3 },'name': 'Urban','fill':'tonexty'}
            data = [set2, set1]
            fig = go.Figure(data=data)
            st.plotly_chart(fig)
            
               
        if not st.checkbox("Hide", False, key='102'):                        
            st.header("Vaccination Coverage")
            df = df_cov

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df.title,
                y=df.partial_vaccinated,
                name='Dose 1',
                marker_color='#330C73',
                opacity=0.75
            ))
            fig.add_trace(go.Bar(
                x=df.title,
                y=df.totally_vaccinated,
                name='Dose 2', # name used in legend and hover labels
                marker_color='#EB89B5',
                opacity=0.75
            ))
            

            fig.update_layout(
                barmode='group',
                title_text='Sampled Results', # title of plot
                xaxis_title_text='State/District', # xaxis label
                yaxis_title_text='Count', # yaxis label
                bargap=0.2, # gap between bars of adjacent location coordinates
                bargroupgap=0.1 # gap between bars of the same location coordinates
            )

            st.plotly_chart(fig)  
    if not st.checkbox("Hide", False, key='101'):                        
        st.header("30-day Registration Data - Pan India")
        df=df_reg30
        set1 = { 'x': df.reg_date, 'y': df.total, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' ,'shape': 'spline',  'smoothing': 1.3},'name': 'total','fill':'tonexty'}
        set2 = { 'x': df.reg_date, 'y': df.age18, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' ,'shape': 'spline',  'smoothing': 1.3},'name': '18-44','fill':'tonexty'}
        set3 = { 'x': df.reg_date, 'y': df.age45, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow','shape': 'spline',  'smoothing': 1.3 },'name': '45-60','fill':'tonexty'}
        set4 = { 'x': df.reg_date, 'y': df.age60, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black','shape': 'spline',  'smoothing': 1.3 },'name': '60 Above','fill':'tonexty'}
        data = [set4, set3, set2, set1]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)


   


