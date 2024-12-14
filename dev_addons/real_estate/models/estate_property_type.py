# -*- coding: utf-8 -*- #

from odoo import models,fields,api


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'EstatePropertyType'

    name = fields.Char(string='Nombre', required=True)

