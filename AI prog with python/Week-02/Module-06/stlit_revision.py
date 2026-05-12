# import streamlit as st

# st.write('Hello world')
# st.title('My first streamlit web apps', anchor=False)
# st.divider()
# st.header('Web app headerr', divider=True ,anchor=False)
# st.subheader('web app sub header', anchor=False, divider=True)

# st.markdown('**Hello** :red[world]')
# st.markdown('**Hello** :red-background[:orange[world]]')
# st.markdown(":thought_balloon: :yellow[*thinking*]")

# st.subheader("Input your information ", anchor=False)

# name = st.text_input('Enter name: ', placeholder='Enter your name: ')
# number = st.number_input("enter a number: ", value=None, placeholder='Type your age')
# passwo = st.text_input("enterr pass: ", type="password")

# pressed = st.button("confirm")
# if pressed:
#     st.write(f"you entered :blue-background[{name}]")
#     st.write(f"you number :red-background[{number}]")
#     st.write(f"you pass :red-background[{passwo}]")
# else:
#     st.warning('press to confirm')

# selected = st.selectbox(
#     "Choose your profession",
#     ("student", "employee", "businessman"),
#     index=None,
#     accept_new_options=True
# )
# but_pressed = st.button('Enter')
# if but_pressed:
#     st.write(f"you select :red-background[{selected}]")

# st.title('Input your file: ', anchor=False)
# st.divider()

# images = st.file_uploader(
#     "Enter your image: ",
#     type=['png','jpg','jpeg'],
#     max_upload_size=30,
#     accept_multiple_files=True
# )
# print(type(images))

# if images:
#     clm = st.columns(len(images))
#     for i, perimage in enumerate(images):
#         with clm[i]:
#             st.image(perimage)

# sound_file = st.file_uploader("enter audio file: ",
#                          type=['mp3', 'flac'],
#                          accept_multiple_files=False,
# )
# print(type(sound_file))
# if sound_file:
#     st.audio(sound_file)


# videos

# video_file = st.file_uploader("Enter file: ",
#                               type = ['mp4'])

# button = st.button('Upload')
# if button:
#     if video_file:
#         st.video(video_file)
#         st.success("upload successfully")
#     else:
#         st.error("you must upload a file")