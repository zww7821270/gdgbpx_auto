from selenium import webdriver
import pyautogui
import time
import string
import math


def switch2frame(par):
    par.switch_to.frame('secondIframe')
    par.switch_to.frame('thirdIframe')
    par.switch_to.frame('dataMainIframe')


def main():
    # 输入账号
    username = "15876540864"
    # 输入密码
    passwd = "xfks1234"
    login_url = 'http://xfks-study.gdsf.gov.cn/'
    option = webdriver.ChromeOptions()
    option.add_argument('--mute-audio')
    browser = webdriver.Chrome(options=option)
    browser.get(login_url)
    browser.implicitly_wait(10)
    # 窗口最大化
    browser.maximize_window()
    time.sleep(2)
    elem = browser.find_element_by_name("mobile")
    elem.clear()
    elem.send_keys(username)
    time.sleep(2)
    elem = browser.find_element_by_name("password")
    elem.clear()
    elem.send_keys(passwd)
    time.sleep(2)
    # 验证码
    code_num = pyautogui.prompt("请输入验证码:")
    elem = browser.find_element_by_name("captcha")
    elem.clear()
    elem.send_keys(code_num)
    elem = browser.find_element_by_name('submit')
    elem.click()
    time.sleep(5)
    #switch2frame(browser)
    studyKind = ["a_a_course_dgdz", "a_a_xjpfzsx"]
    for kind in studyKind:
        run_kind(browser, kind)






    # switch2frame(browser)
    # time.sleep(1)
    #
    # js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
    # video_unstudy_num = browser.execute_script(js_list)
    time.sleep(5)

    #browser.close()
    print("end......")

def run_kind(browser,kind):
    js_list = 'return document.querySelectorAll(\'''div[catalog="'+kind+'"]\''').length;'
    courseKind = browser.execute_script(js_list)
    print(kind + "--当前分类下还有{}个课程……".format(courseKind))
    inx = 1
    while inx <= courseKind:
            # 点击左侧学习分类
            elem = browser.find_element_by_xpath(
            '//div[@class="film_focus_desc"]/ul[@class="film_focus_nav"]/li[@cl="' + kind + '"]')
            elem.click();
            time.sleep(1)
            path = '//ul[@class="film_focus_imgs"]/li[@cl="' + kind + '"]/div[' + str(inx + 1) +']'
            elem = browser.find_element_by_xpath(path)
            if ('100' in elem.text):
                print(elem.text + ",已经完成")
            else:
                # 进入课程
                btn = browser.find_element_by_xpath('//ul[@class="film_focus_imgs"]/li[@cl="' + kind + '"]/div[' + str(inx + 1) +']/div[1]/h3[1]/a[1]')
                btn.click();
                time.sleep(2)
                run_chapter(browser)
            inx = inx + 1
        # except:
        #     print("课程已学完，下一课程")
        # inx = inx + 1


def run_chapter(browser):

    js_list = 'return document.querySelectorAll(\'''li[chapter-type="0"]\''').length;'
    chapterCount = browser.execute_script(js_list)
    print("--当前课程下还有{}个章节……".format(chapterCount))
    cat = 1
    while cat < chapterCount:
        elem = browser.find_element_by_id('chapter-1205').find_element_by_xpath('//ul[1]/li['+str(cat + 1)+']/table[1]')
        elem.click()
        time.sleep(1)
        js_list = 'saveRecord(1);'
        browser.execute_script(js_list)
        cat = cat + 1
        btn = browser.find_element_by_tag_name("button")
        btn.click()
        time.sleep(1)
    btn = browser.find_element_by_class_name("menu-ic-note")
    btn.click();

if __name__ == '__main__':
    main()