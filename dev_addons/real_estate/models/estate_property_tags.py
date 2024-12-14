# -*- coding: utf-8 -*-#

from odoo import models, fields, api


class EstatePropertyTags(models.Model):
    _name = 'estate.property.tags'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string="Color")
