import requests
from app.core.config import settings
from app.lib.util_auth import BearerAuth
from app.lib.redis_util import RedisClient
import json
class ProTyre():
    requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)
    @classmethod
    def authenticate(cls):
        '''
        Returns SCSManager JWT Bearer Token
        '''
        redis_client = RedisClient()
        token = redis_client.get('protyre_jwt')
        if token is None:
            endpoint = '{}/api/auth/'.format(settings.PROTYRE_API_URL)
            r = requests.post(endpoint, allow_redirects=True, verify=False, json={"identity": settings.PROTYRE_USER, "password": settings.PROTYRE_PWD})            
            try:
                res_to_dict = r.json()
                token = res_to_dict['data']['access_token']
                redis_client.setTime('protyre_jwt', token, timeout=3600)              
                return token
            except Exception as e:
                return None
        return token
    

    @classmethod
    def get_api_v1(cls, resource, params=None):
        endpoint = '{}/api/v1{}'.format(settings.PROTYRE_API_URL, resource)

        if params:
            params = json.dumps(params)
        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_batch_code(cls, code, params=None):
        endpoint = '{}/api/v1/batch-orders/?id={}'.format(settings.PROTYRE_API_URL, code)
        # endpoint = '{}/api/v1/batch-orders/?start=0&length=10&search[value]={}'.format(settings.PROTYRE_API_URL, code)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None
    
    @classmethod
    def get_api_v1_tires_from_batch_order(cls, location_id, batch_id, params=None):
        endpoint = '{}/api/v1/transfer-protest/?location_id={}&batch_id={}'.format(settings.PROTYRE_API_URL, location_id, batch_id)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_packs_from_location(cls, location, params=None):
        endpoint = '{}/api/v1/batch-orders/?location_id={}'.format(settings.PROTYRE_API_URL, location)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_locations(cls, params=None):
        endpoint = '{}/api/v1/locations/?exclude_hq=False'.format(settings.PROTYRE_API_URL)

        if params:
            params = json.dumps(params)
        
        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None
    
    @classmethod
    def get_api_v1_location(cls, location_id, params=None):
        endpoint = '{}/api/v1/locations/?_id={}'.format(settings.PROTYRE_API_URL, location_id)

        if params:
            params = json.dumps(params)
        
        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_warehouses(cls, params=None):
        endpoint = '{}/api/v1/warehouses/'.format(settings.PROTYRE_API_URL)

        if params:
            params = json.dumps(params)
        
        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_warehouses_by_location_id(cls, code, params=None):
        endpoint = '{}/api/v1/warehouses/?location_id={}'.format(settings.PROTYRE_API_URL, code)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_samples(cls, code, params=None):
        endpoint = '{}/api/v1/samples/?batch_code={}'.format(settings.PROTYRE_API_URL, code)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_tire_location(cls, code, params=None):
        endpoint = '{}/api/v1/samples/?serial_number={}'.format(settings.PROTYRE_API_URL, code)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None
    
    @classmethod
    def get_api_v1_tire_location_by_barcode(cls, code, params=None):
        endpoint = '{}/api/v1/samples/?barcode={}'.format(settings.PROTYRE_API_URL, code)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def get_api_v1_samples_tire(cls, location_id, status, params=None):
        endpoint = '{}/api/v1/samples/?location_id={}&batch_status={}'.format(settings.PROTYRE_API_URL, location_id, status)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, auth=BearerAuth(cls.authenticate()), params=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None

    @classmethod
    def post_api_v1_transfer_protest(cls, params=None):
        endpoint = '{}/api/v1/transfer-protest/'.format(settings.PROTYRE_API_URL)

        r = requests.post(endpoint, auth=BearerAuth(cls.authenticate()), json=params, allow_redirects=False, verify=True)

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            return None
