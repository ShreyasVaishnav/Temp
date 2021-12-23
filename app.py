import streamlit as st
import pandas as pd

st.header("Hello World!")

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000

# functions that run and return output
