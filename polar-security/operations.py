"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
from .polar_api_auth import *

logger = get_logger('polar-security')


def make_api_call(connector_info, method="GET", endpoint="", config=None, params=None, data=None, json_data=None):
    try:
        polar_object = PolarSecurityAuth(config)
        token = polar_object.validate_token(config, connector_info)
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        server_url = config.get('url').strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        server_url = server_url + endpoint
        response = requests.request(method=method, url=server_url,
                                    headers=headers, data=data, json=json_data, params=params,
                                    verify=config.get('verify_ssl'))
        if response.ok:
            return response.json()
        else:
            if response.text != "":
                err_resp = response.json()
                failure_msg = err_resp['errors']
                error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                     failure_msg if failure_msg else '')
            else:
                error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
            logger.error(error_msg)
            raise ConnectorError(error_msg)
    except requests.exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except requests.exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except requests.exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except requests.exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as err:
        raise ConnectorError(str(err))


def convert_date_time(str_date):
    return datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")


def build_payload(params):
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    return params


def get_linked_vendors(config, params, connector_info):
    endpoint = "/linkedVendor"
    return make_api_call(connector_info, endpoint=endpoint, config=config)


def get_data_stores(config, params, connector_info):
    params = build_payload(params)
    endpoint = "/dataStores"
    return make_api_call(connector_info, endpoint=endpoint, config=config, params=params)


def get_data_stores_summary(config, params, connector_info):
    endpoint = "/dataStores/summary"
    return make_api_call(connector_info, endpoint=endpoint, config=config)


def get_vendors_data_stores(config, params, connector_info):
    params = build_payload(params)
    endpoint = "/linkedVendor/{vendor_id}/dataStore".format(vendor_id=params.get('vendor_id'))
    return make_api_call(connector_info, endpoint=endpoint, config=config, params=params)


def get_data_store(config, params, connector_info):
    params = build_payload(params)
    endpoint = "/dataStores/{store_id}".format(store_id=params.get('store_id'))
    return make_api_call(connector_info, endpoint=endpoint, config=config)


def get_vendor_accessible_data_store(config, params, connector_info):
    endpoint = "/accessible-data-stores"
    return make_api_call(connector_info, endpoint=endpoint, config=config)


def apply_label(config, params, connector_info):
    endpoint = "/dataStores/{store_id}/labels".format(store_id=params.get('store_id'))
    boady = {"label": params.get('label')}
    return make_api_call(connector_info, method='PUT', endpoint=endpoint, config=config, data=boady)


def _check_health(config, connector_info):
    try:
        return check(config, connector_info)
    except Exception as e:
        logger.error("Invalid Credentials: %s" % str(e))
        raise ConnectorError("Invalid Credentials")


operations = {
    'get_linked_vendors': get_linked_vendors,
    'get_data_stores': get_data_stores,
    'get_data_stores_summary': get_data_stores_summary,
    'get_vendors_data_stores': get_vendors_data_stores,
    'get_data_store': get_data_store,
    'get_vendor_accessible_data_store': get_vendor_accessible_data_store,
    'apply_label': apply_label
}
