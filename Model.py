from tkinter import *
from Component import *
from pymongo import *
from datetime import *

class Database:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["db"]

    def CreateCollection(self, cName):
        self.db.create_collection(cName)
        return self.db.get_collection(cName)

    def GetCollection(self, cName):
        return self.db.get_collection(cName)

    def AddUser(self, cName, inpUser, inpPw):
        entry = {
            "_id": inpUser,
            "Password": inpPw
            }
        target = self.GetCollection(cName)
        target.insert_one(entry)

    def AddTeam(self, cName, inpTeam, inpMembers):
        entry = {
            "_id": inpTeam,
            "Members": inpMembers
            }
        target = self.GetCollection(cName)
        target.insert_one(entry)

    def AddTourn(self, cName, tournName, inpTeam1, inpTeam2):
        entry = {
            "_id": tournName,
            "Team 1": inpTeam1,
            "Team 2": inpTeam2
            }
        target = self.GetCollection(cName)
        target.insert_one(entry)

    def FindUser(self, cName, inpUser):
        target = self.GetCollection(cName)
        return target.find(inpUser)

    def FindTeam(self, cName, inpTeam):
        target = self.GetCollection(cName)
        return target.find({"_id":inpTeam})

    def FindMembers(self, cName, inpTeam):
        target = self.GetCollection(cName)
        entry = target.find({"_id":inpTeam})
        res = []
        for i in entry:
            for v in i["Members"]:
                res.append(v)
        return res
        
    def FindTourn(self, cName, inpTourn):
        target = self.GetCollection(cName)
        entry = target.find({"_id":inpTourn})
        res = []
        for i in entry:
            res.append(i["Team 1"])
            res.append(i["Team 2"])
        return res

    def FindUserTeam(self, cName, inpUser):
        target = self.GetCollection(cName)
        entry = []
        for v in target.find({}):
            if (inpUser in v["Members"]):
                entry.append(v["_id"])
        return entry

    def FindUserTourn(self, cNameTeam, cNameTourn, inpUser):
        target = self.GetCollection(cNameTourn)
        teamList = self.FindUserTeam(cNameTeam, inpUser)
        entry = []
        for v in target.find({}):
            for i in teamList:
                if (i in v["Team 1"] or i in v["Team 2"]):
                    entry.append(v["_id"])
        return entry
    
    def Remove(self, cName, inpID):
        #print(inpID)
        target = {
            "_id": inpID
            }
        self.GetCollection(cName).delete_one({"_id": inpID})

    def AddMember(self, cName, teamID, memberName):
        target = self.GetCollection(cName)
        target.update_one({"_id": teamID}, {"$addToSet": {"Members": memberName}})

    def RemoveMember(self, cName, teamID, memberName):
        target = self.GetCollection(cName)
        target.update_one({"_id": teamID}, {"$pull": {"Members": memberName}})

    def Clear(self, cName):
        self.GetCollection(cName).remove({})
