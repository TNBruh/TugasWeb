from tkinter import *
from Model import *
from pymongo import *
from datetime import *

global app
app = Tk()

class ComponentLogin:
    def __init__(self, inpdbObj, inpC, inpMainMenu, inpControl):
        #DB
        self.dbObj = inpdbObj
        self.coll = inpC
        self.MainMenu = inpMainMenu
        self.control = inpControl
        #Login Title
        self.login_label = Label(app, text = "Login or Register", font = 18)
        self.login_label.grid(row = 0, column= 0, sticky = W, columnspan = 2)
        #Name
        self.name_label = Label(app, text = "Name", font = 18)
        self.name_label.grid(row = 1, column = 0, sticky = W)
        self.name_inp = StringVar()
        self.name_entry = Entry(app, textvariable = self.name_inp)
        self.name_entry.grid(row = 1, column = 1)
        #Password
        self.pw_label = Label(app, text = "Password", font = 18)
        self.pw_label.grid(row = 2, column = 0, sticky = W)
        self.pw_inp = StringVar()
        self.pw_entry = Entry(app, textvariable = self.pw_inp)
        self.pw_entry.grid(row = 2, column = 1)
        #Login Button
        self.login_button = Button(app, text = "Login", width = 20, height = 2, command = self.Login)
        self.login_button.grid(row = 3, column = 0, columnspan = 2)
        #Register Button
        self.reg_button = Button(app, text = "Register", width = 20, height = 2, command = self.Register)
        self.reg_button.grid(row = 4, column = 0, columnspan = 2)
        #Hide
        self.Hide()

    def Hide(self):
        self.login_label.grid_remove()
        self.name_label.grid_remove()
        self.name_entry.grid_remove()
        self.pw_label.grid_remove()
        self.pw_entry.grid_remove()
        self.login_button.grid_remove()
        self.reg_button.grid_remove()

    def Show(self):
        app.geometry("240x190")
        self.login_label.grid()
        self.name_label.grid()
        self.name_entry.grid()
        self.pw_label.grid()
        self.pw_entry.grid()
        self.login_button.grid()
        self.reg_button.grid()

    def Register(self):
        self.dbObj.AddUser(self.coll, self.name_entry.get(), self.pw_entry.get())
        #print(self.dbObj.GetCollection(self.coll).find())

    def Login(self):
        target = self.dbObj.GetCollection(self.coll).find_one(self.name_entry.get())
        if (target != None):
            if (target["Password"] == self.pw_entry.get()):
                #print(self.dbObj.GetCollection(self.coll).find())
                self.Hide()
                self.MainMenu.Show()
                self.control.name = self.name_entry.get()
            else:
                print("bruv")
        else:
            print("bruh")

class ComponentMainMenu:
    def __init__(self, inpdbObj, inpLogin, inpUpdateTeam, inpTourn, inpControl):
        #DB
        self.dbObj = inpdbObj
        self.UpdateTeam = inpUpdateTeam
        self.Tourn = inpTourn
        self.control = inpControl
        self.Log = inpLogin
        #Update Team
        self.updateTMenu = Button(app, text = "Update Team", width = 13,padx = 150, pady = 13, command = self.EnterUpdateTeam)
        self.updateTMenu.grid(row = 0, column = 0,sticky = N)
        #Manage Tournament
        self.manageTourn = Button(app, text = "Manage Tournament", width = 13,padx = 150, pady = 13, command = self.EnterTourn)
        self.manageTourn.grid(row = 1, column = 0, sticky = N)
        #Logout
        self.logout = Button(app, text = "Logout", width = 13,padx = 150, pady = 13, command = self.Logout)
        self.logout.grid(row = 2, column = 0, sticky = N)
        #Hide
        self.Hide()

    def Hide(self):
        self.updateTMenu.grid_remove()
        self.manageTourn.grid_remove()
        self.logout.grid_remove()

    def Show(self):
        app.geometry("400x160")
        self.updateTMenu.grid()
        self.manageTourn.grid()
        self.logout.grid()

    def EnterUpdateTeam(self):
        self.Hide()
        self.UpdateTeam.Show()
        self.UpdateTeam.PopulateTeamList()

    def EnterTourn(self):
        self.Hide()
        self.Tourn.Show()
        self.Tourn.PopulateTeamList()
        self.Tourn.PopulateAllTeamList()
        self.Tourn.PopulateTournList()

    def Logout(self):
        self.Hide()
        self.Log.Show()

class ComponentUpdateTeam:
    #note: check Model and update View
    def __init__(self, inpdbObj, inpC, inpMainMenu, inpControl):
        #DB
        self.dbObj = inpdbObj
        self.coll = inpC
        self.MainMenu = inpMainMenu
        self.control = inpControl
        #Views
        #self.viewTeam = inpViewTeam
        #self.viewMember = inpViewMember
        #Team Name
        self.team_label = Label(app, text = "Team Name", font = 9)
        self.team_label.grid(row = 0, column = 0)
        self.team_inp = StringVar()
        self.team_entry = Entry(app, textvariable = self.team_inp, font = 9)
        self.team_entry.grid(row = 1, column = 0)
        #Create Team
        self.createTeam_button = Button(app, text = "Create", width = 13, command = self.CreateTeam)
        self.createTeam_button.grid(row = 2, column = 0)
        #Name
        self.name_label = Label(app, text = "Name", font = 9)
        self.name_label.grid(row = 5, column = 0)
        self.name_inp = StringVar()
        self.name_entry = Entry(app, textvariable = self.name_inp, font = 9)
        self.name_entry.grid(row = 6, column = 0)
        #Add Member
        self.add_button = Button(app, text = "Add Member", width = 13, command = self.AddMember)
        self.add_button.grid(row = 7, column = 0)
        #Remove Member
        self.remove_button = Button(app, text = "Remove Member", width = 13, command = self.RemoveMember)
        self.add_button.grid(row = 8, column = 0)
        #Delete Team
        self.delete_button = Button(app, text = "Delete Team", width = 13, command = self.DeleteTeam)
        self.delete_button.grid(row = 3, column = 0)
        #Back
        self.back_button = Button(app, text = "Back", width = 7, command = self.Back)
        self.back_button.grid(row = 5, column = 0)
        #Team Listbox
        self.team_list = Frame()
        self.team_list.grid(row = 0, column = 1, columnspan = 2, rowspan = 10)
        self.team_listbox = Listbox(self.team_list, height = 20, width = 40, border = 1, selectmode = SINGLE)
        self.team_listbox.pack(side = LEFT)
        self.team_scroll = Scrollbar(self.team_list)
        self.team_scroll.pack(side = LEFT)
        self.team_listbox.configure(yscrollcommand = self.team_scroll.set)
        self.team_scroll.configure(command = self.team_listbox.yview)
        self.team_listbox.bind("<<ListboxSelect>>", self.SelectItemTeam)
        #Members Listbox
        self.member_list = Frame()
        self.member_list.grid(row = 0, column = 3, columnspan = 2, rowspan = 10)
        self.member_listbox = Listbox(self.member_list, height = 20, width = 40, border = 1, selectmode = SINGLE)
        self.member_listbox.pack(side = LEFT)
        self.member_scroll = Scrollbar(self.member_list)
        self.member_scroll.pack(side = LEFT)
        self.member_listbox.configure(yscrollcommand = self.member_scroll.set)
        self.member_scroll.configure(command = self.member_listbox.yview)
        self.member_listbox.bind("<<ListboxSelect>>", self.SelectItemMember)
        #Hide
        self.Hide()

    def Hide(self):
        self.team_label.grid_remove()
        self.team_entry.grid_remove()
        self.createTeam_button.grid_remove()
        self.name_label.grid_remove()
        self.name_entry.grid_remove()
        self.add_button.grid_remove()
        self.remove_button.grid_remove()
        self.delete_button.grid_remove()
        self.team_list.grid_remove()
        self.member_list.grid_remove()
        self.back_button.grid_remove()

    def Show(self):
        app.geometry("760x350")
        self.team_label.grid()
        self.team_entry.grid()
        self.createTeam_button.grid()
        self.name_label.grid()
        self.name_entry.grid()
        self.add_button.grid()
        self.remove_button.grid()
        self.delete_button.grid()
        self.team_list.grid()
        self.member_list.grid()
        self.back_button.grid()

    def SelectItemTeam(self, event):
        global selectedItem
        index = self.team_listbox.curselection()[0]
        selectedItem = self.team_listbox.get(index)
        self.PopulateMemberList(self.team_listbox.get(ACTIVE))

    def SelectItemMember(self, event):
        global selectedItem
        index = self.member_listbox.curselection()[0]
        selectedItem = self.member_listbox.get(index)

    def PopulateTeamList(self):
        self.team_listbox.delete(0, END)
        entry = self.dbObj.FindUserTeam(self.coll, self.control.name)
        for v in entry:
            self.team_listbox.insert(END, v)

    def PopulateMemberList(self, teamID):
        print(teamID)
        self.member_listbox.delete(0, END)
        target = self.dbObj.FindTeam(self.coll, teamID)
        entry = []
        for v in target:
            entry = v["Members"]
        for w in entry:
            self.member_listbox.insert(END, w)

    def CreateTeam(self):
        self.dbObj.AddTeam(self.coll, self.team_entry.get(), [self.control.name])
        self.PopulateTeamList()

    def AddMember(self):
        if (self.CheckMembership()):
            self.dbObj.AddMember(self.coll, self.team_entry.get(), self.name_entry.get())

    def RemoveMember(self):
        if (self.CheckMembership()):
            self.dbObj.RemoveMember(self.coll, self.team_entry.get(), self.name_entry.get())

    def DeleteTeam(self):
        if (self.CheckMembership()):
            self.dbObj.Remove(self.coll, self.team_entry.get())
            self.PopulateTeamList()
            self.member_listbox.delete(0, END)

    def Back(self):
        self.Hide()
        self.MainMenu.Show()

    def CheckMembership(self):
        members = []
        members = self.dbObj.FindMembers(self.coll, self.team_entry.get())
        print(members)
        if (self.control.name in members):
            return True
        else:
            return False

class ComponentTournament:
    def __init__(self, inpdbObj, inpC, inpMainMenu, inpControl):
        #DB
        self.dbObj = inpdbObj
        self.coll = inpC
        self.MainMenu = inpMainMenu
        self.control = inpControl
        #Select Button
        #self.select_button = Button(app, text = "Select Team", width = 13)
        #self.select_button.grid(row = 5, column = 0)
        #Tournament Name
        self.tourn_inp = StringVar()
        self.tourn_entry = Entry(app, textvariable = self.tourn_inp)
        self.tourn_entry.grid(row = 0, column = 0)
        #Challenge Button
        self.challenge_button = Button(app, text = "Challenge Team", width = 13, command = self.Challenge)
        self.challenge_button.grid(row = 1, column = 0)
        #Revoke Button
        self.revoke_button = Button(app, text = "Revoke Tournament", width = 13, command = self.Revoke)
        self.revoke_button.grid(row = 2, column = 0)
        #Team1
        self.team1_label = Label(app, text = "Team 1", font = 6)
        self.team1_label.grid(row = 3, column= 0, sticky = N)
        #Team2
        self.team2_label = Label(app, text = "Team 2", font = 6)
        self.team2_label.grid(row = 4, column= 0, sticky = N)
        #Back
        self.back_button = Button(app, text = "Back", width = 7, command = self.Back)
        self.back_button.grid(row = 5, column = 0)
        #Team List
        self.team_list = Frame()
        self.team_list.grid(row = 0, column = 1, columnspan = 2, rowspan = 6)
        self.team_listbox = Listbox(self.team_list, height = 20, width = 30, border = 1, selectmode = SINGLE, exportselection=0)
        self.team_listbox.pack(side = LEFT)
        self.team_scroll = Scrollbar(self.team_list)
        self.team_scroll.pack(side = LEFT)
        self.team_listbox.configure(yscrollcommand = self.team_scroll.set)
        self.team_scroll.configure(command = self.team_listbox.yview)
        self.team_listbox.bind("<<ListboxSelect>>", self.SelectItemTeam)
        #All Team
        self.teamAll_list = Frame()
        self.teamAll_list.grid(row = 0, column = 3, columnspan = 2, rowspan = 6)
        self.teamAll_listbox = Listbox(self.teamAll_list, height = 20, width = 30, border = 1, selectmode = SINGLE, exportselection=0)
        self.teamAll_listbox.pack(side = LEFT)
        self.teamAll_scroll = Scrollbar(self.teamAll_list)
        self.teamAll_scroll.pack(side = LEFT)
        self.teamAll_listbox.configure(yscrollcommand = self.teamAll_scroll.set)
        self.teamAll_scroll.configure(command = self.teamAll_listbox.yview)
        self.teamAll_listbox.bind("<<ListboxSelect>>", self.SelectItemTeamAll)
        #Tournament List
        self.tourn_list = Frame()
        self.tourn_list.grid(row = 0, column = 5, columnspan = 2, rowspan = 6)
        self.tourn_listbox = Listbox(self.teamAll_list, height = 20, width = 30, border = 1, selectmode = SINGLE, exportselection=0)
        self.tourn_listbox.pack(side = LEFT)
        self.tourn_scroll = Scrollbar(self.teamAll_list)
        self.tourn_scroll.pack(side = LEFT)
        self.tourn_listbox.configure(yscrollcommand = self.tourn_scroll.set)
        self.tourn_scroll.configure(command = self.teamAll_listbox.yview)
        self.tourn_listbox.bind("<<ListboxSelect>>", self.SelectItemTourn)
        #Hide
        self.Hide()

    def PopulateTeamList(self):
        self.team_listbox.delete(0, END)
        entry = self.dbObj.FindUserTeam(self.coll[0], self.control.name)
        for v in entry:
            self.team_listbox.insert(END, v)

    def PopulateAllTeamList(self):
        self.teamAll_listbox.delete(0, END)
        for v in self.dbObj.GetCollection(self.coll[0]).find({}):
            self.teamAll_listbox.insert(END, v["_id"])

    def PopulateTournList(self):
        self.tourn_listbox.delete(0, END)
        for v in self.dbObj.FindUserTourn(self.coll[0], self.coll[1], self.control.name):
            self.tourn_listbox.insert(END, v)

    def SelectItemTeam(self, event):
        global selectedItem
        index = self.team_listbox.curselection()[0]
        selectedItem = self.team_listbox.get(index)

    def SelectItemTeamAll(self, event):
        global selectedItem
        index = self.teamAll_listbox.curselection()[0]
        selectedItem = self.teamAll_listbox.get(index)

    def SelectItemTourn(self, event):
        global selectedItem
        index = self.tourn_listbox.curselection()[0]
        selectedItem = self.tourn_listbox.get(index)
        entry = self.tourn_listbox.get(ACTIVE)
        teams = self.dbObj.FindTourn(self.coll[1], entry)
        self.team1_label["text"] = teams[0]
        self.team2_label["text"] = teams[1]
        print(teams)

    def Hide(self):
        #self.select_button.grid_remove()
        self.tourn_entry.grid_remove()
        self.challenge_button.grid_remove()
        self.revoke_button.grid_remove()
        self.team_list.grid_remove()
        self.teamAll_list.grid_remove()
        self.tourn_list.grid_remove()
        self.back_button.grid_remove()
        self.team1_label.grid_remove()
        self.team2_label.grid_remove()

    def Show(self):
        app.geometry("760x350")
        #self.select_button.grid()
        self.tourn_entry.grid()
        self.challenge_button.grid()
        self.revoke_button.grid()
        self.team_list.grid()
        self.teamAll_list.grid()
        self.tourn_list.grid()
        self.back_button.grid()
        self.team1_label.grid()
        self.team2_label.grid()
        self.team1_label["text"] = "Team 1"
        self.team2_label["text"] = "Team 2"

    def Challenge(self):
        self.dbObj.AddTourn(self.coll[1], self.tourn_entry.get(), self.team_listbox.get(ACTIVE), self.teamAll_listbox.get(ACTIVE))
        self.PopulateTournList()
    
    def Revoke(self):
        entry = self.tourn_listbox.get(ACTIVE)
        self.dbObj.Remove(self.coll[1], entry)
        self.PopulateTournList()

    def Back(self):
        self.Hide()
        self.MainMenu.Show()
