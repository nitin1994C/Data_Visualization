import streamlit as st
import pandas as pd
import numpy as np



app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])
if app_mode == 'Home':
    st.title('LOAN PREDICTION :')
    st.image('isto.jpg')
    st.markdown('DataSet :')
    data = pd.read_csv('loan.csv')
    st.write(data.head())
    st.markdown('Applicant Income VS Loan Amount')
    st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))

elif app_mode == 'Prediction':
        st.image('bigst.jpg')
        st.subheader('Sir/Maam , YOU need to fill all necessary informations in order to get a reply to your loan request !')
        st.sidebar.header("Informations about the client :")
        gender_dict = {"Male":1,"Female":2}
        feature_dict = {"No":1,"Yes":2}
        edu={'Graduate':1,'Not Graduate':2}
        prop={'Rural':1,'Urban':2,'Semiurban':3}
        ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)
        CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)
        LoanAmount=st.sidebar.slider('LoanAmount in Lac',1.0,50.0,10.0)
        Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))
        Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))
        Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))
        Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))
        Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))
        Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])
        Education=st.sidebar.radio('Education',tuple(edu.keys()))
        Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))
        class_0 , class_3 , class_1,class_2 = 0,0,0,0
        if Dependents == '0':
                    class_0 = 1
        elif Dependents == '1':
                    class_1 = 1
        elif Dependents == '2' :
                    class_2 = 1
        else:        
                    class_3= 1    
                    Rural,Urban,Semiurban=0,0,0    
                    if Property_Area == 'Urban' :        
                        Urban = 1    
                    elif Property_Area == 'Semiurban' :        
                        Semiurban = 1   
                    else :        
                        Rural=1
