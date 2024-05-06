from index import verifyUser,user
     
class createEmailLabel(verifyUser,user):
    reqMails=[]
    notreqMails=[]
    def __init__(self,label):
        self.currentUser=verifyUser.activeUser.name
        self.currentEmailId=verifyUser.activeUserMail
        self.groupName=label
        
    def regroupMailsAndCreateLabel(self,*args):
        for (company,arrayOfAllEmailSubjects) in user.allSubjectsOfACompany.items():
            for listOfSUbjectsOfACompany in arrayOfAllEmailSubjects:
                for keyword in args:
                    if(keyword.lower() in listOfSUbjectsOfACompany.lower()):
                        createEmailLabel.reqMails.append(listOfSUbjectsOfACompany)
                    else:
                        createEmailLabel.notreqMails.append(listOfSUbjectsOfACompany)
        print()
        print(self.groupName,": ",createEmailLabel.reqMails)                                     
        

createLabel1=createEmailLabel("Personal Pronouns")
createLabel1.regroupMailsAndCreateLabel("your")

