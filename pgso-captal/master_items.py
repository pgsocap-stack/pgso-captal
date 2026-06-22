import openpyxl
import os

def load_master_list_from_excel(file_name="master_items.xlsx"):
    excel_data = []
    
    # 🔍 Suriin kung umiiral ang file
    if not os.path.exists(file_name):
        # Fallback list kung sakaling hindi mahanap ang file sa simula
        return [
            ("Portland Cement (Type 1)", "bags", 285.00),
            ("Reinforcing Steel Bars 12mm", "pcs", 310.00),
            ("Fine Sand", "cu.m", 1200.00)
        ]

    try:
        # Buksan ang Excel (data_only=True para makuha ang kalkuladong halaga at hindi formula)
        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws = wb.active
        
        # Babasahin mula Row 2 (Column A: Name, Column B: Unit, Column C: Price)
        for row in ws.iter_rows(min_row=2, values_only=True):
            name = row[0]   
            unit = row[1]   
            price = row[2]  
            
            if name and str(name).strip() != "":
                try:
                    # Linisin ang mga simbolo tulad ng ₱ o kuwit kung mayroon man
                    clean_price = str(price).replace("₱", "").replace("P", "").replace(",", "").strip()
                    actual_price = float(clean_price)
                except (ValueError, TypeError):
                    actual_price = 0.00
                
                actual_unit = str(unit).strip() if unit is not None else "pcs"
                excel_data.append((str(name).strip(), actual_unit, actual_price))
                
        return excel_data

    except Exception as e:
        print(f"⚠️ Error sa pagbasa ng Excel: {e}")
        return []

# Isinasalpak ang data sa variable na tatawagin ng preview_pow.py
ITEM_MASTER_LIST = load_master_list_from_excel("master_items.xlsx")
