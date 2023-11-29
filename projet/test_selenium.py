from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = "T:\\Driver_web\\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8080/IT-exo-PHP_bug/projet/form.php")
driver.maximize_window()


jeuDeTest = [  
                ["Florent1", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent2", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent3", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent4", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent5", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent6", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent7", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent8", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent9", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
                ["Florent", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
            ]
for test in jeuDeTest : 
    time.sleep(0.5)
    driver.execute_script("document.getElementById('details').value= 'le champs est renseigné';")

    driver.find_element(By.ID, "firstName").send_keys(test[0])
    time.sleep(0.5)
    driver.find_element(By.ID, "lastName").send_keys(test[1])
    time.sleep(0.5)
    driver.find_element(By.ID, "username").send_keys(test[2])
    time.sleep(0.5)
    driver.find_element(By.ID, "address").send_keys(test[3])
    time.sleep(1)

    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="country"]/option[2]').click()

    time.sleep(0.5)

    driver.find_element(By.XPATH, '//*[@id="state"]/option[2]').click()

    time.sleep(0.5)
    driver.find_element(By.ID, "zip").send_keys(test[4])

    time.sleep(0.5)
    driver.find_element(By.ID, "cc-name").send_keys(test[5])


    time.sleep(0.5)
    driver.find_element(By.ID, "cc-number").send_keys(test[6])

    time.sleep(0.5)
    driver.find_element(By.ID, "cc-expiration").send_keys(test[7])

    time.sleep(0.5)
    driver.find_element(By.ID, "cc-cvv").send_keys(test[8]) 


    time.sleep(0.5)

    buttonContinue = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-block")
    driver.execute_script("arguments[0].click();", buttonContinue)

    # element = driver.find_element(By.ID, "submitForm")
    # driver.execute_script("arguments[0].click();", element)

    time.sleep(1)
    driver.get("http://127.0.0.1:8080/IT-exo-PHP_bug/projet/form.php")
    driver.maximize_window()


input() 



