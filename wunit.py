"""
This is an algorithmic unit conversion tool for the World Unit of Account (WUN).
"""

import streamlit as st
import pandas as pd
import numpy as np


cols = st.beta_columns([1, 3, 1])

cols[1].title("World Unit of Account")


st.write("""
    ## NOT Currency, NOT Money, ONE Unit of Account for All
    """)

# About
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Algorithmic Unit of Account:** Unlike all conventional units of account, WUA uses an algorithm to derive its conversions into currencies.
* **Data source:** [Uniswap](https://uniswap.org) and [Chainlink] (https://chain.link). More sources are being considered.
* We are excited to see online native currencies build an open source distributed financial realm. We have developed an algorithmic unit of account that best represents the current state of trust in world currencies taking into account current population and life expectancy metrics.
""")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("url_goes_here")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)

list_of_coins =('WUN', 'BTC', 'ETH')
# list_of_coins = ("World Unit of Account (WUN)", "Bitcoin (BTC)", "Ethereum (ETH)")
# list_of_coins = ("World Unit of Account (WUN)", "United States dollar (USD)", "Euro (EUR)", "Japanese yen JPY", "Pound sterling (GBP)", "Australian dollar (AUD)", "Canadian dollar (CAD)", "Swiss franc (CHF)", "Renminbi (CNY)", "Hong Kong dollar (HKD)", "New Zealand dollar (ZND)", "Swedish krona (SEK)", "South Korean won (KRW)", "Singapore dollar (SGD)", "Norwegian krone (KOK)", "Mexican peso (MXN)", "Indian rupee (INR)", "Russian ruble (RUB)", "South African rand (ZAR)", "Turkish lira (TRY)", "Brazilian real (BRL)", "New Taiwan dollar (TWD)", "Danish krone (DKK)", "Polish złoty (PLN)", "Thai baht (THB)",  "Bitcoin (BTC)", "Indonesian rupiah (IDR)", "Hungarian forint (HUF)", "Czech koruna (CZK)", "Israeli new shekel (ILS)", "Chilean peso (CLP)", "Philippine peso (PHP)", "Ethereum (ETH)", "UAE dirham (AED)", "Colombian peso (COP)", "Saudi riyal (SAR)", "Malaysian ringgit (MYR)", "Romanian leu (RON)", "XRP (XRP)", "Chainlink (LINK)", "Bitcoin Cash (BCH)")

cols1 = st.beta_columns(2)
amount = cols1[0].number_input('', 0.00000000, 99999999999.99999999)
coin_name = cols1[1].selectbox('', list_of_coins)

# Numbers Collected On 2020-11-12
# Total Population Data was collected from worldbank.org (year 2019)
# Average Life Expectancy was collected from ourworldindata.org
current_number_of_bitcoins = 18538368
current_value_of_ethereum_in_BTC = 3310546
current_world_population = 7673533972
average_life_expectancy_in_years = 72.6

WUNBTC =(current_number_of_bitcoins + current_value_of_ethereum_in_BTC)/(current_world_population * average_life_expectancy_in_years)

st.text("")
st.text("")
st.text("")

if coin_name == 'WUN':
    cols2 = st.beta_columns(3)
    WUNWUN = 1
    WUNETH = WUNBTC * 34.3
    cols2[0].write(f'{amount:16,.2f} WUN')
    cols2[1].write(f'{WUNBTC * amount:16,.8f} BTC')
    cols2[2].write(f'{WUNETH * amount:16,.8f} ETH')
elif coin_name == 'BTC':
    cols2 = st.beta_columns(3)
    BTCWUN = 1/WUNBTC
    BTCETH = 34.3
    cols2[0].write(f'{BTCWUN * amount:16,.2f} WUN')
    cols2[1].write(f'{amount:16,.8f} BTC')
    cols2[2].write(f'{BTCETH * amount:16,.8f} ETH')
else:
    cols2 = st.beta_columns(3)
    ETHWUN = 1/(34.3 * WUNBTC)
    ETHBTC = 1/34.3
    cols2[0].write(f'{ETHWUN * amount:16,.2f} WUN')
    cols2[1].write(f'{ETHBTC * amount:16,.8f} BTC')
    cols2[2].write(f'{amount:16,.8f} ETH')