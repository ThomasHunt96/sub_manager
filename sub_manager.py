from datetime import datetime, timedelta



class user:
	
	def __init__(self, email, name, password, subscriptions):
		self.email = email
		self.name = name
		self.password = password
		self.subscriptions = subscriptions

	def end_subscription(x):
		subscriptions[x].active = False

		return subscription.url

class subscription:
	

	def __init__(self,url,name,date_subbed,price,active):
		self.url = url
		self.name = name
		self.date_subbed = date.today()
		self.price = price
		self.active = True

	def ended():
		self.end_date = date.today()


	def time_subbed():
		current_date = self.date_subbed + timedelta



