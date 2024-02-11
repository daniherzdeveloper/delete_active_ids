from odoo import models, api

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    def cancel_active_orders(self):
        self.write({'state': 'cancel'})
        self.unlink()

class CustomPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def cancel_active_orders(self):
        self.write({'state': 'cancel', 'mail_reminder_confirmed': False})
        self.unlink()

class CustomAccountMove(models.Model):
    _inherit = 'account.move'

    def cancel_active_orders(self):
        self.button_draft()
        self.unlink()