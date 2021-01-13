import time
from bokeh.plotting import figure
import streamlit as st
import random

x = []
y = []
num = 1000000
start_time = time.time()
for i in range(num):
  x.append(random.randint(0,30))
  y.append(random.randint(0,30))
print(len(x))
end_time = time.time()
print('time for generate lists: ', end_time - start_time)



st.title("Test Omer Elezra")
st.title(num)
start_time = time.time()
p = figure(title='simple line example',x_axis_label='x',y_axis_label='y')

p.line(x, y, legend_label='Trend',line_color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), line_width=2)
mid_time = time.time()
print('time of line: ', mid_time - start_time)
st.write('time of line: ', mid_time - start_time)

st.bokeh_chart(p, use_container_width=True)
end_time = time.time()
print('time of print: ', end_time - mid_time)
st.write('time of print: ', end_time - mid_time)
