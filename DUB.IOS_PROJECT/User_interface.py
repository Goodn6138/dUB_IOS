import sqlite3
PASS_DB = 'pass4_db.db'

class User_I:
    def __init__(self):
        self.head = 'headless'
        self.USER_ACCOUNT = 'alekziree28@gmail.com'

    def Enable_Browser(self):
        '''
        ENABLE THE CHROME WINDOW TO BE VISIBLE OR TO CLOSE 
        '''
        if self.head == 'headless':
            self.head = 'OFF'
        else:
            self.head = 'headless'
        return self.head
    def ERROR(self,x , email = 'checker', dancer = 0):
        error = 'False'
        '''
            CHECKS IF THE EMAIL_FIELD IS ON WHEN email == 'checker'
            CHECKS WHETHER THE USER'S PASSWORD DOES EXIST IF THE PASSWORD FIELD IS EMPTY
            CHECKS IF THE USER'S CONRACT EMAIL EXIST SO AS TOE SEND A MESSAGE TO THE EMAIL MODULE
            IF THE CONTACT EMAIL EXISTS IT WILL ASK IF HE/SHE WANTS TO CHANGE HIS/HER CONTACT EMAIL IF THE CONTACT EMAIL IS FIELD WITH A DIFFERENT INPUT 
        '''
        if email == 'checker':
            x = self.USER_ACCOUNT
            if len(x) == x.count(' '):
                error = 'True'
            else:
                error = 'False'
            return error
            
        else:
            conn = sqlite3.connect(PASS_DB)
            c = conn.cursor()
            if len(x) == x.count(' '):
                c.execute('SELECT * FROM entries WHERE email = ? ', (email,))
                data = c.fetchall()
                if data == []:
                    error = 'True'
                else:
                    self.PSWD = '******'
                    error = 'False'
                return error
            conn.commit()
            conn.close() 
