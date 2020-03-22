from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,ElementNotVisibleException

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
		while(1):
			self.driver.execute_script("window.scrollTo(0, 0);")
			sleep(10)
			try:
				driversinfos = self.driver.find_elements_by_xpath('//div[@class = "recent-ride-row-img"]')
				tripinfos =  self.driver.find_elements_by_xpath('//div[@class = "recent-ride-row-info"]')
				tripprice = self.driver.find_elements_by_xpath('//div[@class = "recent-ride-row-price"]')
				for i in range(len(driversinfos)):
					self.drivers.append(driversinfos[i].text.split('\n'))
					self.from_to.append(tripinfos[i].text.split('\n')[0].split(' '))
					if tripinfos[i].text.split('\n')[1].startswith('Date'):
						self.dates_times.append(tripinfos[i].text.split('\n')[1].split(': ')[1].split(' - '))
					else:
						self.dates_times.append(tripinfos[i].text.split('\n')[2].split(': ')[1].split(' - '))
					self.prices.append(tripprice[i].text.split('\n')[0])
					self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				sleep(2)
				self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/ul/li[13]/a").click()
			except ElementNotVisibleException :
				break

	def close(self):
		self.driver.close()
		self.driver.quit()

	def saveinfos(self):
out = open('COVTrips.csv','w')
out.write('driver_name;driver_sex;driver_age;driver_is_smoking;from;to;date;time;price\n')
for i in range(len(bot.drivers)):
	out.write(bot.drivers[i][0]+';'+bot.drivers[i][1].split(' | ')[0]+';'+bot.drivers[i][1].split(' | ')[1]+';'+bot.drivers[i][2].split(' : ')[1]+';'+bot.from_to[i][0]+';'+bot.from_to[i][1]+';'+bot.dates_times[i][0]+';'+bot.dates_times[i][1]+';'+bot.prices[i]+'\n');



bot = COVBot()
bot.get_infos()
bot.saveinfos()
bot.close()




		