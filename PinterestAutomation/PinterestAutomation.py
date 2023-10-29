import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import schedule

service = Service(ChromeDriverManager().install());
options = webdriver.ChromeOptions();
options.add_argument("--disable-notifications");
driver = webdriver.Chrome(options = options,service = service);

driver.implicitly_wait(60);

class Pinterest():
    driver.get('https://br.pinterest.com/');
    driver.maximize_window();
    driver.find_element("xpath",'//div[text()="Entrar"]').click();
    driver.find_element("xpath", '//*[@id="email"]').send_keys('leocordeiro09@gmail.com');
    driver.find_element("xpath", '//*[@id="password"]').send_keys('Teste@123');
    driver.find_element("xpath", '//button/div[text()="Entrar"]').click();
    driver.find_element("xpath", '//span[text()="Criar"]').click();
    driver.find_element("xpath", '//span[text()="Criar Pin"]').click();
    time.sleep(2);
    driver.find_element("xpath", '//input[@aria-label="Upload de arquivo"]').send_keys(r'C:\Users\User_\source\repos\PinterestAutomation\PinterestAutomation\kiluaa.png');
    driver.find_element("xpath",'//br[@data-text="true"]').send_keys("Teste")
    driver.find_element("xpath", '//button/div[text()="Salvar"]').click(); 
    time.sleep(15);
      
     