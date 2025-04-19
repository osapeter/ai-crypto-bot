import streamlit as st
from utils.trading_logic import get_price, trade_with_strategy

st.title('🚀 AI Crypto Bot')
price = get_price('BTCUSDT')
st.write(f'Live BTCUSDT Price: ${price}')

if st.button('Run Trade Strategy'):
    st.write('Executing strategy...')
    trade_with_strategy(symbol='BTCUSDT', buy_amount=10, sl=0.98, tp=1.05)
