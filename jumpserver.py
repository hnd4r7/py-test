#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, requests, time

class HTTP:
    server = None
    token = None

    @classmethod
    def get_token(cls, username, password):
        data              = {'username': username, 'password': password}
        url               = "/api/v1/authentication/auth/"
        res               = requests.post(cls.server + url, data)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            token = res_data.get('token')
            cls.token = token
        else:
            print("获取 token 错误, 请检查输入项是否正确")
            sys.exit()

    @classmethod
    def get(cls, url, params=None, **kwargs):
        url               = cls.server + url
        headers           = {
            'Authorization': "Bearer {}".format(cls.token)
        }
        kwargs['headers'] = headers
        res               = requests.get(url, params, **kwargs)
        return res

    @classmethod
    def post(cls, url, data=None, json=None, **kwargs):
        url               = cls.server + url
        headers           = {
            'Authorization': "Bearer {}".format(cls.token)
        }
        kwargs['headers'] = headers
        res               = requests.post(url, data, json, **kwargs)
        return res

class User(object):

    def __init__(self):
        self.id           = None
        self.name         = user_name
        self.username     = user_username
        self.email        = user_email

    def input_preconditions(self):
        if self.username is None:
            self.username = input("请输入需要新建的用户 (user): ")

    def get_preconditions(self):
        self.input_preconditions()

    def exist(self):
        url               = '/api/v1/users/users/'
        params            = {'username': self.username}
        res               = HTTP.get(url, params=params)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            self.id       = res_data[0].get('id')
        else:
            self.create()

    def create(self):
        print("创建用户 {}".format(self.username))
        url               = '/api/v1/users/users/'
        data              = {
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'is_active': True
        }
        res               = HTTP.post(url, data)
        self.id           = res.json().get('id')

    def perform(self):
        self.get_preconditions()
        self.exist()

class Node(object):

    def __init__(self):
        self.id           = None
        self.name         = asset_node_name

    def input_preconditions(self):
        if self.name is None:
            self.name     = input("请输入资产节点名称 (Default): ")

    def get_preconditions(self):
        self.input_preconditions()

    def exist(self):
        url               = '/api/v1/assets/nodes/'
        params            = {'value': self.name}
        res               = HTTP.get(url, params=params)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            self.id       = res_data[0].get('id')
        else:
            self.create()

    def create(self):
        print("创建资产节点 {}".format(self.name))
        url               = '/api/v1/assets/nodes/'
        data              = {
            'value': self.name
        }
        res               = HTTP.post(url, data)
        self.id           = res.json().get('id')

    def perform(self):
        self.get_preconditions()
        self.exist()

class AdminUser(object):

    def __init__(self):
        self.id           = None
        self.name         = assets_admin_name
        self.username     = assets_admin_username
        self.password     = assets_admin_password

    def input_preconditions(self):
        if self.name is None:
            self.name     = input("请输入资产管理用户名称 (test_root): ")

    def get_preconditions(self):
        self.input_preconditions()

    def exist(self):
        url               = '/api/v1/assets/admin-user/'
        params            = {'username': self.name}
        res               = HTTP.get(url, params=params)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            self.id       = res_data[0].get('id')
        else:
            self.create()

    def create(self):
        print("创建管理用户 {}".format(self.name))
        if self.username is None:
            self.username = input("请输入资产的管理用户 (root): ")
        if self.password is None:
            self.password = input("请输入资产管理用户 {} 的密码 (********): ".format(self.username))
        url               = '/api/v1/assets/admin-users/'
        data              = {
            'name': self.name,
            'username': self.username,
            'password': self.password
        }
        res               = HTTP.post(url, data)
        self.id           = res.json().get('id')

    def perform(self):
        self.get_preconditions()
        self.exist()

class Asset(object):

    def __init__(self):
        self.id           = None
        self.name         = asset_name
        self.ip           = asset_ip
        self.platform     = asset_platform
        self.protocols    = asset_protocols
        self.admin_user   = AdminUser()
        self.node         = Node()

    def input_preconditions(self):
        if self.ip is None:
            self.ip           = input("请输入资产IP (172.16.0.1): ")

    def get_preconditions(self):
        self.input_preconditions()
        self.admin_user.get_preconditions()
        self.node.get_preconditions()

    def exist(self):
        url               = '/api/v1/assets/assets/'
        params            = {
            'hostname': self.name
        }
        res               = HTTP.get(url, params)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            self.id       = res_data[0].get('id')
        else:
            self.create()

    def create(self):
        print("创建资产 {}".format(self.ip))
        if self.platform is None:
            self.platform = input("请输入资产的系统平台 (linux):")
        if self.protocols is None:
            self.protocols= input("请输入资产的协议端口 (ssh/22): ")
        self.admin_user.perform()
        self.node.perform()
        url               = '/api/v1/assets/assets/'
        data              = {
            'hostname': self.ip,
            'ip': self.ip,
            'platform': self.platform,
            'protocols': self.protocols,
            'admin_user': self.admin_user.id,
            'nodes': [self.node.id],
            'is_active': True
        }
        res               = HTTP.post(url, data)
        self.id           = res.json().get('id')

    def perform(self):
        self.get_preconditions()
        self.exist()

class SystemUser(object):

    def __init__(self):
        self.id           = None
        self.name         = assets_system_name
        self.username     = assets_system_username

    def input_preconditions(self):
        if self.name is None:
            self.name     = input("请输入资产的系统用户名称 (test_ssh): ")

    def get_preconditions(self):
        self.input_preconditions()

    def exist(self):
        url               = '/api/v1/assets/system-user/'
        params            = {'name': self.name}
        res               = HTTP.get(url, params)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            self.id       = res_data[0].get('id')
        else:
            self.create()

    def create(self):
        print("创建系统用户 {}".format(self.name))
        if self.username is None:
            self.username = input("请输入资产的系统用户 (devuser): ")
        url               = '/api/v1/assets/system-user/'
        data              = {
            'name': self.name,
            'username': self.username,
            'login_mode': 'auto',
            'protocol': 'ssh',
            'auto_push': 'true',
            'sudo': 'All',
            'shell': '/bin/bash',
            'auto_generate_key': 'true',
            'is_active': 'true'
        }
        res               = HTTP.post(url, data)
        self.id           = res.json().get('id')

    def perform(self):
        self.get_preconditions()
        self.exist()

class AssetPermission(object):

    def __init__(self):
        self.name         = perm_name
        self.user         = User()
        self.asset        = Asset()
        self.system_user  = SystemUser()

    def input_preconditions(self):
        if self.name is None:
            self.name         = input("情输入资产授权名称 (test_ssh_perms): ")

    def get_preconditions(self):
        self.input_preconditions()

    def create(self):
        print("创建资产授权名称 {}".format(self.name))
        url               = '/api/v1/perms/asset-permissions/'
        data              = {
            'name': self.name,
            'users': [self.user.id],
            'assets': [self.asset.id],
            'system_users': [self.system_user.id],
            'actions': ['all'],
            'is_active': True,
            'date_start': perm_date_start,
            'date_expired': perm_date_expired
        }
        print(data)
        res               = HTTP.post(url, data)
        res_data          = res.json()
        if res.status_code in [200, 201] and res_data:
            print("创建资产授权规则成功: ", res_data)
        else:
            print("创建授权规则失败: ", res_data)

    def perform(self):
        self.user.perform()
        self.asset.perform()
        self.system_user.perform()
        self.get_preconditions()
        self.create()

class APICreateAssetPermission(object):

    def __init__(self):
        self.jms_url      = jms_url
        self.username     = jms_username
        self.password     = jms_password
        self.token        = None
        self.server       = None

    def init_http(self):
        HTTP.server       = self.jms_url
        HTTP.get_token(self.username, self.password)

    def perform(self):
        self.init_http()
        self.perm         = AssetPermission()
        self.perm.perform()


if __name__ == '__main__':

    # jumpserver url 地址
    jms_url                = 'http://192.168.100.244'

    # 管理员账户
    jms_username           = 'admin'
    jms_password           = 'admin'

    # 资产节点
    asset_node_name        = 'test'

    # 资产信息
    asset_name             = '192.168.100.1'
    asset_ip               = '192.168.100.1'
    asset_platform         = 'linux'
    asset_protocols        = ['ssh/22']

    # 资产管理用户
    assets_admin_name      = 'test_root'
    assets_admin_username  = 'root'
    assets_admin_password  = 'test123456'

    # 资产系统用户
    assets_system_name     = 'test'
    assets_system_username = 'test'

    # 用户用户名
    user_name              = '测试用户'
    user_username          = 'test'
    user_email             = 'test@jumpserver.org'

    # 资产授权
    perm_name              = 'AutoPerm' +'_'+ (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    perm_date_start        = '2021-05-01 14:25:47 +0800'
    perm_date_expired      = '2021-06-01 14:25:47 +0800'

    api = APICreateAssetPermission()
    api.perform()