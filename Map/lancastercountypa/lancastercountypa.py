from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://lancastercountypa.maps.arcgis.com/apps/webappviewer/index.html?id=97a16dc9b3ae4648b0419a94a607f375')

time.sleep(40)

checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'jimu_dijit_CheckBox_0')))
checkbox.click()
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="widgets_Splash_Widget_14"]/div[2]/div[2]/div[2]/button')))
button.click()

with open('test1.csv', 'r') as file:
    reader = csv.reader(file)
    column_index = 2 
    column = []
    for row in reader:
        column.append(row[column_index])
        print(column)
for i in column:
    text_area = driver.find_element(By.ID,'esri_dijit_Search_0_input')
    text_area.send_keys(i)

    search_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="searchIcon esri-icon-search"]')))
    search_button.click()


    dot_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="map_graphics_layer"]')))
    dot_button.click()


    next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="titleButton next"]')))
    next_button.click()
    time.sleep(5)

    csv_writer = open('lancastercountypa.csv','w',encoding='utf-8')

    owner_name=driver.find_element(By.XPATH,'//tr[15][@valign="top"]')
    Building_assessment=driver.find_element(By.XPATH,'//tr[20][@valign="top"]')
    Owner_address=driver.find_element(By.XPATH,'//tr[28][@valign="top"]')
    csv_writer.write('{},{},{}\n' .format(owner_name.text.replace(","," "),Building_assessment.text.replace(","," "),Owner_address.text.replace(","," ")))
    csv_writer.close()

