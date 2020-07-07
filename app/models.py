from app import db
import datetime 

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, default = '')
    password = db.Column(db.String(255), nullable=False, default = '')

class Farmers(db.Model):
    farmerid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, default = '')
    last_name = db.Column(db.String(100), nullable=False, default = '')
    gender = db.Column(db.String(20), nullable=False, default = '')
    mobilenumber = db.Column(db.Integer, nullable=False, default = 0000000000)
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(200), nullable=False, default = '')
    created = db.Column(db.DateTime, nullable=False, default = datetime.datetime.now())

class Farms(db.Model)
    farmid = db.Column(db.Integer, primary_key=True)
    farm_name = db.Column(db.String(100), nullable=False, default = '')
    soilType = db.Column(db.String(100), nullable=False, default = '')
    subdivision = db.Column(db.String(100), nullable=False, default = '')
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(100), nullable=False, default = '')
    created = db.Column(db.DateTime, nullable=False, default = datetime.datetime.now())
    farmerid = db.Column(db.Integer(), db.ForeignKey('farmers.farmerid'))

class Crops(db.Model):
    cropid =  db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False, default = '')
    crop_type = db.Column(db.String(100), nullable=False, default = '')
    cost =  db.Column(db.Numeric(7, 2), nullable=False)
    
class Yields(db.Model):
    yieldid = db.Column(db.Integer, primary_key=True)
    cropid = db.Column(db.Integer(), db.ForeignKey('crops.cropid'), nullable=False)
    farmid = db.Column(db.Integer(), db.ForeignKey('farms.farmid'), nullable=False)
    revenue = db.Column(db.Numeric(12, 2), nullable=False)
    date_predicted = db.Column()

class Location(db.Model):
    locationid = db.Column(db.Integer, primary_key=True)
    subdivision = db.Column(db.String(100), nullable=False, default = '')
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(100), nullable=False, default = '')
    soil_type = db.Column(db.String(100), nullable=False, default = '')
    altitude = db.Column(db.Numeric(12, 2), nullable=False)
    temperature = db.Column(db.Numeric(12, 2), nullable=False)
    rainfall = db.Column(db.Numeric(12, 2), nullable=False)
    
