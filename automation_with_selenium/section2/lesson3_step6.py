from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Нажимаем на летающую кнопку
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Считаем y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Грабаем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Вводим х в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    input1.send_keys(y)

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()