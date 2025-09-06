import pyautogui
import time
import subprocess
import psutil
import os

#settings
delay = 2

# Your login info (test accounts for practice!)
gmail_email = "gmail acc here"
gmail_password = "gmail pass here"
fb_email = "fb account here"
fb_password = "Fb pass here"
quipper_email = "Quipper account here"
quipper_password = "Your quipper  password here"

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def is_edge_running():
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'] and "msedge" in proc.info['name'].lower():
            return True
    return False

def open_edge(url, incognito=False):
    if incognito:
        subprocess.Popen([edge_path, "--inprivate", url])
    else:
        subprocess.Popen([edge_path, url])

def gmail_login():
    if is_edge_running():
        open_edge("https://mail.google.com", incognito=True)
    else:
        open_edge("https://mail.google.com", incognito=False)

    time.sleep(5)
   
    pyautogui.click(756, 311)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.typewrite(gmail_email, interval=0.05)
    pyautogui.click(1082, 506)
    time.sleep(5)
    pyautogui.typewrite(gmail_password, interval=0.05)
    pyautogui.press("enter")
    time.sleep(8)
    print("✅ Gmail login finished.")

def facebook_login():
    facebook_url = "https://facebook.com"
    if is_edge_running():
        open_edge(facebook_url, incognito=True)
    else:
        open_edge(facebook_url, incognito=False)

    time.sleep(5)
    pyautogui.click(839, 251)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    pyautogui.typewrite(fb_email, interval=0.05)
    pyautogui.press("tab")
    pyautogui.typewrite(fb_password, interval=0.05)
    pyautogui.press("enter")

    time.sleep(5)  
    
    pyautogui.click(554, 212)
    time.sleep(3)
    print("✅ Facebook login finished.")

def quipper_login():
    quipper_login_btn = (976, 562)
    if is_edge_running():
        open_edge("https://learn.quipper.com/en/login", incognito=True)
    else:
        open_edge("https://learn.quipper.com/en/login", incognito=False)

    time.sleep(5)
    pyautogui.click(940, 328)  
    time.sleep(1)
    pyautogui.typewrite(quipper_email, interval=0.05)
    pyautogui.press("tab")
    pyautogui.typewrite(quipper_password, interval=0.05)
    pyautogui.click(quipper_login_btn)
    time.sleep(5)
    pyautogui.click(721,526)
    print("✅ Quipper login finished.")

def OpenComicko():
    #This shit should only be used after gmail was logged in lil vro
    if is_edge_running():
        open_edge("https://comick.io/user/login", incognito=True)
    else:
        open_edge("https://comick.io/user/login", incognito=False)
    time.sleep(5)
    pyautogui.click(704,421)
def OpenWebSites():
    websites = [
        "https://youtube.com",
    ]
    for site in websites:
        if is_edge_running():
            open_edge(site, incognito=True)
        else:
            open_edge(site, incognito=False)
        time.sleep(3) 

# ===== TEST FUNCTIONS =====
gmail_login()
quipper_login()
OpenComicko()
OpenWebSites()
