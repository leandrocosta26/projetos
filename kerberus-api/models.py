# -*- coding: UTF-8 -*-
import requests 
from requests.auth import HTTPBasicAuth

class kerberus_api(object):
    """docstring for kerberus_api"""
    def __init__(self, base_url, user_auth, pass_auth):
        super(kerberus_api, self).__init__()
        self.__base_url = base_url
        self.__user_auth = user_auth
        self.__pass_auth = pass_auth

    def get_url(self):
        return self.__base_url

    def create_order(self, order, header):
        result = requests.post(self.__base_url, data=order,  headers=header, auth=HTTPBasicAuth(self.__user_auth, self.__pass_auth))
        with open('responses.txt', 'w+') as responses :
            responses.write(result.text)

    @classmethod
    def get_orders(cls):
        order = [] 
        with open('order.txt', 'r') as order_file :
            for line in order_file : 
                order.append(str(line.readline()))
        return str(order)