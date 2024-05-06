from database import dataCenter
from passwordGenerator import verification


class binData:
    data=None
    option=None
    mailTypeReplacingDict={}
    
    def __init__(activeUserMailId,companyNames):
        print("what do you want to do with the set of data that was collected based on your lower activity with respect to those mails of esch particular companies collected?")
        print()
        print("1.DELETE all the less visited data without viewing them.")
        print("2.View the less visited data to take decision")
        print("3.Don't delete any of the less visited data")
        print()
        ans=int(input("enter the serial number of the option you prefer: "))
        print()
        binData.option = ans
        binData.verifyForAction(activeUserMailId,companyNames)

    def recieveData(allMailsOfCompanyThatHasLessActivity,activeUserMailId,companyNames):
        binData.data=allMailsOfCompanyThatHasLessActivity
        binData.__init__(activeUserMailId,companyNames)

    def verifyForAction(activeUserMailId,companyNames):
        givenPass = verification.generateRandPass()
        print(givenPass)
        typedPass = input("enter the password recieved: ")
        if(givenPass == typedPass):
            binData.action(activeUserMailId,companyNames)
        else:
            raise Exception("Incorrect Password")
        
    def action(activeUserMailId,companyNames):
        
        match binData.option:
            
            case 1:#DELETE entire data without viewing them
               for mailType in dataCenter.everyOnesData[activeUserMailId]:
                   
                   if(mailType not in binData.mailTypeReplacingDict):
                       replacingArr=[]#put over since after spam mail create new array to put important mails so that prev spam mails are not included in imp mails
                       binData.mailTypeReplacingDict[mailType]=replacingArr
                   else:
                       binData.mailTypeReplacingDict[mailType]=replacingArr
                       
                   for singleMailOfParticularType in (dataCenter.everyOnesData[activeUserMailId][mailType]):
                                 
                       for (subjectType,value) in singleMailOfParticularType.items():#prints only the company names
                           
                           if(subjectType=="company_name"):
                               if(value not in companyNames):
                                   replacingArr.append(singleMailOfParticularType)
               dataCenter.everyOnesData[activeUserMailId]=binData.mailTypeReplacingDict
               print("New Data After Deleting Unwanted Data: ",dataCenter.everyOnesData[activeUserMailId],'\n')
               
            case 2:#View the data to take decision
        
                for mailType in dataCenter.everyOnesData[activeUserMailId]:
                       
                    for singleMailOfParticularType in (dataCenter.everyOnesData[activeUserMailId][mailType]):
                                 
                       for (subjectType,value) in singleMailOfParticularType.items():#prints only the company names
                           
                           if(subjectType=="company_name"):
                               if(value in companyNames):
                                   print(singleMailOfParticularType)
                print()
                binData.__init__(activeUserMailId,companyNames)
                
            case 3:#Don't delete any of the data and send them back
                print("No Data deleted",'\n')
                print("Data of",activeUserMailId,": ",dataCenter.everyOnesData[activeUserMailId])
                
            case _:
                raise Exception("choose correct option")
        
