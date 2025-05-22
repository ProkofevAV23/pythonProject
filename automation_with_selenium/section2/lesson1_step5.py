from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

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

    # Отмечаем checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox.form-check-input").click()

    # Выбираем radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule.form-check-input").click()

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
