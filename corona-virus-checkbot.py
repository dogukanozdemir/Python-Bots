import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
ti
total_deaths_label = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[5]/margin-container/full-container/div/div[1]/div/div[1]/svg/g[2]/svg/text").text
total_deaths_value = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[5]/margin-container/full-container/div/div[1]/div/div[2]/svg/g[2]/svg/text").text

