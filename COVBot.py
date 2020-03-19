from selenium import webdriver
from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException

class COVBot(object):
	"""docstring for COVBot"""
	def __init__(self):
		self.driver = webdriver.Chrome("C:/Program Files/operadriver.exe")
		#self.out = open('COVTrips.csv','a')
		self.driver.maximize_window()
		self.driver.get('https://www.comobila.com/covoiturage/trajet/rechercher')
		
		self.drivers = []
		self.from_to = []
		self.dates_times = []
		self.prices = []


	def get_infos(self):
		tripList = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]').find_elements_by_xpath("//div[contains(@class, 'items')]")
		print(len(tripList))
		sleep(1)
		for trip in tripList:
			driversinfos = trip.find_element_by_xpath('//div[contains(@class, "recent-ride-row-img")]').find_elements_by_xpath('//div')
			tripinfos = trip.find_element_by_xpath('//div[contains(@class,"recent-ride-row-info")]').find_elements_by_xpath('//div')
			tripprice = trip.find_element_by_xpath('//div[contains(@class,"recent-ride-row-price")]').find_elements_by_xpath('//div')
			self.drivers.append([driversinfos[1].text,driversinfos[2].text,driversinfos[3].text])
			self.from_to.append([tripinfos[0].text,tripinfos[3].text,len(tripinfos[2].find_elements_by_xpath('//span'))])
			self.dates_times.append(tripinfos[2].text)
			self.prices.append(tripprice[0].find_elements_by_xpath('//span[contains(@class,"price")]')[0].text)
		print(self.drivers)
		print(self.from_to)
		print(self.dates_times)
		print(self.prices)


bot = COVBot()
bot.get_infos()




		