# decoding uft-8
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import shutil
import threading
import os
import datetime
# data
path=os.path.abspath('.') 
socks5Proxy="127.0.0.1:10808"
whatsAppUrl="https://web.whatsapp.com/"

# cookie func
cookie_path='cookies.txt'

def randomNum():
    i=random.randint(1,3)
    return i

def errorTip():
        print("ERROr: SomeThing wen wrong!log will save to 'errorLog.txt'")
        file = open("errorLog.txt",mode="w")
        file.write(e)
        file.close()
class autoTwitter:
    #used images
    usedImgList=[]
    # is thread closed?
    close = False
    #load cookie   
    def save_cookie(self):
        cookies = self.driver.get_cookies()
        print(self.driver.get_cookies())
        f = open(cookie_path, 'wb')
        jsonCookies = json.dumps(cookies)
        with open(cookie_path, 'w') as f:
            f.write(jsonCookies)
        f.close()
        print('save cookie over')

    def load_cookie(self):
        with open(cookie_path, 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            print(cookie)
            self.driver.add_cookie(cookie)
        print("load cookie over")
        f.close()
        self.driver.get(whatsAppUrl)
        return self.driver
    def new_message(self):
        # 无限循环等待新消息
        while True:
            # 等待新消息出现
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._2hqOq")))

            # 获取最后一条消息
            messages = self.driver.find_elements_by_css_selector("div._2hqOq")
            last_message = messages[-1].find_element_by_css_selector("span.selectable-text")

            # 读取最后一条消息的文本
            text = last_message.text.strip()

            # 如果消息包含 "多少钱"，回复 "大挂壁"
            if "多少钱" in text:
                input_box = self.driver.find_element_by_css_selector("div._3FRCZ.copyable-text.selectable-text")
                input_box.send_keys("大挂壁")
                input_box.submit()
    def __init__(self):
        profile = webdriver.FirefoxOptions()

        # Socks5 Host SetUp:-
        myProxy = socks5Proxy
        ip, port = myProxy.split(':')
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', ip)
        profile.set_preference('network.proxy.socks_port', int(port))
        #F spider
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        #profile.set_preference("dom.webdriver.enabled", False)  # 设置非driver驱动
        #profile.set_preference('useAutomationExtension', False) #关闭自动化提示
        self.driver = webdriver.Firefox(options=profile)

        self.driver.get(whatsAppUrl)
        #self.load_cookie()
# manual post twitter
def manual(user):
    user.driver.get(whatsAppUrl+'/compose/tweet')
    print("please enter what you want to post")
    Etext = input()
    try:
        user.enterText(Etext)
        while True:
            print("please enter image name to add it. enter 'q' to quit")
            imgName=input()
            if imgName == 'q' or imgName == '':
                break
            user.enterImg(imgName)

        user.postTwi()
    except Exception as e:
        errorTip()
    # !!!important: clearing usedImgList
    user.usedImgList=[]
# auto send twitter
def auto(user):
    #read text use gbk
    file = open("postSentence.txt","r", encoding='utf-8', errors='ignore')
    
    while True:
        if user.close==True:
            user.close=False
            break
        user.driver.get(whatsAppUrl+'/compose/tweet')
        time.sleep(random.randint(5,10))
        #text
        line = file.readline()
        if not line:
            print("postSentence.txt is empty. Please write a new one")
            break
        user.enterText(line)
        #img
        filePath = path+"\\unimg\\"
        imgList=os.listdir(filePath)
        r=random.randint(1,4)
        for i in range(r):
            if len(imgList)<r:
                print("your images folder is empty. Please add new images")
                break
            user.enterImg(imgList[i])
        time.sleep(randomNum())
        #send
        try:
            user.postTwi()
        except Exception as e:
            errorTip()
            user.usedImgList=[]
                    # one hour to ten hours
            sendInterval=random.randint(3600,36000)
            print("now is ",int(datetime.datetime.now()))
            print("next post tweet in",datetime.timedelta(minutes=sendInterval),"\n has it been since",int(sendInterval/3600)," hours",int(sendInterval%3600/60),"minute")
        # !!!important: clearing usedImgList
        user.usedImgList=[]
        #time
        # one hour to ten hours
        sendInterval=random.randint(3600,36000)
        print("now is ",datetime.datetime.now())
        print("next post tweet in",datetime.timedelta(minutes=sendInterval),"\n has it been since",int(sendInterval/3600)," hours",int(sendInterval%3600/60),"minute")
        time.sleep(sendInterval)
    file.close()
        
#driver.quit()
print("财神到")
user01=autoTwitter()

while True:
    print(r'''
菜单
1. 保存cookie
2. 载入cookie
3. 手动发推
4. 无人值守自动发推（载入登录成功的cookie才可开启）
5. 停止无人值守
0. 退出
    ''')
    try:
        i=int(input())
        if i == 1:
            user01.save_cookie()
        if i == 2:
            user01.load_cookie()
        if i == 3:
            manual(user01)
        if i == 4:
        # more thread
            new_thread = threading.Thread(target=auto, args=(user01,), name="T1")
            new_thread.start()
        if i == 5:
            #user01.driver.close()
            #new_thread.shutdownThread()
            user01.close=True
        if i == 0:
            user01.driver.close()
            exit()
    # if make some error
    except Exception as e:
        errorTip()

        
#save cookie
#save_cookie(driver)
# post text
# 等待页面加载
# driver.implicitly_wait(10)
# tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']/div/div/div/div[2]")
# tweet.send_keys("""Hello World!""")
# tweet.send_keys(Keys.COMMAND, Keys.ENTER)


# Post img
# element  = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input").send_keys(r'D:\工作\小外包\自动推特机器人\unimg\123.jpg')
# time.sleep(randomNum())
# element  = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input").send_keys(r'D:\工作\小外包\自动推特机器人\unimg\963.jpg')
# driver.execute_script("", element)

# # post
# time.sleep(randomNum())
# tweet_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
# tweet_button.click()
#element.send_keys(filePath)