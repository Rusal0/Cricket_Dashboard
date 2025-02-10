import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class CricketTournamentDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Cricket Tournament Dashboard")

        self.boys_teams = []  # Initialize empty lists for teams
        self.girls_teams = []
        self.boys_matches = {}  # Dictionary to store match details
        self.girls_matches = {}

        self.create_team_entry_section("Boys Teams", self.boys_teams)
        self.create_team_entry_section("Girls Teams", self.girls_teams)

        self.create_schedule_section("Boys Schedule", self.boys_teams, self.boys_matches)
        self.create_schedule_section("Girls Schedule", self.girls_teams, self.girls_matches)

        self.create_match_update_section()  # Section for updating match results

    def create_team_entry_section(self, label_text, team_list):
        group = ttk.LabelFrame(self.master, text=label_text)
        group.pack(pady=10, padx=10, fill=tk.X)

        entry = tk.Entry(group)
        entry.pack(side=tk.LEFT)

        add_button = tk.Button(group, text="Add Team", command=lambda: self.add_team(entry, team_list))
        add_button.pack(side=tk.LEFT)

    def add_team(self, entry, team_list):
        team_name = entry.get()
        if team_name:
            team_list.append(team_name)
            entry.delete(0, tk.END)  # Clear the entry field
            print(f"{team_name} added to { 'Boys' if 'Boys' in entry.master.master.cget('text') else 'Girls'} Teams") #Confirmation message
        else:
            messagebox.showwarning("Warning", "Please enter a team name.")


    def create_schedule_section(self, label_text, team_list, matches):
        group = ttk.LabelFrame(self.master, text=label_text)
        group.pack(pady=10, padx=10, fill=tk.X)

        # Dropdown for date selection
        self.date_var = tk.StringVar(self.master) # Make date_var accessible
        dates = [ (datetime.date.today() + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)] # Example: Next 7 days
        self.date_var.set(dates[0]) # Set the default date
        date_dropdown = ttk.Combobox(group, textvariable=self.date_var, values=dates)
        date_dropdown.pack()

        schedule_button = tk.Button(group, text="Generate Schedule", command=lambda: self.generate_schedule(team_list, matches, label_text))
        schedule_button.pack()

        self.schedule_label = tk.Label(group, text="") # To display the schedule
        self.schedule_label.pack()

    def generate_schedule(self, team_list, matches, group_name):
        selected_date = self.date_var.get()
        if not team_list:
            self.schedule_label.config(text="No teams added yet.")
            return

        # Simple Round Robin for testing (Replace with Knockout for Boys)
        if "Boys" in group_name:
            matches.clear() # Clear existing matches before generating new ones
            num_teams = len(team_list)
            if num_teams < 2:
                self.schedule_label.config(text="Not enough teams for a match.")
                return
            
            # Generate Knockout matches (simplified)
            for i in range(0, num_teams, 2):
                if i+1 < num_teams: # Check for odd number of teams
                    match_id = f"Match {i//2 + 1}"  # Assign a unique ID
                    matches[match_id] = {"team1": team_list[i], "team2": team_list[i+1], "date": selected_date, "winner": None}
            
        else: # Girls matches (for now, same round robin)
            matches.clear()  # Clear existing matches
            for i in range(len(team_list)):
                for j in range(i + 1, len(team_list)):
                    match_id = f"Match {len(matches) + 1}"
                    matches[match_id] = {"team1": team_list[i], "team2": team_list[j], "date": selected_date, "winner": None}

        self.display_schedule(matches)

    def display_schedule(self, matches):
        schedule_text = ""
        for match_id, details in matches.items():
            schedule_text += f"{match_id}: {details['team1']} vs {details['team2']} ({details['date']})\n"
        self.schedule_label.config(text=schedule_text)

    def create_match_update_section(self):
        group = ttk.LabelFrame(self.master, text="Update Match Result")
        group.pack(pady=10, padx=10, fill=tk.X)

        self.match_id_entry = tk.Entry(group)
        self.match_id_entry.pack()

        self.winner_entry = tk.Entry(group)
        self.winner_entry.pack()

        update_button = tk.Button(group, text="Update Result", command=self.update_result)
        update_button.pack()

    def update_result(self):
        match_id = self.match_id_entry.get()
        winner = self.winner_entry.get()

        # Find the correct matches dictionary (Boys or Girls)
        matches_to_update = None
        for matches in [self.boys_matches, self.girls_matches]:
            if match_id in matches:
                matches_to_update = matches
                break

        if matches_to_update and winner:
            if match_id in matches_to_update:
                matches_to_update[match_id]["winner"] = winner
                print(f"{match_id} updated: Winner - {winner}")  # Confirmation message
                self.display_schedule(matches_to_update) # Refresh the schedule display
            else:
                messagebox.showwarning("Warning", "Invalid match ID.")
        else:
            messagebox.showwarning("Warning", "Please enter match ID and winner.")
        self.match_id_entry.delete(0, tk.END)
        self.winner_entry.delete(0, tk.END)


root = tk.Tk()
dashboard = CricketTournamentDashboard(root)
root.mainloop()
