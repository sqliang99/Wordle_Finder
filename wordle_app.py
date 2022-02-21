
import streamlit as st
import find_wordle as fw

try:
    
    dic = {}
    dic2 = {}
    letters = []
    avoidlist = []
    st.title('Find the Wordle Word!')

    st.write('Tell me about this word...')

    first = st.checkbox('i know the first letter')
    if first:
        dic['first']=st.text_input('first letter', 'c').lower()
    
    afirst = st.checkbox('i know letters that are not the first letter')
    if afirst:
        l1 = st.text_input('enter with space between', 'a b c').lower()
        dic2['first'] = l1.split(' ')

    second = st.checkbox('i know the second letter')
    if second:
        dic['second']=st.text_input('second letter', 'r').lower()
    
    asecond = st.checkbox('i know letters that are not the second letter')
    if asecond:
        l2 = st.text_input('enter these letter with space between', 'a b c').lower()
        dic2['second'] = l2.split(' ')

    third = st.checkbox('i know the third letter')
    if third:
        dic['third']=st.text_input('third letter', 'a').lower()
        
    athird = st.checkbox('i know letters that are not the third letter')
    if athird:
        l3 = st.text_input('enter these letter with space between', 'a b c').lower()
        dic2['third'] = l3.split(' ')

    fourth = st.checkbox('i know the fourth letter')
    if fourth:
        dic['fourth']=st.text_input('fourth letter', 'n').lower()
     
    afourth = st.checkbox('i know letters that are not the fourth letter')
    if afourth:
        l4 = st.text_input('enter these letter with space between', 'a b c').lower()
        dic2['fourth'] = l4.split(' ')

    fifth = st.checkbox('i know the fifth letter')
    if fifth:
        dic['fifth']=st.text_input('fifth letter', 'e').lower()
    
    afifth = st.checkbox('i know letters that are not the fifth letter')
    if afifth:
        l5 = st.text_input('enter these letter with space between', 'a b c').lower()
        dic2['fifth'] = l5.split(' ')

    others = st.checkbox('i know letters that are in the word, but im not sure about the position')
    if others:
        l = st.text_input('enter with space between the letters', 'a b c').lower()
        letters = l.split(' ')
        
    avoid = st.checkbox('i know letters that are not in the word')
    if avoid:
        l = st.text_input('enter these letter with space between', 'a b c').lower()
        avoidlist = l.split(' ')
        
    
    out = fw.find_wordle(others,dic,dic2,avoid)
    st.write(out)
    
    luck = st.checkbox('i would like a lucky word')
    if luck:
        try:
            lucky = fw.max_info(others,dic,dic2,avoid)
            st.write(lucky)
        except:
            pass
except:
    pass
