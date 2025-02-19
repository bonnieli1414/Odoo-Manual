---
title: Odoo17ERP 和盟管理者及RPA操作文件
tags: [odoo]

---

# Odoo17ERP 和盟管理者及RPA操作文件
## 1 庫存模組
### 1.1 新增倉庫到「最愛」
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


### 1.2 批次執行「交貨核實」
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



## 2 銷售模組
### 2.1 批次執行「建立發票」和「過帳分錄」
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


## 3 會計模組

### 3.1 批次「登記付款」
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


## 4. 系統基本介面
### 4.1 設定「最愛」
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