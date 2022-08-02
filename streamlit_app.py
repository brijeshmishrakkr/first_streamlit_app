import streamlit
streamlit.title('My Parents New Super Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥗 🐔 🥑🍞')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('Rocket Smoothie')
streamlit.text('Hard boiled Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", # I am getting error in these 2 lines, trying copy paste 
list(my_fruit_list.index))

           
