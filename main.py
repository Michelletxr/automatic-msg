from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=_ZDBVeqyK6g&t=260s")