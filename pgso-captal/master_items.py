import openpyxl
import os

def load_master_list_from_excel(file_name="master_items.xlsx"):
    """
    Dynamic na binabasa ang Excel file para ibalik ang listahan 
    na may pormat na: [("Pangalan", "Unit", Presyo), ...]
    """
    excel_data = []
    
    # 🔍 Suriin kung umiiral ang file sa folder
    if not os.path.exists(file_name):
        # Fallback list para hindi mag-crash ang app kung sakaling nawawala ang Excel file
        return [
            ("Portland Cement (Type 1)", "bags", 285.00),
            ("Reinforcing Steel Bars 12mm", "pcs", 310.00),
            ("Fine Sand", "cu.m", 1200.00)
        ]

    try:
        # Buksan ang excel gamit ang data_only=True para makuha ang value at hindi ang formula
        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws = wb.active
        
        # Babasahin mula Row 2 para lagpasan ang table header ng Excel mo
        for row in ws.iter_rows(min_row=2, values_only=True):
            name = row[0]   # Column A: Item Name / Description
            unit = row[1]   # Column B: Unit
            price = row[2]  # Column C: Presyo
            
            # Siguraduhing may laman ang pangalan bago isama
            if name and str(name).strip() != "":
                # Siguraduhing decimal/float ang presyo, gawing 0.00 kung walang laman
                try:
                    clean_price = str(price).replace("₱", "").replace("P", "").replace(",", "").strip()
                    actual_price = float(clean_price)
                except (ValueError, TypeError):
                    actual_price = 0.00
                
                actual_unit = str(unit).strip() if unit is not None else "pcs"
                
                # Isasabit sa listahan na may tamang pormat
                excel_data.append((str(name).strip(), actual_unit, actual_price))
                
        return excel_data

    except Exception as e:
        print(f"⚠️ Error sa pagbasa ng Excel: {e}")
        return []

# 🔥 DITO TINATAWAG ANG FUNCTION PARA MAPAKAIN SA PREVIEW_POW.PY MO
ITEM_MASTER_LIST = load_master_list_from_excel("master_items.xlsx")