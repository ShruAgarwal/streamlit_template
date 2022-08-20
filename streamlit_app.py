# Imports required ---
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data

st.title('Welcome to the Streamlit Tour! 🎈')
with st.expander("About this App"):
     st.write("""
         This app will introduce you to the Streamlit Library which
         helps to build and deploy data driven web apps with ease using Python. 😉
     """)


st.markdown("Before diving into the code section, you need to **install Streamlit** in your Repl.")
with st.expander("Follow these steps below 👇"):
    st.write("""1. Create a new repl with Python.
              \n2. Go to **Shell** section and type --- `$ pip install streamlit`. It will take few minutes to install.
              \n3. Then check if streamlit is installed by typing --- `$ streamlit --version`.
              \n4. Add a new file in your repl and name it `requirements.txt`. Now, inside this file, add `streamlit==[write version here!]`
              \n5. You can now write code inside `main.py` file and save it.
              \n6. Lastly, go to **Shell** again, and type --- `$ streamlit run main.py`. Your code will be visible in a *Firefox Bowser!* 🎉
              """)

#################################################################################################
# Sidebar section ---
with st.sidebar:
    st.header("Streamlit Elements Corner ✨")
    select = st.selectbox("Explore any element 👀", ["", "Data and Chart displays","Text Elements", "Input data", "Media 📷", "Layouts & Containers"])
    
    if st.button('Streamlit Challenge 🏁'):
        st.info('Check out 👉 [#30DaysofStreamlit](https://share.streamlit.io/streamlit/30days?challenge=Day+1)')
        st.markdown("""**CHALLENGE TRANSLATIONS**
                    \n1. [French](https://30days-in-french.streamlitapp.com/) by [Charly Wargnier](https://twitter.com/DataChaz)
                    \n2. [Portuguese](https://share.streamlit.io/franciscoed/30days) by [franciscoed](https://github.com/franciscoed)""")
    else:
        st.write('If you\'re interested to learn more, then you should definitely try the above *Challenge!* 👆')


################################################################################################
# Data and Charts elements section --->
if select == 'Data and Chart displays':
    st.header('st.dataframe')
    st.write('Dataframes as an interactive table')
    # generates random numeric values!
    df = pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20))
    ) 
    st.dataframe(df) 
    
    # displays stats with ease
    st.header('st.metric')
    st.write('`st.metric` looks especially nice in combination with `st.columns`')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")


    st.header('st.json : The object to print as JSON')
    st.json({
     'foo': 'bar',
     'baz': 'boz',
     'fruits': [
         'apple',
         'watermelon',
         'peach',
     ],
     })

    st.header('Displaying Some Charts 📊')
    st.subheader('st.altair_chart')
    st.write('A choropleth map of unemployment rate per county in the US')
    
    # example taken from altair docs gallery page
    counties = alt.topo_feature(data.us_10m.url, 'counties')  
    source = data.unemployment.url
    
    ch = alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q'
        ).transform_lookup(
            lookup='id',
            from_=alt.LookupData(source, 'id', ['rate'])
        ).project(
            type='albersUsa'
        ).properties(
            width=500,
            height=300
        )
    st.altair_chart(ch, use_container_width=True)
    st.caption('📍 Note : You need to install `altair` library to plot the above map!')

    st.subheader('st.bar_chart')
    chart_data_2 = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])
    st.bar_chart(chart_data_2)
    st.caption('Above is a Bar Chart')

    st.write("""🌟 There are many more library options you can use for data visualization, such as -- 
                 \n - matplotlib
                 \n - Bokeh
                 \n - Vega-Lite
                 \n - Plotly, etc.. for displaying charts!
                 """)

################################################################################################
# Text display section --->
elif select == 'Text Elements':
    st.header('Snippets of Different Types of Texts')
    choice = st.selectbox("Select any type of Text 👇", ["Simple", "Markdown", "Subheader", "Code", "LaTex", "Caption"])
    
    if choice == 'Simple':
        st.write('st.write --> This is an example of simple text')
    elif choice == 'Markdown':
        st.markdown("st.markdown --> *example* of **markdown text**")
    elif choice == 'Subheader':
        st.subheader('st.subheader --> for writing subheadings!')
    elif choice == 'Code':
        st.write('st.code example 👇')
        st.code("console.log('Hello World');")
    elif choice == 'LaTex':
        st.write('st.latex --> You can also write Math equations here! 🤓')
        st.latex("(a + b)^2 = a^2 + 2ab + b^2")
    elif choice == 'Caption':
        st.write('st.caption -->')
        st.caption('This is a caption!')
    else:
        st.write('')

################################################################################################
# Input data display section --->
elif select == 'Input data':
    st.header('Lots of awesome widgets! 🤯')

    # Part of Streamlit's "Layouts and Containers" Section
    col1, col2, col3 = st.columns([5, 5, 5], gap="small") 
    with col1:
        st.write('📌This section covers **button** & **radio buttons** widgets')
        st.subheader('st.button')
        if st.button('Click me!✨'):
            st.balloons()
        else:
            st.write('')
    
    with col2:
        st.write('📌This section covers **selectbox** & **checkbox widgets**')
        st.subheader('st.selectbox')
        fruit = st.selectbox(
            'Which fruit do you like the most?',
            ('Apple 🍎', 'Peach 🍑', 'Banana 🍌', 'Watermelon 🍉', 'Grapes 🍇'))
        st.write('Your favorite fruit is', fruit)
        

    with col3:
        st.write('📌This section covers **slider** & **text input** widgets')
        st.subheader('st.slider')
        age = st.slider('Check your age 👇', 1900, 2022)
        calc = 2022 - age
        st.write('You are', calc, 'years old!')


    col4, col5, col6 = st.columns([5, 5, 5])
    with col4:
        st.subheader('st.radio')
        food = st.radio(
            "What's your favorite cuisine?",
            ('Indian', 'Chinese', 'Italian'))
        if food == 'Indian':
            st.write('You like to taste dishes made with different spices! 🌶')
        else:
            st.write('Your most common picks are either noodles 🍜/ 🍕')
        

    with col5:
        st.subheader('st.checkbox')
        st.write('Streamlit is easy to learn and apply!😎')
        agree = st.checkbox('I agree')
        disagree = st.checkbox("I don't think so! 😅")
        if agree:
            st.write('Great!')
        
        if disagree:
            st.write('No problem! Just start with some basics and then decide! 😏')
        
        
    with col6:
        st.subheader('st.text_input')
        greet = st.text_input('Your name here')
        st.write('👋 Hey!', greet, 'Glad to see you here.')
        
    
    st.markdown('🌟 You can try out with more widgets [here](https://docs.streamlit.io/library/api-reference/widgets)')

################################################################################################
# Media display section --->
elif select == 'Media 📷':
    st.header('You can embed Images, Videos & Audio files all at one place! 😉')
    st.subheader('st.image')

    c1, c2 = st.columns(2)
    with c1:
        st.image('https://blog.streamlit.io/content/images/size/w2000/2022/03/snowflake_streamlit-1.gif', width=300)
        st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg', width=300)
    with c2:
        st.image('https://im.indiatimes.in/media/content/itimes/blog/2014/Jul/9/1404917161_mickey+mouse.jpg', width=200)
        st.image('https://images6.fanpop.com/image/polls/1578000/1578435_1470083461280_full.jpg' ,width=250)
    st.caption('You can add images filepath using both online links (like above 👆) & from your hard disk!')

    st.subheader('st.video')
    st.video('https://www.youtube.com/watch?v=fVsONlc3OUY')

    st.subheader('st.audio')
    audio_file = open('demo.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.write("""Audio Info :
             \n- *Genre* -- Holidays & Christmas, Worship
             \n- *Mood* -- Relaxed, Patient, Respectful, Subdued.
             \n- *Instruments* -- Acoustic Guitar, Flute
             \n- *Downloaded from* -- https://www.videvo.net/royalty-free-music/sort/popular/instrument/flute/""")


################################################################################################
# Layouts & Containers section --->
elif select == 'Layouts & Containers' : 
    st.header('Take control of elements to be laid out on the screen!')

    st.write('👈 **Sidebar is already present in the left side coded using -- `st.sidebar`**')
    st.write('**Columns have been used in Input Data section of the template, coded with -- `st.columns`**')

    st.subheader('st.tabs')
    st.write('*One of the newly launched cool feature for inserting multiple elements into containers as TABS!*')

    tab1, tab2 = st.tabs(["Voila!", "Funny"])
    
    with tab1:
        st.header("WOW!!")
        st.image("https://i.gifer.com/DJR3.gif", width=400)

    with tab2:
        st.header("Funny! 😆")
        st.image("https://res.cloudinary.com/dougsillars/image/upload/v1546606222/shaq_mtl6do.gif", width=200)

    st.write('You are free to add as many tabs you wish!')

    st.subheader('st.expander')
    with st.expander("CLICK ME to expand!"):
     st.write('This is an example of **Expander, that you can use to hold multiple elements for expanding it or to collapse it!**')

    st.subheader('And that\'s a wrap!🎉 Hope you learnt a lot from this tour and had fun as well! 😊')
else:
    st.write('') # left blank if nothing is selected!
