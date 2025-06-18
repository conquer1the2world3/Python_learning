import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException
import time

def setup_driver():
    """设置并返回Edge浏览器驱动"""
    try:
        # 1. 配置驱动路径
        service = EdgeService(executable_path=r"C:\Users\ASUS\WebDriver\edgedriver_win64\msedgedriver.exe")

        # 2. 绕过安全检测
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 4. 启动浏览器
        driver = webdriver.Edge(service=service, options=options)
        return driver
    
        
    except WebDriverException as e:
        print(f"浏览器驱动错误: {str(e)}")
        print("请确保：")
        print("1. Edge浏览器已安装")
        print("2. 网络连接正常")
        raise
    except Exception as e:
        print(f"发生未知错误: {str(e)}")
        raise

def capture_product_images(driver, product_url):
    """抓取单个商品的图片"""
    try:
        # 打开商品链接
        driver.get(product_url)
        time.sleep(2)  # 等待页面加载
        
        # 点击"商品详情"按钮
        detail_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '商品详情')]"))
        )
        detail_button.click()
        time.sleep(3)  # 等待详情页加载
        
        # 模拟按下 ALT + Z
        webdriver.ActionChains(driver).key_down(Keys.ALT).send_keys('z').key_up(Keys.ALT).perform()
        time.sleep(2)  # 等待抓图插件响应
        
        # 点击"全选"按钮
        select_all = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '全选')]"))
        )
        select_all.click()
        time.sleep(1)
        
        # 点击"下载"按钮
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '下载')]"))
        )
        download_button.click()
        time.sleep(3)  # 等待下载完成
        
        print(f"成功抓取商品图片: {product_url}")
        return True
        
    except Exception as e:
        print(f"抓取商品图片时出错: {str(e)}")
        return False

def main():
    # 读取Excel文件
    excel_path = r"D:\Downloads\【6.9-核心价】倍轻松&wacaco品牌.xlsx"
    sheet_name = "倍轻松"  # 设置要读取的表格名称
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    
    # 设置浏览器驱动
    driver = setup_driver()
    
    try:
        # 遍历商品链接
        for index, row in df.iterrows():
            if pd.notna(row['链接']):  # 确保链接不为空
                print(f"正在处理第 {index + 1} 个商品...")
                capture_product_images(driver, row['链接'])
                time.sleep(2)  # 等待一段时间再处理下一个商品
                
    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    main() 