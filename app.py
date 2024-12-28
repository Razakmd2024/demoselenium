from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from flask import Flask, request

app = Flask(__name__)

def download_selenium():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.com/")
    title = driver.title
    languages = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[3]/div").text

    data = {"PageTitle":title, "Language":languages}
    return data

@app.route("/")
def home():
    if (request.method=='GET'):
        return download_selenium()


if __name__ == "__main__":
    app.run(debug=True)