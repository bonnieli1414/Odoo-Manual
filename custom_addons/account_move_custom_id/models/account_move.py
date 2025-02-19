from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"
    
    invoice_origin = fields.Char(
        string='Origin',
        readonly=False,
        tracking=True,
        help="The document(s) that generated the invoice.",
    )

    @api.model_create_multi
    def create(self, vals_list):
        
        for vals in vals_list:  # 遍歷每筆資料
            # 檢查 1.是否有 'invoice_origin' 欄位
            #      2.是否包含 joo-ODM-
            #      3.user_id是否為RPA
            if vals.get('invoice_origin') and 'joo-ODM-' in str(vals['invoice_origin']) and vals.get('user_id') and str(vals['user_id']) == '13':
                sale_order_id = vals['invoice_origin']
                # 自定義外部 ID 格式
                external_id = f"joo-PAM-{sale_order_id[8:]}"
                vals['id'] = external_id    # 將外部 ID 賦值給 `id` 欄位
                vals['name'] = external_id  # 將外部 ID 賦值給 `name` 欄位

        return super(AccountMove, self).create(vals_list)
    

