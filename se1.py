from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# 设置 Firefox 配置（如果需要）
options = Options()
options.headless = False  # 设为 True 则是无头模式，不显示浏览器界面

# 指定本地 Firefox 浏览器路径
options.binary_location = "C:/Users/r/Videos/firefox-128.7.0.en-US.win64/firefox/firefox.exe"  # 本地 Firefox 路径

# 创建 Firefox 服务对象，指定 GeckoDriver 路径
service = Service(executable_path="geckodriver.exe")  # geckodriver 路径

# 创建 Firefox WebDriver 实例
driver = webdriver.Firefox(service=service, options=options)

def search_and_scrape(driver, keywords):
    # 等待 5 分钟（300秒）    
    # 启动浏览器并访问 Google 学术
    driver.get('https://scholar.google.com')


    # 等待页面加载完成
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "gs_hdr_tsi"))
    )

    # 定位到搜索框并输入关键词
    search_box = driver.find_element(By.ID, "gs_hdr_tsi")
    search_box.send_keys(keywords)
    search_box.send_keys(Keys.RETURN)  # 按下回车键进行搜索

    # 进行100页的抓取
    for i in range(1, 101):  # 循环 100 次，抓取 100 页
        # 等待页面加载完成
        WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.ID, "gs_res_ccl_bot"))
        )

        # 执行 JavaScript 代码来获取符合条件的 <a> 元素，并将其信息保存为 JSON 格式
        script = """
        const aElements = document.querySelectorAll('#gs_res_ccl_mid a');
        const result = [];
        aElements.forEach(a => {
            if (a.hasAttribute('id')) {
                const childNodes = [];
                a.childNodes.forEach(child => {
                    if (child.nodeType === Node.TEXT_NODE) {
                        childNodes.push(child.nodeValue.trim());
                    } else if (child.nodeType === Node.ELEMENT_NODE && child.nodeName !== 'B') {
                        childNodes.push(child.nodeName);
                    } else if (child.nodeName === 'B') {
                        child.childNodes.forEach(grandChild => {
                            if (grandChild.nodeType === Node.TEXT_NODE) {
                                childNodes.push(grandChild.nodeValue.trim());
                            } else if (grandChild.nodeType === Node.ELEMENT_NODE) {
                                childNodes.push(grandChild.nodeName);
                            }
                        });
                    }
                });
                
                const aInfo = {
                    "href": a.href,
                    "id": a.id,
                    "childNodes": childNodes
                };

                result.push(aInfo);
            }
        });

        return JSON.stringify(result, null, 2);
        """

        # 执行脚本并获取结果
        json_result = driver.execute_script(script)

        # 打印结果（你可以根据需要将结果保存到文件）
        print(json_result)

        # 保存 JSON 结果到文件
        with open(f'folder/{keywords}_{i}.json', 'w', encoding='utf-8') as f:
            f.write(json_result)

        # 点击下一页
        driver.execute_script("""
        const lastBElement = document.getElementById('gs_res_ccl_bot').querySelectorAll('b');
        if (lastBElement.length > 0) {
            lastBElement[lastBElement.length - 2].click();  // 点击最后一个 <b> 元素
        } else {
            console.log('没有找到 <b> 标签');
        }
        """)

        time.sleep(30)

# 等待并点击 Tor 浏览器的 "Connect" 按钮

try:
    connect_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "connectButton"))  # 假设按钮 ID 为 "connectButton"
    )
    connect_button.click()

    # 等待直到 "Connect" 按钮消失，表示连接成功
    WebDriverWait(driver, 120).until(
        EC.invisibility_of_element_located((By.ID, "connectButton"))
    )
    print("Connected to Tor Network!")
    time.sleep(1)

    # 暂停，等待手动处理弹窗

    # Tor 网络连接成功后，你可以继续执行其他操作
    driver.get("https://scholar.google.com/")
    
    try:
        # 如果是确认框或其他类型的弹窗，可以使用以下方式处理
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()  # 或者用 dismiss() 关闭
        print("弹窗已关闭")
    except Exception as e:
        print(f"没有弹窗或处理失败: {e}")

    input("请手动关闭弹窗后按 Enter 继续...")

    
finally:
    

    

# 主程序循环
    while True:
        # 等待用户输入关键词
        keywords = input("请输入搜索关键词（或输入 'exit' 退出）：")
        if keywords.lower() == 'exit':
            print("退出程序")
            break
        else:
            # 执行搜索并抓取100页数据
            search_and_scrape(driver,keywords)