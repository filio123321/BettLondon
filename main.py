import streamlit as st

PARTIAL_CODES = {
    "challenge1": "elsys{R0l3s_4r3_FuN}",
    "challenge2": "elsys{Who_Tought_you_decrypting}",
    "challenge3": "elsys{WHATT_YOU_ALSO_KNOW_ABOUT_THIS}",
    "challenge4": "elsys{sofia_tech_park}"
}

def show_challenge_1():
    st.title("Challenge 1: URL Manipulation")
    st.write(
        "A suspicious link has been found. There's a parameter called `role` in the URL, "
        "and rumors say you can elevate your privileges by changing it. "
        "We’ve simulated that scenario here. Can you figure out which value grants you access?"
    )
    user_input = st.text_input("Enter the `role` value:", value="")
    if user_input.lower() == "admin":
        st.success("Congratulations! You found the correct role!")
        st.write(f"Your first partial code is: **{PARTIAL_CODES['challenge1']}**")
        st.write("Now head over to Challenge 2 via the sidebar to continue.")
    else:
        st.warning("Access denied. Hint: Try a higher privilege...")

def show_challenge_2():
    st.title("Challenge 2: Multi-Encoding + Caesar Cipher")
    st.write(
        "You’ve intercepted a strange encoded message. It looks like it might involve Base64 "
        "or even a Caesar cipher. Your job is to decode it and uncover the secret key."
    )
    st.write(
        "For instance, you might come across a cryptic string like:\n"
        "`YmlwdnB7VGVsX1FscmRlcV92bHJfYWJ6b3ZtcWZrZH0`\n"
        "Give it your best shot, then enter the final partial code here."
    )
    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge2"]:
        st.success("Well done! Proceed to Challenge 3.")
    elif user_input:
        st.error("Incorrect solution. Try again!")

def show_challenge_3():
    st.title("Challenge 3: Hidden in an Image (Steganography / EXIF)")
    st.write(
        "Some images contain more than meets the eye. "
        "In this challenge, there’s an embedded message waiting to be discovered. "
        "Careful examination (or the right tool) might reveal the secret. "
        "Once you have it, enter your partial code below."
    )
    st.write(
        "Fun fact: Our school ELSYS hosts two iconic annual events, **HackTues** and **TuesFest**, "
        "organized entirely by students for students. Just like hidden data, there's more happening "
        "beneath the surface than you might expect!"
    )
    st.image("images/HackTuesTeam.png", caption="An image with hidden secrets (replace with the real puzzle)")

    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge3"]:
        st.success("Excellent! You uncovered the hidden info. Proceed to Challenge 4.")
    elif user_input:
        st.error("Incorrect code. Try again!")

def show_challenge_4():
    st.title("Challenge 4: Geolocation")
    st.write(
        "A mysterious photo shows a landmark. "
        "Rumor has it that if you can identify this place, you’ll gain access to the final secret. "
        "Use your detective skills (or a reverse image search) to figure out the location—"
        "then enter the partial code."
    )
    st.image("images/GuessTheLocation.png", caption="Where in the world is this? (replace with your puzzle image)")

    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge4"]:
        st.success("Bravo! You’ve reached the final step. Head to 'Final Submit' to finish.")
    elif user_input:
        st.error("Incorrect code. Keep investigating!")

def show_final_submit():
    st.title("Final Stage: Enter All Four Codes")
    st.write("After you’ve conquered every challenge, enter the four partial codes here to claim your reward!")

    code1 = st.text_input("Code from Challenge 1")
    code2 = st.text_input("Code from Challenge 2")
    code3 = st.text_input("Code from Challenge 3")
    code4 = st.text_input("Code from Challenge 4")

    if st.button("Submit"):
        if (
            code1 == PARTIAL_CODES["challenge1"] and
            code2 == PARTIAL_CODES["challenge2"] and
            code3 == PARTIAL_CODES["challenge3"] and
            code4 == PARTIAL_CODES["challenge4"]
        ):
            st.balloons()
            st.success("Congratulations! All codes are correct!")
            st.write("Show this screen to the organizers to receive your prize.")
        else:
            st.error("Some code is incorrect. Please try again.")

def main():
    st.set_page_config(page_title="Mini CTF Challenges", layout="centered")
    st.sidebar.title("CTF Menu")

    pages = {
        "🔓 Challenge 1 (URL Manipulation)": show_challenge_1,
        "🔑 Challenge 2 (Encoding/Caesar)": show_challenge_2,
        "🖼 Challenge 3 (Stego/EXIF)": show_challenge_3,
        "🌍 Challenge 4 (Geolocation)": show_challenge_4,
        "🏁 Final Submit": show_final_submit
    }

    choice = st.sidebar.radio("Select a challenge:", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()
