import pandas as pd
import yfinance as yf
import json
import streamlit as st
from numerize import numerize


@st.cache
def data_csv(filename):
    data = pd.read_csv(filename)
    data1 = data.Symbol
    symbol_list = data1.tolist()
    return symbol_list


def main():
    datas = data_csv("nasdaq_screener_1640095939797.csv")

    options = st.selectbox("Select the Symbol", datas)

    fb = yf.Ticker(options)

    name = fb.info['shortName']
    revenue = numerize.numerize(fb.info['totalRevenue'])
    revenue_increase = fb.info['revenueGrowth']
    summary = fb.info['longBusinessSummary']
    total_cash = numerize.numerize(fb.info['totalCash'])
    totalCashPerShare = numerize.numerize(fb.info['totalCashPerShare'])
    revenue_percent = f"{revenue_increase} %"
    currency = fb.info['financialCurrency']
    image = fb.info['logo_url']
    st.header("Revenue")
    st.image(image)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(name, f"${revenue}", revenue_percent)
        # st.write(fb.info)
    with col2:
        st.write("Total Cash : ", '$', total_cash)
        st.write("Total Cash Per Share : ", '$', totalCashPerShare)
        st.write("Financial Currency : ",currency)
    
    with st.expander("Description"):
        st.write(summary)


hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        border-top:5px
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
