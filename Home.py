import streamlit as st
from pathlib import Path

# --- Page Config ---
st.set_page_config(page_title="🥋 White Crane Training Log", page_icon="🥋", layout="centered")

# --- Header ---
st.title("🥋 White Crane Training Log")
st.write("A personal log for Hard Style, Yoga, and Soft Style training.")

# --- Local image from /assets ---
img_path = Path("assets/GraceSteel.jpg")
if img_path.exists():
    st.image(str(img_path), caption="The spirit of the White Crane", use_container_width=True)
else:
    st.warning(f"Image not found at {img_path}. Make sure the file is in your repo.")
    st.image(
        "https://images.unsplash.com/photo-1589987607627-3d9c1790bdfa?auto=format&fit=crop&w=1200&q=80",
        caption="The spirit of the White Crane (fallback)",
        use_column_width=True
    )

# --- Goals ---
st.subheader("🎯 Goals")
st.markdown("""
- **Train each day** — *consistency beats quantity*.  
- **Build Inner & Outer Strength (Yin & Yang)** — balance hard conditioning with soft/inner work.  
- **Use the daily log to spot patterns** — track what makes you feel strong, mobile, and awake.  
""")

# --- Training Log ---
st.header("Day 1 – Hard Style (Kung Fu Conditioning) – 24th August 2025")
st.markdown("""
- Horse stance: **4 min**  
- Plank hold: **4 min 10 sec**  
- Left forward kicks: **9 × 3 reps**  
- Right forward kicks: **3 × 9 reps**  
- Left outside crescent kicks: **3 × 9 reps**  
- Right outside crescent kicks: **3 × 9 reps**  
- Left wall kicks (height & speed): **2 × 9 reps**  
- Right wall kicks (height & speed): **2 × 9 reps**  
- Left inside crescent kicks: **1 × 9 reps**  
- Right inside crescent kicks: **1 × 9 reps**  
- Crane kick (power): **1 × 9 reps**  
- Roundhouse kick (power): **1 × 9 reps**  
- Side kick (power): **1 × 9 reps**  
- Splits: stretched the length of 2 books  
- Forward splits: **2 total (left + right), 9 breaths each**  
- Push Block: **1 × 9 reps**  
- V-sit hold (reverse plank): **1 min (struggled)**  
- Cool-down: cobra × 9, downward dog (9 breaths), inverted side stretch (9 each), inverted hand stretch (9 breaths)  
- Recovery: **Lower back stretches + Tiger Balm**  
""")

st.header("Day 2 – Yoga Flow – 25th August 2025")
st.markdown("""
- Sun Salutations A: **5 rounds**  
- Sun Salutations B: **2 rounds**  
- Inverted Arrow Pose: **2 holds**  
""")

st.header("Day 3 – Soft Style (Kung Fu / Qigong / Tai Chi) – 26th August 2025")
st.markdown("""
- Lower horse stance: **2 min** (breathing focus, hands on chest & belly)  
- Leg lifts: **9 × 2 breaths each**  
- Very low arrow lunge: **1 × 9 reps right, 1 × 9 reps left**  
- Three Beats of Heaven: **9 horizontal gravity waves, kidney smacks, bear walks**  
- Qigong pattern: energy rise → overhead-to-ground stretch → 1 vertical gravity wave → palm-to-palm energy ball → **2 × 9 finger energy rolls**  
- Tai Chi Bird Walk: **9 steps**  
- Water smacks: **18 reps**  
- Bagua steps: **9 steps**  
- Warrior Tai Chi Form 1: **completed**  
- Feeling after training: **more awake, energized**  
""")

st.header("Day 4 – Conditioning – 27th August 2025")
st.markdown("""
- Press-ups: **4 × 9 reps**  
- Butterfly sit-ups: **4 × 9 reps**  
""")
