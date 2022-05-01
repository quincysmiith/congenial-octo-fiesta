import streamlit as st
import requests
import random
import string

st.header("St.button")

button1 = st.button("Say hello")
if button1:
    st.write("why hello there")
else:
    st.write("Goodbye")

count = 0


def my_random():
    count = random.randrange(1, 10)
    return None


# ----------------------------------------
# helper password generator
# ----------------------------------------

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    # length = int(input("Enter password length: "))
    length = 20

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return "".join(password)


# a button you can press multiple times
st.header("Pressing multiple times")


button2 = st.button("tell me a joke")
if button2:
    r = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    st.write(r.json()["joke"])
    button2 = False


button3 = st.button("password generator")
if button3:
    st.write(generate_random_password())
