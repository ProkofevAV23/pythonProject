from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_class_name_1(self):
        link = "https://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("Smolensk@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)

    def test_class_name_2(self):
        link = "https://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("Smolensk@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
