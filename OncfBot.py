from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as sp
from selenium.common.exceptions import NoSuchElementException
class ONCFBot(object):
	"""docstring for ONCFBot"""
	def __init__(self):
		self.driver = webdriver.Chrome("C:/Program Files/operadriver.exe")
		

	def get_all_gares(self):
		self.driver.get("https://www.oncf-voyages.ma")
		self.driver.maximize_window()
		self.driver.find_element_by_xpath("//div[@id='origin']").click()
		gareList = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul")
		gares = gareList.find_elements_by_xpath('//li')
		gares = [gare.text for gare in gares]
		return gares[22:]

	def search(self,origin,destination):
		self.driver.get("https://www.oncf-voyages.ma")
		sleep(10)
		prices = []
		times = []
		self.driver.find_element_by_xpath("//div[@id='origin']").click()
		self.driver.find_element_by_xpath("//input[@id='origin']").send_keys(origin)
		self.driver.find_element_by_xpath("//h2[@class='SearchForm_title']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//div[@id='destination']").click()
		self.driver.find_element_by_xpath("//input[@id='destination']").send_keys(destination)
		self.driver.find_element_by_xpath("//h2[@class='SearchForm_title']").click()
		sleep(1)
		self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div/button").click()
		while(1):
			sleep(10)
			try:
				tripbox = self.driver.find_element_by_xpath("//div[@class='ant-card trip-card-wrapper']")
				trips = tripbox.find_elements_by_xpath("//label[contains(@class, 'date')]")
				pricess = tripbox.find_elements_by_xpath("//label[contains(@class,'price')]")
				prices.extend([price.text for price in pricess])
				times.extend([trip.text for trip in trips])
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				sleep(2)
				self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div[2]/main/div/div/div/div[1]/div/div[5]/div[2]/a").click()
			except NoSuchElementException :
				break
		return [times,prices]
	def close(self):
		self.driver.close()
		self.driver.quit()
bot = ONCFBot()
#gares = bot.get_all_gares()
gares = ['CASA VOYAGEURS','MEKNES','FES','RABAT AGDAL']
nbGares = len(gares)
data = {}
for i in range(nbGares):
	for j in range(nbGares):
		if i != j:
			data[gares[i]+';'+gares[j]] = bot.search(gares[i],gares[j])

out = open('oncfTrips.csv','w')
out.write('from;to;depart_time;arrival_time;price\n')
for trip in data.keys():
	times = data[trip][0]
	prices = data[trip][1]
	for i in range(len(prices)):
		out.write(trip+";"+times[2*i]+";"+times[2*i+1]+";"+prices[i]+'\n')
bot.close()
