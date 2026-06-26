import streamlit as st
from src.agent import waterintake
from src.database import log_intake,get_intake
import pandas as pd
from datetime import datetime

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started=False

if not st.session_state.tracker_started:
    st.title("Water Intake Tracker")
    st.markdown("""
track your daily water intake and receive personalized hydration analysis.""")
    
    if st.button("start tracking"):
        st.session_state.tracker_started=True
        st.experimental_rerun()

else:
    st.title("💧 water tracker dashboard")
    st.sidebar.header("log your water intake")
    user_id=st.sidebar.text_input("USER ID",value="user_12")
    intake_ml=st.sidebar.number_input("water intake (ml)",min_valuse=0,step=100)

    if st.sidebar.button("submit"):
        log_intake(user_id,intake_ml)
        st.success(f"logged {intake_ml} ml for {user_id}")

        agent=waterintake()
        feedback=agent.analyse_intake(intake_ml)
        st.info(f"Ai feedback:{feedback}")

        st.markdown("---")
        st.header("your water intake history")

        if user_id:
            history=get_intake(user_id)
            if history:
                dates=[datetime.strptime(record[0],"%Y-%m-%d").date() for record in history]
                values=[row[0] for row in history]

                df=pd.DataFrame({"date":dates,"intake_ml":values})

                st.dataframe(df)
                st.line_chart(df,x="date",y="intake_ml")
            else:
                st.warning(" No history found for this user.")
