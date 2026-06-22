import streamlit as st

def render_edit_mode_interface():
    st.markdown("### ✏️ EDIT MODE - Update POW Record")
    
    # 🔍 HAKBANG 1: IMPORT NG MASTER LIST MULA SA MASTER_ITEMS.PY (Na nagbabasa sa Excel)
    try:
        from master_items import ITEM_MASTER_LIST
    except ImportError:
        st.error("⚠️ Hindi mahanap ang master_items.py sa iyong folder!")
        ITEM_MASTER_LIST = []

    # I-convert ang list mula sa Excel para maging mabilisang dictionary finder
    master_pool = {item[0]: {"unit": item[1], "price": float(item[2])} for item in ITEM_MASTER_LIST}

    # Siguraduhing may panimulang listahan ang session state para sa mga idinagdag na aytem
    if 'edit_items_list' not in st.session_state:
        st.session_state.edit_items_list = []

    # --- UPPER FRAME: DETAILS OF POW ---
    with st.container(border=True):
        st.markdown("**📋 General Information**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Project Title / Name:", value="Sample Project PGSO", key="pow_proj_name")
        with col_b:
            st.text_input("Project Location:", value="Province Area", key="pow_location")

    # --- MIDDLE FRAME: TABLE PREVIEW ---
    st.markdown("**📋 List of Items (Current Session)**")
    display_edit_rows = []
    
    # Kukuha ng data mula sa session state para i-display sa live table
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
        st.info("💡 Blangko pa ang listahan ng mga aytem. Mag