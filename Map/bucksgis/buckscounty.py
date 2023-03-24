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
driver.get('https://bucksgis.maps.arcgis.com/apps/webappviewer/index.html?id=2eda3020dd9847eaa00d1d6c0764a607')
time.sleep(50)
checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'jimu_dijit_CheckBox_0')))
checkbox.click()

button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="widgets_Splash_Widget_22"]/div[2]/div[2]/div[2]/button')))
button.click()
# text_area = driver.find_element(By.ID,'esri_dijit_Search_0_input')


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
            
    # text_area.send_keys("3615 NANCY WARD CIRCLE DOYLESTOWN, PA 18901")

    search_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="esri_dijit_Search_0"]/div/div[2]/span[1]')))
    search_button.click()
    time.sleep(10)

    dot_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="map_graphics_layer"]')))
    dot_button.click()

    next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')))
    next_button.click()


    view_parcel_information = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//font[@size="4"]')))
    view_parcel_information.click()
    time.sleep(10)

    csv_writer = open('buckscounty.csv','a',encoding='utf-8')

    driver.switch_to.window(driver.window_handles[-1])
    
    table=driver.find_elements(By.XPATH,'//*[@id="frmMain"]/div[3]/div/div/table/tbody/tr/td/table')
    for data in table:
        
        owner_name=data.find_element(By.XPATH,'//td[1][@class="DataletHeaderBottom"]')
        Property_Address=data.find_element(By.XPATH,'//*[@id="Parcel"]/tbody/tr[6]/td[2]')
        Parcel_Mailing_Details=data.find_element(By.XPATH,'//*[@id="Parcel Mailing Details"]/tbody/tr[2]/td[2]')
        csv_writer.write('{},{},{}\n' .format(owner_name.text.replace(","," "),Property_Address.text.replace(","," "),Parcel_Mailing_Details.text.replace(","," ")))

    
    csv_writer.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)



    delete_button = driver.find_element(By.ID,"esri_dijit_Search_0_input")
    delete_button.clear()
    time.sleep(5)