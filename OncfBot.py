from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as sp
from selenium.common.exceptions import NoSuchElementException
class ONCFBot(object):
	"""docstring for ONCFBot"""
	def __init__(self):
		self.driver = webdriver.Chrome("C:/Program Files/operadriver.exe")
		self.driver.maximize_window()
		self.out = open('oncfTrips.csv','a')
		self.out.write('from;to;depart_time;arrival_time;price\n')
		

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
		sleep(2)
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
		self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div/div/div[1]/div/div/input").click()
		sleep(1)
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[4]").click()
		sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/label[1]/span[2]').click()
		sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
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
		for i in range(len(prices)):
			self.out.write(origin+";"+destination+";"+times[2*i]+";"+times[2*i+1]+";"+prices[i]+'\n')
	def close(self):
		self.driver.close()
		self.driver.quit()
		self.out.close()
bot = ONCFBot()
# gares = bot.get_all_gares() # all gars are a lot 
gares = ['AEROPORT MED V', 'AGADIR  (SUPRAT.)', 'AIN SEBAA', 'AIN-TAOUJDATE',  'ASILAH', 'BENGUERIR', 'BENI-MELLAL', 'BERRECHID', 'BOUZNIKA', 'CASA PORT', 'CASA VOYAGEURS', 'CHEFCHAOUEN', 'EL JADIDA', 'EL KHEMISSET', 'EL KSAR EL KEBIR',  'ERFOUD (SUPRAT.)', 'ERRACHIDIA (SUPRAT.)', 'ESSAOUIRA', 'FACULTES', 'FES', 'FNIDEQ (SUPRA.)', 'FQUIH BEN SALAH', 'GUELMIMA', 'GUELMIME',  'JORF EL MELHA', 'KELAA  DES  SRAGHNAS', 'KENITRA', 'KHENIFRA (SUPRAT.)', 'KHOURIBGA', 'LAAYOUNE', 'LARACHE', "L'OASIS", 'MARRAKECH', 'MARTIL' , 'MEKNES', 'MEKNES AL AMIR',  'MERS SULTAN', 'MIDELT (SUPRAT.)', 'MOHAMMEDIA', 'NADOR VILLE', 'OUARZAZATE', 'OUEZZANE', 'OUJDA', 'RABAT AGDAL', 'RABAT VILLE',  'SAFI', 'SALE', 'SALE TABRIQUET', 'SEBAA-AIOUN', 'SETTAT', 'SIDI KACEM',  'SIDI SLIMANE MEDINA', 'SKHIRAT', 'SOUK EL ARBAA', 'TANGER VILLE', 'TAZA', 'TEMARA', 'TETOUAN', 'TIZNIT',  'YOUSSOUFIA']
nbGares = len(gares)
for i in range(29,nbGares):
	print(i)
	for j in range(nbGares):
		if i != j:
			print(gares[i],gares[j])
			bot.search(gares[i],gares[j])
bot.close()
