from ctypes import alignment
from re import S
import streamlit as st
from PIL import Image

st.set_page_config('wide')
page = st.sidebar.selectbox('Page', ['Topic Selection', 'Classroom', 'Report'])

if page=='Topic Selection':
    PAGE_1 = True
    PAGE_2 = False
    PAGE_3 = False
elif page=='Classroom':
    PAGE_1 = False
    PAGE_2 = True
    PAGE_3 = False
elif page=='Report':
    PAGE_1 = False
    PAGE_2 = False
    PAGE_3 = True

# ----------------------------------------------------------------------------------------------

if PAGE_1:
    logo = Image.open('whirlykop.jpeg')
    logo = logo.crop((0,170,logo.size[0],logo.size[1]-270))
    st.image(logo)
    st.title('Whirlykop')
    st.write("""
    Welcome to Whirlykop, please search for a topic.
    """)
    topic = st.text_input('Topic', 'Data Structures and Algorithms')
    if st.button('Search'):
        st.write(f'Showing reccomendations for ***{topic}***:')
        reccom_1 = Image.open('dsa_1.jpg')
        reccom_2 = Image.open('dsa_2.jpg')
        reccom_3 = Image.open('dsa_3.jpg')
        col1, col2, col3 = st.columns((1,1,1))
        col1.image(reccom_1)
        col1.write("""
        [**Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer**](https://www.youtube.com/watch?v=RBSGKlAvoiM)
 
        [*freeCodeCamp.org*](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ)
        """)
        col2.image(reccom_2)
        col2.write("""
        [**Data Structures and Algorithms in Python - Full Course for Beginners**](https://www.youtube.com/watch?v=pkYVOmU3MgA)
 
        [*freeCodeCamp.org*](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ)
        """)
        col3.image(reccom_3)
        col3.write("""
       [**Data Structures and Algorithms for Beginners**](https://www.youtube.com/watch?v=BBpAmxU_NQo)
 
        [*Programming with Mosh*](https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA)
        """)

# -----------------------------------------------------------------------------------------------

if PAGE_2:
    st.title('Classroom')
    if st.button('Join Class'):
        st.write('**Google Meet Link:** https://meet.google.com/ups-rosq-zpz')
        st.image('google_meet.jpg')

# ------------------------------------------------------------------------------

if PAGE_3:
    st.title('Class Report')

    st.header('Class Attention')
    class_attention = Image.open('class_attention.jpeg')
    st.image(class_attention)
    st.write('Well Done! **91%** of the class was attentive during teaching.')

    st.header('Student Report')
    student = st.selectbox('Student Name', ['Student A', 'Student B'])
    
    if st.button('Get Report'):
        col1, col2= st.columns((1,2))
        student_img = Image.open('student_img.png')
        col1.image(student_img, width=170)

        col2.write(f"""
        ### {student}

        **Class:** CBSE (Class XII), Section B

        **Topic:** Data Structures and Algorithms
        """)
        
        st.write('**Date:** 15 Feb 2022')
        
        st.subheader('Attention Graph')
        attention_graph = Image.open('drowsiness_level.jpg')
        attention_graph = attention_graph.resize((1000,400))
        st.image(attention_graph)

        st.subheader('Emotion Graph')
        emotion_graph = Image.open('emotion_level.jpg')
        emotion_graph = emotion_graph.resize((1000,400))
        st.image(emotion_graph)

        st.subheader('Summary')
        st.write(f"""
        **{student}** was attentive **87%** of the class.

        **{student}** understood **47%** of the topic taught.
        """) 

        st.subheader('Attention Map')
        attention_map = Image.open('attention_map.jpeg')
        st.image(attention_map)

