import streamlit
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Idli Vada - 50 Rs')
streamlit.text('🍞 Masala Dosa - 60 Rs')
streamlit.text('🥗 Girmit - 40 Rs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
