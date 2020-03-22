from app import *
from app.src import l


from app.models import Country
from flask import Flask, render_template, url_for, redirect


from config import Config



@app.route('/')
def index():
	countries = Country.query.all()
	total_infected = 0
	total_deaths = 0
	total_recovered= 0
	total_active = 0
	for country in countries:
		total_infected += country.infected
		total_deaths += country.deaths
		total_recovered += country.recovered
		total_active += country.active
	
	return render_template('index.html', countries= countries,total_infected=total_infected,total_deaths=total_deaths,total_recovered=total_recovered,total_active=total_active, num_countries= len(countries), title="Covid 19 | Home" )



@app.route('/country/<name>')
def country_detail(name):

	countries = Country.query.all()
	country = Country.query.filter_by(name=name).first()
	print("COUNTRY", country.name)
	total_infected = 0
	total_deaths = 0
	total_recovered= 0
	total_active = 0

	for nchi in countries:
		total_infected += nchi.infected
		total_deaths += nchi.deaths
		total_recovered += nchi.recovered
		total_active += nchi.active
	return render_template("country_detail.html", country=country,total_infected=total_infected,total_deaths=total_deaths,total_recovered=total_recovered,total_active=total_active, num_countries= len(countries), countries=countries, title="Covid 19 | {}".format(name))


@app.route('/fight corona')
def fight_corona():
	countries = Country.query.all()
	total_infected = 0
	total_deaths = 0
	total_recovered= 0
	total_active = 0
	for country in countries:
		total_infected += country.infected
		total_deaths += country.deaths
		total_recovered += country.recovered
		total_active += country.active

	half = ((len(countries)+ 1)//2)
	first_half = countries[:half]
	second_half = countries[half:]
	return render_template('fight_corona.html',total_infected=total_infected,total_deaths=total_deaths,total_recovered=total_recovered,total_active=total_active,first_half=first_half, second_half=second_half,title="Covid 19 | Fight Corona Virus")


@app.route('/reload')
def reload():
	# delete data from db
	try:
		db.drop_all()
		db.create_all()
		for data in l:
			country = Country(name=data['country'],image = "default.jpg",infected = data['data'][0],deaths = data['data'][1],recovered = data['data'][2],active= data['data'][3])
			db.session.add(country)
			db.session.commit()	
			print(data)
	except:
		raise "Something bad happened"

	return redirect(url_for('index'))
