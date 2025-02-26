import streamlit as st
import phonenumbers

st.title("Banquet Hall Booking")
st.write("Welcome to our banquet hall in Kachahari Road, Saharsa, Bihar! Please fill out the form below to book, call, email, or message us.")

# Booking Form
st.header("Booking Form")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
phone = st.text_input("Your Phone Number")
date = st.date_input("Event Date")
message = st.text_area("Additional Message")

if st.button("Submit Booking"):
    st.write(f"Thank you {name}! We have received your booking for {date}. We will contact you at {email} or {phone}.")

# Contact Options
st.header("Contact Us")
contact_method = st.selectbox("Choose a contact method", ["Call", "Email", "WhatsApp Message"])

if contact_method == "Call":
    st.write(f"Please call us at +91 92792 00748.")
elif contact_method == "Email":
    st.write(f"Please email us at utkarshraj27122010@gmail.com.")
elif contact_method == "WhatsApp Message":
    phone_number = "+919279200748"
    parsed_number = phonenumbers.format_number(phonenumbers.parse(phone_number, "IN"), phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    whatsapp_url = f"https://api.whatsapp.com/send?phone={parsed_number}&text=Hello%20Banquet%20Hall"
    st.write(f"Send us a message on WhatsApp: [Click Here]({whatsapp_url})")

st.write("Thank you for choosing our banquet hall!")
