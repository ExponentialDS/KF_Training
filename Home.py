import streamlit as st
from pathlib import Path
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="🥋 White Crane Training Log", page_icon="🥋", layout="wide")

# --- Header ---
st.title("🥋 White Crane Training Log")
st.write("A personal log for Hard Style, Yoga, and Soft Style training.")

# --- Hero / Crane Image (local path with fallbacks) ---
local_img = Path(r"C:\Users\crist\AI_projects\Training\GraceSteel.webp")
repo_img = Path("assets/GraceSteel.webp")  # add this to repo for Streamlit Cloud
if local_img.exists():
    st.image(str(local_img), caption="Grace Steel", use_column_width=True)
elif repo_img.exists():
    st.image(str(repo_img), caption="Grace Steel", use_column_width=True)
else:
    st.image(
        "https://images.unsplash.com/photo-1589987607627-3d9c1790bdfa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        caption="The spirit of the White Crane",
        use_column_width=True
    )

# --- Goals ---
st.subheader("🎯 Goals")
st.markdown("""
- **Train each day** — consistency > quantity.  
- **Build Inner & Outer Strength (Yin & Yang).**  
- **Use the daily log to spot good patterns** and adjust training.
""")

# ---------- Week 1 data ----------
W1 = {
    "Day 1 – 24 Aug 2025": [
        "Horse stance: **4 min**",
        "Plank hold: **4 min 10 sec**",
        "Left forward kicks: **9 × 3**",
        "Right forward kicks: **3 × 9**",
        "Left outside crescent kicks: **3 × 9**",
        "Right outside crescent kicks: **3 × 9**",
        "Left wall kicks (height & speed): **2 × 9**",
        "Right wall kicks (height & speed): **2 × 9**",
        "Left inside crescent kicks: **1 × 9**",
        "Right inside crescent kicks: **1 × 9**",
        "Crane kick (power): **1 × 9**",
        "Roundhouse kick (power): **1 × 9**",
        "Side kick (power): **1 × 9**",
        "Splits: length of **2 books**",
        "Forward splits: **2 total (L+R), 9 breaths each**",
        "Push Block: **1 × 9**",
        "V-sit hold (reverse plank): **1 min** (struggled)",
        "Cool-down: cobra × 9, downward dog (9 breaths), inverted side stretch (9 each), inverted hand stretch (9 breaths)",
        "Recovery: **Lower back stretches + Tiger Balm**",
    ],
    "Day 2 – 25 Aug 2025": [
        "Sun Salutations A: **5 rounds**",
        "Sun Salutations B: **2 rounds**",
        "Inverted Arrow Pose: **2 holds**",
    ],
    "Day 3 – 26 Aug 2025": [
        "Lower horse stance: **2 min** (breath, hands on chest & belly)",
        "Leg lifts: **9 × 2 breaths each**",
        "Very low arrow lunge: **1 × 9 R**, **1 × 9 L**",
        "Three Beats of Heaven: **9** horizontal gravity waves, kidney smacks, bear walks",
        "Qigong pattern: energy rise → overhead-to-ground → **1** vertical gravity wave → palm-to-palm energy ball → **2 × 9** finger energy rolls",
        "Tai Chi Bird Walk: **9 steps**",
        "Water smacks: **18**",
        "Bagua steps: **9**",
        "Warrior Tai Chi Form 1: **completed**",
        "Feeling: **more awake, energized**",
    ],
    "Day 4 – 27 Aug 2025": [
        "**Different kicks:** **5 × 9** (mix: forward / outside / inside / roundhouse / side)",
        "**Push-ups:** **4 × 9**",
        "**Butterfly sit-ups:** **4 × 9**",
    ],
    "Day 5 – 28 Aug 2025": [
        "_No log entered._"
    ],
    "Day 6 – 29 Aug 2025": [
        "**Push-ups:** **4 × 9 + 2 extra** (total **38**)"
    ],
    "Day 7 – 30 Aug 2025": [
        "**Horse stance:** **4 min 10 sec**",
        "**Plank hold:** **4 min 20 sec**",
    ],
}

# Compute Week 1 bests for targets
def best_time_sec(timestr_list):
    best = 0
    for s in timestr_list:
        parts = s.split()
        try:
            mins = int(parts[0].replace("min", "").strip())
            secs = int(parts[2].replace("sec", "").strip()) if "sec" in s else 0
        except Exception:
            mins = int(parts[0]) if parts else 0; secs = 0
        best = max(best, mins*60 + secs)
    return best

w1_best_horse = best_time_sec(["4 min", "4 min 10 sec"])
w1_best_plank = best_time_sec(["4 min 10 sec", "4 min 20 sec"])

# Slightly-better Week 2 targets (+10s stances; +1–2 reps on strength)
W2_TARGETS = [
    f"Horse stance target: **{(w1_best_horse + 10)//60} min {(w1_best_horse + 10)%60} sec**",
    f"Plank target: **{(w1_best_plank + 10)//60} min {(w1_best_plank + 10)%60} sec**",
    "Push-ups target: **4 × 9 + 4 extra** (or **5 × 9** on one day)",
    "Butterfly sit-ups target: **+1 set** (aim **5 × 9** once)",
    "Kicks: keep **5 × 9 mixed**; refine speed/height/precision",
    "Mobility: repeat **cobra × 9**, **downward dog 9 breaths**, add **pigeon (L/R) 9 breaths** 1–2 days",
]

# ---------- Navigation ----------
week_tabs = st.tabs(["Week 1", "Week 2"])

# Week 1: day tabs
with week_tabs[0]:
    day_tabs = st.tabs(list(W1.keys()))
    for tab, (day_label, items) in zip(day_tabs, W1.items()):
        with tab:
            st.subheader(day_label)
            st.markdown("\n".join([f"- {it}" for it in items]))

# Week 2: targets + empty day tabs to fill
with week_tabs[1]:
    st.subheader("Week 2 — Aim to slightly beat Week 1")
    st.markdown("**Targets (auto-derived from Week 1 bests):**")
    st.markdown("\n".join([f"- {t}" for t in W2_TARGETS]))

    st.markdown("---")
    st.markdown("#### Daily logs")
    w2_days = [f"Day {i} – (Week 2)" for i in range(1, 8)]
    w2_tabs = st.tabs(w2_days)
    for i, t in enumerate(w2_tabs, start=1):
        with t:
            st.markdown(f"##### {w2_days[i-1]}")
            st.info("Fill in your training here (copy/paste from Week 1 format).")
            # Optional: simple text area to jot notes during Week 2
            st.text_area("Notes", key=f"w2_notes_{i}", height=120, placeholder="e.g., Horse stance 4:20, Push-ups 4×9+4, …")
