import json
from bs4 import BeautifulSoup
from pprint import pprint

class HtmlSparser:
	def __init__(self, html):
		self.html = BeautifulSoup(html, features="html.parser")
		self.item_data = {}

	@classmethod
	def from_file(cls, path):
		with open(path, encoding="UTF-8") as html_file:
			return cls(html_file.read())
	
	@classmethod
	def name_key(cls, key):
		return str("-".join(key.getText(strip=True).split(" ")).lower())

	def parse(self):
		self.parseDetails()
		self.parse_nutrition_table()
		self.parse_recommended()

		return self

	def parseDetails(self):
		self.item_data['details'] = {}
		for container in self.html.find_all(class_='detail__container'):
			key = container.find(class_= 'detail__title')
			data = container.find(class_= 'detail__content')
			if key and data:
				self.item_data['details'][HtmlSparser.name_key(key)] = data.getText(strip=True)
		return self
	
	def parse_nutrition_table(self):
		self.item_data['details']['nutri-info'] = {}

		for container in self.html.find_all("dl", class_="detail__container__table"):
			key = container.find(class_= 'detail__content bold')
			data = container.find(class_= 'detail__content justify-end-mobile')
			if key and data and len(key.getText(strip=True)) > 0:
				self.item_data['details']['nutri-info'][HtmlSparser.name_key(key)] = data.getText(strip=True).replace(",", ".")
		
		return self
	
	def parse_recommended(self):
		container = self.html.find(class_="productCarouselComponentContainer")
		if container:
			self.item_data['recommended'] = [i['data-id'] for i in container.find_all(class_= 'spar-productBox__content')]
		return self


			
if __name__ == "__main__":
	parser = HtmlSparser.from_file('products/292934.html')
	parser.parse()
	print(json.dumps(parser.item_data,indent=4))