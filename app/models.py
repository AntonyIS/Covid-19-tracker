from app import db

class Country(db.Model):
	__tablename__ = "countries"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	image = db.Column(db.String(50))
	infected = db.Column(db.Integer, default=0)
	deaths = db.Column(db.Integer, default=0)
	recovered = db.Column(db.Integer, default=0)
	active = db.Column(db.Integer, default=0)


	def __repr__(self):
		return '<Country {}>'.format(self.name) 