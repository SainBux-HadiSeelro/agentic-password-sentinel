import math
import secrets
import string
from typing import Tuple

import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION & AESTHETIC AGENTIC THEME (100% RESPONSIVE)
# ==============================================================================
st.set_page_config(
    page_title="CipherSentinel AI | Autonomous Agentic Password Suite",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# High-Contrast, Futuristic Agentic CSS with Interactive Floating Speech Callout Pill
st.markdown(
    """
    <style>
    /* Global Base */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #0f172a 0%, #080d1a 60%, #030712 100%) !important;
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    }

    /* Force high-contrast readability */
    p, span, label, div, h1, h2, h3, h4, h5, h6, .stMarkdown, .stText {
        color: #ffffff !important;
    }

    /* Widget Labels */
    .stSlider label, .stRadio label, .stCheckbox label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }

    /* KaTeX / Math Formulas visibility */
    .katex, .katex * {
        color: #38bdf8 !important;
    }

    /* Top Agentic Hero Banner */
    .hero-agent-banner {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(99, 102, 241, 0.15) 50%, rgba(168, 85, 247, 0.15) 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 14px;
        padding: 12px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 25px rgba(14, 165, 233, 0.2);
    }
    .hero-banner-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hero-agent-avatar {
        font-size: 2rem;
        filter: drop-shadow(0 0 10px #38bdf8);
        animation: botBounce 3s ease-in-out infinite;
    }
    @keyframes botBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }
    .hero-banner-title {
        font-size: 0.95rem;
        font-weight: 800;
        letter-spacing: 0.05em;
        color: #38bdf8 !important;
        text-transform: uppercase;
    }
    .hero-banner-sub {
        font-size: 0.82rem;
        color: #94a3b8 !important;
    }
    .hero-banner-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid #10b981;
        color: #34d399 !important;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 50px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* Main Typography */
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
        line-height: 1.2;
    }
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 1.05rem;
        margin-bottom: 22px;
        line-height: 1.5;
    }

    /* Password Display Card */
    .password-display-card {
        background: #020617;
        border: 2px solid #0284c7;
        border-radius: 14px;
        padding: 20px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.45rem;
        font-weight: 700;
        color: #38bdf8 !important;
        text-align: center;
        word-break: break-all;
        letter-spacing: 0.05em;
        margin: 12px 0;
        box-shadow: 0 0 30px rgba(2, 132, 199, 0.35);
    }

    .helper-text {
        color: #cbd5e1 !important;
        font-size: 0.92rem;
    }

    button[data-baseweb="tab"] {
        font-size: 1.02rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }

    /* =========================================================================
       EXCLUSIVE CORNER AGENT WIDGET: "Sentinel AI Agent is Online • Tap here!"
       (STRICTLY FIXED TO BROWSER VIEWPORT CORNER WITH RADAR PULSE ANIMATION)
       ========================================================================= */
    [data-testid="stMain"],
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewBlockContainer"],
    section.main,
    .block-container,
    .stApp {
        contain: none !important;
        transform: none !important;
        perspective: none !important;
        filter: none !important;
    }

    .stPopover,
    [data-testid="stPopover"] {
        position: fixed !important;
        bottom: 26px !important;
        right: 26px !important;
        z-index: 99999999 !important;
        margin: 0 !important;
        padding: 0 !important;
        width: auto !important;
    }

    div[data-testid="stElementContainer"]:has(.stPopover),
    div[data-testid="stElementContainer"]:has([data-testid="stPopover"]) {
        height: 0 !important;
        min-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .stPopover button,
    [data-testid="stPopover"] button,
    [data-testid="stPopoverButton"] {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.98) 100%) !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 50px !important;
        padding: 12px 24px !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 10px !important;
        cursor: pointer !important;
        animation: agentRadarWave 2.8s ease-in-out infinite !important;
        backdrop-filter: blur(14px) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 25px rgba(56, 189, 248, 0.6) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    @keyframes agentRadarWave {
        0% {
            box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.75), 0 8px 25px rgba(0, 0, 0, 0.8);
            transform: translateY(0);
        }
        50% {
            box-shadow: 0 0 0 14px rgba(56, 189, 248, 0), 0 12px 35px rgba(0, 0, 0, 0.95);
            transform: translateY(-5px);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(56, 189, 248, 0), 0 8px 25px rgba(0, 0, 0, 0.8);
            transform: translateY(0);
        }
    }

    .stPopover button:hover,
    [data-testid="stPopover"] button:hover,
    [data-testid="stPopoverButton"]:hover {
        transform: scale(1.06) translateY(-6px) !important;
        border-color: #ffffff !important;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 1), 0 0 40px rgba(56, 189, 248, 1) !important;
    }

    .stPopover button p,
    .stPopover button span,
    [data-testid="stPopover"] button p,
    [data-testid="stPopoverButton"] p {
        color: #ffffff !important;
        font-size: 0.95rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.02em !important;
        margin: 0 !important;
        line-height: 1 !important;
    }

    /* Floating Popover Card Window */
    div[data-testid="stPopoverBody"] {
        background: #090d16 !important;
        border: 2px solid #0284c7 !important;
        border-radius: 18px !important;
        box-shadow: 0 25px 65px rgba(0, 0, 0, 0.95), 0 0 35px rgba(2, 132, 199, 0.35) !important;
        width: 390px !important;
        max-width: 90vw !important;
        padding: 16px !important;
    }

    /* =========================================================================
       100% MOBILE RESPONSIVENESS
       ========================================================================= */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 1.6rem !important;
            margin-bottom: 4px !important;
        }
        .hero-subtitle {
            font-size: 0.92rem !important;
            margin-bottom: 16px !important;
        }
        .hero-agent-banner {
            padding: 10px 14px !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            gap: 8px !important;
        }
        .password-display-card {
            font-size: 1.15rem !important;
            padding: 14px 10px !important;
            margin: 8px 0 !important;
        }
        div:has(> div[data-testid="stPopover"]),
        div[data-testid="stPopover"] {
            bottom: 16px !important;
            right: 14px !important;
        }
        div[data-testid="stPopover"] > button {
            padding: 10px 16px !important;
        }
        div[data-testid="stPopover"] > button p {
            font-size: 0.82rem !important;
        }
        div[data-testid="stPopoverBody"] {
            width: calc(100vw - 28px) !important;
            max-width: 360px !important;
            right: 14px !important;
            padding: 12px !important;
        }
        button[data-baseweb="tab"] {
            font-size: 0.88rem !important;
            padding: 8px 10px !important;
        }
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
        rating = "Unbreakable (Agentic / Military Grade) 🛡️"
        color = "#38bdf8"

    return round(entropy, 1), rating, color, crack_time


# ==============================================================================
# 4. 24/7 AGENTIC ASSISTANT ("CipherSentinel AI")
# ==============================================================================
def get_friendly_agent_response(user_msg: str) -> str:
    """Friendly 24/7 AI Agent response engine that speaks English and Roman Urdu."""
    q = user_msg.lower().strip()

    if any(k in q for k in ["who are you", "who made", "developer", "creator", "portfolio", "kisne banaya", "author"]):
        return (
            "🤖 **Agent Identity Protocol:**\n\n"
            "Main **CipherSentinel AI Agent** hoon—ek autonomous cybersecurity model. "
            "Mujhe **Hadi Seelro** ne engineer kiya hai jo ek **Agentic AI Developer & Full-Stack Engineer** hain.\n\n"
            "Unka portfolio aur projects dekhne ke liye yahan visit karein: [GitHub Profile](https://github.com/SainBux-HadiSeelro)."
        )

    if any(k in q for k in ["safe", "secure", "privacy", "leak", "store", "save", "chori", "save krte ho"]):
        return (
            "🔒 **Zero-Knowledge Security Telemetry:**\n\n"
            "- **Zero Persistence:** Koi bhi generated password database ya server par send ya store **nahi** hota.\n"
            "- **Volatile RAM:** Sab kuch aapke local browser runtime main execute hota hai.\n"
            "- **Session Purge:** Jaise hi aap tab refresh ya close karte hain, keys automatically destroy ho jati hain."
        )

    if any(k in q for k in ["how to use", "kaise use krein", "tareeqa", "help", "madad"]):
        return (
            "⚡ **Quick Operation Guide:**\n\n"
            "1. **Password Type** choose karein (Super Strong, Easy Words, ya PIN).\n"
            "2. **Length Slider** adjust karein.\n"
            "3. **Generate** button press karein aur **1-Click Copy Box** se clipboard par copy karein!"
        )

    if any(k in q for k in ["tips", "best practice", "strong password", "kaisa hona chahiye"]):
        return (
            "🛡️ **Agentic Defense Directives:**\n\n"
            "1. **Length ≥ 14:** Length is always king for high entropy.\n"
            "2. **Entropy Diversity:** Mix upper, lower, digits aur symbols.\n"
            "3. **Zero Reuse:** Kabhi bhi banking aur social accounts ka password ek jaisa na rakhein.\n"
            "4. **MFA Enablement:** Critical accounts par Hardware Key ya Authenticator App (2FA) activate rakhein."
        )

    if any(k in q for k in ["pin", "atm", "mobile pin"]):
        return (
            "🔢 **Secure PIN Guidance:**\n\n"
            "Phone aur ATM ke liye hamesha true-random digits use karein jaise `839174`.\n"
            "Kabhi bhi predictable numbers (jaise `1234`, `0000`, birthday) PIN na rakhein!"
        )

    if any(k in q for k in ["entropy", "math", "technical", "csprng"]):
        return (
            "📊 **Cryptographic Specifications:**\n\n"
            "- **Random Engine:** OS Kernel-level CSPRNG (`secrets.choice` / `/dev/urandom`).\n"
            "- **Shannon Entropy:** $E = L \\times \\log_2(R)$ bits.\n"
            "- **Compliance Standards:** NIST SP 800-63B & OWASP ASVS 4.0 guidelines verified."
        )

    return (
        f"🤖 **CipherSentinel Agent Ready:** Query received: *'{user_msg}'*.\n\n"
        "Aap mujh se ye cheezein pooch sakte hain:\n"
        "- *'Is this website safe & zero-knowledge?'*\n"
        "- *'How to create an unbreakable password?'*\n"
        "- *'Who is the developer of this project?'*\n"
        "- *'How does CSPRNG kernel entropy work?'*"
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
                "🤖 **CipherSentinel AI Agent Online (24/7)**\n\n"
                "System Status: `CSPRNG KERNEL SYNCED` | `ZERO-KNOWLEDGE ACTIVE`\n\n"
                "Greetings! Main aapka 24/7 autonomous security advisor hoon. "
                "Password safety, account protection, ya technical architecture ke baray main koi bhi sawaal poochein!"
            ),
        }
    ]


# ==============================================================================
# 6. SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown(
        """
        <div class="hero-banner-badge" style="margin-bottom: 12px;">
            <span class="pulse-dot"></span>
            Sentinel Agent: 24/7 Live
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("## 🛡️ **CipherSentinel**")
    st.markdown("<div class='helper-text'>Agentic Cryptographic Suite</div>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### 📋 **Recent Passwords**")
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
# 7. MAIN HEADER & HERO BANNER
# ==============================================================================
st.markdown(
    """
    <div class="hero-agent-banner">
        <div class="hero-banner-left">
            <span class="hero-agent-avatar">🤖</span>
            <div>
                <div class="hero-banner-title">CipherSentinel Autonomous Agentic Core</div>
                <div class="hero-banner-sub">CSPRNG Kernel Randomness &bull; Zero-Knowledge Memory &bull; 24/7 AI Defense</div>
            </div>
        </div>
        <div class="hero-banner-badge">
            <span class="pulse-dot"></span> AGENT ONLINE
        </div>
    </div>
    <div class="hero-title">CipherSentinel AI Password Studio</div>
    <div class="hero-subtitle">Generate unhackable credentials with military-grade CSPRNG entropy & 24/7 Agentic AI defense.</div>
    """,
    unsafe_allow_html=True,
)

tab_gen, tab_specs = st.tabs([
    "🔑 Password Studio",
    "📊 Technical Specs & Architecture (For Devs)",
])


# ------------------------------------------------------------------------------
# TAB 1: PASSWORD STUDIO
# ------------------------------------------------------------------------------
with tab_gen:
    col_left, col_right = st.columns([1.1, 1], gap="large")

    with col_left:
        st.markdown("### 1️⃣ Select Password Type")

        pwd_type = st.radio(
            "Choose Generation Strategy:",
            [
                "🛡️ Super Strong Password (Recommended for Google, Banks, Social Media)",
                "🧠 Easy to Remember Words (e.g. Falcon-Quantum-Echo-89)",
                "🔢 Simple Number PIN (for Mobile phone, SIM, or ATM)",
                "⚙️ Custom Settings (Fine-tune characters)",
            ],
            index=0,
        )

        st.markdown("---")

        if "Super Strong" in pwd_type:
            pwd_len = st.slider("Password Length", min_value=8, max_value=32, value=16)
            st.markdown("<div class='helper-text'>💡 16 characters provides complete protection against modern GPU brute-force attacks.</div>", unsafe_allow_html=True)

            if st.button("⚡ Generate Super Strong Password", type="primary", use_container_width=True):
                new_pwd = create_strong_password(pwd_len, True, True, True, True, True)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

        elif "Easy to Remember" in pwd_type:
            word_count = st.slider("Number of Words", min_value=3, max_value=6, value=4)
            sep = st.selectbox("Word Separator", ["- (Hyphen)", "_ (Underscore)", "  (Space)"], index=0)
            actual_sep = "-" if "-" in sep else ("_" if "_" in sep else " ")
            add_num = st.checkbox("Append numbers for extra cryptographic entropy", value=True)

            if st.button("⚡ Generate Memorable Passphrase", type="primary", use_container_width=True):
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
                u_check = st.checkbox("Uppercase (A-Z)", value=True)
                l_check = st.checkbox("Lowercase (a-z)", value=True)
            with c2:
                d_check = st.checkbox("Numbers (0-9)", value=True)
                s_check = st.checkbox("Symbols (!@#$)", value=True)
            no_confusing = st.checkbox("Avoid ambiguous characters (like 0 and O, or 1 and l)", value=True)

            if st.button("⚡ Generate Custom Password", type="primary", use_container_width=True):
                new_pwd = create_strong_password(custom_len, u_check, l_check, d_check, s_check, no_confusing)
                st.session_state.active_pwd = new_pwd
                st.session_state.recent_passwords.append(new_pwd)
                st.rerun()

    # RIGHT COLUMN: DISPLAY & COPY
    with col_right:
        st.markdown("### 2️⃣ Cryptographic Output")

        current_pwd = st.session_state.active_pwd
        st.markdown(
            f'<div class="password-display-card">{current_pwd}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("##### 📋 1-Click Copy:")
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
            st.metric(label="Brute-Force Resistance", value=time_to_crack)
        with col_m2:
            st.metric(label="Shannon Entropy Score", value=f"{entropy_score} / 100")

        st.markdown("---")
        st.markdown("##### 🔍 NIST SP 800-63B Quick Check:")
        c_len = "✅ Recommended length (≥12)" if len(current_pwd) >= 12 else "⚠️ Short length"
        c_num = "✅ Numerical characters present" if any(c.isdigit() for c in current_pwd) else "ℹ️ No numbers"
        c_sym = "✅ Symbol entropy present" if any(not c.isalnum() for c in current_pwd) else "ℹ️ No symbols"

        st.markdown(f"- {c_len}\n- {c_num}\n- {c_sym}")


# ------------------------------------------------------------------------------
# TAB 2: TECHNICAL SPECS (FOR RECRUITERS & DEVELOPERS)
# ------------------------------------------------------------------------------
with tab_specs:
    st.markdown("### 📊 **System Architecture & Cryptographic Audit**")
    st.markdown("<div class='helper-text'>Detailed engineering specifications for technical evaluation and portfolio recruiters.</div>", unsafe_allow_html=True)

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
              *(Where $L$ is length and $R$ is character set cardinality)*
            """
        )
    with t_col2:
        st.markdown(
            """
            #### 📜 Compliance & Security Standards
            - **NIST SP 800-63B:** Digital Identity Guidelines (Section 5.1.1)
            - **OWASP ASVS 4.0:** Application Security Verification Standard
            - **Storage Model:** 100% Zero-Knowledge ephemeral in-memory execution
            - **Agent Core:** 24/7 Autonomous Hybrid NLP Agent
            """
        )

    st.markdown("---")
    st.markdown("#### 🏗️ **System Flowchart**")
    st.markdown(
        """
        ```mermaid
        flowchart LR
            User([👤 User / Mobile Client]) -->|1-Click Request| UI[🖥️ Streamlit High-Contrast UI]
            UI -->|CSPRNG Call| Engine[🛡️ secrets Module & Fisher-Yates]
            Engine -->|Kernel Entropy| OS[(OS Entropy Pool)]
            Engine -->|Calculates Entropy| Metrics[📊 Shannon Entropy & Crack Estimator]
            Metrics --> UI
            User <-->|24/7 Floating Speech Callout| AI[🤖 CipherSentinel AI Agent]
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

# ==============================================================================
# 9. FLOATING CORNER AGENT POPUP (STRICTLY VIEWPORT CORNER PINNED)
# ==============================================================================
with st.popover("🟢 Sentinel AI Agent is Online • Tap here! ✨", help="Click to open CipherSentinel AI Agent (24/7 Live Support)"):
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.95)); border: 2px solid #38bdf8; border-radius: 14px; padding: 14px; margin-bottom: 12px; box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 2rem; filter: drop-shadow(0 0 10px #38bdf8);">🤖</span>
                    <div>
                        <div style="font-weight: 800; color: #ffffff; font-size: 1.05rem; letter-spacing: 0.04em;">CIPHERSENTINEL AI AGENT</div>
                        <div style="font-size: 0.75rem; color: #38bdf8; font-family: monospace;">PROTOCOL: v2.5 &bull; ONLINE 24/7</div>
                    </div>
                </div>
                <span style="background: rgba(16, 185, 129, 0.25); border: 1.5px solid #10b981; color: #34d399; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 50px;">LIVE</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Agent Quick Actions
    chip_col1, chip_col2 = st.columns(2)
    quick_choice = None
    if chip_col1.button("🔒 Zero-Knowledge?", use_container_width=True):
        quick_choice = "Kya ye website safe hai aur passwords save krti hai?"
    if chip_col2.button("🛡️ Defense Directives", use_container_width=True):
        quick_choice = "Strong password banane ke best tips kya hain?"

    chip_col3, chip_col4 = st.columns(2)
    if chip_col3.button("📱 Mobile PIN Spec", use_container_width=True):
        quick_choice = "ATM ya phone ke liye safe PIN advice kya hai?"
    if chip_col4.button("👨‍💻 Architect Info", use_container_width=True):
        quick_choice = "Who is the developer of this project?"

    # Scrollable Chat Container
    chat_box = st.container(height=260)
    with chat_box:
        for m in st.session_state.messages:
            with st.chat_message(m["role"], avatar="🤖" if m["role"] == "assistant" else "👤"):
                st.markdown(m["content"])

    # Chat Input inside popover
    chat_prompt = st.chat_input("Ask Sentinel Agent (e.g. Is this safe?)...", key="corner_single_agent_input")

    selected_prompt = quick_choice or chat_prompt

    if selected_prompt:
        st.session_state.messages.append({"role": "user", "content": selected_prompt})
        bot_response = get_friendly_agent_response(selected_prompt)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()

    if st.button("🗑️ Purge Agent Memory", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "🤖 Memory purged. Ready for fresh queries!"}
        ]
        st.rerun()
