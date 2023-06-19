from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import base64
path=os.path.abspath('.') 
socks5Proxy="127.0.0.1:10808"
whatsAppUrl="https://web.whatsapp.com/"
profile = webdriver.FirefoxOptions()

# Socks5 Host SetUp:-
myProxy = socks5Proxy
ip, port = myProxy.split(':')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', ip)
profile.set_preference('network.proxy.socks_port', int(port))
#F spider
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# 启动 Firefox 浏览器并登录 WhatsApp
driver = webdriver.Firefox(options=profile)
#driver = webdriver.Firefox()
driver.get(whatsAppUrl)


loginCanvas = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'canvas'))
)
image_data = driver.execute_script('return arguments[0].toDataURL("image/png").substring(21);', loginCanvas)
# 去除类型，只要数据部分 
image_data = image_data[image_data.find(',') + 1:]

#loginImg=base64.b64decode(image_data)
with open("canvas.png", "wb") as f:
    f.write(base64.b64decode(image_data))
print("登陆好了直接回车")
t=input()
# wait = WebDriverWait(driver, 60)
# wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"]')))

# 循环检查所有会话
while True:
    print("开始摇滚吧")
    try:
        # 获取所有聊天
        chats = driver.find_elements(By.CSS_SELECTOR, '.lhggkp7q.ln8gz9je.rx9719la')
        print('chats',chats)
        # 对所有聊天进行循环._1pJ9J
        for chat in chats:
            print('chat',chat)
            isReaded = chat.find_elements(By.CSS_SELECTOR,'._1pJ9J')
            print('isReaded',isReaded)
            if isReaded:
                # 获取聊天标题和最后一条消息
                title_element = chat.find_element(By.CSS_SELECTOR,'.Hy9nV')
                #last_message_element = chat.find_element(By.XPATH, './/div[contains(@class,"_3ExzF")]//span[contains(@class,"selectable-text")]')

                # 获取聊天标题和最后一条消息的文本
                title = title_element.get_attribute('title')
                #last_message = last_message_element.text.strip()

                # 如果最后一条消息包含 "多少钱"，回复 "大挂壁"
                if "多少钱" in title:
                    title_element.click()
                    time.sleep(1)
                    input_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
                    for i in "40W开发费，买断，之后维护费另付，本软件仅供展示":
                        input_box.send_keys(i)
                    time.sleep(1)
                    input_box.send_keys(Keys.RETURN)
                    
                    #input_box.submit()
            else:
                # 如果元素不存在，进行其他处理
                print("E消息已读")
        # 暂停 5 秒后继续检查会话
        time.sleep(5)

    except Exception as e:
        print(f"发生错误：{e}")
        # 出现异常后等待 5 秒再继续执行
        time.sleep(5)
