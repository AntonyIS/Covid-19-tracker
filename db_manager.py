from app.models import Country


# process scrapped data and add or refresh the database
class DbManager():
	countries = Country.query.all()
	def add():
		for data in l:
			country = Country(name=data['country'],image = "default.jpg",infected = data['data'][0],deaths = data['data'][1],recovered = data['data'][2],active= data['data'][3])
			db.session.add(country)
			db.session.commit()

	def refresh():
		
		for country in countries:
			db.session.delete(country)
			db.session.commit()
