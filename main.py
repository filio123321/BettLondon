import streamlit as st

# Updated partial codes
PARTIAL_CODES = {
    "challenge1": "elsys{R0l3s_4r3_FuN}",
    "challenge2": "elsys{Who_Tought_you_decrypting}",
    "challenge3": "elsys{WHATT_YOU_ALSO_KNOW_ABOUT_THIS}",
    "challenge4": "elsys{sofia_tech_park}"
}

# String to be decrypted (mentioned in your request):
# "YmlwdnB7VGVsX1FscmRlcV92bHJfYWJ6b3ZtcWZrZH0"
# You can incorporate this string into Challenge 2 or wherever appropriate in your puzzle.

def show_challenge_1():
    st.title("Challenge 1: URL Manipulation")
    st.write(
        "Typically, you would change `?role=guest` to `?role=admin` in the URL, "
        "but here we simulate that by letting you guess the correct parameter value in a text field."
    )
    user_input = st.text_input("Enter the `role` value:", value="")
    if user_input.lower() == "admin":
        st.success("Congratulations! You found the correct 'role'!")
        st.write(f"Your first partial code is: **{PARTIAL_CODES['challenge1']}**")
        st.write("Proceed to Challenge 2 via the sidebar menu.")
    else:
        st.warning("Access denied. Hint: consider a higher privilege...")

def show_challenge_2():
    st.title("Challenge 2: Multi-Encoding + Caesar Cipher")
    st.write(
        "Here you would have some Base64/Caesar-encrypted text. "
        "Your task is to decode it and enter the final partial code."
    )
    st.write(
        "For instance, you might see something like this: "
        "`YmlwdnB7VGVsX1FscmRlcV92bHJfYWJ6b3ZtcWZrZH0`, "
        "which you must decode or decrypt to get the correct code."
    )
    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge2"]:
        st.success("Well done! Proceed to Challenge 3.")
    elif user_input:
        st.error("Incorrect solution. Try again!")

def show_challenge_3():
    st.title("Challenge 3: Hidden in an Image (Steganography / EXIF)")
    st.write(
        "Did you know our school ELSYS holds two iconic events each year, "
        "organized by students for students? They are **HackTues** and **TuesFest**."
    )
    st.write(
        "Here, you have an image with hidden information (EXIF data or steganography). "
        "After extracting the hidden data, enter the partial code below."
    )
    # Show your puzzle image. If you store it in the same folder, just use its filename:
    st.image("images/HackTuesTeam.png", caption="Example image (replace with real puzzle)")

    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge3"]:
        st.success("Congratulations! You found the hidden info. Proceed to Challenge 4.")
    elif user_input:
        st.error("Incorrect code. Try again!")

def show_challenge_4():
    st.title("Challenge 4: Geolocation")
    st.write(
        "You receive an image of a slightly unusual landmark. "
        "Use reverse image search or clues to figure out where it is located. "
        "Then enter the partial code below."
    )
    # Show your puzzle image for geolocation:
    st.image("images/GuessTheLocation.png", caption="Example landmark (replace with real puzzle)")

    user_input = st.text_input("Enter the discovered partial code:", value="")
    if user_input == PARTIAL_CODES["challenge4"]:
        st.success("Excellent! You've found the final code. Go to 'Final Submit' to finish.")
    elif user_input:
        st.error("Incorrect code. Try again!")

def show_final_submit():
    st.title("Final Stage: Enter All Four Codes")
    st.write("After completing all challenges, enter the four partial codes here to claim your reward!")

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
