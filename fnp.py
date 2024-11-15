import streamlit as st 
import numpy as np 
import pandas as pd
# import streamlit as st
# import streamlit_pydantic as sp
# from pydantic import BaseModel
import re

def function(corpus , s):
    l=[]
    for word in corpus:
        if s in word:
            l.append(word)
    return l

# @st.cache
def mail(s):
    pass
# data = {}


from twilio.rest import Client

# Twilio credentials (replace with your own Account SID and Auth Token)
account_sid = 'ACb7b9fa71d46bd0ded58d0f0d0614ee43'
auth_token = '08ee0b2467787699d720ce20938381c2'
twilio_phone_number = '+17753414880'

client = Client(account_sid, auth_token)

corpus = {"Bouquet" : "one.jpg", 'flowers': "top-view-beautiful-roses-bouquet-with-pink-ribbon.jpg", "cough syrup": "beautiful-roses-bouquet-indoors.jpg"}

try :
    st.set_page_config(layout = "wide")
    st.image(["head.jpg"], width = None)
    st.title("Raghav Bouquets")
    tab1 ,tab3 = st.tabs(["Menu" ,"Choose"])

    with tab1 :
        st.image(["one.jpg"],width =300,caption =["one"])
        pass

    with tab3:
        data = {}
        options = st.multiselect("Choose products :",corpus.keys())
        # st.write(options)
        # st.write(type(options))
        for i in range(len(options)):
            if options[i] in corpus.keys():
                
                st.image([corpus[options[i]]] , width = 200,caption =[options[i]] )
                value = st.text_input("How many do you want to buy ?",key = i)
                data[options[i]] = value
        if st.button('Order') :
            try:
                # Send the message
                message = client.messages.create(
                    body = str(data),
                    from_ = twilio_phone_number,
                    to = '+919399607245',
                )
                st.success(f"Message sent successfully!")
            except Exception as e:
                pass
                st.error(f"Error sending message: {str(e)}")

            
        
except Exception as e :
    print(e)
    raise e