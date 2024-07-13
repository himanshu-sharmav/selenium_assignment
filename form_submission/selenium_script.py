# form_submission/selenium_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def submit_form():
    driver = webdriver.Chrome()  
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    time.sleep(5)
    # Fill out the form
    # WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("Himanshu Sharma")
    # time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("8738059086")
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("himan9506492198@gmail.com")
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys("friends colony,muradnagar,ghaziabad.")
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("284001")
    # time.sleep(50)
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys("05")
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys("10")
    # time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys("2004")
    # time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("Male")
    # time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("GNFPYC")
    time.sleep(2)

    # time.sleep(50)


    # Submit the form
    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    time.sleep(2)

    # Wait for the confirmation page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]')))

    # Take a screenshot
    time.sleep(2)
    screenshot_path = "confirmation_screenshot.png"
    driver.save_screenshot(screenshot_path)

    driver.quit()
    return screenshot_path
# print(submit_form)
# submit_form.click(
if __name__ == "__main__":
    screenshot_path = submit_form()
    print(f"Screenshot saved at: {screenshot_path}")
