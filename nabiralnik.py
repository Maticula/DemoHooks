from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import random
import string
import time
import traceback

def otsd(driver, logs, potrdiVlogo):
    ###Driver/URL
    driver.get("https://btw-inbox-sb1.tstest.telekom.si/tkminboxasp/Default.aspx")
    
    ###Iframe
    iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
    driver.switch_to.frame(iframe)
    
    ###Kreiraj nov zahtevek
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cphBody_viewList1_btBeginView"]'))).click()
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cphBody_viewList1_btBeginView"]'))).click()
        except:
            continue
        else:
            break
    
    ###Iframe
    iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
    driver.switch_to.frame(iframe)
    time.sleep(1)
    
    ###Obrazec nabava
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recordList1_gvRecordList_lbtTaskEdit_1"]'))).click()
    
    ###Nov window
    ogWindow = driver.window_handles[0]
    newWindow = driver.window_handles[1]
    driver.switch_to.window(newWindow)
    
    ###OTSD nadaljuj
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_1"]/div/button'))).click()
    
    ###Random textbox
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_3_1"]'))).send_keys("5454")
    
    ###Oznaka postopka
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_2"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_2"]')).select_by_index(2)
    
    ###Predmet naročila
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_4"]'))).send_keys("test")
    
    ###Cena
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_5_1_1"]'))).send_keys(Keys.CONTROL + "a")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_5_1_1"]'))).send_keys(Keys.DELETE)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_5_1_1"]'))).send_keys("1000,00")
    
    ###Dodaj dobavitelja
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_4_1_2_1_2_1_1"]/div[1]/div/div/a'))).click()
    
    ###Naziv dobavitelja
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_7_1_1_1_1"]'))).send_keys("naziv")
    
    ###Naslov dobavitelja
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_7_1_1_1_2"]'))).send_keys("naslov")
    
    ###Davčna dobavitelja
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_7_1_1_1_3"]'))).send_keys("000")
    
    ###Potrdi
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_4_1_2_1_2_1_1_5"]/div/button'))).click()
    
    ###Vprašalnik
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_4_1_1_1_1_1_8_r8"]/div/button'))).click()

    ###Iframe
    iframe = driver.find_element_by_xpath('//*[@id="dj_history"]')
    driver.switch_to.frame(iframe)
    time.sleep(1)
    
    ###Tip vprašalnika
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_2"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_2"]')).select_by_index(1)
    
    ###Nadaljuj vprašalnik
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_3_1_1_1_1"]/div/button'))).click()
    
    ###Da/Ne vprašanja
    randomNum = random.randint(1, 2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_4_1_1_1_1_3_1_r2"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
    
    randomNum = random.randint(1, 2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_4_1_1_1_1_3_1_r6"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
    
    randomNum = random.randint(1, 2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_4_1_1_1_1_3_1_r10"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
    
    randomNum = random.randint(1, 2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_4_1_1_1_1_3_1_r14"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
    
    randomNum = random.randint(1, 2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_4_1_1_1_1_3_1_r18"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
    
    ###Finančna cena dobavitelja
    randomNum = random.randint(1, 4)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_6"]/div/div/div/label[' + str(randomNum) + ']/input'))).click()
        
    ###Dodaj ukrep
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_20_1_3"]/div[1]/div/div/a'))).click()
        except:
            continue
        else:
            break
    
    ###Kratek opis
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_26_1_1"]'))).send_keys("naslov")
    
    ###Področje
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_27"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_27"]')).select_by_index(1)
    
    ###Opis
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_28"]'))).send_keys("test")
    
    ###Rok za izvedbo
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datetimepicker_div_29"]/input'))).send_keys("11.08.2021")
    
    ###Odgovroni
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_26_1_2"]'))).send_keys("Matic Marušič [IKT in storitve omrežja;IT podporni sistemi in storitve;Portali in aplikacije]")
    
    ###Potrdi
    potrdiButton = driver.find_elements_by_xpath('//*[@id="div_20_1_3_5"]/div/button')
    while True:
        try:
            potrdiButton = driver.find_elements_by_xpath('//*[@id="div_20_1_3_5"]/div/button')
            potrdiButton[0].click()
            time.sleep(1)
        except:
            break
    
    ###Dodatna utemeljitev
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_18"]'))).send_keys("test")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_19"]'))).send_keys("test")
    except:
        pass
    else:
        while True:
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_6_1_3"]/div[1]/div/div/a'))).click()
            except:
                continue
            else:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_14"]'))).send_keys("test")
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_15"]')))
                Select(driver.find_element_by_xpath('//*[@id="combo_div_15"]')).select_by_index(1)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_16"]')))
                Select(driver.find_element_by_xpath('//*[@id="combo_div_16"]')).select_by_index(1)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_6_1_3_5"]/div/button'))).click()
                break

    ###Potrdi
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_33_1_2"]/div/button'))).click()
    
    ###Reset
    driver.switch_to.default_content()
    
    ###Wait for page to load
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_1_1_4"]')))
    
    ###Brisanje delovnih tokov
    tabela = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[8]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table')
    stVrstic = tabela.find_elements_by_css_selector('tr')
    for row in range(1, len(stVrstic)):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[8]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/div/button'))).click()

    ###Dodaj delovni tok
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_11_1_2"]/div[1]/div/div/a'))).click()
    
    ###Naziv opravila
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_12_1_1"]'))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_12_1_1"]'))).send_keys("test")
    
    ###Zaporedna številka
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_13"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_13"]')).select_by_index(1)
    
    ###Tip opravila
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_14"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_14"]')).select_by_index(2)
    
    ###Odgovroni
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_12_1_2"]'))).send_keys("Matic Marušič [IKT in storitve omrežja;IT podporni sistemi in storitve;Portali in aplikacije]")
     
    ###Potrdi
    potrdiButton = driver.find_elements_by_xpath('//*[@id="div_11_1_2_5"]/div/button')
    while True:
        try:
            potrdiButton = driver.find_elements_by_xpath('//*[@id="div_11_1_2_5"]/div/button')
            potrdiButton[0].click()
            time.sleep(1)
        except:
            break
    
    ###Wait
    wait = input("Waiting...")
    
    ###Oddaj zahtevek
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_18_1_1"]/div/button'))).click()
            time.sleep(1)
        except:
            continue
        else:
            break
            
    ###Številka zahtevka
    stReq = ""
    while len(stReq) == 0:
        try:
            temp = driver.find_elements_by_xpath('//*[@id="div_1_1_1"]/div/span')
            stReq = temp[0].text
            if len(stReq) != 0:
                break
        except:
            continue
    stReq = stReq[28:]

    ###Zaprtje okna
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    ###Reset
    driver.switch_to.default_content()
    
    ###Potrdi/Zavrni opravilo
    if potrdiVlogo:
        ###Potrdi
        while True:
            ###Pridobivanje statusa REQ
            trenutniStatus = statusOTSD(stReq, driver)
            
            ###Reset
            driver.switch_to.default_content()
            
            if trenutniStatus == "vOpravilih":
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Vsa moja opravila
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div/div/table/tbody/tr/td[1]/contenttemplate/div/div[3]/div/div/ul/li[2]/ul/li[1]/a'))).click()
    
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Odpri opravilo
                tabela = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]')
                stVrstic = tabela.find_elements_by_css_selector('tr')
                for row in range(1, len(stVrstic)):
                    opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[3]')
                    if str(opraviloButton.text) == str(stReq):
                        opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[1]/nobr/a[2]')
                        opraviloButton.click()             
                
                ###Nov window(Pregled reklamacije)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                ###Potrditev
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_39_1_1_3_3"]/div/button'))).click()

                ###Reset window(Pregled reklamacije)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

                ###Reset
                driver.switch_to.default_content()
                
            elif trenutniStatus == "Zaključen":
                logs[9].append("Uspešno potrjen OTSD(šifra opravila: " + str(stReq) + ").")
                print("Uspešno potrjen OTSD(šifra opravila: " + str(stReq) + ").")
                return
            
            else:
                print("Napaka, ni v opravilih.")
                return

                
    else:
        ###Zavrni
        while True:
            ###Pridobivanje statusa COD
            trenutniStatus = statusOTSD(stReq, driver)
            
            ###Reset
            driver.switch_to.default_content()
            
            if trenutniStatus == "vOpravilih":
                ###Reset
                driver.switch_to.default_content()
            
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Vsa moja opravila
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div/div/table/tbody/tr/td[1]/contenttemplate/div/div[3]/div/div/ul/li[2]/ul/li[1]/a'))).click()
    
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
       
                ###Odpri opravilo
                tabela = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]')
                stVrstic = tabela.find_elements_by_css_selector('tr')
                for row in range(1, len(stVrstic)):
                    opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[3]')
                    if str(opraviloButton.text) == str(stReq):
                        opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[1]/nobr/a[2]')
                        opraviloButton.click()              
    
                ###Nov window(Pregled reklamacije)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                ###Stornitev
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_39_1_1_3_1_1"]/div[1]/div/div/a'))).click()
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_2"]'))).send_keys("test")
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_39_1_1_3_1_1_5"]/div/button'))).click()
                except:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_1_1_2_1_2_1"]/div[1]/div/div/a'))).click()
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_7"]'))).send_keys("test")
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_1_1_2_1_2_1_5"]/div/button'))).click()

                ###Reset window(Pregled reklamacije)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

                ###Reset
                driver.switch_to.default_content()
                
            elif trenutniStatus == "Storniran":
                logs[10].append("Uspešno storniran OTSD(šifra opravila: " + str(stReq) + ").")
                print("Uspešno storniran OTSD(šifra opravila: " + str(stReq) + ").")
                return
                
            else:
                print("Napaka, ni v opravilih.")
                return

###Izpis v html
def writeToHtml(logs, file):
    stringLogs = ["", "", "", "", "", "", "", "", "", "", ""]
    for i in range(11):
        for j in range(len(logs[i])):
            stringLogs[i] = stringLogs[i] + "<b>" + str(j) + "</b>: " + logs[i][j] + "<br>"
        if len(stringLogs[i]) == 0:
            stringLogs[i] = "Ni primerov."
    f = open(file, "w")
    
    ###
    f.write('<!DOCTYPE html><html><head><title>Rezultati</title><script src="script.js"></script><link href="style.css" rel="stylesheet" type="text/css"></head><body><div class="container"><table><tr><td class="gray" colspan="2">Rezultati:</td></tr>')
    
    ###
    f.write('<tr onclick="displayLogs(1)"><td class="green">Uspešno ustvarjene reklamacije:</td><td class="green">' + str(len(logs[0])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(2)"><td class="blue">Uspešno potrjeni testni obrazci:</td><td class="blue">' + str(len(logs[1])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(3)"><td class="blue">Uspešno zavrnjeni testni obrazci:</td><td class="blue">' + str(len(logs[2])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(4)"><td class="blue">Ustvarjen nezaključen testni obrazci:</td><td class="blue">' + str(len(logs[3])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(8)"><td class="purple">Uspešno potrjeni COD:</td><td class="purple">' + str(len(logs[7])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(9)"><td class="purple">Uspešno stornirani COD:</td><td class="purple">' + str(len(logs[8])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(10)"><td class="cyan">Uspešno potrjeni OTSD:</td><td class="cyan">' + str(len(logs[9])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(11)"><td class="cyan">Uspešno stornirani OTSD:</td><td class="cyan">' + str(len(logs[10])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(5)"><td class="red">Napaka pri SPP:</td><td class="red">' + str(len(logs[4])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(6)"><td class="red">Napaka pri e-pošti:</td><td class="red">' + str(len(logs[5])) + '</td></tr>')
    f.write('<tr onclick="displayLogs(7)"><td class="red">Druge napake:</td><td class="red">' + str(len(logs[6])) + '</td></tr>')
    
    ###
    f.write('</table></div>')
    
    ###
    f.write('<div class="logs" id="logs1" onclick="hide()">' + str(stringLogs[0]) + '</div>')
    f.write('<div class="logs" id="logs2" onclick="hide()">' + str(stringLogs[1]) + '</div>')
    f.write('<div class="logs" id="logs3" onclick="hide()">' + str(stringLogs[2]) + '</div>')
    f.write('<div class="logs" id="logs4" onclick="hide()">' + str(stringLogs[3]) + '</div>')
    f.write('<div class="logs" id="logs5" onclick="hide()">' + str(stringLogs[4]) + '</div>')
    f.write('<div class="logs" id="logs6" onclick="hide()">' + str(stringLogs[5]) + '</div>')
    f.write('<div class="logs" id="logs7" onclick="hide()">' + str(stringLogs[6]) + '</div>')
    f.write('<div class="logs" id="logs8" onclick="hide()">' + str(stringLogs[7]) + '</div>')
    f.write('<div class="logs" id="logs9" onclick="hide()">' + str(stringLogs[8]) + '</div>')
    f.write('<div class="logs" id="logs10" onclick="hide()">' + str(stringLogs[9]) + '</div>')
    f.write('<div class="logs" id="logs11" onclick="hide()">' + str(stringLogs[10]) + '</div>')
    
    ###
    f.write('</body>')
    
    ###
    f.close()
    
def cod(driver, logs, potrdiVlogo):
    ###Driver/URL
    driver.get("https://btw-inbox-sb1.tstest.telekom.si/tkminboxasp/Default.aspx")
    
    ###Iframe
    iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
    driver.switch_to.frame(iframe)
    
    ###Kreiraj nov zahtevek
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cphBody_viewList1_btBeginView"]'))).click()
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cphBody_viewList1_btBeginView"]'))).click()
        except:
            continue
        else:
            break
    
    ###Iframe
    iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
    driver.switch_to.frame(iframe)
    time.sleep(1)
    
    ###Obrazec nabava
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recordList1_gvRecordList_lbtTaskEdit_1"]'))).click()
    
    ###Nov window
    ogWindow = driver.window_handles[0]
    newWindow = driver.window_handles[1]
    driver.switch_to.window(newWindow)
    
    ###COD nadaljuj
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_2_1_1"]/div/button'))).click()
    
    ###SPP
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_2_1_1_1_1"]'))).send_keys("1")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_2_1_1_1_1"]'))).send_keys(Keys.RETURN)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_3_1_1_1_1_1_1_r1"]/div/button'))).click()
    
    ###Uredi ocenitev
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_2_1_2_1_2_1_1"]/div/button'))).click()
    
    ###Tip ocenitve
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_2"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_2"]')).select_by_index(2)
    
    ###Nadaljuj
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_3_1_1_1_1"]/div/button'))).click()
    
    ###A
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[4]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[5]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[6]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[7]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###B
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###C
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###D
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###E
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[5]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[5]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[5]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###F
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[6]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[6]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[6]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###G
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[7]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[7]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###H
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[8]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))

    ###I
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[4]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[5]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[6]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###J
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[10]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    Select(driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div/div/div[10]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/div/div/select')).select_by_index(random.randint(1, 4))
    
    ###Potrdi
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_7_1_2"]/div/button'))).click()
    
    ###Brisanje delovnih tokov
    tabela = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[14]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table')))
    stVrstic = tabela.find_elements_by_css_selector('tr')
    for row in range(1, len(stVrstic)):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[14]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/div/button'))).click()
    
    ###Dodaj normalen delovni tok
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_39_1_2"]/div[1]/div/div/a'))).click()
    ###Naziv opravila
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_40_1_1"]'))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_40_1_1"]'))).send_keys("test")
    ###Zaporedna številka
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_41"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_41"]')).select_by_index(1)
    ###Tip opravila
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_div_42"]')))
    Select(driver.find_element_by_xpath('//*[@id="combo_div_42"]')).select_by_index(2)
    ###Odgovorni
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_div_40_1_2"]'))).send_keys("Matic Marušič [IKT in storitve omrežja;IT podporni sistemi in storitve;Portali in aplikacije]")
    ###Potrdi
    potrdiButton = driver.find_elements_by_xpath('//*[@id="div_39_1_2_5"]/div/button')
    while True:
        try:
            potrdiButton = driver.find_elements_by_xpath('//*[@id="div_39_1_2_5"]/div/button')
            potrdiButton[0].click()
            time.sleep(1)
        except:
            break
    
    ###Strategija razvoja
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_7"]'))).send_keys("test")
    
    ###Analiza trga
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_23"]'))).send_keys("test")
    
    ###Nabavni vidik
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_24"]'))).send_keys("test")
    
    ###Prodajni vidik
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_25"]'))).send_keys("test")
    
    ###Oddaj zahtevek
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_46_1_1"]/div/button'))).click()
            time.sleep(1)
        except:
            continue
        else:
            break
            
    ###Številka zahtevka
    stReq = ""
    while len(stReq) == 0:
        try:
            temp = driver.find_elements_by_xpath('//*[@id="div_1_1_1"]/div/span')
            stReq = temp[0].text
            if len(stReq) != 0:
                break
        except:
            continue
    stReq = stReq[28:]

    ###Zaprtje okna
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    ###Reset
    driver.switch_to.default_content()
    
    ###Potrdi/Zavrni opravilo
    if potrdiVlogo:
        ###Potrdi
        while True:
            ###Pridobivanje statusa REQ
            trenutniStatus = statusCOD(stReq, driver)
            
            ###Reset
            driver.switch_to.default_content()
            
            if trenutniStatus == "vOpravilih":
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Vsa moja opravila
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div/div/table/tbody/tr/td[1]/contenttemplate/div/div[3]/div/div/ul/li[2]/ul/li[1]/a'))).click()
    
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Odpri opravilo
                tabela = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]')
                stVrstic = tabela.find_elements_by_css_selector('tr')
                for row in range(1, len(stVrstic)):
                    opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[3]')
                    if str(opraviloButton.text) == str(stReq):
                        opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[1]/nobr/a[2]')
                        opraviloButton.click()             
                
                ###Nov window(Pregled reklamacije)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                ###Potrditev
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_100_1_1_3_2"]/div/button'))).click()
                except:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_80_1_1_3_3"]/div/button'))).click()

                ###Reset window(Pregled reklamacije)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

                ###Reset
                driver.switch_to.default_content()
                
            elif trenutniStatus == "Zaključen":
                logs[7].append("Uspešno potrjen COD(šifra opravila: " + str(stReq) + ").")
                print("Uspešno potrjen COD(šifra opravila: " + str(stReq) + ").")
                return
            
            else:
                print("Napaka, ni v opravilih.")
                return

                
    else:
        ###Zavrni
        while True:
            ###Pridobivanje statusa COD
            trenutniStatus = statusCOD(stReq, driver)
            
            ###Reset
            driver.switch_to.default_content()
            
            if trenutniStatus == "vOpravilih":
                ###Reset
                driver.switch_to.default_content()
            
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="inboxFrame"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Vsa moja opravila
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div/div/table/tbody/tr/td[1]/contenttemplate/div/div[3]/div/div/ul/li[2]/ul/li[1]/a'))).click()
    
                ###Iframe
                iframe = driver.find_element_by_xpath('//*[@id="iFramRecordsList"]')
                driver.switch_to.frame(iframe)
                time.sleep(1)
    
                ###Odpri opravilo
                tabela = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]')
                stVrstic = tabela.find_elements_by_css_selector('tr')
                for row in range(1, len(stVrstic)):
                    opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[3]')
                    if str(opraviloButton.text) == str(stReq):
                        opraviloButton = driver.find_element_by_xpath('//*[@id="recordList1_gvRecordList"]/tbody/tr[' + str(row) + ']/td[1]/nobr/a[2]')
                        opraviloButton.click()              
    
                ###Nov window(Pregled reklamacije)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                ###Stornitev
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_1_1_2_1_3_1"]/div[1]/div/div/a'))).click()
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="textArea_div_10"]'))).send_keys("test")
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_1_1_1_1_2_1_3_1_5"]/div/button'))).click()

                ###Reset window(Pregled reklamacije)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

                ###Reset
                driver.switch_to.default_content()
                
            elif trenutniStatus == "Storniran":
                logs[8].append("Uspešno storniran COD(šifra opravila: " + str(stReq) + ").")
                print("Uspešno storniran COD(šifra opravila: " + str(stReq) + ").")
                return
                
            else:
                print("Napaka, ni v opravilih.")
                return
