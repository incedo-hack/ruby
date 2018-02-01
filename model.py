import sys
import logging
from peewee import *
# import rds_config
import datetime
import configparser
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    db_env = 'LOCAL_DATABASE'
    #db_env = 'CLOUD_DATABASE'

    cp = configparser.SafeConfigParser()
    cp.read(os.path.splitext(__file__)[0] + '.ini')
    logging.debug('\n==================================')
    logging.debug('url       : ' + cp.get(db_env, 'db_endpoint'))
    
    rds_host = cp.get(db_env, 'db_endpoint')
    db_username =  cp.get(db_env,'db_username')
    password = cp.get(db_env,'db_password')
    db_name = cp.get(db_env,'db_name')
    port = cp.get(db_env,'port')

    database = MySQLDatabase(db_name, host=rds_host, port=3306, user=db_username, passwd=password)

except Exception as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance. %s", e)
    sys.exit()

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Account(BaseModel):
    name = TextField(null=True)
    address1 = TextField(null=True)
    address2 = TextField(null=True)
    state = TextField(null=True)
    city = TextField(null=True)
    zip = TextField(null=True)
    phone = TextField(null=True)
    web = TextField(null=True)
    contact_name = TextField(null=True)
    contact_email = TextField(null=True)

    class Meta:
        order_by = ('name',)
        
class Branch(BaseModel):
    name = TextField(null=True)
    address1 = TextField(null=True)
    address2 = TextField(null=True)
    state = TextField(null=True)
    city = TextField(null=True)
    zip = TextField(null=True)
    phone = TextField(null=True)
    web = TextField(null=True)
    contact_name = TextField(null=True)
    contact_email = TextField(null=True)    
#    account = ForeignKeyField(Account)

class User(BaseModel):
#    commission_status = TextField(null=True)
    role = TextField(null=True)
    user_name = TextField(null=True)
    first_name = TextField( null=True)
    last_name = TextField( null=True)
    phone_number = TextField( null=True)
    email_id = TextField( null=True)
#    account = ForeignKeyField(Account)
#   branch = ForeignKeyField(Branch)

    class Meta:
         order_by = ('user_name',)        

class prefix_nodes(BaseModel):
    parent_id = IntegerField(null=True)
    order = IntegerField(null=True)
    name = TextField(null=True)
    is_deleted = IntegerField(null=True)
    user_id = IntegerField(null=True)
    user_type = IntegerField(null=True)

class Test(BaseModel):
    ts = DateTimeField(default=datetime.datetime.now)

class Utils(object):
    
    def bulk_insert_device_readings(self,data_source):
        # Insert rows 100 at a time.
        with database.atomic():
            for idx in range(0, len(data_source), 100):
                DeviceReadings.insert_many(data_source[idx:idx+100]).execute()

    def setup_tables(self):
        database.create_tables([Account, User, Branch])
        # database.create_tables([DeviceReadings])

    def drop_all_tables(self):
        #database.drop_table(DeviceReadings)
        #database.drop_table(Device)
        database.drop_table(User)
        #database.drop_table(Country)
        database.drop_table(Branch)
        database.drop_table(Account)
        
    def load_mock_data(self):
        
        #Add some Account
        account = Account(name = 'Incedo Inc', address1 = '2350 Mission College Blvd.,Suite 246', address2 = 'Santa Clara', state = 'CA', city = 'Santa Clara', zip = '95054', phone = '+1 408 531 6040', web = 'www.incedoinc.com', contact_name = 'Robert', contact_email = 'robert@incedoinc.com')
        account.save()      

        #Add some countries
        # country = Country(name = 'India', short_name='IN', code='+91')
        # country.save()
        # country = Country(name = 'United States', short_name='US', code='+106')
        # country.save()
        # country = Country(name = 'Australia', short_name='AUS', code='+99')
        # country.save()

        #Add some devices
        # device = Device(health = 1, loc_area = 'Zone 1', loc_x = 100, loc_y = 100, name = 'Sensor-300578', status = 1, devicetype = 'v-mon-I')
        # device.save()
        # device = Device(health = 2, loc_area = 'Zone 2', loc_x = 101, loc_y = 101, name = 'Sensor-300577', status = 3, devicetype = 'v-mon-II')
        # device.save()
        # device = Device(health = 3, loc_area = 'Zone 3', loc_x = 102, loc_y = 102, name = 'Sensor-300575', status = 2, devicetype = 'v-mon-III')
        # device.save()
        # device = Device(health = 1, loc_area = 'Zone 4', loc_x = 103, loc_y = 103, name = 'Sensor-300579', status = 2, devicetype = 'v-mon-IV')
        # device.save()
        # device = Device(health = 2, loc_area = 'Zone 5', loc_x = 104, loc_y = 104, name = 'Sensor-195732', status = 3, devicetype = 'v-mon-V')
        # device.save()

        #Add some users
        user = User(role = 'Branch Manager', user_name = 'Robert', first_name = 'Robert', last_name = 'Mathew', phone_number = '+919876543245', email_id = 'robert.mathew@incedoinc.com')
        user.save()
        user = User(role = 'HR', user_name = 'Lisa', first_name = 'Lisa', last_name = 'hydon', phone_number = '+914567890987', email_id = 'lisa.hydon@incedoinc.com')
        user.save()

    #Add some branch
        branch = Branch(name = 'Incedo Inc', address1 = 'KadubeesanaHalli Varthur Hobli', address2 = 'Outer Ring road', state = 'Karnataka', city = 'Bangalore', zip = '560103', phone = '+918067085800', web = 'www.incedoinc.com', contact_name = 'Robert', contact_email = 'robert@incedoinc.com')
        branch.save()

        #Add some prefix_nodes
        prefixNodes = prefix_nodes(name = 'Info Systems', user_id = 0, user_type = 0)
        prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 14, name = 'Asia', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 14, name = 'Africa', user_id = 0, user_type = 2)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 16, name = 'India', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 16, name = 'China', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 20, name = 'Karnataka', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 20, name = 'Kerala', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 22, name = 'Bangalore', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 22, name = 'Mangalore', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 23, name = 'Kannur', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 23, name = 'Thrissur', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 24, name = 'Bangalore/B1', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 24, name = 'Bangalore/B2', user_id = 0, user_type = 3)
        #prefixNodes.save()

        # prefixNodes = prefix_nodes(parent_id = 42, name = 'India', user_id = 0, user_type = 3)
        # prefixNodes.save()
        # prefixNodes = prefix_nodes(parent_id = 43, name = 'Karnataka', user_id = 0, user_type = 3)
        # prefixNodes.save()
        # prefixNodes = prefix_nodes(parent_id = 44, name = 'Bangalore', user_id = 0, user_type = 3)
        # prefixNodes.save()
        # prefixNodes = prefix_nodes(parent_id = 45, name = 'Bangalore/B1', user_id = 0, user_type = 3)
        # prefixNodes.save()

        #prefixNodes = prefix_nodes(parent_id = 27, name = 'Thrissur/B1', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 27, name = 'Thrissur/B2', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 21, name = 'Beijing', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 21, name = 'Shanghai', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 36, name = 'Beijing/B1', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 37, name = 'Shanghai/B1', user_id = 0, user_type = 3)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 19, name = 'Africa/B1', user_id = 0, user_type = 2)
        #prefixNodes.save()
        #prefixNodes = prefix_nodes(parent_id = 19, name = 'Africa/B1', user_id = 0, user_type = 2)
        #prefixNodes.save()        
    
if __name__ == "__main__":
    Utils().drop_all_tables()
    Utils().setup_tables()
    Utils().load_mock_data()
    test = Test()
    dt = '08-08-2017 08:14'
    print(test.ts)
    datetime_object = datetime.datetime.strptime(dt, '%d-%m-%Y %H:%M')
    print(datetime_object)
    print(type(datetime_object))
