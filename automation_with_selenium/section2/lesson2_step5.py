from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # Находим и считаем х
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Прокручиваем страницу вниз на 200 пикселей
    browser.execute_script("window.scrollBy(0, 200);")

    # Вводим y в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox.form-check-input").click()

    # Выбираем radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule.form-check-input").click()

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()