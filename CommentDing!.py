from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
import os
from time import sleep
from playsound import playsound

sound_path = os.path.join(os.path.dirname(__file__), f'bell_sound.wav')
webdriv_path = os.path.join(os.path.dirname(__file__), f'msedgedriver.exe')
stream_link = input("Paste your stream URL here! (Youtube only, Twitch is disabled for now) \n")
t_or_yt = ""
if "youtube" in stream_link.lower():
    t_or_yt = "youtube"
elif "twitch" in stream_link.lower():
    t_or_yt = "twitch"


edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('mute-audio')
browser = Edge(executable_path=webdriv_path, options=edge_options)
os.system('cls' if os.name == 'nt' else 'clear')
delay = int(input("What would you like your delay to be, as in how often it checks chat for new messages (in seconds)? (15 second minimum)\n"))
if t_or_yt == "youtube": 
    current_chat = []
    while True:
        browser.get(stream_link)
        os.system('cls' if os.name == 'nt' else 'clear')
        WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='chatframe']")))
        os.system('cls' if os.name == 'nt' else 'clear')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='item-scroller']"))) ; sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        ele = browser.find_element_by_xpath("//div[@id='item-scroller']")
        for x in ele.text.splitlines():
            if x not in current_chat: 
                playsound(sound_path)
                current_chat.append(x)
                print(x)
                break
            elif x in current_chat:
                pass
        current_chat = [y for y in ele.text.splitlines()]
elif t_or_yt == False:
    #DISABLED FOR NOW 
    current_chat = []
    while True:
        browser.get(stream_link)
        os.system('cls' if os.name == 'nt' else 'clear')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]"))) ; sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        ele = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]")
        for x in ele.text.splitlines():
            if x not in current_chat: 
                playsound(sound_path)
                current_chat.append(x)
                print(x)
                break
            elif x in current_chat:
                pass
        current_chat = [y for y in ele.text.splitlines()]
else:
    print("Link is invalid, youtube only!")
    browser.quit()
    exit()
    