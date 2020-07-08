from flask import session, request, make_response, jsonify
from app import app, db
from .models import Farmers, Farms,Crops, Locations
import jwt, datetime

@app.route('/api/dashboard', methods=['GET'])
def api_dashbord():
    all_farmers = Farmers.query.all()
    count_farmers = all_farmers.count()
    
    all_farms = Farms.query.all()
    count_farms = all_farms.count()
    
    count = 0
    farmers = list()
    
    for farmer in all_farmers:
        if count == 7:
            break
        count += 1
        farmer_data = {}
        
        farmer_data = {}
        farmer_data["id"] = farmer.farmerid
        farmer_data["name"] = farmer.first_name + " " + farmer.last_name
        farm = Farms.query.filter_by(farmerid = farmer.farmerid).first()
        farmer_data["farm"] = farm.farm_name
        farmer_data["contact"] = user.mobilenumber
        farmer_data["parish"] = user.parish
        farmer_data["district"] = user.district
        
        farmers.append(farmer_data) #dictionary within a list
        
    return jsonify({'farmers':farmers,'count_farmers':count_farmers,'count_farms':count_farms })
    
@app.route('/api/add-farmer', methods =['POST'])
def api_addFarmer():
    data = request.get_json()
    
    if  'firstname' in data:
        firstname = data["name"]
    if  'lastname' in data:
        lastname= data["lastname"]
    if  'gender' in data:
        gender = data["gender"]
    if  'contact' in data:
        mobile = data["contact"]
    if  'parish' in data:
        parish = data["parish"]
    if  'district' in data:
        district = data["district"]
    if 'trn' in data:
        trn = data['trn']
        
    farmer = Farmers(firstname = first_name, lastname = last_name,gender = gender , mobilenumber = mobile,parish = parish, district = district )
    db.session.add(farmer)
    db.session.commit()

    return jsonify({'Message':'This farmer name : %s is now added' %farmer.firstname})


@app.route('/api/add-farm', methods =['GET'])
def api_addFarm1():

    all_farmers = Farmers.query.all()
    
    farmers = list()
    for farmer in all_farmers:
        farmer_data = {}
        farmer_data["name"] = farmer.first_name + " " + farmer.last_name
        farmer_data["id"] = farmer.farmerid
        farmers.append(farmer_data) #dictionary within a list
    return jsonify({"farmers":farmers})

@app.route('/api/add-farm', methods =['POST'])
def api_addFarm2():
    data = request.get_json()
    
    if  'farmname' in data:
        farmname = data["farmname"]
    if  'farmer' in data:
        farmer = data["farmer"]
    if  'subdivision' in data:
        subdivision = data["subdivision"]
    if  'parish' in data:
        parish = data["parish"]
    if  'district' in data:
        district = data["district"]
        
    farm = Farms(farm_name = farmname, farmer = farmer, subdivision = subdivision,parish = parish , district = district)
    db.session.add(farm)
    db.session.commit()

    return jsonify({'Message':'This Farm name : %s is now added' %farm.farmname})
   
@app.route('/api/yield-calculator', methods =['GET'])
def api_yieldCalculator1():
    all_crops = Crops.query.all()
    locations = Locations.query.all()
    
    crops = list()
    for crop in all_crops:
        crop_data={}
        crop_data["id"] = crop.cropid
        crop_data["cropname"] = crop.cropname
        crops.append(crop_data) #dictionary within list
        
    divisions = set()
    parishes = set()
    districts = []
    
    for location in locations:
        divisions.add(location["subdivision"])
        parish.add(location["parish"])
        district.append(location["district"])
    divisions = list(divisions)
    parishes = list(parishes)
    return jsonify({"crops":crops,"divisions":divisions, "parishes":parishes, "districts":districts})
    
@app.route('/api/yield-calculator', methods =['POST'])
def api_yieldCalculator2():
    data = request.get_json()
    
    if  'crop' in data:
        farmname = data["crop"]
    if  'district' in data:
        district = data["district"]
    if  'parish' in data:
        parish = data["parish"]
    if  'land_size' in data:
        district = data["land_size"]
    
    #soil_type = 
    return "incomplete"
    '''
    Get the attributes that will be passed as parameters to the model
    tentative atributes are:
        crop name, soil type, altitude, rainfall, temperature, location
    '''
    

    '''
    Here is where the model drops in
    '''

@app.route('/api/search', methods =['POST'])
def api_farmer_search():
    data = request.get_json()
    
    if 'trn' in data:
        searchval = data['trn']
        searchdata = trnSearch(searchval)
        return searchdata
    if 'name' in data:
        searchdata = nameSearch(searchval)
        return searchdata
        

def trnSearch(trn):
    farmer = Farmers.query.filter_by(trn=trn).first()
    farmerdata = {}
    
    farmerdata['farmerid'] = farmer.farmerid
    farmerdata['firstname'] = farmer.name
    farmerdata['lastname']= farmer.lastname
    farmerdata['gender'] = farmer.gender
    farmerdata['mobile'] = farmer.contact
    farmerdata['parish'] = farmer.parish
    farmerdata['district'] = farmer.district
    farmerdata['trn'] = trn
    
    return farmerdata
    








