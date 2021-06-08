from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
#loginname="201894069"
name = "201894108"
password = "123456"
screenshot_path="/Users/sunzhengyu/Desktop/japt/"

options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
browser = webdriver.Chrome("/Users/sunzhengyu/Desktop/chromedriver_mac64/chromedriver", options=options)

browser.get("http://106.3.22.13:8230")


def screenshot(fileName) :
    browser.get_screenshot_as_file(screenshot_path+fileName+".png")


def wait_and_cut(fileName):
    sleep(2)
    screenshot(fileName)
    sleep(1)


def input(xPath,content):
    sleep(1)
    browser.find_element_by_xpath(xPath).send_keys(content)
    sleep(1)


def click(xPath):
    browser.find_element_by_xpath(xPath).click()


sleep(3)
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div[1]/div/input").send_keys(name)
sleep(1)
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div[2]/div/input").send_keys(password)
sleep(1)
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div[4]/button").click()

sleep(3)

try:
    #browser.get_screenshot_as_file("/Users/sunzhengyu/Desktop/japt/step0_enter.png")
    screenshot("step0_login")

except BaseException as msg:
    print(msg)

sleep(2)
# /html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[3]
# /html/body/div/div/div[2]/div[2]/div[1]/div/ul
#                                       '//*[@id="app"]/div/div[1]/div[2]/div[1]/div
#while :
# //*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/svg
# # //*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]
openbar=browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[1]/div[1]/div[1]")
ActionChains(browser).click(openbar).perform()
sleep(2)

bxmgl=browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]")
ActionChains(browser).click(bxmgl).perform()
sleep(2)
sxmgl=browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/li/ul/div/a/li")
ActionChains(browser).click(sxmgl).perform()
sleep(2)
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/section/div/div[2]/div[1]/ul/li[1]/button").click()
sleep(2)

browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div[1]/input").send_keys(name)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[2]/div/div/div/input").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]").click()
sleep(2)
screenshot("step1.1")
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/div/button[2]").click()
sleep(2)
screenshot("step1.2")
ActionChains(browser).click(openbar).perform()
sleep(1)
#测试环境，配置管理
# browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[4]/li/div").click()
# sleep(1)
# browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[4]/li/ul/div/a/li").click()
# sleep(1)
##压力机
# browser.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div[2]/div[1]/ul/li[1]/button").click()
# input("/html/body/div[2]/div/div[2]/form/div[1]/div/div[1]/input", name)
# input("/html/body/div[5]/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input", "10.114.10.69")
# click("/html/body/div[8]/div/div[2]/form/div[2]/div[2]/div/div/div/label[1]/span[1]/span")#是
# click("/html/body/div[7]/div/div[2]/form/div[3]/div[1]/div/div/div/div")
# click("/html/body/div[8]/div[1]/div[1]/ul/li[@]")

#测试准备
click("/html/body/div[1]/div/div[2]/div[2]/div[1]/div/ul/div[5]/li/div")
sleep(1)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[5]/li/ul/div[1]/a/li")
sleep(3)
input("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]/input", name)
click("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/input")
sleep(2)
click("/html/body/div[2]/div[1]/div[1]/ul/li/span[text()='"+name+"']/..")

click("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div")
sleep(3)
click("/html/body/div[3]/div[1]/div[1]/ul/li/span[text()='http']/..")
input("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div[1]/input","www.baidu.com")

input("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div/div[1]/input","80")#port

input("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div/div[1]/input","/")

click("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/form/div[3]/div[1]/div/div/div/label[3]/span[1]/span")#Get

click("/html/body/div/div/div[2]/section/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/button")
sleep(6)
wait_and_cut("step2tiaoshi")
click("/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/div[2]/button[2]")
sleep(1)
ActionChains(browser).click(openbar).perform()
sleep(1)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[5]/li/ul/div[2]/a/li")
sleep(2)
wait_and_cut("step2.2screenshotguanli")
ActionChains(browser).click(openbar).perform()
sleep(1)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[5]/li/ul/div[4]/a/li")
sleep(2)
click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/ul/li[1]/button")
sleep(2)
       #/html/body/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]/input
input("/html/body/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]/input", name)
    #/html/body/div[2]/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/input
click("/html/body/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/input")
sleep(3)
      #/html/body/div[3]/div/div[2]/div[1]/form/div[1]/div[3]/div/div/div/input
      #/html/body/div[5]/div[1]/div[1]/ul/li[1]
click("/html/body/div/div[1]/div[1]/ul/li/span[text()='"+name+"']/..")
input("/html/body/div/div/div[2]/div[1]/form/div[1]/div[3]/div/div/div/input", name)
input("/html/body/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div[1]/textarea", "pass")#预期结果
input("/html/body/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/textarea", name)
sleep(2)
 #     "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/div/span[text()='"+name+"']/../../label/span/span"
        #/html/body/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span
click("/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span")
      #  /html/body/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span
#click("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/div/span[text()='"+name+"']/../../label/span/span")
sleep(2)
        #/html/body/div[3]/div/div[2]/div[2]/div/div[2]/button[1]/span/span
click("/html/body/div/div/div[2]/div[2]/div/div[2]/button[1]/span/span")
sleep(2)
wait_and_cut("step2.3anlidesign")
click("/html/body/div/div/div[3]/span/button[2]")
wait_and_cut("step2.4outcome")
ActionChains(browser).click(openbar).perform()
sleep(2)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[6]/li/div")
sleep(2)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[6]/li/ul/div[1]/a/li")
sleep(5)
        #/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[5]/div/span[1]/div/span
click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[4]/div/button[1]")
sleep(2)
click("/html/body/div[1]/div/div[2]/section/div/div[3]/div/div/div[2]/div/form/div[1]/div/div/span[2]/i")
input("/html/body/div[1]/div/div[2]/section/div/div[3]/div/div/div[2]/div/form/div[2]/div/div/div/input", "10")
input("/html/body/div[1]/div/div[2]/section/div/div[3]/div/div/div[2]/div/form/div[3]/div/div/div/input", "10")
wait_and_cut("step3.1YiJianSetting")
click("/html/body/div[1]/div/div[2]/section/div/div[3]/div/div/div[2]/div/div[1]/button[2]")

sleep(2)
#time setting
click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[4]/div/button[2]")
input("/html/body/div[1]/div/div[2]/section/div/div[4]/div/div/div[2]/div/form/div/div/div/div/input", "1")
wait_and_cut("step3.2timesetting")
click("/html/body/div[1]/div/div[2]/section/div/div[4]/div/div/div[2]/div/div[1]/button[2]")
sleep(2)

#执行
click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[5]/div/span[1]/div/span")
sleep(2)
click("/html/body/div[1]/div/div[2]/section/div/div[5]/div/div/div[3]/div/button[2]")
sleep(120)

click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div/button")

wait_and_cut("step4.1inspect")
    #/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div/button/span
    #/html/body/div[1]/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[7]/div/button[2]
try:
    click("/html/body/div[3]/div/div[1]/button/i")
except:
    click("/html/body/div/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div/button")
    sleep(3)
    wait_and_cut("step4.1inspect")
    click("/html/body/div[3]/div/div[1]/button/i")
sleep(3)
click("/html/body/div[1]/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[7]/div/button[2]")
input("/html/body/div[4]/div/div[2]/div/div[1]/div[2]/p[1]/span[2]/div/input", name)
sleep(2)
wait_and_cut("step3.3baogao")
click("/html/body/div[4]/div/div[2]/div/div[1]/div[2]/p[4]/button")

sleep(2)
#openbar=browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[1]/div[1]/div[1]")
ActionChains(browser).click(openbar).perform()
sleep(2)
click("/html/body/div/div/div[2]/div[2]/div[1]/div/ul/div[6]/li/ul/div[2]/a/li")
wait_and_cut("step4existconfirm")
click("/html/body/div[1]/div/div[2]/section/div/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[5]/div/button[1]")





sleep(60)


browser.quit()

