# pip install selenium 셀레니움 설치
# 웹 드라이버 설치 chrome://version/ 버전 확인
# chromedriver 검색 > 확인한 버전에 맞는 드라이버 다운로드 후 워크스페이스에 압축 풀어 파일 넣기
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

# browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()  # 같은 경로 내에 있을 경우 크롬 드라이버의 경로를 적지 않아도 괜찮음

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()


# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)  # 3초 지연

# 5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료

'''
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()

DevTools listening on ws://127.0.0.1:61034/devtools/browser/b8686174-737c-4ef6-a32d-e4be6c838840
[1180:18516:0329/162342.844:ERROR:device_event_log_impl.cc(214)] [16:23:42.844] USB: usb_device_handle_win.cc:1056 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)       
[1180:18516:0329/162342.855:ERROR:device_event_log_impl.cc(214)] [16:23:42.855] USB: usb_device_handle_win.cc:1056 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)       
>>> browser.get("http://naver.com") 
>>> elem = browser.find_element_by_class_name("link_login")
>>> elem.click()
>>> browser.back()
>>> browser.forward()
>>> browser.refresh()
>>> browser.back()
>>> elem = browser.find_element_by_id("query")
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="4759aa5115c38f6a60b1e8fc1fca834c", element="a5eaf132-5ab6-405a-bfc1-32e06a3faeec")>
>>> from selenium.webdriver.common.keys import Keys # Keys.ENTER 를 위해!(글자 입력하는..거가튼..)
>>> elem.send_keys("나도코딩")
>>> elem.send_keys(Keys.ENTER)
>>> elem = browser.find_element_by_tag_name("a")
>>> elem = browser.find_elements_by_tag_name("a")
>>> for e in elem:         ef)
...     e.get_attribute("href")
>>> browser.get("http://daum.net")
>>> elem = browser.find_element_by_name("q")
>>> elem.send_keys("나도코딩")
>>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
>>> elem.click()
>>> browser.quit()
'''
