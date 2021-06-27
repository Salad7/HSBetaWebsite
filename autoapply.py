import pyautogui
import selenium
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 3)
# visible = EC.visibility_of_element_located
#
# browser.get('https://www.youtube.com/watch?v=AFNUeUed8Ro&ab_channel=NDTV')
# wait.until(visible((By.ID, "video-title")))
# browser.find_element_by_id("video-title").click()
# browser.minimize_window()
# time.sleep(7)
# browser.quit()
import webbrowser
def openConsole():
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('j')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('j')

def clickConsoleArea():
    pyautogui.click(1359, 500) # Move mouse to (10, 5)

def loginNike():
    time.sleep(2)
    pyautogui.click(64, 466)
    pyautogui.write('test3212312311')
    time.sleep(2)
    #Enter Password
    pyautogui.click(81, 536)
    pyautogui.write('123@lmfao2!')
    time.sleep(2)

    #Press Enter
    pyautogui.click(73, 675)

def acceptPrivacyPolicy():
    time.sleep(2)
    pyautogui.click(82, 695)

def openSite():
    webbrowser.open('https://nike.taleo.net/careersection/10100m/jobapply.ftl?job=203_NIKE_FT_EVG&lang=en&languageCode=en&countryCode=US&countryName=United%20States', new=2)
    openConsole()
    time.sleep(2)
    clickConsoleArea()

def signupNike():
    #Click new user
    pyautogui.click(151, 664)
    time.sleep(2)

    #Click username
    pyautogui.click(84, 455)
    time.sleep(2)
    pyautogui.write('test32123123124')

    #Click password
    pyautogui.click(135, 538)
    time.sleep(2)
    pyautogui.write('123@lmfao2!')

    #Click re-enter
    pyautogui.click(118, 603)
    time.sleep(2)
    pyautogui.write('123@lmfao2!')

    #Click Register
    # pyautogui.click(111, 679)
    time.sleep(4)

def createApplicationProcess():
    #Page 1 Resume parsing..Do not want to upload resume is already selected, click continue
    pyautogui.click(115, 744)
    time.sleep(4)

    #Page 2, basic details
    #First Name
    pyautogui.click(115, 744)
    pyautogui.write('John')

    #Last Name
    pyautogui.click(832, 781)
    pyautogui.write('John')

    #Street Address
    pyautogui.click(142, 983)
    pyautogui.write('John')

    #Scroll Down
    pyautogui.scroll(-1000)

    #City
    pyautogui.click(126, 253)
    pyautogui.write('Charlotte')

    #Zipcode
    pyautogui.click(675, 244)
    pyautogui.write('28213')

    #Country
    pyautogui.click(130, 368)
    pyautogui.click(234, 414)

    #State
    pyautogui.click(381, 444)
    #Move Mouse down. dont click
    pyautogui.moveTo(145, 458)
    pyautogui.scroll(-300)
    #Select NC
    pyautogui.click(116, 674)

    #Select Metropolitan Area and charlotte
    pyautogui.click(102, 498)
    pyautogui.click(152, 607)



    # #Cell Number
    pyautogui.click(881, 570)
    pyautogui.write('704-579-9523')
    #
    # #Select Primary Number
    pyautogui.click(304, 685)
    pyautogui.click(205, 770)
    #
    # #Email Address
    pyautogui.click(108, 786)
    pyautogui.write('kukgiplayer2@gmail.com')
    #
    # #Scroll Down
    pyautogui.scroll(-1000)
    #
    # #Select Source Type
    pyautogui.click(102, 753)
    pyautogui.click(176, 883)
    pyautogui.click(70, 813)
    pyautogui.click(67, 882)
    #
    # #Click Save and Continue
    pyautogui.click(68, 914)

    #Page 3
    # #Scroll Up
    pyautogui.scroll(5000)

    #Enter Employer
    #Enter Job Description
    #Start Month
    #Start Year

# openSite()
# acceptPrivacyPolicy()
# loginNike()
# # signupNike()
# createApplicationProcess()


print("Loc: "+str(pyautogui.position()))
