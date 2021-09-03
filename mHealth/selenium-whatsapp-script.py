# try:
#     from pip import main as pipmain
# except ImportError:
#     from pip._internal import main as pipmain

# # from pip._internal import main as pipmain

# pipmain(['install', 'selenium'])

import sys, time
from datetime import date, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


print("done importing modules...")
today = date.today().strftime('%d/%m/%Y') # getting today date ddmmyyyy format
current_time = datetime.now().strftime("%H:%M:%S") # getting current time

day = input('Enter day to send in numbers: ')
month = input('Enter month to send in numbers: ')
year = input('Enter year to send in numbers: ')
msgDate = day+"/"+month+"/"+year  # dd/mm/yyyy
hour = input('Enter hour in 24hour fomart: ')
minutes = input('Enter the minute: ')
print("Message will be sent on: "+day+"/"+month+"/"+year+" at "+hour+":"+minutes)
msgTime = hour+":"+minutes  # hh:mm 24 hour clock
msg = 'Hello!'


def new_chat(user_name):
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
    new_chat.send_keys(user_name)
    time.sleep(2)
    
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        print('Username not in contact list')
        time.sleep(2)
        chrome_browser.close()
        # sys.exit()
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()

    
    
if __name__ == '__main__': # protects from accidentally invoking the script 
    
    while True: # keep running script until sending time
        if msgDate == today:
            current_time = datetime.now().strftime("%H:%M:%S") # updating current time
            if current_time >= msgTime:

                # path to browser cache in home
                # /home/joshua/.config/google-chrome/Default
                options = webdriver.ChromeOptions()
                # options.add_argument(r'--user-data-dir=home/collins/.config/google-chrome/Default')
                options.add_argument('--profile-directory=Default')
                options.add_argument('--disable-popup-blocking')

                 # path where webdriver is stored
                 #/home/collins/Downloads/Compressed
                 # /home/joshua/Downloads/chromedriver_linux64/chromedriver
                #chrome_browser = webdriver.Chrome(executable_path=r'/home/joshua/Downloads/chromedriver_linux64/chromedriver', options=options)
                chrome_browser = webdriver.Chrome(executable_path=r'chromedriver_linux64/chromedriver', options=options)
                print("done")
                chrome_browser.execute_script("window.onbeforeunload = function() {};") 
                chrome_browser.get('https://web.whatsapp.com/')
                time.sleep(5)
                 
                user_name_list = ['+256751964081', '+256787689679']

                for user_name in user_name_list:
                    try:
                        #chat exists
                        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
                        user.click()
                    except NoSuchElementException as se:
                        # chat doesnot exist hence new chat
                        print("New number")
                        chrome_browser.execute_script("window.onbeforeunload = function() {};") 
                        chrome_browser.get('https://web.whatsapp.com/send?phone={}&text&source&data&app_absent'.format(user_name))
                        # new_chat(user_name)
                        time.sleep(10)

                    time.sleep(5)
                    message_box = chrome_browser.find_element_by_xpath('//div[@class="p3_M1"]')
                    print("find message bar..")
                    time.sleep(5)
                    message_box.send_keys(msg) 
                    # typing message
                    time.sleep(1)
                    print("Message typed..  ")
                    # if  message_box.send_keys(msg):
                    message_box = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')
                    print("find button..")
                    message_box.click()
                    # input_box.send_keys(Keys.ENTER)
                    print('message sent to: "{}"'.format(user_name))
                    time.sleep(5) # time for last message to actually be sent....   ==================================================
                    # chrome_browser.close()
                #     # sys.exit()
                chrome_browser.close()
                sys.exit()
            today = date.today().strftime('%d/%m/%Y') # updating today
            time.sleep(10)  
