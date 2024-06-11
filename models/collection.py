import requests
from odoo import models, fields

class Collection(models.Model):
    _name = 'my_odoo_module.collection'
    _description = 'Collection'

    owner = fields.Char(string='Owner')
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    number_of_items = fields.Integer(string='Number of Items')
    category = fields.Char(string='Category')

    def import_collections(self):
        api_token = "a6031d9af1ff4ffb82d5449867e227d6b2c0a969"  # Your API token
        url = 'http://127.0.0.1:3000/api/v1/collections'
        headers = {'Authorization': f'Token {api_token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            collections_data = response.json()
            for data in collections_data:
                self.create({
                    'owner': data.get('owner'),
                    'name': data.get('name'),
                    'description': data.get('description'),
                    'number_of_items': data.get('number_of_items'),
                    'category': data.get('category'),
                })
        else:
            raise Exception('Failed to import collections')
