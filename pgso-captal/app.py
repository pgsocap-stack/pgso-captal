import streamlit as st
import preview_pow

# 1. I-set ang configuration ng page (Gagawing Wide Screen para malawak ang table)
st.set_page_config(
    page_title="PGSO POW Management System", 
    page_icon="🏛️",
    layout="wide"
)

# 2. Pamagat sa pinakataas ng screen
st.title("🏛️ PGSO POW Management System")
st.subheader("Program of Works (POW) Encoder Console")
st.markdown("---")

# 3. Kusa nitong patatakbuhin at ipapakita ang ginawa nating interface na may Smart Dropdown
preview_pow.render_edit_mode_interface()