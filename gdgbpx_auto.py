from selenium import webdriver
import pyautogui
import time
import math


def switch2frame(par):
    par.switch_to.frame('secondIframe')
    par.switch_to.frame('thirdIframe')
    par.switch_to.frame('dataMainIframe')


def run_main(video_unstudy_num, browser):
    if int(video_unstudy_num) > 0:
        print("nonlocal--当前页下还有{}个视频未学习……".format(video_unstudy_num))
        js_click = 'document.getElementsByClassName("courseware-list-reed")[0].click()'
        browser.execute_script(js_click)
        time.sleep(3)
        # 拿到所有的窗口
        all_handles = browser.window_handles
        pre_window_handle = browser.current_window_handle
        for handle in all_handles:
            if handle != pre_window_handle:
                browser.switch_to.window(handle)
                browser.implicitly_wait(10)
                # time.sleep(10)
                # elem = browser.find_element_by_class_name("introjs-button")
                # elem = browser.find_element_by_link_text('好的，我知道了')
                # elem.click()
                time.sleep(2)
                browser.switch_to.frame('course_frame')
                time.sleep(10)
                # 点击播放
                js_paused = 'return document.getElementById("my-video_html5_api").paused;'
                view_paused_status = browser.execute_script(js_paused)
                print('viewPaused：' + str(view_paused_status))
                # false 点击了播放  true 点击了暂停
                if view_paused_status:
                    elem = browser.find_element_by_class_name("vjs-play-control")
                    elem.click()
                time.sleep(5)
                # 获取视频播放时长?
                js_duration_str = 'return document.getElementById("my-video_html5_api").duration;'
                view_time = browser.execute_script(js_duration_str)
                print('viewTime:' + str(view_time))
                time.sleep(5)
                js_current_time_str = 'return document.getElementById("my-video_html5_api").currentTime;'
                view_current_time = browser.execute_script(js_current_time_str);
                print('viewCurrentTime:' + str(view_current_time))

                if math.ceil(view_current_time) >= math.ceil(view_time):
                    print('1111')
                    browser.switch_to.default_content()
                    elem = browser.find_element_by_id('btnexit')
                    elem.click()
                    # 关闭视频网站页面 进入pre_window_handle页面
                    browser.switch_to.window(pre_window_handle)
                    browser.refresh()
                    browser.implicitly_wait(10)
                    switch2frame(browser)
                    js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
                    video_unstudy_num = browser.execute_script(js_list)
                    time.sleep(3)
                    # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                    run_main(video_unstudy_num, browser)
                else:
                    time.sleep(math.ceil(view_time) - math.ceil(view_current_time))
                    browser.switch_to.default_content()
                    elem = browser.find_element_by_id('btnexit')
                    elem.click()
                    # 关闭视频网站页面 进入pre_window_handle页面
                    browser.switch_to.window(pre_window_handle)
                    browser.refresh()
                    browser.implicitly_wait(10)
                    switch2frame(browser)
                    js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
                    video_unstudy_num = browser.execute_script(js_list)
                    time.sleep(3)
                    # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                    run_main(video_unstudy_num, browser)
    else:
        print("该目录下还有视频已学习完毕……")


def main():
    # 输入账号
    username = "******"
    # 输入密码
    passwd = "******"
    login_url = 'https://gbpx.gd.gov.cn/gdceportal/index.aspx'
    option = webdriver.ChromeOptions()
    option.add_argument('--mute-audio')
    browser = webdriver.Chrome(options=option)
    browser.get(login_url)
    browser.implicitly_wait(10)
    # 窗口最大化
    browser.maximize_window()
    elem = browser.find_element_by_xpath('//*[@id="pnlLogin"]/div[1]/div[2]')
    elem.click()
    time.sleep(1)
    elems = browser.find_elements_by_class_name("nav-items")
    elems[0].click();
    time.sleep(1)
    elem = browser.find_element_by_id("txtLoginName")
    elem.clear()
    elem.send_keys(username)
    time.sleep(1)
    elem = browser.find_element_by_id("txtPassword")
    elem.clear()
    elem.send_keys(passwd)
    time.sleep(1)
    # 验证码
    code_num = pyautogui.prompt("请输入验证码:")
    elem = browser.find_element_by_id("txtValid")
    elem.clear()
    elem.send_keys(code_num)
    elem = browser.find_element_by_xpath('//*[@id="user-login-form"]/div[2]/input[1]')
    elem.click()
    time.sleep(3)
    elems = browser.find_elements_by_class_name("is-round");

    elems[0].click();
    time.sleep(3)
    elem = browser.find_element_by_id('btnStudy')
    elem.click()
    time.sleep(3)
    # browser.switch_to_frame('secondIframe')
    # browser.switch_to.frame('secondIframe')
    # browser.switch_to.frame('thirdIframe')
    # browser.switch_to.frame('dataMainIframe')
    switch2frame(browser)
    time.sleep(1)

    js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
    video_unstudy_num = browser.execute_script(js_list)
    time.sleep(3)
    run_main(video_unstudy_num, browser)
    browser.close()
    print("end......")


if __name__ == '__main__':
    main()