import streamlit as st
import pandas as pd
import sqlite3
import datetime
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

import plotly.express as px


def view_all_data():
	c.execute('SELECT * FROM commentsdatabase')
	data = c.fetchall()
	return data

def main():

	result = view_all_data()
	result_df = pd.DataFrame(result, columns=["Date","Correctness", "Picture filename", "Comments"])
	st.dataframe(result_df)

	count_df = result_df['Correctness'].value_counts().to_frame()
	# st.dataframe(task_df)
	count_df = count_df.reset_index()
	st.dataframe(count_df)

	p1 = px.pie(count_df, names='index', values='Correctness')
	st.plotly_chart(p1, use_container_width=True)

if __name__ == '__main__':
    main()