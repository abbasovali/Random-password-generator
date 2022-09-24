import streamlit as st
import random
import time

header = st.container()

with header:
    st.title("Random password generator")
    letters = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'z', 'x', 'c', 'v', 'b', 'n']

    capletters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
                  'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    numbers = ["1", "2", "3", "4", "5",
               "6", "7", "8", "9", "0"]

    symbols = ['!', '@', '#', '$', '%', '^', '&', '&', '*', '~', '[', ']', ':', '/']

    length = int(st.slider('Indicate number of charachters', min_value=4, max_value=20))

    password = []

    options = st.multiselect(
        'Make stronger',
        ['Include uppercase', 'Include number', 'Include symbol'])

    if ('Include uppercase' in options) and ('Include number' not in options) and ('Include symbol' not in options):
        addcharachters = random.choice(capletters)
        for length in range(length - 1):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)


    elif ('Include number' in options) and ('Include uppercase' not in options) and ('Include symbol' not in options):
        addcharachters = random.choice(numbers)
        for length in range(length - 1):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)

    elif ('Include symbol' in options) and ('Include uppercase' not in options) and ('Include number' not in options):
        addcharachters = random.choice(symbols)
        for length in range(length - 1):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)


    elif ('Include uppercase' in options) and ('Include number' in options) and ('Include symbol' not in options):
        addcharachters = random.choice(capletters) + random.choice(numbers)
        for length in range(length - 2):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)

    elif ('Include uppercase' in options) and ('Include symbol' in options) and ('Include number' not in options):
        addcharachters = random.choice(capletters) + random.choice(symbols)
        for length in range(length - 2):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)

    elif ('Include number' in options) and ('Include symbol' in options) and ('Include uppercase' not in options):
        addcharachters = random.choice(numbers) + random.choice(symbols)
        for length in range(length - 2):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)

    elif ('Include uppercase' in options) and ('Include number' in options) and ('Include symbol' in options):
        addcharachters = random.choice(capletters) + random.choice(numbers) + random.choice(symbols)
        for length in range(length - 3):
            charachters = random.choice(letters)

            password += charachters

        password += addcharachters
        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)

    else:
        for length in range(length):
            charachters = random.choice(letters)

            password += charachters

        random.shuffle(password)
        password = ''.join(password)
        result = st.button('Generate!')
        st.write(result)
        if (result):
            st.write(password)
