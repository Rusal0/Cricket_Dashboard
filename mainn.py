import streamlit as st
import pandas as pd
from datetime import datetime, date

# Sample match data (replace with your actual data)
match_data = {
    'Date': ['2024-03-10', '2024-03-10', '2024-03-11', '2024-03-11', '2024-03-12'],
    'Time': ['10:00 AM', '2:00 PM', '11:00 AM', '3:00 PM', '1:00 PM'],
    'Team 1': ['Team A', 'Team C', 'Team B', 'Team D', 'Team A'],
    'Team 2': ['Team B', 'Team D', 'Team A', 'Team C', 'Team C'],
    'Venue': ['Ground 1', 'Ground 2', 'Ground 1', 'Ground 2', 'Ground 1'],
    'Result': ['', '', '', '', ''],  # Add results as the tournament progresses
}

df = pd.DataFrame(match_data)
df['Date'] = pd.to_datetime(df['Date']) # Convert 'Date' column to datetime objects


st.title("Cricket Tournament Dashboard")

# Date Filter
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
selected_date = st.date_input("Select Date", min_value=min_date, max_value=max_date, value=min_date)

# Convert the selected date to datetime for filtering
selected_datetime = datetime.combine(selected_date, datetime.min.time())



# Filtering the DataFrame based on the selected date
filtered_df = df[df['Date'].dt.date == selected_date]



if not filtered_df.empty:
    st.subheader(f"Matches on {selected_date.strftime('%Y-%m-%d')}")  # Display the selected date

    # Display matches in a table
    st.dataframe(filtered_df[['Time', 'Team 1', 'Team 2', 'Venue', 'Result']],  # Displaying the required columns
                 column_config={
                     "Result": st.column_config.ColumnConfig(
                         "Result",
                         width="medium",
                         # Add a selectbox for updating results (if needed)
                         # You'll need more logic to save these results
                         # e.g., using a session state or writing to a file.
                     )
                 },
                 )

else:
    st.write(f"No matches scheduled on {selected_date.strftime('%Y-%m-%d')}")



# --- Overall Tournament Schedule (Optional) ---
st.subheader("Overall Tournament Schedule")
st.dataframe(df[['Date', 'Time', 'Team 1', 'Team 2', 'Venue', 'Result']])  # Display all matches



# --- Add more features as needed ---
# For example:
# - Team standings
# - Top scorers
# - Graphs and charts
# - Admin panel to update match results (requires more complex state management)
