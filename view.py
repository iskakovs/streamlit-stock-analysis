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

    with st.sidebar:
        st.text_input("Ticker:", key="symbol")
        st.date_input("Start date", key="start_date")
        st.date_input("End date", key="end_date")
        apply_button = st.button("Apply")
        st.markdown("---")

        name = st.text_input(label="Manage my recordings", placeholder="Name", key="name")

    st.selectbox("My recordings:", st.session_state.history['name'], key="curr_history",
                 on_change=restore_from_history)


    col1, col2, col3 = st.sidebar.columns(3, gap="small")


    if apply_button or st.session_state.symbol:
        data = stock_data.fetch_stock_data(st.session_state.symbol, st.session_state.start_date,
                                           st.session_state.end_date)
        display_graph(data)
        st.text_area("Comment", key="comment")
        display_data_table(data)

    if st.session_state.curr_history:
        record_id = st.session_state.history[st.session_state.history['name'] == st.session_state.curr_history].iloc[0][
            'id']
        btn_update = col2.button("Update")
        btn_delete = col3.button("Suppr.")
        if btn_update:
            if name == "":
                st.sidebar.error("Please, enter the name")
                logger.error(f'Update button : Empty name')
            else:
                db_sql.update_record_in_db(db_path, record_id, st.session_state.symbol, st.session_state.start_date,
                                           st.session_state.end_date, st.session_state.name, st.session_state.comment)
                st.experimental_rerun()

        if btn_delete:
            db_sql.delete_record_from_db(db_path, record_id)
            st.experimental_rerun()

    if col1.button("Add"):
        if name == "":
            st.sidebar.error("Please, enter the name")
            logger.error(f'Add button : Empty name')
        elif st.session_state.history[st.session_state.history['name'] == name].shape[0]:
            st.sidebar.error("This name already exists in the database")
            logger.error(f'Add button : Name {name} already exist in database')
        else:
            db_sql.save_into_db(db_path, st.session_state.symbol, st.session_state.start_date, st.session_state.end_date,
                                st.session_state.name, st.session_state.comment)
            st.experimental_rerun()

