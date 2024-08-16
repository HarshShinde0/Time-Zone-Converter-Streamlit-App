import streamlit as st
from datetime import datetime
import pytz

# Mapping of time zones
time_zone_codes = {
    'UTC': 'UTC',
    'IST': 'Asia/Kolkata',
    'EST': 'America/New_York',
    'CST': 'America/Chicago',
    'MST': 'America/Denver',
    'PST': 'America/Los_Angeles',
    'BST': 'Europe/London',
    'CET': 'Europe/Paris',
    'JST': 'Asia/Tokyo',
    'AEST': 'Australia/Sydney',
    'NZST': 'Pacific/Auckland',
    'HST': 'Pacific/Honolulu',
    'ART': 'Africa/Cairo',
    'EET': 'Europe/Bucharest',
    'PHT': 'Asia/Manila',
    'KST': 'Asia/Seoul',
    'SGT': 'Asia/Singapore',
}

def convert_time(input_time, input_date, input_tz, output_tz):
   
    input_datetime = datetime.combine(input_date, input_time)
    
    
    localized_time = pytz.timezone(input_tz).localize(input_datetime)
    
    
    converted_time = localized_time.astimezone(pytz.timezone(output_tz))
    
    return converted_time

def main():
    st.title("Time Zone Converter")

    
    input_date = st.date_input("Select the date:", datetime.now().date())
    input_time = st.time_input("Select the time:", datetime.now().time())

   
    input_timezone = st.selectbox("Select the input timezone:", list(time_zone_codes.keys()))
    output_timezone = st.selectbox("Select the output timezone:", list(time_zone_codes.keys()))

    if st.button("Convert"):
        
        converted_time = convert_time(input_time, input_date, time_zone_codes[input_timezone], time_zone_codes[output_timezone])
        
        
        st.success(f"The time in {output_timezone} ({time_zone_codes[output_timezone]}) is: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")

   
    st.write("Developed by .hks")

if __name__ == "__main__":
    main()
