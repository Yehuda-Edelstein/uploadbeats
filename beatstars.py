import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

username = os.getenv('BEATSTARS_USERNAME')
password = os.getenv('BEATSTARS_PASSWORD')
url = os.getenv('BEATSTARS_URL')
profile = os.getenv('BEATSTARS_PROFILE')
browser = webdriver.Chrome(executable_path=os.getenv('BEATSTARS_PATH'))
wait = WebDriverWait(browser, 500)

def beatstars(wav, stems, sq):
    browser.maximize_window()
    browser.get(url)

    try:
        sign_in()
    except Exception as e:
        print(e)
    try:
        upload(wav, stems)
    except Exception as e:
        print(e)
    # try:
    #     info(sq, wav)
    # except Exception as e:
    #     print(e)
    browser.close()

def sign_in():
    browser.find_element(By.ID, "oath-email").send_keys(username, Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.ID, "userPassword"))).send_keys(password, Keys.ENTER)
    print('signed into beatstars')
    # time.sleep(30)

def upload(wav, stems):
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/studio-root/div/ng-component/studio-header/header/div/div/bs-square-button/button"))).click()
    print('upload track')

    time.sleep(30)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/mat-tab-group/div/mat-tab-body[1]/div/studio-wrapper-track-files/studio-form-files/div/section[1]/div/studio-form-file-box/div/div/div[2]/bs-upload-button/bs-universal-upload-button/div/div/bs-square-button/button'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.uppy-DragDrop-input[type='file']"))).send_keys(f"/Users/almoni/Desktop/Code/uploadbeats/{wav}")
    print('wav uploaded')

    time.sleep(30)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/mat-tab-group/div/mat-tab-body[1]/div/studio-wrapper-track-files/studio-form-files/div/section[2]/div/studio-form-file-box/div/div/div[2]/bs-upload-button/bs-universal-upload-button/div/div/bs-square-button/button'))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.uppy-DragDrop-input[type='file']"))).send_keys(f"/Users/almoni/Desktop/Code/uploadbeats/{stems}")
    print('stems uploaded')

    time.sleep(30)
 
def info(sq, wav):
    # # turn wav into beatstars title
    a = wav.split('/')
    b = a[1].split('.')
    c = b[0].split('"')
    title = f'{c[0]} - "{c[1]}"'

    # # edit draft
    # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/studio-root/div/ng-component/studio-tabs/ng-component/studio-page-container/div/studio-inventory-list-holder/studio-container-grid/div[1]/studio-media-card/div/div[4]/studio-button-item-menu/bs-menu-more-options/div/bs-square-button/button'))).click()
    # # figure this button out
    # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-menu-panel-52"]/div/studio-option-edit'))).click()
    # print('draft selected')
    # time.sleep(30)

    # # switch to basic info tab
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]'))).click()

    # edit artwork
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/mat-tab-group/div/mat-tab-body[2]/div/studio-wrapper-track-basic-info/studio-inventory-form-basic-info/div/div[1]/bs-upload-button/bs-artwork-composed-button/bs-menu-more-options/div/bs-square-button/button'))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-menu-panel-109"]/div/bs-artwork-option-upload/bs-external-action-option/button'))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.uppy-DragDrop-input[type='file']"))).send_keys(f"/Users/almoni/Desktop/Code/uploadbeats/{sq}")

    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/mat-dialog-container/ng-component/mat-dialog-content/bs-crop-image/div[2]/div[2]'))).click()
    print('image uploaded')

    time.sleep(30)

    browser.find_element(By.ID, "title").clear()

    browser.find_element(By.ID, "title").send_keys(title)

    print('basic info entered')

    time.sleep(30)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/div/div/bs-square-button[2]/button'))).click()
    time.sleep(30)
    # add tags and other metadata
    # print('metadata entered')

    # return beatstars link and save it to Beat to upload link to youtube