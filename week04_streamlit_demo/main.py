import streamlit as st

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("I love AI VIET NAM")
st.caption("This is a caption")

st.divider()

st.markdown('# xem thêm thông tin trong  ')
st.markdown('[AI Viet nam](https://)')
st.markdown("""
            1. Machine learning
            2. Deep learning
            """)

st.markdown(r'$ \sqrt{2x}')

st.divider()

st.write('AI Viet Nam')
st.write('#Heading 1')
st.write('[Google](http://)')
st.write(r'$ \sqrt{2x} $')
st.write('1 + 1=', 2)

st.divider()
# Hiển thị code trên giao diện
st.code("""
    import random
    value = random.randint(3,10)
    print(value)
""")


def get_year():
    return '19'


with st.echo():
    st.write('This is a text')

    def get_name():
        return 'Nga'
    name = get_name()
    year = get_year()
    st.write(name, year)

st.divider()

st.logo('./logo.png')

st.image('./dog.jpeg', caption='Funny dog.')

st.audio('./audio.mp4')

st.video('./video.mp4')

st.divider()

agree = st.checkbox("I agree!")
if agree:
    st.write('Thank')


st.divider()


def get_name():
    st.write("Nga")


agree = st.checkbox("I agree", on_change=get_name)

if agree:
    st.write("Great!")
    color_options = {'Yellow': 'Vàng', 'Blue': 'Xanh'}
    selected_color = st.radio("Your favorite color:",
                              list(color_options.keys()))
    st.write(f'You selected: {color_options[selected_color]}')


st.divider()


# Single selection with selectbox
option = st.selectbox(
    "Your contact:",
    ("Email", "Home phone", "Mobile phone")
)
st.write("Selected:", option)

# Multiple selection with multiselect
options = st.multiselect(
    "Your favorite colors:",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"]
)
st.write("You selected:", options)

# Single selection with select_slider
color = st.select_slider(
    "Your favorite color:",
    options=["red", "orange", "violet"]
)
st.write("My favorite color is", color)


st.divider()

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

# Using st.markdown to create a link button
st.markdown("[Go to Google](https://www.google.com.vn/)")


st.divider()

import random
value 
