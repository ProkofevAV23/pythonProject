from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считаем y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Грабаем значение х
    chest_element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x = chest_element.get_attribute("id")
    y = calc(x)

    # Вводим х в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox.check-input").click()

    # Выбираем radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule.check-input").click()

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
