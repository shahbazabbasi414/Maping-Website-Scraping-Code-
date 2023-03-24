from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://propertyrecords.montcopa.org/pt/search/CommonSearch.aspx?mode=PARID')
time.sleep(15)
products = driver.find_element(By.XPATH,'//button[@id="btAgree"]')
products.click()

property_search = driver.find_element(By.XPATH,'//a[@href="../datalets/datalet.aspx"]')
achains = ActionChains(driver)
achains.move_to_element(property_search).perform()
time.sleep(5)
advanc_search=driver.find_element(By.XPATH,'//*[@id="pd_2"]/div[3]/a')
advanc_search.click()



select = Select(driver.find_element(By.ID,'sCriteria'))
# select by visible text
select.select_by_visible_text('Street Number')

# select by value 
select.select_by_value('14')



text_area = driver.find_element(By.ID,'txtCrit')
text_area.send_keys("15")

text_area = driver.find_element(By.ID,'txtCrit2')
text_area.send_keys("15")
time.sleep(5)

driver.find_element(By.ID,"btAdd").send_keys(Keys.ENTER)
driver.find_element(By.ID,"btSearch").send_keys(Keys.ENTER)


csv_writer = open('propertyrecords.csv','w',encoding='utf-8')

table=driver.find_elements(By.XPATH,'//table[@id="searchResults"]')
html_source = driver.page_source
for i in range(24):
    all_data= driver.find_elements(By.XPATH,'//tr[@class="SearchResults"]')
    csv_writer = open('propertyrecords.csv','a',encoding='utf-8')
    for data in all_data:
        parcelId=data.find_element(By.XPATH,'.//td[1]')
        owner_name=data.find_element(By.XPATH,'.//td[2]')
        property_adress= data.find_element(By.XPATH,'.//td[3]')
        sales_dates=data.find_element(By.XPATH,'.//td[4]')
        sales_accounts=data.find_element(By.XPATH,'.//td[5]')
        luc=data.find_element(By.XPATH,'.//td[6]')
        tex_map=data.find_element(By.XPATH,'.//td[7]')
        csv_writer.write('{},{},{},{},{},{},{},\n' .format(parcelId.text.replace(","," "),owner_name.text.replace(","," "),property_adress.text.replace(","," "),sales_dates.text.replace(","," "),sales_accounts.text.replace(","," "),luc.text.replace(","," "),tex_map.text.replace(","," ")))
    csv_writer.close()
    next = driver.find_element(By.XPATH,"//b[text()='Next >>']")
    achains.move_to_element(next).perform()
    time.sleep(5)
    next.click()
    time.sleep(15)

