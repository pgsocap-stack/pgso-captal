import streamlit as st

def render_edit_mode_interface():
    st.markdown("### ✏️ EDIT MODE - Update POW Record")
    
    try:
        from master_items import ITEM_MASTER_LIST
    except ImportError:
        st.error("⚠️ Hindi mahanap ang master_items.py sa iyong folder!")
        ITEM_MASTER_LIST = []

    master_pool = {item[0]: {"unit": item[1], "price": float(item[2])} for item in ITEM_MASTER_LIST}

    if 'edit_items_list' not in st.session_state:
        st.session_state.edit_items_list = []

    with st.container(border=True):
        st.markdown("**📋 General Information**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Project Title / Name:", value="Sample Project PGSO", key="pow_proj_name")
        with col_b:
            st.text_input("Project Location:", value="Province Area", key="pow_location")

    st.markdown("**📋 List of Items (Current Session)**")
    display_edit_rows = []
    
    for idx, row in enumerate(st.session_state.edit_items_list):
        qty = row[0]
        unit = row[1]
        desc = row[2]
        price = row[3]
        amount = qty * price
        
        display_edit_rows.append({
            "Line": idx + 1,
            "QTY": qty,
            "UNIT": unit,
            "ITEM DESCRIPTION": desc,
            "UNIT PRICE": f"₱{price:,.2f}",
            "AMOUNT": f"₱{amount:,.2f}"
        })
    
    if display_edit_rows:
        st.dataframe(display_edit_rows, use_container_width=True, hide_index=True)
    else:
        st.info("💡 Blangko pa ang listahan ng mga aytem. Mag-search at pumili sa form sa ibaba para magdagdag.")

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
        
        if selected_item != "✨ Manu-manong Isusulat (Custom Entry) / Pumili sa ibaba...":
            chosen_desc = selected_item
            default_unit = master_pool[selected_item]["unit"]
            default_price = master_pool[selected_item]["price"]

        col1, col2, col3 = st.columns([1, 1, 1.5])
        with col1:
            input_qty = st.number_input("QTY (Dami):", min_value=0.0, step=1.0, value=0.0, key="enc_qty")
        with col2:
            input_unit = st.text_input("UNIT:", value=default_unit, key="enc_unit")
        with col3:
            input_price = st.number_input("UNIT PRICE (Presyo):", min_value=0.0, step=0.01, value=default_price, key="enc_price")

        if selected_item == "✨ Manu-manong Isusulat (Custom Entry) / Pumili sa ibaba...":
            final_description = st.text_input("Isulat ang Pangalan ng Custom Material dito, boss:", key="enc_custom_desc")
        else:
            final_description = chosen_desc

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Isama sa Listahan ng Materyales", use_container_width=True, type="primary"):
            if not final_description.strip():
                st.error("⚠️ Error: Hindi pwedeng iwanang blangko ang Description ng materyales!")
            elif input_qty <= 0:
                st.warning("⚠️ Paalala: Siguraduhing ang QTY ay higit sa 0 para ma-compute ang amount.")
            else:
                st.session_state.edit_items_list.append([
                    float(input_qty), 
                    input_unit.strip(), 
                    final_description.strip(), 
                    float(input_price), 
                    final_description.strip()
                ])
                st.toast(f"🎉 Naidagdag na: {final_description.strip()}", icon="✅")
                st.rerun()
