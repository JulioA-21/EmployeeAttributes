from odoo import models, fields


class EmployeeAttributes(models.Model):
     _inherit = "hr.employee"
     dni  = fields.Integer("DNI")
     DogName  = fields.Char(string="Dog Name")