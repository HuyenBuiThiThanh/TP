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
log_file = "LOG/log.txt"
driver.get("http://127.0.0.1:8080/IT-exo-PHP_bug/projet_loading/form.php")
driver.maximize_window()

# jeuDeTest = [  
#                 [ "Florent1", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
#                 ["Florent2", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
#                 ["Florent3", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ],
#             ]

jeuDeTest = [
                { "firstName":"Florent1", "lastName":"Bailly", "username":"Huy" , "adress":"11 rue de it 69000 Lyon", "zip":"123", "cc-name":"Huyen", "cc-number":"00001111", "cc-expiration":"9/24" , "cc-cvv":"zip" },
                { "firstName":"Florent2", "lastName":"Bailly", "username":"Huy" , "adress":"11 rue de it 69000 Lyon", "zip":"123", "cc-name":"Huyen", "cc-number":"00001111", "cc-expiration":"9/24" , "cc-cvv":"zip" },
                { "firstName":"Florent3", "lastName":"Bailly", "username":"Huy" , "adress":"11 rue de it 69000 Lyon", "zip":"123", "cc-name":"Huyen", "cc-number":"00001111", "cc-expiration":"9/24" , "cc-cvv":"zip" },
                { "firstName":"Florent4", "lastName":"Bailly", "username":"Huy" , "adress":"11 rue de it 69000 Lyon", "zip":"123", "cc-name":"Huyen", "cc-number":"00001111", "cc-expiration":"9/24" , "cc-cvv":"zip" },
]

with open(log_file, 'w', encoding = "UTF-8") as file:
    file.write("")


for test in jeuDeTest : 
    try:   
        driver.execute_script("document.getElementById('details').value= 'le champs est renseigné' ")
        # driver.execute_script("document.getElementById('details').value= ' " + test[0] + " ' ")


        # driver.find_element(By.ID, "firstName").send_keys(test[0])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "lastName").send_keys(test[1])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "username").send_keys(test[2])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "address").send_keys(test[3])


        driver.find_element(By.ID, "firstName").send_keys(test["firstName"])
        time.sleep(0.1)
        driver.find_element(By.ID, "lastName").send_keys(test["lastName"])
        time.sleep(0.1)
        driver.find_element(By.ID, "username").send_keys(test["username"])
        time.sleep(0.1)
        driver.find_element(By.ID, "address").send_keys(test["adress"])
   

        driver.find_element(By.XPATH, '//*[@id="country"]/option[2]').click()
        time.sleep(0.1)
        driver.find_element(By.XPATH, '//*[@id="state"]/option[2]').click()
        time.sleep(0.1)

        # driver.find_element(By.ID, "zip").send_keys(test[4])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "cc-name").send_keys(test[5])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "cc-number").send_keys(test[6])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "cc-expiration").send_keys(test[7])
        # time.sleep(0.1)
        # driver.find_element(By.ID, "cc-cvv").send_keys(test[8]) 
        # time.sleep(0.1)


        driver.find_element(By.ID, "zip").send_keys(test["zip"])
        time.sleep(0.1)
        driver.find_element(By.ID, "cc-name").send_keys(test["cc-name"])
        time.sleep(0.1)
        driver.find_element(By.ID, "cc-number").send_keys(test["cc-number"])
        time.sleep(0.1)
        driver.find_element(By.ID, "cc-expiration").send_keys(test["cc-expiration"])
        time.sleep(0.1)
        driver.find_element(By.ID, "cc-cvv").send_keys(test["cc-cvv"]) 



        buttonContinue = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-block")
        driver.execute_script("arguments[0].click();", buttonContinue)

        # element = driver.find_element(By.ID, "checkoutForm")
        # driver.execute_script("arguments[0].click();", element)

        time.sleep(1)
        driver.get("http://127.0.0.1:8080/IT-exo-PHP_bug/projet_loading/form.php")
        driver.maximize_window()

        time.sleep(2)

        #Ecriture dans le fichier log
        with open(log_file, 'a', encoding = "UTF-8" ) as file:
            file.write(f'Test avec {test["firstName"]} effectué à {time.ctime()} - succès: test validé \n')
            # file.write(f'Test avec {test[0]} effectué à {time.ctime()} - succès: test validé \n')



    except Exception as e:
        with open(log_file, 'a', encoding = "UTF-8") as file:
            file.write(f'erreur lors du test avec {test["firstName"]} à {time.ctime()} : test erreur\n')
            # file.write(f'erreur lors du test avec {test[0]} à {time.ctime()} : test erreur\n')


input()