import streamlit as st
from twilio.rest import Client

# Twilio credentials (replace with your own Account SID and Auth Token)
account_sid = 'ACb7b9fa71d46bd0ded58d0f0d0614ee43'
auth_token = '08ee0b2467787699d720ce20938381c2'
twilio_phone_number = '+17753414880'

client = Client(account_sid, auth_token)

# Streamlit UI
# st.title('Send SMS Using Twilio and Streamlit')

phone_number = st.text_input("Enter the recipient's phone number (with country code):")
message_text = st.text_area("Enter the message you want to send:")

if st.button('Send SMS'):
    if phone_number and message_text:
        try:
            # Send the message
            message = client.messages.create(
                body=message_text,
                from_=twilio_phone_number,
                to=phone_number
            )
            st.success(f"Message sent successfully to {phone_number}!")
        except Exception as e:
            st.error(f"Error sending message: {str(e)}")
    else:
        st.error("Please enter both phone number and message.")
