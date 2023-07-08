import logging #package is responsible for collecting all the logs (see the file)

import pandas as pd #import pandas
import streamlit as st #import streamlit (used for creating a visual app in your browser)

import db_sql #import 'db_sql' file
import stock_data #import 'stock_data' file

logger = logging.getLogger()

# Define 'config_streamlit' function with parameter 'config'.
# Usine strealit we create a visually appealing file to see in the browser with a sidebar
def config_streamlit(config, db_path):
    """
    config streamlit
    :param config: config file
    :type config: dict
    :param db_path: database path
    :type db_path: string
    :return: None
    """
    st.set_page_config(page_title=config['streamlit_parameters']['page_title'],
                       layout=config['streamlit_parameters']['layout'],
                       initial_sidebar_state=config['streamlit_parameters']['initial_sidebar_state'])
    st.session_state.history = db_sql.fetch_data_from_db(db_path)
