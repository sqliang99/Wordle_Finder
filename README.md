# Wordle_Finder
An app that helps you filter words for wordle. If you ask for it you can also get an algorithm generated lucky word for you to try.

The list of wordle words are kindly provided by Cyrus Freshman. You can find it here: https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b

This app is supported by streamlit and deployed on streamlit cloud, you can access it here: https://share.streamlit.io/sqliang99/wordle_finder/main/wordle_app.py

This project is partially inspired by 3blue1brown, although his video on information theory lost me half way.

### Updates
2022/2/21:<br/>
Users can now enter letters they don't want to see at a certain location.

2022/2/16:<br/>
Included an algorithm that generates a lucky word if the user asks for it

One minor update which I forgot the date of:<br/>
Supports capitalized letter input

### How it works
Users can enter certain qualities of the word (for example, what the first letter is, what letters are not in the word, what letters are not the second letter, etc) and words that fit this filter will be returned.<br/>
The algorithm-generated "lucky word" is a word that fits the filter that carries the most amount of "information". The goal of the lucky word is to filter out as many words as possible so the user can quickly narrow down on the range of possibly correct words. The lucky word is not a guess of the correct answer; rather, it is a word that allows for the user to filter out as many false answers as possible.
