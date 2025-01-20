import streamlit as st

# Store partial codes here (like we did in Flask).
PARTIAL_CODES = {
    "challenge1": "URL-HACK-123",
    "challenge2": "MULTI-ENCODING-456",
    "challenge3": "HIDDEN-IMAGE-789",
    "challenge4": "LOCATION-ABC-999"
}

def show_challenge_1():
    st.title("Challenge 1: URL Манипулация")
    st.write(
        "Обикновено ще промените `?role=guest` на `?role=admin` в URL-а, "
        "но тук просто въведете кой параметър да промените, за да получите админ достъп."
    )
    # We simulate "URL manipulation" by letting the user guess the correct param value.
    user_input = st.text_input("Въведете стойността на `role`:", value="")
    if user_input.lower() == "admin":
        st.success("Поздравления! Открихте правилното 'role'!")
        st.write(f"Вашият първи частичен код е: **{PARTIAL_CODES['challenge1']}**")
        st.write("Можете да преминете към Challenge 2 от страничното меню.")
    else:
        st.warning("Достъп отказан. Подсказка: Помислете за по-високи права...")

def show_challenge_2():
    st.title("Challenge 2: Многократно кодиране + Шифър на Цезар")
    st.write(
        "Тук бихте получили малко Base64/Цезар шифрован текст. "
        "Открийте крайното декодирано съобщение и въведете частичния код."
    )
    user_input = st.text_input("Въведете разкрития частичен код:", value="")
    if user_input == PARTIAL_CODES["challenge2"]:
        st.success("Точно така! Продължете към Challenge 3.")
    elif user_input:
        st.error("Грешно решение. Опитайте отново!")

def show_challenge_3():
    st.title("Challenge 3: Скрито в изображение (Стеганография / EXIF)")
    st.write(
        "Знаехте ли, че нашето училище ELSYS има две емблематични събития всяка година, "
        "организирани от ученици за ученици? Това са **HackTues** и **TuesFest**."
    )
    st.write(
        "Тук ще имате изображение, където е скрита информация (EXIF или стеганография). "
        "След като намерите текста, въведете частичния код."
    )
    # Placeholder image demonstration
    st.image("placeholder-stego.jpg", caption="Примерно изображение (поставете истинското)")
    
    user_input = st.text_input("Въведете открития частичен код:", value="")
    if user_input == PARTIAL_CODES["challenge3"]:
        st.success("Поздравления, намерихте скритата информация!")
        st.write("Преминете към Challenge 4.")
    elif user_input:
        st.error("Грешно решение. Опитайте пак!")

def show_challenge_4():
    st.title("Challenge 4: Геолокация")
    st.write(
        "Получавате снимка на по-необичайна забележителност. "
        "Използвайте reverse image search или улики, за да откриете мястото. "
        "После въведете частичния код."
    )
    # Placeholder image demonstration
    st.image("placeholder-landmark.jpg", caption="Примерно изображение (поставете истинското)")
    
    user_input = st.text_input("Въведете открития частичен код:", value="")
    if user_input == PARTIAL_CODES["challenge4"]:
        st.success("Чудесно! Открихте финалния код. Отидете на 'Final Submit', за да завършите.")
    elif user_input:
        st.error("Невалиден код. Опитайте пак!")

def show_final_submit():
    st.title("Финален етап: Въведете четирите кода")
    st.write("След като сте преминали всички предизвикателства, въведете четирите кода тук.")
    
    code1 = st.text_input("Код от Challenge 1")
    code2 = st.text_input("Код от Challenge 2")
    code3 = st.text_input("Код от Challenge 3")
    code4 = st.text_input("Код от Challenge 4")
    
    if st.button("Изпрати"):
        if (code1 == PARTIAL_CODES["challenge1"] and
            code2 == PARTIAL_CODES["challenge2"] and
            code3 == PARTIAL_CODES["challenge3"] and
            code4 == PARTIAL_CODES["challenge4"]):
            st.balloons()
            st.success("Поздравления! Успяхте да въведете всички кодове правилно!")
            st.write("Покажете този екран, за да получите вашата награда (тениска и т.н.).")
        else:
            st.error("Някой от кодовете не е верен. Опитайте отново!")

def main():
    st.set_page_config(page_title="Mini CTF Challenges", layout="centered")
    st.sidebar.title("CTF Меню")
    
    pages = {
        "🔓 Challenge 1 (URL Manipulation)": show_challenge_1,
        "🔑 Challenge 2 (Encoding/Caesar)": show_challenge_2,
        "🖼 Challenge 3 (Stego/EXIF)": show_challenge_3,
        "🌍 Challenge 4 (Geolocation)": show_challenge_4,
        "🏁 Final Submit": show_final_submit
    }
    
    choice = st.sidebar.radio("Изберете предизвикателство:", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()
