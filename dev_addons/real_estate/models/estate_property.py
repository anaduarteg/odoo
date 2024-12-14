# -*- coding: utf-8 -*-#

from datetime import timedelta
from odoo import fields, models, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Modelo de propiedades inmobiliarias'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripcion')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Disponible desde',
                                    copy=False,
                                    default=lambda self: self.get_default_date_availability())
    expected_price = fields.Float(string='Precio actual', required=True)
    selling_price = fields.Float(string='Precio de venta', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Habitaciones', default=2)
    living_area = fields.Integer(string='Area de living')
    facades = fields.Integer(string='Fachadas')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Jardin')
    garden_area = fields.Integer(string='Area del Jardin')
    garden_orientation = fields.Selection(
        string='Orientacion del jardin',
        selection=[('north', 'North'),
                   ('south', 'South'),
                   ('east', 'East'),
                   ('west', 'West')])
    active = fields.Boolean(string='Activo', default=True)
    state = fields.Selection(string='Estado',
                             selection=[('new', 'New'),
                                        ('offer_received', 'Offer received'),
                                        ('offer_accepted', 'Offer accepted'),
                                        ('sold', 'Sold'),
                                        ('cancelled', 'Cancelled')],
                             default='new', required=True, copy=False)
    property_type_id = fields.Many2one("estate.property.type", string="Tipo de propiedad")
    partner_id = fields.Many2one("res.partner", string="Comprador", copy=False)
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tags', string="Etiquetas")
    offers_ids = fields.Many2one('estate.property.offers', string="Ofertas")

    @api.model
    def get_default_date_availability(self):
        return fields.Datetime.today() + timedelta(days=90)
