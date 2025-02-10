import streamlit as st
import datetime

class CricketTournamentDashboard:
    def __init__(self):
        self.boys_teams = []
        self.girls_teams = []
        self.boys_matches = {}
        self.girls_matches = {}

    def display_teams(self, team_list, team_type):
        st.subheader(f"{team_type} Teams")
        for team in team_list:
            st.write(team)

    def add_team(self, team_name, team_list, team_type):
        if team_name:
            team_list.append(team_name)
            st.success(f"{team_name} added to {team_type} Teams")
        else:
            st.warning("Please enter a team name.")

    def display_schedule(self, matches):
        for match_id, details in matches.items():
            st.write(f"{match_id}: {details['team1']} vs {details['team2']} ({details['date']})  Winner: {details.get('winner', 'TBD')}") #Show Winner or TBD

    def generate_schedule(self, team_list, matches, group_name, selected_date):
        if not team_list:
            st.warning("No teams added yet.")
            return

        if "Boys" in group_name:
            matches.clear()
            num_teams = len(team_list)
            if num_teams < 2:
                st.warning("Not enough teams for a match.")
                return

            for i in range(0, num_teams, 2):
                if i + 1 < num_teams:
                    match_id = f"Match {i // 2 + 1}"
                    matches[match_id] = {"team1": team_list[i], "team2": team_list[i + 1], "date": selected_date, "winner": None}

        else:  # Girls matches (round robin)
            matches.clear()
            for i in range(len(team_list)):
                for j in range(i + 1, len(team_list)):
                    match_id = f"Match {len(matches) + 1}"
                    matches[match_id] = {"team1": team_list[i], "team2": team_list[j], "date": selected_date, "winner": None}

        self.display_schedule(matches)

    def update_result(self, match_id, winner, matches):
        if match_id in matches and winner:
            matches[match_id]["winner"] = winner
            st.success(f"{match_id} updated: Winner - {winner}")
            self.display_schedule(matches)  # Refresh the schedule
        else:
            st.warning("Invalid match ID or winner.")


# Streamlit app
st.title("Cricket Tournament Dashboard")

dashboard = CricketTournamentDashboard()

# Boys Teams
boys_team_col, boys_schedule_col = st.columns(2)  # Two columns for layout

with boys_team_col:
    st.subheader("Boys Teams")
    boys_team_input = st.text_input("Enter Boys Team Name:")
    if st.button("Add Boys Team"):
        dashboard.add_team(boys_team_input, dashboard.boys_teams, "Boys")
    dashboard.display_teams(dashboard.boys_teams, "Boys")

with boys_schedule_col:
    st.subheader("Boys Schedule")
    boys_date = st.date_input("Select Date for Boys Matches")
    if st.button("Generate Boys Schedule"):
        dashboard.generate_schedule(dashboard.boys_teams, dashboard.boys_matches, "Boys", boys_date.strftime("%Y-%m-%d"))
    dashboard.display_schedule(dashboard.boys_matches)

    st.subheader("Update Boys Match Result")
    boys_match_id = st.text_input("Boys Match ID:")
    boys_winner = st.text_input("Boys Winner:")
    if st.button("Update Boys Result"):
        dashboard.update_result(boys_match_id, boys_winner, dashboard.boys_matches)


# Girls Teams (similar structure)
girls_team_col, girls_schedule_col = st.columns(2)

with girls_team_col:
    st.subheader("Girls Teams")
    girls_team_input = st.text_input("Enter Girls Team Name:")
    if st.button("Add Girls Team"):
        dashboard.add_team(girls_team_input, dashboard.girls_teams, "Girls")
    dashboard.display_teams(dashboard.girls_teams, "Girls")

with girls_schedule_col:
    st.subheader("Girls Schedule")
    girls_date = st.date_input("Select Date for Girls Matches")
    if st.button("Generate Girls Schedule"):
        dashboard.generate_schedule(dashboard.girls_teams, dashboard.girls_matches, "Girls", girls_date.strftime("%Y-%m-%d"))
    dashboard.display_schedule(dashboard.girls_matches)

    st.subheader("Update Girls Match Result")
    girls_match_id = st.text_input("Girls Match ID:")
    girls_winner = st.text_input("Girls Winner:")
    if st.button("Update Girls Result"):
        dashboard.update_result(girls_match_id, girls_winner, dashboard.girls_matches)
