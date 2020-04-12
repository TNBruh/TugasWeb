from tkinter import *
from Component import *
from pymongo import *
from datetime import *

class ControlData:
    def __init__(self):
        self.name = ""

control = ControlData()

#Database Control
DB = Database()
try:
    users = DB.CreateCollection("Users")
    teams = DB.CreateCollection("Teams")
    tourns = DB.CreateCollection("Tournaments")
except:
    users = DB.GetCollection("Users")
    #for v in users.find({}):
    #    print(v)
    teams = DB.GetCollection("Teams")
    tourns = DB.GetCollection("Tournaments")

#for i in users.find({}):
    #print(i["_id"])

for i in tourns.find({}):
    print(i["_id"])

#Component Control
Login = ComponentLogin(DB, "Users", None, control)
MainMenu = ComponentMainMenu(DB, Login, None, None, control)
TeamMenu = ComponentUpdateTeam(DB, "Teams", MainMenu, control)
TournMenu = ComponentTournament(DB, ["Teams","Tournaments"], MainMenu, control)
Login.MainMenu = MainMenu
MainMenu.UpdateTeam = TeamMenu
MainMenu.Tourn = TournMenu

Login.Show()
#MainMenu.Show()
#TeamMenu.Show()
#TournMenu.Show()

#app.geometry("800x600")
app.mainloop()


