import openpyxl
import os

def load_master_list_from_excel(file_name="master_items.xlsx"):
    excel_data = []
    
    if not os.path.exists(file_name):
        return [
            ("Portland Cement (Type 1)", "bags", 285.00),
            ("Reinforcing Steel Bars 12mm", "pcs", 310.00),
            ("Fine Sand", "cu.m", 1200.00)
        ]

    try:
        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws = wb.active
        
        # Babasahin mula Row 2 pababa
        for row in ws.iter_rows(min_row=2, values_only=True):
            # ⚠️ Paki-check ang pwesto ng columns mo sa Excel, boss!
            name = row[0]   # Column A
            unit = row[1]   # Column B
            price = row[2]  # Column C
            
            if name and str(name).strip() != "":
                # Siguraduhing malinis ang pagkaka-parse ng presyo
                try:
                    clean_price = str(price).replace("₱", "").replace("P", "").replace(",", "").strip()
                    actual_price = float(clean_price)
                except (ValueError, TypeError):
                    actual_price = 0.00
                
                actual_unit = str(unit).strip() if unit is not None else "pcs"
                
                # Inilalagay sa listahan: (Pangalan, Unit, Presyo)
                excel_data.append((str(name).strip(), actual_unit, actual_price))
                
        return excel_data

    except Exception as e:
        print(f"⚠️ Error sa pagbasa ng Excel: {e}")
        return []

ITEM_MASTER_LIST = load_master_list_from_excel("master_items.xlsx")
