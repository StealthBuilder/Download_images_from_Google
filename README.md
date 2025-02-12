Here's an updated version of your README with the new name, **Download_images_from_Google**:

---

# **Download Images from Google**  

This Flask web application allows users to enter a URL, scrape images from the webpage using Selenium and BeautifulSoup, and download them as a ZIP file.  

## **Features**  
✔️ Scrapes all images from a given webpage  
✔️ Downloads images to a local folder  
✔️ Provides a ZIP file for easy download  
✔️ Uses Selenium in headless mode for automation  

## **Prerequisites**  
Ensure you have the following installed before running the application:  
- **Python 3.x**  
- **Google Chrome** (latest version)  
- **ChromeDriver** (managed automatically by `webdriver_manager`)  

## **Installation**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/StealthBuilder/Download_images_from_Google.git
   cd Download_images_from_Google
   ```  

2. **Create a Virtual Environment** (Optional but Recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```  

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```  

## **Usage**  

1. **Run the Flask Application**  
   ```bash
   python app.py
   ```  

2. **Access the Web App**  
   Open your browser and go to:  
   ```
   http://127.0.0.1:5000/
   ```  

3. **Download Images**  
   - Enter the website URL  
   - Click **Submit**  
   - Download the ZIP file containing all scraped images  

## **Dependencies**  
This project uses the following libraries:  
- `Flask` – Web framework  
- `Selenium` – Automates browser interaction  
- `webdriver_manager` – Manages ChromeDriver  
- `requests` – Handles HTTP requests  
- `BeautifulSoup` – Parses HTML  
- `zipfile` – Compresses images into a ZIP file  

---

Let me know if you'd like further adjustments! 😊
