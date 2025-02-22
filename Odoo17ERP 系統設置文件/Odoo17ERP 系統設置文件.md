---
title: Odoo17ERP 系統設置文件
tags: [odoo]

---

# Odoo17ERP 系統設置文件
## 一、模板
### 1.1 Odoo 主機資料
* [Odoo 主機資料列表](https://docs.google.com/spreadsheets/d/1VdZ6y2LfEQqHV5eBv3OYwaR2kVeEXpCMl_aNII4B4ZM/edit?usp=drive_link)

### 1.2 系統模板備份
* [00-jooERP-Template-2025-01-06(測試機)](https://odoo.ewebs.tw/web/login?db=00-jooERP-Template-2025-01-06)
* [odoo-sample-test(正式機)](https://sample.odoo.ewebs.tw/web?db=odoo-sample-test)

### 1.3 原生模組安裝
* 銷售
* 庫存
* 採購
* 會計
* 製造
* 自動化規則
### 1.4 版本17的原植addon安裝列表
* 原植odoo17-核心ERP課程的補充檔案，[請按此處](https://drive.google.com/drive/u/1/folders/1uWsFt2zeK6BXaFX27zQrgVa_DBzBNaZl)
1. account_print_journal_voucher：台灣會計傳票列印
2. accounting_pdf_reports：Odoo 17 Accounting Financial Reports
3. l10n_tw_standard_ifrss：台灣常用會計科目與台灣財務報表結構(社區版)


## 二、記錄規則設定
### 2.1 新增「只允許 Administrator 訪問所有使用者資料」
* 路徑：設定>技術>安全>記錄規則
* 名稱：只允許 Administrator 訪問所有使用者資料
* 資料集：使用者
* 存取權：已閱讀、建立、寫入、刪除
* 規則定義：['|', ('id', '=', user.id), ('id', '!=', 2)] 
* 群組名稱：空白


## 三、群組設定
### 3.1 新增「技術 / Administrator 特殊權限」
* 說明：新增「技術 / Administrator 特殊權限」群組，將部分功能只限定Administrator設定
* 設定方式：
    * 路徑：設定>使用者及公司>群組
    * 新增設定值：
        * 應用程式：技術
        * 名稱：Administrator 特殊權限
        * 使用者：只設定Administrator及MIS
        * 選單：
            * 設定/一般設定
            * 設定/翻譯
            * 設定/使用者及公司/群組
            * 設定/技術
            * 應用程式
        * 其他頁籤都設定：空白

### 3.2 刪除「額外的權利/技術特性」
* 說明：刪除「額外的權利/技術特性」的部分功能，轉部分功能轉為只有Administrator和MIS獨有
* 設定方式：
    * 路徑：設定>使用者及公司>群組，搜尋「額外的權利/技術特性」點擊「選單」頁籤
    * 刪除「選單」頁籤的設定：
        * 設定/翻譯
        * 設定/技術

### 3.3 修改「會計 / 會計人員」(正式機)
* 說明：修改「會計 / 會計人員」名稱為「會計 / 帳單管理員」
* 設定方式：
    * 路徑：設定>使用者及公司>群組，搜尋「會計 / 會計人員」，修改名稱為「會計 / 帳單管理員」

### 3.4 修改「技術 / 只限讀取功能」(正式機)
* 說明：修改「技術 / 只限讀取功能」名稱為「顯示會計功能 - 唯讀」
* 設定方式：
    * 路徑：設定>使用者及公司>群組，搜尋「技術 / 只限讀取」，修改名稱為「顯示會計功能 - 唯讀」

### 3.5 修改「技術 / 簿記員」(正式機)
* 說明：修改「技術 / 簿記員」名稱為「技術 / 顯示所有會計功能」
* 設定方式：
    * 路徑：設定>使用者及公司>群組，搜尋「技術 / 簿記員」，修改名稱為「技術 / 顯示所有會計功能」


## 四、使用者設定
### 4.1 新增「RPA」
* 說明：新增使用者「RPA」，以便進一步設定自動化規則
* 設定方式：
    * 路徑：設定>使用者及公司>使用者，點擊「新增」按鈕
    * 資料設定：
        * 名稱：RPA
        * 電子郵件地址：service@ewebs.com.tw
        * 銷售：管理者
        * 庫存：管理者
        * 採購：管理者
        * 會計：帳單管理者
        * 系統管理：管理者
### 4.2 新增「ec管理員」
* 說明：新增使用者「ec管理員」
* 設定方式：
    * 路徑：設定>使用者及公司>使用者，點擊「新增」按鈕
    * 資料設定：
        * 名稱：ec管理員
        * 電子郵件地址：ec@ewebs.com.tw
        * 銷售：管理者
        * 庫存：管理者
        * 採購：管理者
        * 會計：帳單管理者
        * 系統管理：管理者
  
## 五、自動化規則
* 路徑：設定>技術>自動化>自動化規則
### 5.1 新增「RPA報價單自動轉銷售訂單」
* 設定如下：
    * 名稱：RPA報價單自動轉銷售訂單
    * 資料集：銷售訂單
    * 觸發器：狀態已設為：報價
    * 更新網域前：
    ```python!
    # (user_id.id測試機是13、正式機是6)
    ["&", ("user_id", "=", 6), ("state", "=", "draft")]
    ```
    * 應採取的行動：加入操作
    * Execute Code(執行程式碼)
    * 程式碼：
    ```python!
    # (user_id.id測試機是13、正式機是6)
    if record.user_id.id == 6 and record.state == 'draft':
        record.action_confirm()
    ```
## 六、功能表項目設定
### 6.1 調整「功能表項目」序列號
* 路徑：設定>技術>使用者介面>功能表項目
* 調整順序：
	* 0：概覽畫面(或稱Dashboard)
	* 1：採購
	* 2：銷售
	* 3：庫存
	* 4：會計
	* 5：製造
	* 6：聯絡人
	* 7：討論

### 6.2.1 概覽畫面
* 概覽畫面/配置/概覽畫面：空白，改為「概覽畫面 / 管理員」
### 6.2.2 討論
* 討論：「使用者類型/內部使用者」，改為「額外的權利/技術特性」
### 6.2.3 應用程式
* 應用程式：空白，改為「技術 / Administrator 特殊權限」
### 6.2.4 採購
* 採購/產品/產品：空白，改為「額外的權利/技術特性」
### 6.2.5 銷售
* 銷售/待開立發票/追加銷售訂單：空白，改為「額外的權利/技術特性」
* 銷售/產品/產品：空白，改為「額外的權利/技術特性」
* 銷售/產品/價格表：「技術 / 基本價格表」，改為「額外的權利/技術特性」
### 6.2.6 設定
* 設定/一般設定：「系統管理 / 設定」，改為「技術 / Administrator 特殊權限」
* 設定/使用者及公司/公司：空白，改為「額外的權利/技術特性」
* 設定/使用者及公司/群組：「技術 / Administrator 特殊權限」
* 設定/技術：「技術 / Administrator 特殊權限」

## 七、一般設定初始化
### 7.1 銷售模組
### 7.1.1 開啟毛利功能
* 路徑：設定>銷售>價目表>勾選「毛利」
### 7.1.2 勾選計量單位功能
* 路徑：設定>銷售>產品目錄>勾選「計量單位」
### 7.1.3 產品品項初始化
* 功能：新增「折讓」、「折扣」和「運費」的產品品項
* 路徑：銷售>產品>產品變體，匯入
* [產品初始設定的匯入模板連結](https://docs.google.com/spreadsheets/d/1ttaN-erDRJUIpLyvIGcxJ34HWFzeq8Milt2nk45LrSQ/edit?gid=525876499#gid=525876499)
### 7.1.4 銷售團隊移除Administrator
* 功能：移除Administrator，避免點擊銷售>訂單>銷售團隊，出現錯誤
* 路徑：銷售>配置>銷售團隊>點擊「銷售」，「成員」頁籤移除「Administrator」


### 7.2 採購模組
### 7.2.1 啟用變體功能
* 功能：啟用變體功能，提供使用者可以由採購>產品>產品變體，匯入資料
* 路徑：設定>採購>產品>勾選「變體」
### 7.2.1-2 產品類型預設為庫存產品
* 功能：產品類型預設為「庫存產品」，不用下拉，節省時間
* 須先開啟開發者
1. 路徑：採購>產品>產品，點擊「新增」按鈕
* 開發者工具選擇「設預設」，預設：選擇「產品類型=庫存產品」，所有使用者，點擊「儲存預設」
2. 路徑：採購>產品>產品變體，點擊「新增」按鈕
* 開發者工具選擇「設預設」，預設：選擇「產品類型=庫存產品」，所有使用者，點擊「儲存預設」

### 7.3 庫存模組
### 7.3.1 取消到貨的簡訊確認功能
* 功能：取消簡訊確認功能
* 路徑：設定>一般設定>庫存>送貨>取消「簡訊確認」勾選
### 7.3.2 啟用到期日功能
* 功能：啟用批次及序號和到期日功能
* 路徑：設定>一般設定>庫存>追溯性>勾選「批次及序號」和「到期日」
### 7.3.3 啟用分倉功能
* 功能：啟用分倉功能
* 路徑：設定>一般設定>庫存>倉庫>勾選「儲存位置」
### 7.3.4 自動建立欠單
* 功能：啟用由系統依據入庫的數量是否滿足採購單，自動建立欠單
* 路徑：庫存>配置>操作類型>點擊「內部調撥」、「收貨」和「交貨單」，「建立欠單」欄位選擇「總是」
### 7.3.4-1 新增倉庫預設自動建立欠單
* 功能：讓之後新增倉庫也適用自動建立欠單
* 須先開啟開發者
* 開發者工具選擇「設預設」，預設：選擇「建立欠單=總是」，所有使用者，點擊「儲存預設」
### 7.3.5 新增「進貨退出」和「銷貨退回」
* 功能：新增「進貨退出」和「銷貨退回」操作類型
* 路徑：庫存>配置>操作類型>點擊「新增」
![image alt](https://i.imgur.com/nhROnca.png)
![image alt](https://i.imgur.com/uqllBCS.png)
### 7.3.5-1 設定「收貨」和「交貨」的退回類型
* 功能：設定「收貨」和「交貨單」的退回類型，讓系統自動產品RIN和ROUT單據
* 路徑：庫存>配置>操作類型>點擊「收貨」和「交貨」!
![image alt](https://i.imgur.com/0I4QN9c.png)
![image alt](https://i.imgur.com/FYaCHRA.png)

### 7.3.5 設定共享倉庫到「最愛」
* 功能：最愛先預設一項「My Company倉」，提供參考
* 路徑：庫存>報告>位置
* 搜尋欄位：名稱設定「My Company倉」
* 條件：
	```python!
	[("warehouse_id", "=", 1)]
	```
### 7.3.7 設定「庫存數量」的匯出模板
* 功能：提供大批匯出以查詢庫存數量
* 路徑：庫存>報告>位置，設定「庫存數量」的匯出模板
* [「庫存數量」的匯出模板連結](https://docs.google.com/spreadsheets/d/1GENIXxh1_dFsMRQkKsg_G9bUWYLmcVd8vrz3ZrK25Mw/edit?usp=drive_link)
### 7.3.8 設定共享「準備交貨」到「最愛」
* 功能：提供給RPA操作時，精準選擇可出貨執行交貨
* 路徑：庫存>製程>調撥>交貨，
* 搜尋欄位：名稱設定「準備交貨」
* 條件：
	```
	["&", ("picking_type_code", "=", "outgoing"),	("state", "=", "assigned")]
	```
### 7.3.9 強制下架策略設定先到期先出
* 功能：設定先到期先出，系統將自動選擇最早到期產品
* 路徑：庫存>配置>產品>產品類別，點擊「All」，強制下架策略選擇「先到期先出（FEFO）」

### 7.5 會計模組
### 7.5.1 稅金改為內含5%
* 功能：「銷項稅」和「進項稅」改為內含5%
* 路徑：設定>一般設定>會計>稅金>預設稅>「銷項稅」和「進項稅」，均設定「5% INC」
### 7.5.2 顯示所有會計功能
* 功能：讓有會計「帳單管理員」功能的使用者可以查看所有會計功能
* 須先開啟開發者
* 路徑：設定>使用者及公司>群組>搜尋「帳單管理員」「繼承」頁面搜尋「顯示所有會計功能」，點擊加入「技術 / 顯示所有會計功能」
### 7.5.3 設定銀行初始化
* 功能：設定銀行名稱
* 路徑：聯絡人>配置>銀行帳戶>銀行
### 7.5.4-1 增加銀行帳戶，預設銀行
* 功能：新增一個銀行帳戶名稱為：銀行，作為EC付款銀行。
* 路徑：會計>配置>銀行>增加銀行帳戶，帳戶號碼設定為「銀行」，其他為空白
![image alt](https://i.imgur.com/8t57NWA.png)
### 7.5.4-2 日記帳本的未結收付款科目
* 路徑：會計>配置>會計>日記帳，日記帳選擇類型為「銀行」，
* 「收款」頁籤 > 「名稱」和「未結收款科目」欄位，選擇「111301銀行」
* 「付款」頁籤 > 「名稱」和「未結付款科目」欄位，選擇「111301銀行」

## 八、初始資料設定
### 8.1 [匯入-商品>初始設定](https://docs.google.com/spreadsheets/d/1ttaN-erDRJUIpLyvIGcxJ34HWFzeq8Milt2nk45LrSQ/edit?usp=drive_link)
### 8.2 [匯入-銀行>初始設定](https://docs.google.com/spreadsheets/d/1O_hWBfkv72YltDApbQd_DVIUZPnq2Ga6sGBSF8_6fGk/edit?usp=drive_link)

## 九、權限設定
### 9.1 RPA和ec負責人權限
* RPA和ec負責人權限設定(模板已先預設)
![image alt](https://i.imgur.com/893srUQ.png)
