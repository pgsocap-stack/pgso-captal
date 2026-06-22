# I-convert ang list mula sa Excel para maging mabilisang dictionary finder
    # Gamit ang .strip() sa key para walang sumasabit na espasyo
    master_pool = {str(item[0]).strip(): {"unit": str(item[1]).strip(), "price": float(item[2])} for item in ITEM_MASTER_LIST}

    # ... [panatilihin ang mga naunang code para sa general info at table preview] ...

    # --- THE SMART DROPDOWN FORM ---
    dropdown_options = list(master_pool.keys())
    dropdown_options.insert(0, "✨ Manu-manong Isusulat (Custom Entry) / Pumili sa ibaba...")

    st.markdown("### ➕ Magdagdag ng Bagong Aytem sa POW")

    with st.container(border=True):
        selected_item = st.selectbox(
            "Mag-search o Pumili ng Materyales (Galing sa master_items.xlsx):",
            options=dropdown_options,
            index=0
        )
        
        default_unit = ""
        default_price = 0.00
        chosen_desc = ""
        
        # Gagamit ng .strip() para siguradong magkatugma ang hinahanap sa dictionary
        clean_selected = str(selected_item).strip()
        
        if clean_selected != "✨ Manu-manong Isusulat (Custom Entry) / Pumili sa ibaba...":
            chosen_desc = clean_selected
            if clean_selected in master_pool:
                default_unit = master_pool[clean_selected]["unit"]
                default_price = master_pool[clean_selected]["price"]

        col1, col2, col3 = st.columns([1, 1, 1.5])
        with col1:
            input_qty = st.number_input("QTY (Dami):", min_value=0.0, step=1.0, value=0.0, key="enc_qty")
        with col2:
            # 🎯 DITO PAPASOK ANG UNIT KUSA MULA SA EXCEL
            input_unit = st.text_input("UNIT:", value=default_unit, key="enc_unit")
        with col3:
            # 🎯 DITO PAPASOK ANG PRESYO KUSA MULA SA EXCEL
            input_price = st.number_input("UNIT PRICE (Presyo):", min_value=0.0, step=0.01, value=default_price, key="enc_price")
