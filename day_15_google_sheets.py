import streamlit as st
import gspread
from gspread_dataframe import get_as_dataframe
import pathlib


# ------------------------
# authenticate
# ------------------------

my_directory = pathlib.Path.cwd()

creds_path = my_directory / 'gcp-wow-food-wlx-digaspt-dev-2be171e95f5f.json'
gc = gspread.service_account(filename=creds_path)


# ------------------------
# get data
# ------------------------

sh = gc.open("iris")
#sh = gc.open_by_key('1lgdr1iptFlZvaPF2L9XJmHB8lnX9UZoK-jBALDluhR8')


worksheet = sh.worksheet("Sheet2")

df = get_as_dataframe(worksheet, usecols=[0,1,2,3,4])

# get_as_dataframe loads all rows in the spreadsheet whether or not they have data
# remove all blank rows from dataframe
df = df.dropna(how='all')



st.header("Using data from Google Sheets")

google_auth_code = """
import gspread
from gspread_dataframe import get_as_dataframe
import pathlib


my_directory = pathlib.Path.cwd()
creds_path = my_directory / 'credential_file.json'
gc = gspread.service_account(filename=creds_path)

sh = gc.open_by_key('1lgdr1iptFlZvaPF2L9XJmHB8lnX9UZoK-jBALDluhR8')
worksheet = sh.worksheet("Sheet2")

df = get_as_dataframe(worksheet, usecols=[0,1,2,3,4])

# get_as_dataframe loads all rows in the spreadsheet whether or not they have data
# remove all blank rows from dataframe
df = df.dropna(how='all')
"""

st.code(google_auth_code)

my_slider = st.sidebar.slider("pick a number", 0, 10, 5)

st.write(df)
