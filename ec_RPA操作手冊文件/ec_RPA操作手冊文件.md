---
title: ec_RPA操作手冊文件
tags: [Odoo ERP 導入]

---

# Odoo ERP 導入與RPA自動化作業v17.2(原始)
## 1. 系統功能
### 1.1 設定最愛
* 說明：有兩種設定方式：
    1. 預設篩選器：設定**個人化**常用的篩選條件。
    2. 分享：統一設定篩選條件，提供**其他登入者共用**同一篩選條件。
* 路徑：任一模組的「搜尋」欄位
* 操作步驟：
    1. 「搜尋」欄位，點擊「▼」按鈕。
    2. 點擊「加入自訂準則」，點擊後會出現彈跳視窗。
    3. 設定要篩選的條件，例如：選擇「銷售人員」為「RPA」，可依照需求調整設定。
    4. 點擊「加入」按鈕。
    5. 「搜尋」欄位，點擊「▼」按鈕。
    6. 勾選「預設篩選器」或「分享」。
    7. 點擊「儲存」按鈕。
![image alt](https://i.imgur.com/RTZiVa3.png)
![image alt](https://i.imgur.com/3SaoCVX.png)
![最愛](https://i.imgur.com/1NOdyCb.png)

### 1.2 新增倉庫到最愛
* 路徑：庫存>報告>位置
* 設為最愛的操作步驟：
	1. 在搜尋結果頁面右邊，找到並點擊「▼」按鈕。
	2. 選擇其中「My Company倉」並點擊。
	3. 滑鼠移至「★」，會換為「⚙️」，點擊後會出現彈跳視窗。
	4. 「My Company」，可更換要設定的庫存名稱
	5. 點擊「確認」
	6. 點擊「儲存目前搜尋」
	7. 設定最愛名稱
	8. 勾選「分享」
	9. 點擊「儲存」
![image alt](https://i.imgur.com/NHK1C8c.png)
![image alt](https://i.imgur.com/QZU2wn1.png)
![image alt](https://i.imgur.com/SUBWaEj.png)

## 2. 系統初始化設置
### 2.1 [Odoo 系統開通申請書](https://docs.google.com/spreadsheets/d/19vIevFCzKYWVFx8RVH3VKdkses1U4VRIiIZwAGhVigQ/edit?usp=drive_link)
* 由相關負責人提出申請

## 3. 基本資料建檔
### 3.1 [匯入-銷售團隊](https://docs.google.com/spreadsheets/d/19HaL4ylA4nzpJtPKCFtLpHsqAome_xtUBkOan7FiwgQ/edit?usp=drive_link)
* 資料來源：ec資料
### 3.2 [匯入-倉庫](https://docs.google.com/spreadsheets/d/15Ps4Z7w7vaY8amxFeIZ7UfgwOROg_ZErR6KfVCf73RM/edit?usp=drive_link)
* 資料來源：ec資料
### 3.3 [匯入-客戶](https://docs.google.com/spreadsheets/d/1RMp2w_YYaAzf7aNU3msrdxI_gDMwBgS4AbfV33i0ywc/edit?usp=drive_link)
* 資料來源：ec資料
### 3.4 [匯入-商品](https://docs.google.com/spreadsheets/d/1ttaN-erDRJUIpLyvIGcxJ34HWFzeq8Milt2nk45LrSQ/edit?usp=drive_link)
* 資料來源：ec資料
### 3.5 [匯入-供應商資料蒐集表](https://docs.google.com/spreadsheets/d/1PD7f4vVO0h02vCrFeRo-9qEE6TKP74mG5dBWfZVCIHw/edit?usp=drive_link)
* 資料來源：請客戶填寫「匯入 - 供應商資料蒐集表」中的「填寫表單」工作表。
### 3.6 [匯入-期初庫存開帳盤點表](https://docs.google.com/spreadsheets/d/1dyyxhzWxAkEN6QUwS_ct0WXYgQGome1qdG-aQPaaHCA/edit?usp=drive_link)
* 資料來源：請客戶填寫「匯入-期初庫存開帳盤點表」中的「填寫表單」工作表。
* 匯入時程：與客戶協商並排定資料匯入的時程。



## 4. RPA銷售流程操作說明
* Odoo 銷售流程作業，說明從銷售訂單資料匯入後，關於建立發票、交付產品、到付款的批次操作步驟。
### 4.1 [銷售訂單資料匯入範本](https://docs.google.com/spreadsheets/d/1YLBqYdamy1934N9Hg7dgEQW74LljCIbKTk_yFldJ5Wk/edit?gid=793998794#gid=793998794)
### 4.2 批次執行「建立發票」和「過帳分錄」
* 路徑：銷售>待開立發票>待開立發票訂單
* 操作步驟：
    1. 「待開立發票訂單」列表，請確認「發票狀態」為「待開立發票」
    2.         
        • 未超過一頁筆數：勾選「編號」欄位左邊的☑️，即可整批選擇。
        • 超過一頁的筆數：勾選「編號」欄位左邊的☑️，例如:400筆，會顯示：「→全選400」按鈕，點擊「→全選400」按鈕後，則是選擇全部，按鈕會顯示「所有400已選取」。
    3. 點擊「建立發票」，會出現「建立發票」的彈跳視窗
    4. 點擊☑️，將「合併帳單」的checkbox修改為「☐」
    5. 點擊「建立草稿發票」按鈕
    6. 畫面會跳轉為「應收憑單」列表，請確認「狀態」為「草稿」階段
    7. 
        • 未超過一頁筆數：勾選「號碼」欄位左邊的☑️，即可整批選擇。
        • 超過一頁的筆數：勾選「編號」欄位左邊的☑️，例如:400筆，會顯示：「→全選400」按鈕，點擊後，則是選擇全部，按鈕會顯示「所有400已選取」。
    8. 點擊「動作⚙️」
    9. 點擊「過帳分錄」按鈕
    10. 點擊☐，將「強制」的checkbox修改為「☑️」
    11. 點擊「過帳日記帳記項」按鈕
    12. 「應收憑單」列表，即可查看「狀態」為「已過帳」
<details>
  <summary>未超過一頁筆數</summary>
    
![image alt](https://i.imgur.com/8rTXEJg.png)
</details>

<details>
  <summary>超過一頁的筆數</summary>

![image alt](https://i.imgur.com/gdDmPqR.png)
</details>

![image alt](https://i.imgur.com/uD3eN0D.png)
![image alt](https://i.imgur.com/wtMEf7L.png)
<details>
  <summary>未超過一頁筆數</summary>
    
  ![image alt](https://i.imgur.com/JMrPWx5.png)
</details>

<details>
  <summary>超過一頁的筆數</summary>

  ![image alt](https://i.imgur.com/jHDeP56.png)
  ![image alt](https://i.imgur.com/5BAStxf.png)
  ![image alt](https://i.imgur.com/mVYX87i.png)
</details>

![image alt](https://i.imgur.com/0Ql3iGX.png)
![image alt](https://i.imgur.com/6RULUaI.png)
![image alt](https://i.imgur.com/aPnKODK.png)

### 4.3 批次執行「交貨核實」
* 路徑：庫存>製程>調撥>交貨
* 操作步驟：
	1. 在搜尋結果頁面右邊，找到並點擊「▼」按鈕。
	2. 「最愛」選擇「準備交貨」並點擊。
	3. 
        • 未超過一頁筆數：勾選「編號」欄位左邊的☑️，即可整批選擇。
        • 超過一頁的筆數：勾選「編號」欄位左邊的☑️，例如:400筆，會顯示：「→全選400」按鈕，點擊「→全選400」按鈕後，則是選擇全部，按鈕會顯示「所有400已選取」。
	5. 點擊「動作⚙️」
	6. 點擊「核實」
![image alt](https://i.imgur.com/XhtA6U7.png)
<details>
  <summary>未超過一頁筆數</summary>

  ![image alt](https://i.imgur.com/gtMNhqI.png)
</details>

<details>
  <summary>超過一頁的筆數</summary>

  ![image alt](https://i.imgur.com/DIgGo3Z.png)
  ![image alt](https://i.imgur.com/QQ0D07W.png)
</details>

![image alt](https://i.imgur.com/nZ9Fqaa.png)


### 4.4 批次「登記付款」
* 路徑：會計>儀表板
* 操作步驟：
    1. 「客戶發票」區塊，點擊「未付款應收憑單」
    2.  • 未超過一頁筆數：勾選「號碼」欄位左邊的☑️，即可整批選擇。
        • 超過一頁的筆數：勾選「編號」欄位左邊的☑️，例如:400筆，會顯示：「→全選400」按鈕，點擊後，則是選擇全部，按鈕會顯示「所有400已選取」。
    3. 點擊「登記付款」，會出現「登記付款」的彈跳視窗
    4. 日記帳選擇「銀行」或「現金」
    5. 付款日期依需求選擇
    6. 點擊「建立付款」按鈕
![image alt](https://i.imgur.com/yuZoVyv.png)
<details>
  <summary>未超過一頁筆數</summary>
    
  ![image alt](https://i.imgur.com/8FsuMLN.png)
</details>

<details>
  <summary>超過一頁的筆數</summary>

  ![image alt](https://i.imgur.com/DafUaA6.png)
  ![image alt](https://i.imgur.com/TgYAPPm.png)
</details>

![image alt](https://i.imgur.com/ixFMlBD.png)
![image alt](https://i.imgur.com/991OEiV.png)


## 5. 人工銷售流程操作說明
• Odoo 銷售流程作業，說明從建立銷售訂單、建立發票到交付產品的操作步驟。
### 5.1 建立銷售訂單
1. 登入後，主選單中點擊「銷售」模組。
2. 點擊「訂單」 > 「報價單」。
3. 點擊「新增」按鈕。
4. 填寫銷售訂單資料：
	• 客戶(必填欄位)：下拉選擇客戶。
    • 報價日期：相當於ec的訂單日期。
    • 付款條件：選擇「立即付款」。
	• 產品：在訂單明細中，點擊「添加產品」，輸入銷售的商品，指定數量、單價和稅金。
    • 條款和條件：填寫備註
5. 確認銷售訂單：
	• 確認訂單內容無誤後，點擊「確認訂單」。
	• 訂單會進入「銷售訂單」狀態，系統會自動建立對應的交貨單，智慧面板將產生一筆「交貨」。
![image alt](https://i.imgur.com/3JEfhBZ.png)
![image alt](https://i.imgur.com/57MizS0.png)
![image alt](https://i.imgur.com/tCQm7Nm.png)
![image alt](https://i.imgur.com/vLzw94V.png)

### 5.2 建立發票
1. 在交付產品後，點擊 「建立發票」
2. 彈跳視窗，點擊 「建立草稿發票」，將會產生「應收憑單」草稿。
3. 檢查帳單是否正確，點擊 「確認」按鈕。
![image alt](https://i.imgur.com/XdQYk0d.png)
![image alt](https://i.imgur.com/sPGWNEu.png)
![image alt](https://i.imgur.com/vniSWHb.png)

### 5.3 交貨
• 在 Odoo 中，交貨核實時，如果產品設定了「無批次/序號」或「有批次/序號」，處理方式略有不同。以下是兩種情況的處理步驟：
#### 5.3.1 「無批次/序號」產品的交貨核實
1. 進入庫存模組：
	• 在主選單中點選「庫存」模組。
![image alt](https://i.imgur.com/NjdvTcT.png)
2. 選擇待處理的交貨單：
	• 在庫存模組中，點選「概覽」，依照實際出庫的倉庫，點擊「待處理」按鈕。
![image alt](https://i.imgur.com/4URTEp2.png)
	• 可依 **「聯絡人」** 或 **「來源單據」的銷售單號** ，點擊出貨單。
![image alt](https://i.imgur.com/VCfoClt.png)
3. 核實出庫的產品數量：
	• 交貨單頁面中，會看到「需求」和「數量」欄位，「需求」為銷售訂單的數量，「數量」為實際要核收的數量，「數量」欄位中會自動帶入與「需求」相同數量，可修改為實際出貨數量。
    • 如果產品全部出貨，則可直接按左上角的「核實」。
![image alt](https://i.imgur.com/oIlF9LK.png)
    • 如果是部分出貨，可以輸入部分數量再按左上角的「核實」，系統會針對剩餘的數量自動再產生一筆交貨單。
![image alt](https://i.imgur.com/P2vC14W.png)
    • 選擇部分出貨，下次收貨可點擊「概覽」，依照實際出庫的倉庫，點擊「待處理」按鈕，挑選「來源單據」的銷售單號進行交貨。
![image alt](https://i.imgur.com/e1BS6uv.png)

#### 5.3.2 「有批次/序號」產品的交貨核實
如果產品啟用了批次或序號，Odoo 會要求在交貨時為每件產品分配對應的批次號或序號。以下是具體步驟：

1. 進入庫存模組：
	• 在主選單中點選「庫存」模組。
![image alt](https://i.imgur.com/J5Y8F10.png)

2. 選擇待處理的交貨單：
	• 在庫存模組中，點選「概覽」，依照實際出庫的倉庫，點擊「待處理」按鈕。
![image alt](https://i.imgur.com/XC05XK3.png)
	• 可依 **「聯絡人」** 或 **「來源單據」的銷售單號** ，點擊交貨單。
![image alt](https://i.imgur.com/KTHkC6f.png)

3. 核實出庫的產品數量：
	• 交貨單頁面中，會看到「需求」和「數量」欄位，「需求」為銷售訂單的數量，「數量」為實際要核收的數量，在「數量」欄位中會自動帶入與「需求」相同數量，可修改為實際出貨數量。
![image alt](https://i.imgur.com/G1uWwKl.png)

4. 輸入批次號碼或序號：
	• 對於「有批次/序號」的產品，須點擊「詳細資料」欄位的圖標，開啟批次輸入頁面。
![image alt](https://i.imgur.com/CXMAUQs.png)

5. 完成批次/序號分配：
    • 輸入每批次的數量和對應的批次號碼。
	• 填寫完批次或序號後，點選「儲存」返回交貨單頁面。
	• 確保所有產品都已經正確分配了批次或序號。
![image alt](https://i.imgur.com/8ALGLQc.png)
    • 如果是部分交貨，設定完批次/序號，系統會自動修改「數量」欄位的數字，於左上角點擊「核實」，系統會針對剩餘的數量自動再產生一筆交貨單。
![image alt](https://i.imgur.com/oAJn89G.png)
![image alt](https://i.imgur.com/7OSzAxL.png)
    • 選擇部分交貨，下次收貨可點擊「概覽」，依照實際出庫的倉庫，點擊「待處理」按鈕，挑選「來源單據」的銷售單號進行交貨。
![image alt](https://i.imgur.com/VUPJj01.png)

### 5.4 帳單收款
1. 點擊「會計」模組。
2. 「儀表板」中，於「客戶發票」>點擊「未付款應收憑單」。系統將顯示所有未收款的應收憑單。
![image alt](https://i.imgur.com/BIwXusS.png)
3. 點擊需要收款的「應收憑單」，進入「登記付款」表單頁面。
![image alt](https://i.imgur.com/lk2Q84e.png)
4. 點擊左上角的「登記付款」按鈕。
![image alt](https://i.imgur.com/VbkqYYD.png)
5. 在「付款」表單中，填寫以下付款資訊：
* 日記賬：選擇將使用的收款方式，如「銀行」或「現金」日記帳。
* 付款日期：系統會自動設置為當前日期，請根據實際情況修改此日期。
* 備忘錄：輸入發票編號等相關資訊作為記錄。
6. 核對無誤後，點擊「建立付款」按鈕。系統將自動生成收款記錄，並更新客戶的收款狀態，同時記錄至選擇的日記帳中。
![image alt](https://i.imgur.com/l8rzmZ0.png)