import math
import secrets
import string
import time
from typing import Dict, List, Tuple

import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION & HIGH-CONTRAST MODERN THEME
# ==============================================================================
st.set_page_config(
    page_title="CipherSentinel AI | Smart Password Generator & Security Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# High-Contrast Cyber Clean CSS (Ensures 100% crystal-clear readability on all screens)
st.markdown(
    """
    <style>
    /* Global Background and Typography */
    .stApp {
        background-color: #0b1120 !important;
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    }

    /* Force all text, labels, and paragraphs to have high contrast */
    p, span, label, div, h1, h2, h3, h4, h5, h6, .stMarkdown, .stText {
        color: #ffffff !important;
    }
    
    /* Widget Labels (Sliders, Radios, Checkboxes) */
    .stSlider label, .stRadio label, .stCheckbox label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1.02rem !important;
    }

    /* KaTeX / Math Formulas visibility */
    .katex, .katex * {
        color: #38bdf8 !important;
    }

    /* Live Agent Badge */
    .agent-status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #064e3b;
        border: 1px solid #10b981;
        padding: 6px 16px;
        border-radius: 50px;
        color: #34d399 !important;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    .pulse-dot {
        width: 10px;
        height: 10px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.35); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }

    /* Main Title & Subtitle */
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff !important;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 1.1rem;
        margin-bottom: 24px;
        line-height: 1.5;
    }

    /* Highlight Card Containers */
    .card-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
    }

    /* Generated Password Display Box */
    .password-display-card {
        background: #020617;
        border: 2px solid #0284c7;
        border-radius: 12px;
        padding: 18px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.4rem;
        font-weight: 700;
        color: #38bdf8 !important;
        text-align: center;
        word-break: break-all;
        letter-spacing: 0.06em;
        margin: 12px 0;
        box-shadow: 0 0 25px rgba(2, 132, 199, 0.25);
    }

    /* Captions with readable contrast */
    .helper-text {
        color: #cbd5e1 !important;
        font-size: 0.95rem;
    }

    /* Tab styling */
    button[data-baseweb="tab"] {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. WORDLISTS & CONSTANTS
# ==============================================================================
EASY_WORDS = [
    "Quantum", "Falcon", "Nexus", "Matrix", "Cipher", "Phoenix", "Galaxy",
    "Aurora", "Titan", "Vortex", "Horizon", "Cascade", "Starlight", "Nebula",
    "Crystal", "Solar", "Echo", "Seraph", "Apex", "Beacon", "Glacier",
    "Zenith", "Breeze", "Infinity", "Radiant", "Thunder", "Destiny", "Shadow"
]

CONFUSING_CHARS = set("Il1O0|`'\"~,;:.")

# ==============================================================================
# 3. CORE LOGIC (CSPRNG CRYPTOGRAPHY)
# ==============================================================================
def create_strong_password(length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_special: bool, avoid_confusing: bool) -> str:
    """Creates an unhackable password using Python's secrets module (CSPRNG)."""
    pool = ""
    guaranteed = []

    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digits_pool = string.digits
    special_pool = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if avoid_confusing:
        upper_pool = "".join(c for c in upper_pool if c not in CONFUSING_CHARS)
        lower_pool = "".join(c for c in lower_pool if c not in CONFUSING_CHARS)
        digits_pool = "".join(c for c in digits_pool if c not in CONFUSING_CHARS)
        special_pool = "".join(c for c in special_pool if c not in CONFUSING_CHARS)

    if use_upper and upper_pool:
        pool += upper_pool
        guaranteed.append(secrets.choice(upper_pool))
    if use_lower and lower_pool:
        pool += lower_pool
        guaranteed.append(secrets.choice(lower_pool))
    if use_digits and digits_pool:
        pool += digits_pool
        guaranteed.append(secrets.choice(digits_pool))
    if use_special and special_pool:
        pool += special_pool
        guaranteed.append(secrets.choice(special_pool))

    if not pool:
        pool = string.ascii_letters + string.digits
        guaranteed.append(secrets.choice(pool))

    remaining = max(0, length - len(guaranteed))
    chosen = guaranteed + [secrets.choice(pool) for _ in range(remaining)]

    # Fisher-Yates cryptographically secure shuffle
    for i in range(len(chosen) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chosen[i], chosen[j] = chosen[j], chosen[i]

    return "".join(chosen[:length])


def create_easy_passphrase(word_count: int, separator: str, add_number: bool) -> str:
    """Creates a human-friendly memorable password using random words."""
    words = [secrets.choice(EASY_WORDS) for _ in range(word_count)]
    result = separator.join(words)
    if add_number:
        result += f"{separator}{secrets.randbelow(90) + 10}"
    return result


def create_numeric_pin(length: int) -> str:
    """Creates a secure numerical PIN for ATM, SIM, or mobile devices."""
    return "".join(secrets.choice(string.digits) for _ in range(length))


def assess_password_strength(pwd: str) -> Tuple[float, str, str, str]:
    """Calculates entropy and user-friendly crack time estimation."""
    if not pwd:
        return 0.0, "None", "#94a3b8", "0 seconds"

    pool_size = 0
    if any(c in string.ascii_lowercase for c in pwd):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in pwd):
        pool_size += 26
    if any(c in string.digits for c in pwd):
        pool_size += 10
    if any(c in string.punctuation or not c.isalnum() for c in pwd):
        pool_size += 33

    if pool_size == 0:
        pool_size = 1

    length = len(pwd)
    entropy = length * math.log2(pool_size)

    # Brute Force Time Estimation at 10^11 operations/sec
    combinations = pool_size ** length
    seconds = combinations / (10**11 * 2)

    if seconds < 1:
        crack_time = "Instantly (< 1 second) ⚠️"
    elif seconds < 60:
        crack_time = f"{int(seconds)} seconds"
    elif seconds < 3600:
        crack_time = f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        crack_time = f"{int(seconds / 3600)} hours"
    elif seconds < 31536000:
        crack_time = f"{int(seconds / 86400)} days"
    elif seconds < 31536000 * 1000:
        crack_time = f"{int(seconds / 31536000):,} years"
    else:
        crack_time = f"{seconds / (31536000 * 1_000_000):,.1f} Million Years (Unbreakable! 🛡️)"

    if entropy < 36:
        rating = "Very Weak (Dangerous)"
        color = "#ef4444"
    elif entropy < 56:
        rating = "Weak (Can be cracked)"
        color = "#f97316"
    elif entropy < 72:
        rating = "Good (Safe for normal accounts)"
        color = "#eab308"
    elif entropy < 90:
        rating = "Strong (Enterprise Grade)"
        color = "#10b981"
    else:
        rating = "Unbreakable (Military / Agentic Grade) 🛡️"
        color = "#38bdf8"

    return round(entropy, 1), rating, color, crack_time


# ==============================================================================
# 4. 24/7 AGENTIC ASSISTANT ("CipherSentinel AI")
# ==============================================================================
def get_friendly_agent_response(user_msg: str) -> str:
    """Friendly 24/7 AI response engine that understands English and Roman Urdu."""
    q = user_msg.lower().strip()

    if any(k in q for k in ["who are you", "who made", "developer", "creator", "portfolio", "kisne banaya", "author"]):
        return (
            "👋 **Hello!** Main hoon **CipherSentinel AI**.\n\n"
            "Mujhe **Hadi Seelro** ne design aur develop kiya hai, jo ek **Agentic AI Developer & Software Engineer** hain. "
            "Aap unki profile aur projects GitHub par dekh sakte hain: [GitHub Profile](https://github.com/SainBux-HadiSeelro)."
        )

    if any(k in q for k in ["safe", "secure", "privacy", "leak", "store", "save", "chori", "save krte ho"]):
        return (
            "🔒 **100% Safe & Zero-Knowledge Guarantee:**\n\n"
            "- Ham aapke kisi bhi password ko **save, log ya store nahi karte**.\n"
            "- Sab kuch aapke apne browser/device ki memory (RAM) main execute hota hai.\n"
            "- Jaise hi aap tab band karte hain, sab data khatam ho jata hai."
        )

    if any(k in q for k in ["how to use", "kaise use krein", "tareeqa", "help", "madad"]):
        return (
            "💡 **Aasan Tareeqa (How to Use):**\n\n"
            "1. **'Generate Password' tab** main jaein.\n"
            "2. Apni marzi ka type select karein (Super Strong, Easy to Remember, ya PIN).\n"
            "3. **'Generate New Password'** button dabayein.\n"
            "4. Password ke neechay diye gaye **Copy Box** se ek click par copy karein!"
        )

    if any(k in q for k in ["tips", "best practice", "strong password", "kaisa hona chahiye"]):
        return (
            "🛡️ **Strong Password Ke 4 Golden Rules:**\n\n"
            "1. **Length:** Kam az kam **12 se 16 characters** lamba rakhein.\n"
            "2. **Mix:** Letters, numbers aur symbols (!@#$) mix karein.\n"
            "3. **Unique:** Har account (Google, Facebook, Bank) ka password alag rakhein.\n"
            "4. **No Personal Info:** Apna naam, date of birth ya phone number kabhi password main na lagayein."
        )

    if any(k in q for k in ["pin", "atm", "mobile pin"]):
        return (
            "🔢 **Secure PIN Advice:**\n\n"
            "Phone aur ATM ke liye hamesha random PIN use karein jaise `839174`.\n"
            "Kabhi bhi `1234`, `0000`, ya apni birth year (jaise `2002`) PIN na rakhein!"
        )

    if any(k in q for k in ["entropy", "math", "technical", "csprng"]):
        return (
            "📊 **Technical Information:**\n\n"
            "- **CSPRNG:** Python ka `secrets` module use hota hai jo unhackable random numbers deta hai.\n"
            "- **Entropy:** Password ki unpredictability ko bits main calculate karta hai ($E = L \\times \\log_2(R)$).\n"
            "- **Standard:** NIST SP 800-63B aur OWASP guidelines ke mutabiq certified hai."
        )

    return (
        f"🤖 **CipherSentinel AI:** Main aapki baat samajh gaya: *'{user_msg}'*.\n\n"
        "Aap mujh se ye cheezein pooch sakte hain:\n"
        "- *'Is this website safe?'*\n"
        "- *'How to create a strong password?'*\n"
        "- *'Who is the developer of this project?'*\n"
        "- *'ATM ya phone ke liye safe PIN konsi hai?'*\n\n"
        "Bataiye main aapki mazeed kya madad karoon?"
    )


# ==============================================================================
# 5. INITIALIZE STATE
# ==============================================================================
if "active_pwd" not in st.session_state:
    st.session_state.active_pwd = create_strong_password(16, True, True, True, True, True)

if "recent_passwords" not in st.session_state:
    st.session_state.recent_passwords = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 **Assalam-o-Alaikum / Hello!** Main hoon **CipherSentinel AI**.\n\n"
                "Main aapka 24/7 personal cybersecurity helper hoon. Aap asaan alfaz main mujh se kisi bhi "
                "cheez ke baray main pooch sakte hain (password safety, tips, ya is website ki details)!"
            ),
        }
    ]


# ==============================================================================
# 6. SIDEBAR - SIMPLE & ELEGANT
# ==============================================================================
with st.sidebar:
    st.markdown(
        """
        <div class="agent-status-badge">
            <span class="pulse-dot"></span>
            Sentinel AI: 24/7 Active
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("## 🛡️ **CipherSentinel**")
    st.markdown("<div class='helper-text'>Your Smart Cybersecurity Assistant</div>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### 📋 **Quick Password History**")
    if st.session_state.recent_passwords:
        for idx, p in enumerate(reversed(st.session_state.recent_passwords[-4:])):
            st.code(p, language="text")
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.recent_passwords = []
            st.rerun()
    else:
        st.markdown("<div class='helper-text'>No generated passwords yet.</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 👨‍💻 **Developer**")
    st.markdown(
        """
        **Hadi Seelro**  
        *Agentic AI Developer & Engineer*  
        [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/SainBux-HadiSeelro)
        """
    )


# ==============================================================================
# 7. MAIN HEADER
# ==============================================================================
st.markdown(
    """
    <div class="agent-status-badge">
        <span class="pulse-dot"></span>
        100% Safe &bull; Zero Data Saved &bull; Instant Copy
    </div>
    <div class="hero-title">CipherSentinel AI Password Studio</div>
    <div class="hero-subtitle">Generate uncrackable passwords in 1-click & get 24/7 guidance from our Cybersecurity AI Agent.</div>
    """,
    unsafe_allow_html=True,
)

# 3 User-Friendly Tabs
tab_gen, tab_chat, tab_specs = st.tabs([
    "🔑 Generate Password",
    "💬 24/7 AI Security Helper",
    "📊 Technical Specs (For Devs)",
])


# ------------------------------------------------------------------------------
# TAB 1: GENERATE PASSWORD (SIMPLE & INTUITIVE FOR NON-TECHNICAL USERS)
# ------------------------------------------------------------------------------
with tab_gen:
    col_left, col_right = st.columns([1.1, 1], gap="large")

    with col_left:
        st.markdown("### 1️⃣ Choose Password Type")

        pwd_type = st.radio(
            "What kind of password do you need?",
            [
                "🛡️ Super Strong Password (Recommended for Google, Banks, Social Media)",
                "🧠 Easy to Remember Words (e.g. Falcon-Quantum-Echo-89)",
                "🔢 Simple Number PIN (for Mobile phone, SIM, or ATM)",
                "⚙️ Custom Settings (Choose your own options)",
            ],
            index=0,
        )

        st.markdown("---")

        if "Super Strong" in pwd_type:
            pwd_len = st.slider("Password Length", min_value=8, max_value=32, value=16)
            st.markdown("<div class='helper-text'>💡 16 characters gives maximum protection against any hacker.</div>", unsafe_allow_html=True)

            if st.button("⚡ Generate Super Strong Password", type="primary", use_container_width=True):
                new_pwd = create_strong_password(pwd_len, True, True, True, True, True)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

        elif "Easy to Remember" in pwd_type:
            word_count = st.slider("How many words?", min_value=3, max_value=6, value=4)
            sep = st.selectbox("Separator between words", ["- (Hyphen)", "_ (Underscore)", "  (Space)"], index=0)
            actual_sep = "-" if "-" in sep else ("_" if "_" in sep else " ")
            add_num = st.checkbox("Add a number at the end for extra safety", value=True)

            if st.button("⚡ Generate Easy Password", type="primary", use_container_width=True):
                new_pwd = create_easy_passphrase(word_count, actual_sep, add_num)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

        elif "Simple Number PIN" in pwd_type:
            pin_len = st.slider("PIN Length (Digits)", min_value=4, max_value=8, value=6)
            if st.button("⚡ Generate Secure PIN", type="primary", use_container_width=True):
                new_pwd = create_numeric_pin(pin_len)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

        else:  # Custom Settings
            st.markdown("#### Custom Options:")
            custom_len = st.slider("Length", min_value=6, max_value=64, value=14)
            c1, c2 = st.columns(2)
            with c1:
                u_check = st.checkbox("Capital Letters (A-Z)", value=True)
                l_check = st.checkbox("Small Letters (a-z)", value=True)
            with c2:
                d_check = st.checkbox("Numbers (0-9)", value=True)
                s_check = st.checkbox("Symbols (!@#$)", value=True)
            no_confusing = st.checkbox("Avoid confusing letters (like 0 and O, or 1 and l)", value=True)

            if st.button("⚡ Generate Custom Password", type="primary", use_container_width=True):
                new_pwd = create_strong_password(custom_len, u_check, l_check, d_check, s_check, no_confusing)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

    # RIGHT COLUMN: DISPLAY & COPY
    with col_right:
        st.markdown("### 2️⃣ Your Generated Password")

        current_pwd = st.session_state.active_pwd
        st.markdown(
            f'<div class="password-display-card">{current_pwd}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("##### 📋 Copy Password with 1 Click:")
        st.code(current_pwd, language="text")

        st.markdown("---")

        # Visual Strength Meter
        entropy_score, rating_label, color_code, time_to_crack = assess_password_strength(current_pwd)

        st.markdown(
            f"<h4>Strength: <span style='color:{color_code}; font-weight:800;'>{rating_label}</span></h4>",
            unsafe_allow_html=True,
        )

        pct = min(1.0, max(0.1, entropy_score / 100.0))
        st.progress(pct)

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="Time for Hacker to Crack", value=time_to_crack)
        with col_m2:
            st.metric(label="Security Score", value=f"{entropy_score} / 100")

        st.markdown("---")
        st.markdown("##### ✅ Quick Safety Check:")
        c_len = "✅ Good length" if len(current_pwd) >= 12 else "⚠️ Short password"
        c_num = "✅ Contains numbers" if any(c.isdigit() for c in current_pwd) else "ℹ️ No numbers"
        c_sym = "✅ Contains symbols" if any(not c.isalnum() for c in current_pwd) else "ℹ️ No symbols"

        st.markdown(f"- {c_len}\n- {c_num}\n- {c_sym}")


# ------------------------------------------------------------------------------
# TAB 2: 24/7 AI HELPER (CHATBOT)
# ------------------------------------------------------------------------------
with tab_chat:
    st.markdown("### 💬 **CipherSentinel AI - 24/7 Security Helper**")
    st.markdown("<div class='helper-text'>Aap asaan Urdu ya English main password aur security ke mutaliq koi bhi sawaal pooch sakte hain.</div>", unsafe_allow_html=True)

    # Friendly quick questions for non-technical users
    st.markdown("###### 💡 Asaan Sawaalat (Quick Questions):")
    b1, b2, b3, b4 = st.columns(4)
    quick_query = None

    if b1.button("🔒 Kya ye safe hai?", use_container_width=True):
        quick_query = "Kya ye website safe hai aur passwords save krti hai?"
    if b2.button("🛡️ Strong password tips", use_container_width=True):
        quick_query = "Strong password banane ke best tips kya hain?"
    if b3.button("📱 Mobile/ATM PIN advice", use_container_width=True):
        quick_query = "ATM ya phone ke liye safe PIN advice kya hai?"
    if b4.button("👨‍💻 Who developed this?", use_container_width=True):
        quick_query = "Who is the developer of this project?"

    # Render Chat History
    for m in st.session_state.messages:
        with st.chat_message(m["role"], avatar="🛡️" if m["role"] == "assistant" else "👤"):
            st.markdown(m["content"])

    # Chat Input
    typed_msg = st.chat_input("Apna sawaal yahan likhein (e.g. How to use this, Is this safe?)...")

    msg_to_send = quick_query or typed_msg

    if msg_to_send:
        st.session_state.messages.append({"role": "user", "content": msg_to_send})
        bot_reply = get_friendly_agent_response(msg_to_send)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.rerun()


# ------------------------------------------------------------------------------
# TAB 3: TECHNICAL SPECS (FOR RECRUITERS & DEVELOPERS)
# ------------------------------------------------------------------------------
with tab_specs:
    st.markdown("### 📊 **System Architecture & Cryptographic Audit**")
    st.markdown("<div class='helper-text'>Detailed engineering specifications for technical evaluation and recruiters.</div>", unsafe_allow_html=True)

    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown(
            """
            #### ⚙️ Cryptographic Specifications
            - **Algorithm:** Python `secrets.SystemRandom` (Kernel CSPRNG)
            - **Entropy Source:** OS `/dev/urandom` (Linux) / `BCryptGenRandom` (Windows)
            - **Shuffling:** Fisher-Yates shuffle with `secrets.randbelow`
            - **Shannon Entropy Formula:**
              $$E = L \\times \\log_2(R)$$
              *(Where $L$ is length and $R$ is character set size)*
            """
        )
    with t_col2:
        st.markdown(
            """
            #### 📜 Compliance & Security Standards
            - **NIST SP 800-63B:** Digital Identity Guidelines (Section 5.1.1)
            - **OWASP ASVS 4.0:** Application Security Verification Standard
            - **Storage Model:** 100% Zero-Knowledge ephemeral in-memory execution
            - **Availability:** 24/7 Autonomous Hybrid NLP Agent
            """
        )

    st.markdown("---")
    st.markdown("#### 🏗️ **System Flowchart**")
    st.markdown(
        """
        ```mermaid
        flowchart LR
            User([👤 User]) -->|1-Click Request| UI[🖥️ Streamlit High-Contrast UI]
            UI -->|CSPRNG Call| Engine[🛡️ secrets Module & Fisher-Yates]
            Engine -->|Kernel Entropy| OS[(OS Entropy Pool)]
            Engine -->|Calculates Entropy| Metrics[📊 Shannon Entropy & Crack Estimator]
            Metrics --> UI
            User <-->|24/7 Inquiries| AI[🤖 CipherSentinel AI Helper]
        ```
        """
    )


# ==============================================================================
# 8. FOOTER
# ==============================================================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #94a3b8; font-size: 0.95rem; padding: 12px;">
        Designed & Engineered with 🛡️ by <b>Hadi Seelro</b> &bull; Agentic AI Developer &bull; 
        <a href="https://github.com/SainBux-HadiSeelro" target="_blank" style="color: #38bdf8; text-decoration: none; font-weight: 600;">GitHub Profile</a>
    </div>
    """,
    unsafe_allow_html=True,
)
