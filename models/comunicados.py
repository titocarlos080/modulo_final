from random import randint
from odoo import api, fields, models


class Comunicados(models.Model):
    _name = 'oe.school.comunicados'
    
    name = fields.Char(string='name', required=True)
    descripcion = fields.Text(string='descripcion')
    
     
 