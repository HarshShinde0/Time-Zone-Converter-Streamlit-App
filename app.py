import streamlit as st
from datetime import datetime
import pytz

def convert_time(input_time, input_date, input_tz, output_tz):
    # Combine date and time into a datetime object
    input_datetime = datetime.combine(input_date, input_time)
    
    # Localize the input datetime to the input timezone
    localized_time = pytz.timezone(input_tz).localize(input_datetime)
    
    # Convert to the output timezone
    converted_time = localized_time.astimezone(pytz.timezone(output_tz))
    
    return converted_time

def main():
    st.title("Time Zone Converter")
    
    # Select input date and time
    input_date = st.date_input("Select the date:", datetime.now().date())
    input_time = st.time_input("Select the time:", datetime.now().time())
    
    # Select input and output timezones
    input_timezone = st.selectbox("Select the input timezone:", pytz.all_timezones)
    output_timezone = st.selectbox("Select the output timezone:", pytz.all_timezones)
    
    if st.button("Convert"):
        # Perform the conversion
        converted_time = convert_time(input_time, input_date, input_timezone, output_timezone)
        
        # Display the result
        st.success(f"The time in {output_timezone} is: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Footer
    st.write("Developed by .hks")

if __name__ == "__main__":
    main()
