from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from flask import Flask, jsonify
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

def download_selenium():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    
    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(2)
    
    # Fetch data
    driver.get("https://www.google.com/")
    title = driver.title
    languages = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[3]/div").text
    driver.quit()  # Always quit the driver
    
    # Return data as a dictionary
    data = {"PageTitle": title, "Language": languages}
    return data

@app.route("/", methods=["GET"])
def home():
    try:
        result = download_selenium()
        return jsonify(result)  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
