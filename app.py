import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="K-Pop Re-Entry Dashboard",
    page_icon="🎵",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

reentry = pd.read_csv("dashboard_data/reentry_frequency.csv")
momentum = pd.read_csv("dashboard_data/momentum_score.csv")
retention = pd.read_csv("dashboard_data/retention_days.csv")
rank_recovery = pd.read_csv("dashboard_data/rank_recovery_speed.csv")
album = pd.read_csv("dashboard_data/album_comeback_advantage.csv")
fandom = pd.read_csv("dashboard_data/fandom_intensity_score.csv")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎵 Dashboard Navigation")

top_n = st.sidebar.selectbox(
    "📊 Top Records",
    [5, 10, 15, 20],
    index=1
)
st.sidebar.success(f"Showing Top {top_n} Records")


page = st.sidebar.radio(
    "Choose Analysis",
    [
        "🏠 Overview",
        "🎵 Re-Entry Analysis",
        "🚀 Momentum Analysis",
        "📈 Retention Analysis",
        "🏆 Rank Recovery Analysis",
        "💿 Album Analysis",
        "🔥 Fandom Analysis"
    ]
)


# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

if page == "🏠 Overview":

    st.markdown("""
    <div style="
    padding:25px;
    border-radius:20px;
    background:linear-gradient(90deg,#6C63FF,#DB2777);
    color:white;
    margin-bottom:20px;
    ">
    <h1 style="
    color:white;
    font-size:58px;
    font-weight:900;
    margin-bottom:10px;
    ">
    🎵 K-Pop Re-Entry Analysis Dashboard
    </h1>

    <p style="font-size:18px;">
    Comeback Momentum, Chart Re-Entry and Fandom Intensity Analysis
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="kpi-card purple-card">
        <h4>🎵 Songs Analyzed</h4>
        <h1>{len(fandom)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card blue-card">
        <h4>📈 Re-Entry Events</h4>
        <h1>{int(reentry['reentry_count'].sum())}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card pink-card">
        <h4>🔥 Top Fandom Score</h4>
        <h1>{round(fandom['fandom_score'].max(),2)}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("📊 Key Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(
             f"🔥 Most Re-Entered Song\n\n{reentry.head(top_n).iloc[0]['song']}"
    )

    with col2:
        st.info(
             f"🚀 Highest Momentum Song\n\n{momentum.head(top_n).iloc[0]['song']}"
    )

    with col3:
       st.warning(
            f"👑 Highest Fandom Song\n\n{fandom.head(top_n).iloc[0]['song']}"
    )

    st.divider()

    st.subheader("📌 Project Overview")
    st.divider()

    st.subheader("🏆 Project Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(f"{len(fandom)} Songs Analysed")

    with c2:
        st.success(
            f"{int(reentry['reentry_count'].sum())} Re-Entry Events"
        )

    with c3:
        st.warning("K-Pop Chart Intelligence Dashboard")

    st.markdown("""
    ### Dashboard Covers

    - Chart Re-Entry Frequency
    - Comeback Momentum
    - Post-Comeback Retention
    - Rank Recovery Speed
    - Album vs Single Advantage
    - Fandom Intensity

    using South Korea's Top 50 Music Charts.
    """)
# --------------------------------------------------
# REENTRY
# --------------------------------------------------

elif page == "🎵 Re-Entry Analysis":

    st.title("🎵 Re-Entry Analysis")

    top_data = reentry.head(top_n)

    fig = px.bar(
        top_data,
        x="reentry_count",
        y="song",
        orientation="h",
        color="reentry_count",
        color_continuous_scale="purples",
        title=f"Top {top_n} Songs by Re-Entry Frequency"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        reentry.head(top_n),
        use_container_width=True
    )

# --------------------------------------------------
# MOMENTUM
# --------------------------------------------------

elif page == "🚀 Momentum Analysis":

    st.title("🚀 Momentum Analysis")

    top_data = momentum.head(top_n)

    fig = px.bar(
        top_data,
        x="momentum_score",
        y="song",
        orientation="h",
        color="momentum_score",
        color_continuous_scale="blues",
        title=f"Top {top_n} Momentum Songs"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        momentum.head(top_n),
        use_container_width=True
    )

# --------------------------------------------------
# RETENTION
# --------------------------------------------------

elif page == "📈 Retention Analysis":

    st.title("📈 Retention Analysis")

    top_data = retention.head(top_n)

    fig = px.bar(
        top_data,
        x="retention_days",
        y="song",
        orientation="h",
        color="retention_days",
        color_continuous_scale="greens",
        title=f"Top {top_n} Songs by Retention"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        retention.head(top_n),
        use_container_width=True
    )

# --------------------------------------------------
# RANK RECOVERY
# --------------------------------------------------

elif page == "🏆 Rank Recovery Analysis":

    st.title("🏆 Rank Recovery Analysis")

    top_data = rank_recovery.head(top_n)

    fig = px.bar(
        top_data,
        x="rank_recovery_speed",
        y="song",
        orientation="h",
        color="rank_recovery_speed",
        color_continuous_scale="tealgrn",
        title=f"Top {top_n} Rank Recovery Songs"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        rank_recovery.head(top_n),
        use_container_width=True
    )

# --------------------------------------------------
# ALBUM ANALYSIS
# --------------------------------------------------

elif page == "💿 Album Analysis":

    st.title("💿 Album Analysis")

    fig = px.bar(
        album,
        x="album_type",
        y="avg_popularity",
        color="album_type",
        title="Album Type vs Popularity"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        album,
        use_container_width=True
    )

# --------------------------------------------------
# FANDOM ANALYSIS
# --------------------------------------------------

elif page == "🔥 Fandom Analysis":

    st.title("🔥 Fandom Intensity Analysis")

    top_data = fandom.head(top_n)

    fig = px.bar(
        top_data,
        x="fandom_score",
        y="song",
        orientation="h",
        color="fandom_score",
        color_continuous_scale="sunset",
        title=f"Top {top_n} Fandom Scores"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        fandom.head(top_n),
        use_container_width=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">
<h3>🎵 K-Pop Re-Entry Analysis Dashboard</h3>
<p>Developed by Sudheer Reddy</p>
<p>Unified Mentor Internship Project</p>
</div>
""", unsafe_allow_html=True)