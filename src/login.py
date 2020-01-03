import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36")
# opts.add_argument('--headless')  # 无头模式

driver = webdriver.Chrome(chrome_options=opts)


def Login():
    driver.get("http://s.dianping.com/event/shenzhen")
    login = driver.find_element_by_xpath('//*[contains(text(),"登录")]')
    login.click()
    print('请扫描登录')
    sleep(10)
    dp = driver.get_cookie('dper')
    if dp is not None:
        print(dp)
        with open("dper.txt", "r+") as f:
            f.seek(0)
            f.write(dp['value'])
            # f.write('\r\n')
            print('登录成功，dper存入成功')
    else:
        print('未登录成功，dper存取失败')



#
# def writeCookies(cookies):
#     """
#     从浏览器中向文件写入cookies
#     """
#     with open("cookies.json", "w") as f:
#         json.dump(cookies, f)


if __name__ == '__main__':
    try:
        Login()
    except Exception as e:
        print(e)
    driver.quit()
    print('退出浏览器了')
