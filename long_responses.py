#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_WEATHER = "Why dont you step outside and check for yourself, take a break ;)"
R_PLACE = "Currently I live in this system, I am a traveller you see"
R_CREATED = "I was created by DHANUSH, he also took help from internet to develop me..obviously %)"

def unknown():
    response = ["Could you please re-phrase that? ",
                ".....",
                "Sorry, I was not developed so sophisticated to answer this question",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(5)]
    return response

