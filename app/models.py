from app import db
import datetime 

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, default = '')
    password = db.Column(db.String(255), nullable=False, default = '')
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repre__(self):
        return '<Name %r>' % self.username

class Farmers(db.Model):
    farmerid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, default = '')
    last_name = db.Column(db.String(100), nullable=False, default = '')
    gender = db.Column(db.String(20), nullable=False, default = '')
    mobilenumber = db.Column(db.Integer, nullable=False, default = 0000000000)
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(200), nullable=False, default = '')
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self,first_name,last_name,gender,mobilenumber, parish, district):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.mobilenumber = mobilenumber
        self.parish = parish
        self.district = district
        created = datetime.datetime.now()

    def __repre__(self):
        return '<Name %r>' % self.first_name

class Farms(db.Model):
    farmid = db.Column(db.Integer, primary_key=True)
    farm_name = db.Column(db.String(100), nullable=False, default = '')
    soilType = db.Column(db.String(100), nullable=False, default = '')
    subdivision = db.Column(db.String(100), nullable=False, default = '')
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(100), nullable=False, default = '')
    created = db.Column(db.DateTime, nullable=False)
    farmerid = db.Column(db.Integer(), db.ForeignKey('farmers.farmerid'))

    def __init__(self,farm_name,soilType,subdivision, parish, district,farmerid):
        self.farm_name = farm_name
        self.soilType = soilType
        self.subdivision = subdivision
        self.farmerid = farmerid
        self.parish = parish
        self.district = district
        created = datetime.datetime.now()

    def __repre__(self):
        return '<Name %r>' % self.farm_name
        
class Crops(db.Model):
    cropid =  db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False, default = '')
    crop_type = db.Column(db.String(100), nullable=False, default = '')
    cost =  db.Column(db.Numeric(7, 2), nullable=False)

    def __init__(self,crop_name,crop_type,cost):
        self.crop_name = crop_name
        self.crop_type = crop_type
        self.cost = cost

    def __repre__(self):
        return '<Name %r>' % self.crop_name
        
        
class Locations(db.Model):
    locationid = db.Column(db.Integer, primary_key=True)
    subdivision = db.Column(db.String(100), nullable=False, default = '')
    parish = db.Column(db.String(100), nullable=False, default = '')
    district = db.Column(db.String(100), nullable=False, default = '')
    soil_type = db.Column(db.String(100), nullable=False, default = '')
    altitude = db.Column(db.Numeric(12, 2), nullable=False)
    temperature = db.Column(db.Numeric(12, 2), nullable=False)
    rainfall = db.Column(db.Numeric(12, 2), nullable=False)

    def __init__(self,subdivision,parish, district, soil_type,altitude, temperature, rainfall):
        self.subdivision = subdivision
        self.parish = parish
        self.district = district
        self.soil_type = soil_type
        self.altitude = altitude
        self.temperature = temperature
        rainfall = rainfall

    def __repre__(self):
        return '<Name %r>' % self.farm_name

class Yields(db.Model):
    yieldid = db.Column(db.Integer, primary_key=True)
    cropid = db.Column(db.Integer(), db.ForeignKey('crops.cropid'), nullable=False)
    farmid = db.Column(db.Integer(), db.ForeignKey('farms.farmid'), nullable=False)
    locationid = db.Column(db.Integer(), db.ForeignKey('locations.locationid'), nullable=False)
    revenue = db.Column(db.Numeric(12, 2), nullable=False)
    date_predicted = db.Column(db.DateTime, nullable=False, default = datetime.datetime.now())

    def __init__(self,cropid,farmid,locationid,revenue):
        self.cropid = cropid
        self.farmid = farmid
        self.locationid = locationid
        self.revenue = revenue
        self.date_predicted = datetime.datetime.now()
