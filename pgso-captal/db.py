import streamlit as st
import mysql.connector

def get_connection():
    """
    Ligtas na koneksyon sa MySQL Database gamit ang Streamlit Secrets.
    Kapag local, babasahin nito ang secrets file mo.
    """
    try:
        return mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"],
            port=int(st.secrets["mysql"].get("port", 3306))
        )
    except Exception as e:
        st.error(f"❌ Error sa pag-konekta sa Database: {e}")
        return None
        