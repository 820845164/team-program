import time

from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
path =r'C:\Users\ChenBenYuan\AppData\Local\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("http://s.manmanbuy.com/Default.aspx?key=%B6%FE%BC%D7%CB%AB%EB%D2&btnSearch=%CB%D1%CB%F7")
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
button = driver.find_element_by_xpath("//div[@class='bjlineSmall singlebj bj_2687420905']/div[@class='cost']/div[@class='p AreaPrice']/span[@class='poptrend']/a").get_attribute("href")
# print(button)
driver.get(button)
Action = ActionChains(driver)
# time.sleep(5)
# button.click()
# time.sleep(2)
# driver.save_screenshot('mangmangmai6.png')
# js = 'document.getElementById("SM_BTN_WRAPPER_1").click();'
# driver.execute_script(js)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })
button2 = driver.find_element_by_xpath("/html/body/div/div/div/div[position()=1]")
# button2.click()
Action.move_to_element(button2).click().perform()
time.sleep(5)
button3 = driver.find_element_by_xpath("/html/body/div/div/div/div[position()=3]/div[position()=1]/div/div[position()=1]/span")
Action.move_to_element(button3).click_and_hold().perform()
Action.move_by_offset(258,0)
# 第三步：释放鼠标
Action.release()
# 执行动作
Action.perform()
time.sleep(3)
bottom = 'document.documentElement.scrollTop=100000'
driver.execute_script(bottom)
time.sleep(3)
driver.save_screenshot('mangmangmai2.png')  # 一次截图：形成全图

left = 100
top =  130
right = left + 1700  # 区块截图右下角在网页中的x坐标
bottom = top + 650  # 区块截图右下角在网页中的y坐标
# print({"left": left, "top": top, "right": right, "bottom ": bottom})
# print("baidu.size['width']:%s" % baidu.size['width'])
# print("baidu.size['height']:%s" % baidu.size['height'])
picture = Image.open('mangmangmai2.png')
picture = picture.crop((left, top, right, bottom))  # 二次截图：形成区块截图
picture.save(r'photo2.png')
# driver.quit()

# button2.click()
# time.sleep(5)

# button2.click()
# time.sleep(15)
# driver.save_screenshot('mangmangmai4.png')