from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "https://suninjuly.github.io/selects1.html"
    # link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
        return str(int(x) + int(y))

    # Грабаем значение х и y
    x_element = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
    y = y_element.text

    # Считаем z
    z = calc(x, y)

    # Ищем z в выпадающем списке и кликаем
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{z}']").click()

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
