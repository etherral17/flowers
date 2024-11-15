import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, message, to_email):
    # Sender email and password
    sender_email = "etherral17@gmail.com"  # Replace with your email address
    sender_password = "nuwezxexhhxwstbn "  # Replace with your email password or app-specific password
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = 'etherral17@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message content
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login
        server.sendmail(sender_email, to_email, msg.as_string())  # Send the email
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title('Send Email from Streamlit App')

# Input fields
user_name = st.text_input("Your Name")
user_email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Recipient email (the email that will receive the message)
recipient_email = "rattzsengar02@gmail.com"  # Replace with the email address you want to send to

if st.button("Send Email"):
    if user_name and user_email and message:
        # Compose the email details
        subject = f"Message from {user_name} via Streamlit"
        full_message = f"Name: {user_name}\nEmail: {user_email}\nMessage:\n{message}"
        
        # Send the email
        result = send_email(subject, full_message, recipient_email)
        st.success(result)
    else:
        st.error("Please fill in all the fields.")
