from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite3
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 90  # Set Duration To 1000 ms == 1 second

PASS_DB = 'pass4_db.db'
KEY_DB = 'config'
key = '1234'
lock = '4566'
class SCRAPE:
    def __init__(self , visible = 'headless' , password = '******' , email = '', refresh_time = 5):
        self.PASS_DB = PASS_DB        
        try:
            conn = sqlite3.connect(self.PASS_DB)
            c = conn.cursor()
            c.execute("""CREATE TABLE entries (password text,  email text)""")
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
            pass

        self.visible = visible
        self.password , self.email = password  , email# self.PASS_CODES(password , email , contact_email)
        self.refresh_time = refresh_time

    def Launch(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        PATH = ChromeDriverManager().install()#'C:\Program Files (x86)\chromedriver.exe'
        
        if self.visible == 'headless':
            self.driver  = webdriver.Chrome(PATH , options = option)
        else:
            self.driver  = webdriver.Chrome(PATH)


        print('INTRO')
        self.driver.get('https://app.qa-world.com')
        
        self.ERROR(r'/html/body/header/div[2]/div/div/a') #LOGIN BUTTON
        print('CREDENTIALS')

        email_entry = self.driver.find_element_by_xpath('//*[@id="contractor_user_email"]')
        email_entry.send_keys(self.email)
        
        pswd_entry = self.driver.find_element_by_xpath('//*[@id="contractor_user_password"]')
        pswd_entry.send_keys(self.password)

        print('LOGIN')

        self.ERROR(r'//*[@id="new_contractor_user"]/div[5]/div/input') #LOGIN BUTTON

        error = self.JOB_CAPTURE()
        return error
    def ERROR(self , url ):
        '''z`1x
            We take the url and allow the time for the page to load
            If it doesnt we raise the given error
        '''
        reload = 0
        if reload == 5:
            print('CHECK THE NET DUMBASS')
            pass #RAISE TKINTER ERROR
        try:
            buttn = WebDriverWait(self.driver , self.refresh_time).until(EC.presence_of_element_located((By.XPATH,url)))
            buttn.click()
        except:
            
            try:
                    err = WebDriverWait(driver , 1).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="diagnose-link"]')))
                    print('POOO Mc DOOOGLEEEEEEEE')
                    #RAISE TKINTER ERROR
            except:
                    self.driver.refresh()
                    reload += 1 
    
    def JOB_CAPTURE(self):
        error = False
        '''
            THE START BUTTON IS PRESSED HERE
        '''
        while True:
            try:
                job = WebDriverWait(self.driver , self.refresh_time).until(EC.presence_of_element_located((By.NAME,r'queue_item')))
                job.click()
                try:
                    job = WebDriverWait(self.driver , self.refresh_time).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="root"]/div/div[3]/div/div[4]/div[2]/div[3]/div[2]/div/div[2]')))
                    for i in range (10):
                        winsound.Beep(frequency, duration)
                        error = 'SUCCESSFUL'
                    break
                except:
                    for i in range (5):
                        winsound.Beep(frequency , duration)
                        time.sleep(2)
                        
                    error = 'FAILED'
                    break
            except:
                try:
                    err = WebDriverWait(self.driver , 1).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="diagnose-link"]')))
                    #RAISE TKINTER ERROR
                except:
                    self.driver.refresh()
        return error
    def PASS_CODES(self , password , email):
        print(password , email)
        '''
            SAVES THE USER INPUT PASSWORDS
            CHECKS WHETHER THE USER PASSWORD MATCHES THE EMAIL PASSWORD 
            IF THEY DONT IT ASK THE USER TO INPUT HIS/HER PASSWORD
        '''
        if password == '******':
            conn = sqlite3.connect(self.PASS_DB)
            c = conn.cursor()
            c.execute('SELECT password FROM entries WHERE email = ?' , (email,))
            data = c.fetchall()
            if data == []:
                pass #TKINTER ERROR
            else:
              #  print(email , data)
                return data[0][0] , email 
            conn.commit()
            conn.close()

        elif password != '******' or email != '':
            conn = sqlite3.connect(self.PASS_DB)
            c = conn.cursor()
            c.execute('SELECT password FROM entries WHERE email = ?', (email,))
            data = c.fetchall()
            if data == []:
                c.execute("insert into entries (password , email  ) values( ?,?)" , (password , email))
                conn.commit()
                conn.close()
                return password , email
            else:
                conn.commit()
                conn.close()                
                return data[0][0] , email
            

#<a href="#" data="[object Object]" id="queue-0-9508296079" name="queue_item">Start Work</a>
