from flask import Flask, render_template, request, send_file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests as rq
import os
import zipfile
from bs4 import BeautifulSoup
import time

app = Flask(__name__)
output_folder = "output"

# Setup Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def get_url(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        time.sleep(5)
        if driver.current_url == "data:,":
            return None
        return driver.page_source
    finally:
        driver.quit()

def get_img_links(res):
    soup = BeautifulSoup(res, "html.parser")
    return [img["src"] for img in soup.find_all("img", src=True)]

def download_img(img_link, index):
    try:
        extensions = [".jpeg", ".jpg", ".png", ".gif"]
        extension = ".jpg"
        for exe in extensions:
            if img_link.find(exe) > 0:
                extension = exe
                break
        img_data = rq.get(img_link).content
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        file_path = os.path.join(output_folder, f"{index + 1}{extension}")
        with open(file_path, "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Error downloading {img_link}: {e}")

def zip_images():
    zip_path = "images.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    return zip_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            result = get_url(url)
            if result:
                img_links = get_img_links(result)
                for index, img_link in enumerate(img_links):
                    if img_link.startswith("http"):
                        download_img(img_link, index)
                zip_path = zip_images()
                return send_file(zip_path, as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)