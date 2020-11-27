#!/usr/bin/env python
# coding: utf-8

# In[6]:


import base64
import datetime

import requests

# In[39]:


class SpotifyAPI(object):
    """
    Spotify Client

    Parameters
    ---
    client_id : str
    client_secret : str
    """
    token_url = "https://accounts.spotify.com/api/token"
    access_token = None
    access_token_expires = datetime.datetime.now()
    client_id = None
    client_secret = None

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns :  a base 64 encoded string.
        """
        if self.client_id is None or self.client_secret is None:
            raise Exception("You must set client_id and client_secret")
        client_cred = f"{self.client_id}:{self.client_secret}"
        client_cred_b64 = base64.b64encode(client_cred.encode())
        return client_cred_b64.decode()

    def get_token_headers(self):
        client_cred_b64 = self.get_client_credentials()
        return {
            'Authorization': f'Basic {client_cred_b64}'}

    def get_token_data(self):
        return {
            'grant_type': 'client_credentials'
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_headers()
        r = requests.post(token_url,
                          data=token_data,
                          headers=token_header)
        if r.status_code not in range(200, 299):
            raise Exception('Could not authenticate client')
        data = r.json()
        now = datetime.datetime.now()
        self.access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            return self.perform_auth()
        elif token is None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        access_token = self.access_token
        headers = {
            'Authorization': f"Bearer {access_token}"
        }
        return headers

    def get_resource(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def get_album(self, _id):
        return self.get_resource(_id, resource_type='albums')

    def get_artist(self, _id):
        return self.get_resource(_id, resource_type='artists')

    def base_search(self, query_params):
        headers = self.get_resource_header()
        endpoint = 'https://api.spotify.com/v1/search'
        lookup_url = f"{endpoint}?{query_params}"
        r = requests.get(lookup_url, headers=headers)
        print(r.status_code)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def search(self, query=None, operator=None, operator_query=None, search_type='artist'):
        from urllib.parse import urlencode
        if query is None:
            raise Exception('A query is required to search')
        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for (k, v) in query.items()])
        if operator is not None and operator_query is not None:
            if operator.lower() == 'or' or operator.lower() == 'not':
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({"q": query, "type": search_type.lower()})
        print(query_params)
        return self.base_search(query_params)


# In[40]:
