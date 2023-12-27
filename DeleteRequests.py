from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import pyperclip
import time


options = webdriver.ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

#로그인 구현 
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
driver.get(login_url)
pyperclip.copy("godgodgod96")
driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL, 'V')
pyperclip.copy("akekfk123!")
driver.find_element(By.ID, 'pw').send_keys(Keys.CONTROL, 'V') 
driver.find_element(By.XPATH, '//*[@id="log.login"]/span').click()
driver.implicitly_wait(3)

#유저 블로그 아이디 가져오기
blog_url = 'https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0'
driver.get(blog_url)
driver.find_element(By.CSS_SELECTOR,'#container > div > aside > div > div:nth-child(1) > nav > a:nth-child(1)').click()
driver.implicitly_wait(3)
all_window_handles = driver.window_handles
new_window_handle = all_window_handles[-1]
driver.switch_to.window(new_window_handle)
blog_id = driver.current_url.replace('https://blog.naver.com/','')
time.sleep(1.5)
print("블로그 아이디:",blog_id)

#블로그 관리 페이지로 이동 구현 
admin_url =f'https://admin.blog.naver.com/BuddyInviteSentManage.naver?blogId={blog_id}'
driver.get(admin_url)
driver.implicitly_wait(3)
time.sleep(1.3)

#서로이웃 신청 취소 구현 
while(True):
    driver.find_element(By.CSS_SELECTOR,'#invite > table > thead > tr > th.checkwrap > input').click()
    driver.implicitly_wait(3)
    delete_button = driver.find_element(By.CSS_SELECTOR,'#invite > div.action2.neighborlist > div > span > button')
    delete_button.click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    if alert_text == '신청취소할 사람을 먼저 선택해주세요.':
        print("모든 요청 삭제 완료.")
        break
    print("Alert 내용:", alert_text)
    alert.accept()
    driver.implicitly_wait(3)
    alert.accept()
    driver.implicitly_wait(3)
    time.sleep(3)