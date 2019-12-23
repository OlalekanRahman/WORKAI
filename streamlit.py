import time,streamlit as st,pandas as pd,numpy as np,matplotlib.pyplot as p
st.title('Equation plotter App')
Degree=st.sidebar.selectbox('Select degree of equation',(1,2,3,4))
values=[x for x in range(-6,6)]
if Degree==1:
    st.write('Input values of coefficient')                        
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter constant')
    eq=[a*x+b for x in values]
elif Degree==2:
    st.write('Input values of coefficient')
    a=st.number_input('Enter x squared coefficient')
    b=st.number_input('Enter x coefficient')
    c=st.number_input('Enter constant')
    eq=[a*x**2-b*x+c for x in values]
elif Degree==3:
    st.write('Input values of coefficient')
    a=st.number_input('Enter x cube coefficient')
    b=st.number_input('Enter x squared coefficient')
    c=st.number_input('Enter x coefficient')                       
    d=st.number_input('Enter a constant')
    eq=[a*x**3+b*x**2+c*x+d for x in values]
else:
    st.write('Input values of coefficient')
    a=st.number_input('Enter x quartic coefficient')
    b=st.number_input('Enter x cube coefficient')
    c=st.number_input('Enter x squared coefficient')
    d=st.number_input('Enter x coefficient')
    e=st.number_input('Enter a constant')
    eq=[a*x**4+b*x**3+c*x**2+d*x+e for x in values]                       
df=pd.DataFrame({'x':values,'y':eq})
if st.checkbox("Show/Hide values' ranges"):
    st.write(df,width=100, height=50)
p.plot(df['x'],df['y'])
p.axhline(0)
p.axvline(0)
p.xlabel('values[x]')
p.ylabel('solutions[y]')
st.pyplot()