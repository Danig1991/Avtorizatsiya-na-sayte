import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# найти на странице элемент под id "user-name"
user_name = driver_chrome.find_element(By.ID, "user-name")

# пауза 2 секунды
time.sleep(2)

# установить в поле значение "standard_user"
user_name.send_keys("standard_user")

# найти на странице элемент под id "password"
password = driver_chrome.find_element(By.ID, "password")

# пауза 2 секунды
time.sleep(2)

# установить в поле значение "secret_sauce"
password.send_keys("secret_sauce")

# пауза 2 секунды
time.sleep(2)

# найти на странице элемент под id "login-button"
login_button = driver_chrome.find_element(By.ID, "login-button")
# нажать на кнопку
login_button.click()

# пауза 2 секунды
time.sleep(2)

# закрыть окно браузера
driver_chrome.close()