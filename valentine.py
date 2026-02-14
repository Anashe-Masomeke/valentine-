import streamlit as st
import random
import time
import os
from datetime import datetime

st.set_page_config(page_title="Valentine Emergency Center BY POPE MASO", page_icon="💘")

# ---- Background Styling ----
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
background: linear-gradient(to right, #ff4b6e, #ff758c, #ff8fa3);
color: black;
}
h1, h2, h3, h4 {
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- File Setup ----
FILE_NAME = "singles.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass

# ---- Title ----
st.title("💔 Valentine Emergency Support Center BY POPE MASO")
st.subheader("Official Database of The Forgotten 😂")

# ---- Name Input ----
name = st.text_input("Enter your name so we confirm your heartbreak 😭")

# ---- Roast Messages ----
roasts = [
    "{}... even your crush updated status: 'Finally happy' 💀😂",
    "{}... your phone was so dry today even Sahara is jealous 🏜️",
    "{}... even spam messages avoided you today 📩😭",
    "{}... your shadow walked faster than you 💔",
    "{}... even Bluetooth said 'No devices found' 📶💀",
    "{}... your love life is buffering at 1% 😂"
]

# ---- Button ----
if st.button("Check My Valentine Status 💘"):

    if name == "":
        st.warning("Enter your name first so we roast you properly 😂")
    else:

        # Read existing names
        with open(FILE_NAME, "r") as f:
            existing_names = [n.strip().lower() for n in f.readlines()]

        # Save only if not duplicate
        if name.lower() not in existing_names:
            with open(FILE_NAME, "a") as f:
                f.write(name + "\n")

        # Fake loading
        with st.spinner("Scanning the Valentine Database... 🎁"):
            time.sleep(2)

        progress = st.progress(0)
        for percent in range(100):
            time.sleep(0.01)
            progress.progress(percent + 1)

        time.sleep(1)

        # Random roast
        message = random.choice(roasts).format(name)

        st.error(message)
        st.success("System result: ZERO gifts detected 💀")

        # 🚨 Flash + Shake Alert
        st.markdown("""
        <style>
        @keyframes flash {
            0% {background-color: red;}
            50% {background-color: darkred;}
            100% {background-color: red;}
        }

        @keyframes shake {
            0% { transform: translate(0px, 0px); }
            25% { transform: translate(5px, -5px); }
            50% { transform: translate(-5px, 5px); }
            75% { transform: translate(5px, 5px); }
            100% { transform: translate(0px, 0px); }
        }

        .alert-box {
            animation: flash 0.5s infinite;
            padding: 20px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
        }

        .shake {
            animation: shake 0.3s infinite;
        }
        </style>

        <div class="alert-box shake">
        🚨 ALERT: PERMANENT SINGLE DETECTED 🚨
        </div>
        """, unsafe_allow_html=True)

        # Confetti
        st.balloons()

        # ---- AUTO PLAY ONLINE SOUND ----
        audio_url = "https://www.myinstants.com/media/sounds/emotional-damage-meme.mp3"

        audio_html = f"""
        <audio autoplay>
            <source src="{audio_url}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

        # ---- Countdown ----
        today = datetime.today()
        next_valentine = datetime(today.year, 2, 14)

        if today > next_valentine:
            next_valentine = datetime(today.year + 1, 2, 14)

        days_left = (next_valentine - today).days

        st.markdown("### ⏳ Countdown To Next Valentine")
        st.info(f"💘 Only {days_left} days left to prepare better 😂")

        st.markdown("### Stay strong soldier 💪😂")
        st.markdown("## — BY POPE ANASHE MASO")


# ---- DISPLAY ALL STORED NAMES ----
st.markdown("## 📜 Official Single Registry")

with open(FILE_NAME, "r") as f:
    names = f.readlines()

if names:
    for n in names:
        st.write("💔", n.strip())
else:
    st.write("No singles recorded yet... suspicious 👀")
