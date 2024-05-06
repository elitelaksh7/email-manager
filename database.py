class database:
    loginDetails={"laksh@gmail.com":"lakshjain7","vedaanth@gmail.com":"vedaanthsingh"}
    
    def addDetails(emailId,emailPass):
        database.loginDetails[emailId]=emailPass
        
    def removeDetails(emailId,emailPass):
        del database.loginDetails[emailId]
        
    def updateDetails(emailId,emailPass):
        database.loginDetails[emailId]=emailPass

    

class dataCenter:
    #this is everyones seperated data of spam and important which is obtained by scanning for keywords in mail
    everyOnesData= {"laksh@gmail.com":{
    "spam_emails": [
    {
      "subject": "Hot Singles in Your Area!",
      "company_name": "DateFinder",
      "activity": "unseen"
    },
    {
      "subject": "Find Your Perfect Match Today!",
      "company_name": "DateFinder",
      "activity": "seen"
    },
    {
      "subject": "Meet Local Singles Now!",
      "company_name": "DateFinder",
      "activity": "seen"
    },
    {
      "subject": "Increase Your Credit Score Overnight!",
      "company_name": "CreditBoosters",
      "activity": "unseen"
    },
    {
      "subject": "Get Approved for a Loan Today!",
      "company_name": "CreditBoosters",
      "activity": "unseen"
    },
    {
      "subject": "Unlock Your Financial Potential!",
      "company_name": "CreditBoosters",
      "activity": "unseen"
    }
      ],
    "important_emails": [
    {
      "subject": "Security Alert: Unusual Activity Detected",
      "company_name": "BankOfFinance",
      "activity": "seen"
    },
    {
      "subject": "Your New Account Statement",
      "company_name": "BankOfFinance",
      "activity": "unseen"
    },
    {
      "subject": "Notification: Bill Payment Due Soon",
      "company_name": "BankOfFinance",
      "activity": "seen"
    },
    {
      "subject": "Your Tax Documents",
      "company_name": "TaxServicesInc",
      "activity": "seen"
    },
    {
      "subject": "Reminder: Tax Filing Deadline Approaching",
      "company_name": "TaxServicesInc",
      "activity": "unseen"
    },
    {
      "subject": "Action Required: Verify Your Identity",
      "company_name": "TaxServicesInc",
      "activity": "seen"
    }
    ]
    },
    "vedaanth@gmail.com" : {
    "spam_emails": [
    {
      "subject": "Special Offer Inside!",
      "company_name": "SpammyMart",
      "activity": "unseen"
    },
    {
      "subject": "You've won a prize!",
      "company_name": "ScamCorp",
      "activity": "unseen"
    },
    {
      "subject": "Limited Time Discount",
      "company_name": "JunkMail Inc.",
      "activity": "seen"
    },
    {
      "subject": "Free Trial for You",
      "company_name": "SpammyMart",
      "activity": "unseen"
    }
    ],
    "important_emails": [
    {
      "subject": "Your Order Confirmation",
      "company_name": "GreatProducts Ltd.",
      "activity": "unseen"
    },
    {
      "subject": "Important Update: Account Security",
      "company_name": "SecureBank",
      "activity": "seen"
    },
    {
      "subject": "Your Monthly Newsletter",
      "company_name": "GreatProducts Ltd.",
      "activity": "unseen"
    },
    {
      "subject": "Action Required: Verify Your Email",
      "company_name": "SecureBank",
      "activity": "unseen"
    }
    ]}}

    def currentUserData(emailId):
        return dataCenter.everyOnesData[emailId]

