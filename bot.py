from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import lxml.html
import pandas as pd

import time
import pandas as pd
from bs4 import BeautifulSoup

profile = Options()
profile.set_preference('browser.download.folderList', 2)  # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')  # type of file to download

# use the out folder of the script path
profile.set_preference('browser.download.dir',"/home/Downloads")
#options.add_argument("--headless")
driver=webdriver.Firefox(options=profile)

action = ActionChains(driver)
driver.get("https://trends.google.com/trends/?geo=US")
driver.find_element_by_xpath("//input[contains(@id,'input-254')]").send_keys("hello")
driver.find_element_by_xpath("//input[contains(@id,'input-254')]").send_keys(Keys.ENTER)


#element=driver.find_element_by_xpath("//div[contains(@class,'VfPpkd-Jh9lGc selectorgadget_selected')]")

#inputs = driver.find_element_by_xpath("//li[text()='One way']").click()


#a=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[@role='option'][contains(.,'One way')]"))).click()
#z=driver.find_element_by_link_text('One way')
#print(z)
time.sleep(10)
driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fe-line-chart-header-container", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "export", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "gray", " " ))]').click()
driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fe-geo-chart-generated", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "export", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "gray", " " ))]').click()


'''
curr_usd=driver.find_element_by_xpath("//input[contains(@value,'USD')]").click()
curr_usd=driver.find_element_by_xpath("//span[@jsname='V67aGc'][contains(.,'OK')]").click()
time.sleep(2)
rt=driver.find_element_by_xpath("//span[@class='snByac'][contains(.,'Round trip')]").click()
ow=driver.find_element_by_xpath("//li[@role='option'][contains(.,'One way')]").click()
time.sleep(5)
driver.find_element_by_xpath("(//input[@jsname='yrriRe'])[5]").send_keys(Keys.CONTROL + "a")
driver.find_element_by_xpath("(//input[@jsname='yrriRe'])[5]").send_keys(Keys.DELETE)
time.sleep(2)
driver.find_element_by_xpath("(//input[@jsname='yrriRe'])[5]").send_keys("28-06-2021")
driver.find_element_by_xpath("(//input[@jsname='yrriRe'])[5]").send_keys(Keys.ENTER)
time.sleep(2)
main_df=pd.DataFrame(columns=['Airline','Arr_t','Dep_t',"Dep_weekday","Arrival_weekday",'Duration','Arr','Dep','Connection','Price'])
main_df.to_csv("test.csv")
for i in range(2):
	#temp_df={}
	temp_df=pd.DataFrame(columns=['Airline','Arr_t','Dep_t',"Dep_weekday","Arrival_weekday",'Duration','Arr','Dep','Connection','Price'])
	driver.find_element_by_class_name("LEoa9b").click()
	time.sleep(5)
	tree = lxml.html.fromstring(driver.page_source)

	
	#print(len(mmm))
	#for i in mmm:
	#	print(i.text_content())

	#airline='//*[contains(concat( " ", @class, " " ), concat( " ", "L1Wood", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "sSHqwe", " " ))]//g-bubble[(((count(preceding-sibling::*) + 1) = 1) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "NppLad", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "sSHqwe", " " ))]//g-bubble+//g-bubble | //*[contains(concat( " ", @class, " " ), concat( " ", "sSHqwe", " " )) and contains(concat( " ", @class, " " ), concat( " ", "ogfYpf", " " ))]//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]'
	#divmain=tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "KC3CM", " " ))]')
	#div=[]
	#for i in divmain:
	#	print(i.text_content())
	#	print("--------------------")
	
	arl = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "TQqf0e", " " ))]')
	airline=[]
	for i in arl:
		airline.append(i.text_content())
	#print(len(airline))
	#print(airline)
	#print('----')
	temp_df['Airline']=airline



	dur = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "AdWm1c", " " )) and contains(concat( " ", @class, " " ), concat( " ", "ogfYpf", " " ))]')
	duration=[]
	for i in dur:
		duration.append(i.text_content())
	#print(len(duration))
	#print(duration)
	#print('----')
	temp_df['Duration']=duration

	conn = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pIgMWd", " " ))]')
	#print(len(conn))
	connection=[]
	for i in conn:
		connection.append(i.text_content())
	#print(len(connection))
	#print(connection)
	#print('---------------')


	temp_df['Connection']=connection


	#print(results[0].text_content())

	
	depa_t = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mv1WYe", " " ))]//g-bubble')
	depa_tt=[]
	week_day=[]
	arr_=[]
	week_day_arr=[]
	for i in range(0,len(depa_t),2):
		temp_t=depa_t[i].text_content().split("\xa0on\xa0")
		arr_temp_t=depa_t[i+1].text_content().split("\xa0on\xa0")
		
		#print(temp_t)
		temp_time=temp_t[0].split('M',1)
		arr_temp_time=arr_temp_t[0].split('M',1)
		
		arr_.append(arr_temp_time[1])
		depa_tt.append(temp_time[1])
		week_day.append(temp_t[1])
		week_day_arr.append(arr_temp_t[1])

	temp_df['Dep_t']=depa_tt
	#print(len(depa_tt))
	#print(depa_tt)
	#print('------')
	#print(week_day)
	#print('------')

	#print('week_day_arr------')
	#print(week_day_arr)
	#print(len(week_day_arr))
	#print('------arr')
	#print(arr_)
	#print(len(arr_))
	#print('--------------')

	temp_df['Arr_t']=arr_
	temp_df['Dep_weekday']=week_day
	temp_df['Arrival_weekday']=week_day_arr
	
	#temp_df['Time']=times
	conn = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pIgMWd", " " ))]')
	connn=[]
	for i in conn:
		#print(i.text_content())
		connn.append(i.text_content())
	temp_df['Connection']=connn
	#print(len(connn))
	#print(connn)
	#print('--------------')

	#airline = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " )) and (((count(preceding-sibling::*) + 1) = 49) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "nQgyaf", " " ))]//g-bubble | //*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " )) and (((count(preceding-sibling::*) + 1) = 71) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "sSHqwe", " " ))]//g-bubble | //*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " )) and (((count(preceding-sibling::*) + 1) = 67) and parent::*)]//g-bubble | //*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " )) and (((count(preceding-sibling::*) + 1) = 42) and parent::*)]//g-bubble | //*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//g-bubble | //*~[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " ))]//*+[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "Qpcsfe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "z0fuv", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "sSHqwe", " " )) and contains(concat( " ", @class, " " ), concat( " ", "ogfYpf", " " ))]//span')
	#for i in airline:
	#	print(i.text_content())

	
	pricesl=[]
	prices = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "FpEdX", " " ))]//span')
	for i in range(0,len(prices),3):
		pricesl.append(prices[i].text_content())
	#print(len(pricesl))
	#print(pricesl)
	#print('----')
	temp_df['Price']=pricesl
	temp_df['Arr']='SEA'
	temp_df['Dep']='LAX'
	main_df=main_df.append(temp_df,ignore_index=True)
	main_df.to_csv("test.csv",mode='a',header=None)
	#print('-------------------------------------------------')
	nextday=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Xbfhhd", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "VfPpkd-kBDsod", " " ))]').click()
	time.sleep(5)


#element=driver.find_element_by_xpath("//li[@role='option'][contains(.,'Round trip')]")
#drp=Select(element)
#button1 = driver.find_element_by_css_selector(".uT1UOd")

#print(drp)
'''
