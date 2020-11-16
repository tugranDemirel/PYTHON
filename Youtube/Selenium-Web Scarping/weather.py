from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class weather:
    def __init__(self, sehir):
        self.url = "https://www.mgm.gov.tr/?il="
        self.browser = webdriver.Firefox()
        self.sehir = sehir

    def ilHava(self):
        self.browser.get(self.url+self.sehir)
        time.sleep(2)
        day = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[1]").text.lower()
        dayTwo = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[2]/div/div[1]/div[1]").text.lower()
        durum = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[3]").text.lower()
        durumIki = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[2]/div/div[1]/div[3]").text.lower()
        tempurature = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[5]/span[1]").text
        tempuratureTwo = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[2]/div/div[1]/div[5]/span[1]").text
        # celcium = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[5]/span[2]").text
        print(f"\nYozgat'ta bugün ({day}) {durum} ve hava sıcaklığı {tempurature} derece olması bekleniyor. Yarın ({dayTwo}) ise {durumIki}, hava sıcaklığı {tempuratureTwo} derece olması bekleniyor. Buna göre ilçelerdeki durum aşağıda belirtilmiştir.\n")

    def ilceHava(self ):
        ilceler = ["Akdağmadeni", "Aydıncık", "Boğazlıyan", "Çandır", "Çayıralan", "Çekerek", "Kadışehri", "Saraykent",
                   "Sarıkaya", "Sorgun", "Şefaatli", "Yenifakılı", "Yerköy"]
        for ilce in ilceler:
            self.browser.get(f"https://www.mgm.gov.tr/?il={self.sehir}&ilce=" + ilce)
            time.sleep(2)
            durum = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[3]").text.lower()
            tempurature = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[5]/span[1]").text
          #  celcium = self.browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[5]/span[2]").text
            print(f"{ilce}, {durum} {tempurature} derece olması bekleniyor.\n")
    def off(self):
        self.browser.close()

if __name__ == '__main__':
    Weather = weather("Yozgat")
    Weather.ilHava()
    Weather.ilceHava()
    Weather.off()



