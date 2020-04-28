'''this program prints the current coronavirus cases around india
and also the daily cases
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def execute():
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.covid19india.org")
    currentcase= driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h4')
    current=str(currentcase.text)
    j=len(current)-1
    current_case=current[2:j]
    totcase=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h1')
    fir=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/td[2]/span[2]')
    firname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/td[1]/div/span[2]')
    firin=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/td[2]/span[1]')
    secname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[3]/td[1]/div/span[2]')
    sec=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/table/tbody[1]/tr[3]/td[2]/span[2]')
    secin=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[3]/td[2]/span[1]')
    thiname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[5]/td[1]/div/span[2]')
    thi=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[5]/td[2]/span[2]')
    thiin=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/table/tbody[1]/tr[5]/td[2]/span[1]')
    print("NEW CASES AS OF TODAY IN INDIA IS",current_case)
    print("TOTAL CASE IN INDIA IS",totcase.text)
    print("FIRST MOST INFECTED STATE IS",firname.text,"WITH",fir.text,"CASES","WITH INCREASE BY",firin.text)
    print("SECOND MOST INFECTED STATE IS",secname.text,"WITH",sec.text,"CASES","WITH INCREASE BY",secin.text)
    print("THIRD MOST INFECTED STATE IS",thiname.text,"WITH",thi.text,"CASES","WITH INCREASE BY",thiin.text)
    driver.quit()
    time.sleep(3600)

while(True):
    execute()


