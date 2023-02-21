from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
from save import Save


class ManageBacBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.target = "https://mingdao.managebac.com/student"
        self.targetClasses = []
        self.email = Save.email
        self.password = Save.password

        self.result = {}

    def login(self):
        self.driver.get(self.target)
        email = self.driver.find_element(By.NAME, "login")
        password = self.driver.find_element(By.NAME, "password")
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.submit()

    def getClasses(self):
        classList = self.driver.find_elements(
            By.XPATH, "/html/body/div[1]/ul/li[7]/ul/li")
        i = 1
        while i < len(classList):
            classLink = self.driver.find_element(
                By.XPATH, f'/html/body/div[1]/ul/li[7]/ul/li[{i}]/a').get_attribute("href")
            className = self.driver.find_element(
                By.XPATH, f'/html/body/div[1]/ul/li[7]/ul/li[{i}]/a/span').get_attribute("innerHTML")
            self.targetClasses.append((classLink,className))
            i += 1

    def getScores(self):
        self.driver.implicitly_wait(2)
        i = 1
        for link in self.targetClasses:
            self.driver.get(link[0]+"/core_tasks")
            tasks = self.driver.find_elements(
                By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div")
            taskResults = []
            j = 1
            while j < len(tasks):
                taskName = self.driver.find_element(
                    By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[1]/div[2]/h4/a").text
                try:
                    taskScore = self.driver.find_element(
                        By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[2]/div/div/span").get_attribute("innerHTML")
                except NoSuchElementException:
                    taskScore = self.driver.find_element(
                        By.XPATH, f"/html/body/main/div[2]/div[3]/div[4]/div[{j}]/div[2]/div/h4").get_attribute("innerHTML")
                taskResults.append((taskName, taskScore))
                j += 1
            self.result[self.targetClasses[i-1][1]] = taskResults
            i += 1
    
    def getResult(self):
        with open("result.json","w",encoding="utf8") as file:
            json.dump(self.result,file,indent=4, ensure_ascii=False)
        self.driver.quit()


bot = ManageBacBot()
bot.login()
bot.getClasses()
bot.getScores()
bot.getResult()