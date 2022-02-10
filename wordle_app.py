#!/usr/bin/env python
# coding: utf-8




import streamlit as st
import find_wordle as fw

try:
    
    dic = {}
    letters = []
    avoidlist = []
    st.title('Find the Wordle Word!')

    st.write('Tell me about this word...')

    first = st.checkbox('i know the first letter')
    if first:
        dic['first']=st.text_input('first letter', 'c').lower()

    second = st.checkbox('i know the second letter')
    if second:
        dic['second']=st.text_input('second letter', 'r').lower()

    third = st.checkbox('i know the third letter')
    if third:
        dic['third']=st.text_input('third letter', 'a').lower()

    fourth = st.checkbox('i know the fourth letter')
    if fourth:
        dic['fourth']=st.text_input('fourth letter', 'n').lower()

    fifth = st.checkbox('i know the fifth letter')
    if fifth:
        dic['fifth']=st.text_input('fifth letter', 'e').lower()

    others = st.checkbox('i know letters that are in the word, but im not sure about the position')
    if others:
        l = st.text_input('enter with space between the letters', 'a b c').lower()
        letters = l.split(' ')
    avoid = st.checkbox('i know letters that are not in the word')
    if avoid:
        l = st.text_input('enter these letter with space between', 'a b c').lower()
        avoidlist = l.split(' ')
    out = fw.find_wordle(avoidlist,*letters,**dic)
    st.write(out)
except:
    pass
