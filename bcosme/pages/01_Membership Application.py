import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.title(":blue[Bulawayo Chamber OF SMEs Membership Application]", help="Use this submit to fill the information needed and submit")
st.divider()
st.write(":orange[EMPOWERING ZIMBABWE SMALL & MEDIUM ENTERPRISES FOR GLOBAL COMPOTETIVENESS]")
st.toast("Bulawayo Chamber OF SMEs Membership Application",icon="🧵")
# Part A - Ownership of business
long_text = "Lorem ipsum. " * 1000
with st.container(border=True,height=500):
    st.write(":orange[Ownership of Business]")
    st.divider()
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ["Male", "Female"])
    phone_number = st.number_input("Phone Number", step=1)
    address = st.text_input("Current Address")
    cities_in_zimbabwe = ["Bulawayo", "Harare", "Gweru", "Mutare", "Kwekwe", "Masvingo", "Victoria Falls", "Hwange", "Chinhoyi", "Chegutu", "Kadoma"]
    city = st.selectbox("City", cities_in_zimbabwe)
    id_number = st.text_input("ID Number")
    email = st.text_input("Email Address")
    business_type = st.multiselect("Type of Business", ["Sole Trader", "Partnership", "Trust", "PBC", "Limited Company", "Association"])
    position = st.text_input("Position in Business")
    business_duration = st.text_input("How long have you been in business?")

# Business Details
    st.write(":orange[Business Details]")
    st.divider()
    business_name = st.text_input("Business Name")
    business_address = st.text_input("Business Address")
    business_duration_at_address = st.text_input("How long at this address?")
    zimbabwean_cities_and_towns = ["Bulawayo", "Harare", "Gweru", "Mutare", "Kwekwe", "Masvingo", "Victoria Falls", "Hwange", "Chinhoyi", "Chegutu", "Kadoma"]
    business_city = st.selectbox("Zimbabwean Cities and Towns", zimbabwean_cities_and_towns)
    mobile_number = st.number_input("Mobile Number", step=1)
    business_phone = st.number_input("Business Phone Number", step=1)
    industry = st.text_input("Industry")
    num_directors = st.slider("Number of Directors", min_value=1, max_value=20, step=1)
    num_employees = st.slider("Number of Employees", min_value=1, max_value=50, step=1)
    incorporation_date = st.date_input("Year of Incorporation")
    main_activity = st.text_area("Main Business Activity")
    products_services = st.text_area("Details of Products or Services")
    registered_office = st.text_input("Registered Office Address")
    licenses = st.multiselect("Company is Licensed with", ["ZIMRA", "NSSA", "PRAZ", "City Council", "Other"])
    is_exporter = st.radio("Are you an Exporter?", ["Yes", "No"])

# Member Card Details
    st.write(":orange[Member Card Details]")
    st.divider()
    require_id_card = st.radio("Do you require a membership ID card?", ["Yes", "No"])
    if require_id_card == "Yes":
        card_name = st.text_input("Full Name on ID")
        card_id_number = st.text_input("National ID Number")
        card_association = st.text_input("Association (if any)")
        card_industry = st.text_input("Business Industry")
        card_number = st.text_input("Card Number")

# Contact

    st.write(":orange[Contact]")
    contact_name = st.text_input("Contact Name")
    contact_email = st.text_input("Contact Email Address")
    contact_phone = st.number_input("Contact Phone Number")

# Additional Business Information
    st.write(":orange[Additional Business Information]")
    has_insurance = st.radio("Do you have current insurance cover?", ["Yes", "No"])
    business_assets_value = st.number_input("Estimated Value of Business Assets")
    expected_from_bcsme = st.text_area("What do you expect most from BCSME?")

# Partner/Director Details
    st.write(":orange[Partner/Director Details]")
    st.divider()
    director_data = []
    for i in range(1, 5):
        st.subheader(f"Director {i}")
        director_name = st.text_input(f"Name {i}")
        director_id = st.text_input(f"ID Number {i}")
        director_address = st.text_input(f"Home Address {i}")
        director_dob = st.date_input(f"Date of Birth {i}")
        director_gender = st.selectbox(f"Gender {i}", ["Male", "Female"])
        director_data.append({
        "Name": director_name,
        "ID Number": director_id,
        "Home Address": director_address,
        "Date of Birth": director_dob,
        "Gender": director_gender
    })

# Submit button
    if st.button("Submit Application"):
    # Create a dictionary with the form data
     form_data = {
        "Name": name,
        "Date of Birth": dob,
        "Gender": gender,
        "Phone Number": phone_number,
        "Current Address": address,
        "City": city,
        "ID Number": id_number,
        "Email Address": email,
        "Type of Business": ", ".join(business_type),
        "Position in Business": position,
        "How long in business": business_duration,
        "Business Name": business_name,
        "Business Address": business_address,
        "How long at this address": business_duration_at_address,
        "Business City": business_city,
        "Mobile Number": mobile_number,
        "Business Phone Number": business_phone,
        "Industry": industry,
        "Number of Directors": num_directors,
        "Number of Employees": num_employees,
        "Year of Incorporation": incorporation_date,
        "Main Business Activity": main_activity,
        "Details of Products or Services": products_services,
        "Registered Office Address": registered_office,
        "Licenses": ", ".join(licenses),
        "Exporter": is_exporter,
        "Require ID Card": require_id_card,
        "Full Name on ID": card_name,
        "National ID Number": card_id_number,
        "Association": card_association,
        "Business Industry": card_industry,
        "Card Number": card_number,
        "Contact Name": contact_name,
        "Contact Email": contact_email,
        "Contact Phone": contact_phone,
        "Have Insurance": has_insurance,
        "Estimated Value of Business Assets": business_assets_value,
        "Expected from BCSME": expected_from_bcsme
    }

    # Combine the form data with the director data
     form_data.update({"Director " + str(i+1): str(director) for i, director in enumerate(director_data)})

    # Add a timestamp
     form_data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a Pandas DataFrame from the form data
     df = pd.DataFrame([form_data])

    # Save the DataFrame to an Excel file
     df.to_excel("bcosme/databases/bulawayo_chamber_smes_application.xlsx", index=False)

     st.success("Your application has been submitted and saved to the Database.")