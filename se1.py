from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 设置 Firefox 配置（如果需要）
options = Options()
options.headless = False  # 设为 True 则是无头模式，不显示浏览器界面

# 指定本地 Firefox 浏览器路径
options.binary_location = "C:/Users/r/Desktop/bin/firefox.exe"  # 本地 Firefox 路径

# 创建 Firefox 服务对象，指定 GeckoDriver 路径
service = Service(executable_path="geckodriver.exe")  # geckodriver 路径

# 创建 Firefox WebDriver 实例
driver = webdriver.Firefox(service=service, options=options)

# 访问 Google Scholar 页面
driver.get("https://scholar.google.com/")

# 等待页面加载完成
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gs_hdr_tsi"))
)

# 定位到搜索框并输入 "Geo-location"
search_box = driver.find_element(By.ID, "gs_hdr_tsi")
keywords = "geolocation machine learning"
search_box.send_keys(keywords)
search_box.send_keys(Keys.RETURN)  # 按下回车键进行搜索

for i in range(1,1000):
# 等待页面加载完成
# 等待搜索结果的最后一个部分加载
    WebDriverWait(driver, 180).until(
        EC.presence_of_element_located((By.ID, "gs_res_ccl_bot"))
    )

    # 执行 JavaScript 代码来获取第一个符合条件的 <a> 元素，并将其信息保存为 JSON 格式
    script = """
    const aElements = document.querySelectorAll('#gs_res_ccl_mid a');
    const result = [];  // 创建一个空数组，用于存储每个 <a> 元素的信息

    aElements.forEach(a => {
        if (a.hasAttribute('id')) {  // 检查是否有 'id' 属性
            const childNodes = [];
            a.childNodes.forEach(child => {
                // 如果是文本节点，直接添加到 childNodes
                if (child.nodeType === Node.TEXT_NODE) {
                    childNodes.push(child.nodeValue.trim());  // 获取文本节点的内容
                } 
                // 如果是元素节点，但不是 <b>，则直接添加元素节点的名称
                else if (child.nodeType === Node.ELEMENT_NODE && child.nodeName !== 'B') {
                    childNodes.push(child.nodeName);  // 获取元素节点的名称
                } 
                // 如果是 <b> 标签，获取其子节点并添加到 childNodes
                else if (child.nodeName === 'B') {
                    child.childNodes.forEach(grandChild => {
                        if (grandChild.nodeType === Node.TEXT_NODE) {
                            childNodes.push(grandChild.nodeValue.trim());  // 获取 <b> 子节点的文本内容
                        } else if (grandChild.nodeType === Node.ELEMENT_NODE) {
                            childNodes.push(grandChild.nodeName);  // 获取 <b> 子节点的元素名称
                        }
                    });
                }
            });
            
            const aInfo = {
                "href": a.href,  // a元素的文本内容
                "id": a.id,  // a元素的文本内容
                "childNodes": childNodes // a元素的所有子节点
            };

            result.push(aInfo);  // 将每个 aInfo 添加到数组中
        }
    });

    // 将结果转换为 JSON 格式
    return JSON.stringify(result, null, 2);  // 返回格式化后的 JSON 字符串
    """

    # 执行脚本并获取结果
    json_result = driver.execute_script(script)

    # 打印结果（你可以根据需要将结果保存到文件）
    print(json_result)

    # 保存 JSON 结果到文件
    with open(f'{keywords}_{i}.json', 'w', encoding='utf-8') as f:
        f.write(json_result)

    driver.execute_script("""
    const lastBElement = document.getElementById('gs_res_ccl_bot').querySelectorAll('b');
    if (lastBElement.length > 0) {
        lastBElement[lastBElement.length - 2].click();  // 点击最后一个 <b> 元素
    } else {
        console.log('没有找到 <b> 标签');
    }
    """)

    time.sleep(1)