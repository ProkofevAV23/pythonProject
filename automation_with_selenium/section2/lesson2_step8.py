from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Smolensk@mail.ru")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__)) #получаем путь до папки, в которой лежит исполняемый файл,
                                                             # заранее создаем текстовый документ example.txt
    file_path = os.path.join(current_dir, 'example.txt') #добавляем к пути этот документ, получаем полный путь до него
    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']") #находим селектор кнопки Загрузить файл
    input4.send_keys(file_path) #не кликаем на неё, а отправляем путь к файлу через send_keys

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()