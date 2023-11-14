import requests
from app.core.config import settings
from app.lib.util_auth import BearerAuth
from app.lib.redis_util import RedisClient
import json
import logging

class Methodology():
    
    @classmethod
    def authenticate(cls):
        redis_client = RedisClient()
        token = redis_client.get('methodology_jwt')
        if token is None:
            endpoint = '{}/api/auth/'.format(settings.METHODOLOGY_API_URL)            
            r = requests.post(endpoint, allow_redirects=True, verify=False, json={"identity": settings.METHODOLOGY_API_USER, "password": settings.METHODOLOGY_API_PWD}, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})
            try:
                res_to_dict = r.json()
                token = res_to_dict['data']['access_token']
                redis_client.setTime('methodology_jwt', token, timeout=3600)              
                return token
            except Exception as e:
                logging.warning(e)
                return None
        return token
    
    @classmethod
    def get_api_v1_methodology(cls, params=None):
        endpoint = '{}{}'.format(settings.METHODOLOGY_API_URL, settings.METHODOLOGY_API_ENDPOINT)
        
        if params:
            params = json.dumps(params)
        r = requests.get(endpoint, params=params, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})
        
        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            logging.warning(e)
            return None
    
    @classmethod
    def get_api_v1_measurement_unit(cls, params=None):
        endpoint = '{}{}'.format(settings.METHODOLOGY_API_URL, settings.METHODOLOGY_API_UNIT_ENDPOINT)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, params=params, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            logging.warning(e)
            return None

    @classmethod
    def get_api_v1_test_type(cls, params=None):
        endpoint = '{}{}'.format(settings.METHODOLOGY_API_URL, settings.METHODOLOGY_API_TYPE_ENDPOINT)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, params=params, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            logging.warning(e)
            return None

    @classmethod
    def get_api_v1_test_type_by_id(cls, id, params=None):
        endpoint = '{}{}?id={}&status=active'.format(settings.METHODOLOGY_API_URL, settings.METHODOLOGY_API_TYPE_ENDPOINT, id)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, params=params, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            logging.warning(e)
            return None

    @classmethod
    def get_api_v1_methodology_full(cls, id, params=None):
        endpoint = '{}{}?id={}&full=true'.format(settings.METHODOLOGY_API_URL, settings.METHODOLOGY_API_ENDPOINT, id)

        if params:
            params = json.dumps(params)

        r = requests.get(endpoint, params=params, headers={'CF-Access-Client-Id': settings.CF_TEST_METHODOLOGIES_ACCESS_ID, 'CF-Access-Client-Secret': settings.CF_TEST_METHODOLOGIES_SECRET})

        try:
            json_response = r.json()
            return json_response
        except Exception as e:
            logging.warning(e)
            return None
