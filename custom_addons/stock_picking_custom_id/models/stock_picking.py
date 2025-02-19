from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model_create_multi
    def create(self, vals_list):    
        for vals in vals_list:  # 遍歷每筆資料
            # 檢查銷售訂單是否包含 joo-ODM-，且收貨位置為客戶
            if 'joo-ODM-' in str(vals['origin']) and vals['location_dest_id'] == 5:
                sale_order_id = vals['origin']
                # 自定義外部 ID 格式
                external_id = f"joo-DVM-{sale_order_id[8:]}"
                vals['id'] = external_id    # 將外部 ID 賦值給 `id` 欄位
                vals['name'] = external_id  # 將外部 ID 賦值給 `name` 欄位

        return super(StockPicking, self).create(vals_list)
    

