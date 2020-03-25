from selenium import webdriver
from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException

class CTMBot(object):
	"""docstring for CTMBot"""
	def __init__(self):
		self.driver = webdriver.Chrome("C:/Program Files/operadriver.exe")
		self.out = open('CTMTrips.csv','a')
		self.driver.maximize_window()

	def search(self,origin,destination):
		self.driver.get('http://www.ctm.ma/home/index')
		sleep(2)
		prices = []
		times = []
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[1]/div/input").click()
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[1]/div/input").send_keys(origin)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[7]/h1').click()
		sleep(1)
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[2]/div/input").click()
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[2]/div/input").send_keys(destination)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[7]/h1').click()
		sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[3]/div/div/input').click()
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[7]/div[2]/div/form/div[2]/div[3]/div/div/input').send_keys("20-03-2020")
		sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[7]/div[2]/div/form/div[4]/div[2]/button').click()
		sleep(10)
		try:
			timeList = self.driver.find_elements_by_xpath("//span[contains(@class, 'horaires-tab')]")
			priceList = self.driver.find_elements_by_xpath("//span[contains(@class, 'cell-price')]")
			prices.extend([price.text for price in priceList])
			times.extend([time.text for time in timeList])
			for i in range(len(prices)):
				self.out.write(origin+";"+destination+";"+times[2*i]+";"+times[2*i+1]+";"+prices[i]+'\n')
		except UnexpectedAlertPresentException :
			self.driver.switch_to.alert.accept()
		
	def close(self):
		self.driver.close()
		self.driver.quit()
		self.out.close()


bot = CTMBot()
gares = ['Agadir','Al Hoceima','Azrou','Beni Mellal','Fkih Ben Salah','Berkane','Casablanca FAR','Casablanca Ain Sebaa','Casablanca Maarif','Chefchaouen','Dakhla','El Hajeb','Errachidia','Essaouira','Fes','Fnidek','Guelmim','Ifrane','Kasbat Tadla','Kelaa Sraghna','Khemisset','Khenifra','Khouribga','Ksar El Kébir','Laayoune','Larache','Marrakech','Meknes','Midelt','Mrirt','Nador','Ouarzazate','Oujda','Rabat','Safi','Saidia','Sidi Kacem','Souk Larbaa','Tan Tan','Tanger','Taounate','Taza','Tetouan','Tiflet']
nbGares = len(gares)
for i in range(32,nbGares):
	print(i)
	for j in range(nbGares):
		if i != j:
			print(gares[i],gares[j])
			bot.search(gares[i],gares[j])
bot.close()


