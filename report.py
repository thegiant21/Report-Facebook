import os
import time
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pystyle import Colors, Colorate

DELAY_BETWEEN_REPORTS = (6, 12) 
GITHUB_URL = "https://github.com/thegiant21"
WATERMARK = "reports"

def animated_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ascii_art = """
 _____                       _       
|  __ \                     | |      
| |__) |___ _ __   ___  _ __| |_ ___ 
|  _  // _ \ '_ \ / _ \| '__| __/ __|
| | \ \  __/ |_) | (_) | |  | |_\__ \
|_|  \_\___| .__/ \___/|_|   \__|___/
           | |                       
           |_|                       
    """
    

    red_color = "\033[91m"
    bold = "\033[1m"
    reset = "\033[0m"
    

    for line in ascii_art.split('\n'):
        print(f"{bold}{red_color}{line}{reset}")
        time.sleep(0.08)
        
    print("\n" + "=" * 55)
    
    wm_text = f" [*] {WATERMARK}\n [*] GitHub: {GITHUB_URL}"
    for char in wm_text:
        sys.stdout.write(f"{bold}{red_color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(0.02)
        
    print("\n" + "=" * 55 + "\n")
    time.sleep(1)

def init_driver():
    chrome_options = Options()
    
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)
    return driver, wait

def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

def report_account(driver, wait, account_url, index, total_reports):
    print(Colorate.Horizontal(Colors.red_to_white, f"\n[+] [{WATERMARK}] Starting report #{index + 1} of {total_reports} for: {account_url}"))

    try:
        driver.get(account_url)
        time.sleep(5)

   
        more_btn = wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//div[@role='main']//div[@aria-haspopup='menu' and @role='button'] | //div[contains(@class, 'x1i10hfl')]//div[@role='button']//i[contains(@style, 'background-image')]"
        )))
        js_click(driver, more_btn)
        time.sleep(2)

   
        report_profile_btn = wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[normalize-space()='Report profile']"
        )))
        js_click(driver, report_profile_btn)
        time.sleep(2.5)

        something_btn = wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[normalize-space()='Something about this profile']"
        )))
        js_click(driver, something_btn)
        time.sleep(2.5)

        fake_profile_btn = wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[normalize-space()='Fake profile']"
        )))
        js_click(driver, fake_profile_btn)
        time.sleep(2.5)

        try:
            me_btn = wait.until(EC.presence_of_element_located((
                By.XPATH, "//span[normalize-space()='Me' or normalize-space()='They’re not a real person']"
            )))
            js_click(driver, me_btn)
            time.sleep(2)
        except:
            pass

        try:
            next_btn = wait.until(EC.presence_of_element_located((
                By.XPATH, "//div[@role='button' and (normalize-space()='Next' or normalize-space()='Submit' or normalize-space()='Done')]"
            )))
            js_click(driver, next_btn)
            time.sleep(2)
        except:
            pass

        print(Colorate.Horizontal(Colors.green_to_white, f"[✓] Report #{index + 1} submitted successfully by {WATERMARK}."))
        time.sleep(random.uniform(*DELAY_BETWEEN_REPORTS))

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"[✗] Report attempt #{index + 1} failed: {type(e).__name__}"))

def main():
    animated_banner()
    while True:
        count_input = input("Enter number of reports to send (e.g. 10): ").strip()
        if count_input.isdigit() and int(count_input) > 0:
            report_count = int(count_input)
            break
        print(Colorate.Horizontal(Colors.red_to_white, "[!] خطأ: يرجى إدخال رقم صحيح أسبوعياً أكبر من 0"))

    while True:
        raw_url = input("Enter the account URL to report: ").strip()
        if raw_url.startswith("http://") or raw_url.startswith("https://"):
            account_url = raw_url.split('&')[0].split('#')[0]
            break
        print(Colorate.Horizontal(Colors.red_to_white, "[!] خطأ: يجب إدخال رابط صحيح يبدأ بـ https:// أو http://"))

    driver, wait = init_driver()

    try:
        driver.get("https://www.facebook.com/")
        
        print(Colorate.Horizontal(Colors.green_to_white, "\n[i] Please make sure you are logged into Facebook in the opened browser window."))
        input("Press Enter here in the terminal *after* you are logged into Facebook and ready to start reporting...")

        for i in range(report_count):
            report_account(driver, wait, account_url, i, report_count)

        print(Colorate.Horizontal(Colors.green_to_white, f"\n[✓] Finished all {report_count} report attempts successfully."))
        print(Colorate.Horizontal(Colors.red_to_white, f"[i] Developed by {WATERMARK} - GitHub: {GITHUB_URL}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"[✗] Main execution error: {e}"))

    finally:
        driver.quit()
        print(Colorate.Horizontal(Colors.white_to_blue, "Browser closed."))

if __name__ == "__main__":
    main()
