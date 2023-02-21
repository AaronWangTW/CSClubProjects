from selenium import webdriver
from selenium.webdriver.common.by import By
import save
import json

class ManageBacBot:

    def __init__(self) -> None:
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=option)
        self.target = "https://mingdao.managebac.com"

        self.target_classes = []
        
        self.email = save.Save.email # "hello@gmail.com"
        self.password = save.Save.password # "12345667"

        self.result = {}

    def login(self):
        self.driver.get(self.target) # get to managebac.com
        # find elements to enter email and password
        email = self.driver.find_element(By.NAME,"login")
        password = self.driver.find_element(By. NAME,"password")
        # enter email and password to the element
        email.send_keys(self.email)
        password.send_keys(self.password)
        # submit the form to login
        email.submit()

    def get_classes(self):
        class_list = self.driver.find_elements(By.XPATH, "/html/body/div[1]/ul/li[7]/ul/li")
        for i in range(1,len(class_list)):
            # get the link for each class
            class_link = self.driver.find_element(
                By.XPATH, f"/html/body/div[1]/ul/li[7]/ul/li[{i}]/a").get_attribute("href")
            class_name = self.driver.find_element(
                By.XPATH, f"/html/body/div[1]/ul/li[7]/ul/li[{i}]/a/span").get_attribute("innerHTML")
            self.target_classes.append((class_link,class_name))
    
    def get_scores(self):
        self.driver.implicitly_wait(2)
        i = 1
        for link in self.target_classes:
            self.driver.get(link[0]+"/core_tasks")
            tasks = self.driver.find_elements(By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div")
            tasks_result = []
            j = 1
            while j < len(tasks):
                task_name = self.driver.find_element(
                    By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[1]/div[2]/h4/a").text
                try:
                    task_score = self.driver.find_element(
                        By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[2]/div/div/span").get_attribute("innerHTML")
                except Exception:
                    task_score = self.driver.find_element(
                        By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[2]/div/h4").get_attribute("innerHTML")
                tasks_result.append((task_name,task_score))
                j+=1
            self.result[self.target_classes[i-1][1]] = tasks_result
            i+=1
    
    def get_result(self):
        with open("result.json","w",encoding="utf-8") as file:
            json.dump(self.result,file,indent=4,ensure_ascii=False)
        self.driver.quit()
                
            

bot = ManageBacBot()
bot.login()
bot.get_classes()
bot.get_scores()
bot.get_result()