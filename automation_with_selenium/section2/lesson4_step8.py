from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

try:

    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока текст у локатора станет нужным
    WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    browser.find_element(By.ID, "book").click()

    # Прокручиваем страницу вниз на 200 пикселей
    browser.execute_script("window.scrollBy(0, 200);")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Находим и считаем х
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Вводим y в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button#solve.btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()