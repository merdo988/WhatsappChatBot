from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.headless = False

browser = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
browser2= webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
url='https://web.whatsapp.com'



browser.get(url)
time.sleep(20)

while True:
    time.sleep(10)
    try:
        sohbet_ust=browser.find_elements_by_class_name("_3j7s9")
        sohbet_ust[0].click()
        sohbet_text=browser.find_elements_by_class_name("Tkt2p")
        count=len(sohbet_text)
        son_sohbet=sohbet_text[count-1].text
        son_sohbet = son_sohbet[:-5]
        son_sohbet = son_sohbet.lower()
        
    
        hava="-hava durumu"
        if son_sohbet.find(hava) is not -1:
            try:
                browser2.get("https://www.google.com/search?q="+son_sohbet[1:])
                hava_durumu=browser2.find_element_by_xpath("//*[@id='wob_tm']")
                mesaj=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                mesaj.send_keys(hava_durumu.text + " derece")
                mesaj.send_keys(u'\ue007')
                time.sleep(1)
            except:
                mesaj=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                mesaj.send_keys("Her yeri aradım ama inan bulamadım ;(")
                mesaj.send_keys(u'\ue007')
                time.sleep(1)
                
    except:
        pass
        
    browser.get(url)
        
        
        
        
        
	
    

