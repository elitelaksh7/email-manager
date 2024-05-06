from passwordGenerator import verification
from database import dataCenter
from my_bin import binData




#classes
class verifyUser:    
  
    activeUser=input("who is logging in? Enter Your Name: ")
    activeUserMail=input("what is the mail id you are using? ")
    verifyPassword=input("enter the password: ")
    currentUserData=[dataCenter.currentUserData(activeUserMail)]
    
    def __init__(self):
        verification.emailPassVerification(verifyUser.activeUserMail,verifyUser.verifyPassword)
        if(verification.verified):
            verifyUser.activeUser = user(verifyUser.activeUserMail,verifyUser.activeUser)
            print(verifyUser.activeUser.name,"has successfully logged in.")
            verifyUser.activeUser.storeData(verifyUser.currentUserData)
            if __name__ == "__main__":
                verifyUser.activeUser.sendDataToBin()
        else:
            raise Exception("Incorrect Details!, Login Failed.")
        
    
class user:
    companyNameList=[]
    eachCompanyActivity={}
    allSubjectsOfACompany={}
    
    def __init__(self,eid,name):
        self.emailId=eid
        self.name=name

    def storeData(self,info):
        self.data=info
        
        for allMails in self.data:#allMails is the entire object including both spam and important messages.Returns object
            
            for typeOfMail in allMails:#typeOfMail is the element inside object: spam and important
                
               listOfAllMailsOfAType = allMails[typeOfMail]#since dictionary use object[spam] => retireves entire spam object then entire important object
               
               for singleMailOfParticularType in listOfAllMailsOfAType:#prints each element in spam and important
                   
                   for (subjectType,value) in singleMailOfParticularType.items():#prints only the company names
                       
                        if(subjectType=="company_name"):
                           user.companyNameList.append(value)
                           #create dictionary for activity based on presence of company
                           if(value not in user.eachCompanyActivity):
                               user.eachCompanyActivity[value]={"seen":0,"unseen":0}
                               if(singleMailOfParticularType["activity"]=="seen"):
                                   user.eachCompanyActivity[value]["seen"]+=1
                               else:
                                   user.eachCompanyActivity[value]["unseen"]+=1
                           else:
                               if(singleMailOfParticularType["activity"]=="seen"):
                                   user.eachCompanyActivity[value]["seen"]+=1
                               else:
                                   user.eachCompanyActivity[value]["unseen"]+=1
                                   
                           #create dictionary for all subjects of all the emails of a company
                           if(value not in user.allSubjectsOfACompany):
                               #if new comapny create an empty array and at the same time append that value
                               user.allSubjectsOfACompany[value]=[]
                               user.allSubjectsOfACompany[value].append(singleMailOfParticularType["subject"])
                           else:
                               user.allSubjectsOfACompany[value].append(singleMailOfParticularType["subject"])
                               
        print("your data has been stored")
        
    def sendDataToBin(self):
        
        self.listOfCompanyMailsWithLessActivity={}
        self.listOfCompanyWithLessActivity=[]
        
        for (company,activityList) in user.eachCompanyActivity.items():
            companyFinalActivity=0
            for activity in activityList:
                if(activity=="seen"):
                    companyFinalActivity+=int((user.eachCompanyActivity[company]["seen"]))
                else:
                    companyFinalActivity-=int((user.eachCompanyActivity[company]["unseen"]))
            
            #checks through the company that is currently being iterated
            
            for allMails in verifyUser.currentUserData:#i is the entire object including both spam and important messages.Returns object
        
                for typeOfMail in allMails:#j is the element inside object: spam and important
            
                    listOfAllMailsOfAType = allMails[typeOfMail]#since dictionary use object[spam] => retireves entire spam object then entire important object
           
                    for singleMailOfParticularType in listOfAllMailsOfAType:#prints each element in spam and important
               
                        for (subjectType,value) in singleMailOfParticularType.items():#prints only the company names
                            if(subjectType=="company_name"):
                                if(companyFinalActivity < 0):
                                    if(value == company):
                                        if(company not in self.listOfCompanyMailsWithLessActivity):
                                            self.listOfCompanyMailsWithLessActivity[company]=[]

                                            self.listOfCompanyMailsWithLessActivity[company].append(singleMailOfParticularType)

                                            self.listOfCompanyWithLessActivity.append(company)
                                        else:
                                            self.listOfCompanyMailsWithLessActivity[company].append(singleMailOfParticularType)
                                else:
                                    continue
        binData.recieveData(self.listOfCompanyMailsWithLessActivity,verifyUser.activeUserMail,self.listOfCompanyWithLessActivity)
                
               
        
#driver code


userCreated=verifyUser()




