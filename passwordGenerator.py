import random
from database import database

class verification:
    verified =False
    
    def generateRandPass():
        randLength=random.randint(5,5)    
        Pass=random.sample(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],randLength)
        Pass=''.join(Pass)
        return Pass

    def emailPassVerification(typedEmailId,typedEmailPass):
        try:
            typedEmailId in database.loginDetails
            if(typedEmailPass == database.loginDetails[typedEmailId]):
                verification.verified = True
            else:
                verification.verified = False
        except KeyError:
            print("Incorrect Details!, Login Failed.")
                
            

            
                
                        
        
