import streamlit as st
import pandas as pd

# Pages
from pages.map_explorer import show_map_explorer
from pages.cultural_calendar import show_cultural_calendar
from pages.trend_dashboard import show_trend_dashboard
from pages.story_cards import show_story_cards
from pages.sustainability_tips import show_sustainability_tips

# Components
from components.header import show_header
from components.hero import show_hero
from components.stats_section import show_stats_section
from components.featured_destinations import show_featured_destinations
from components.sidebar import show_sidebar
from components.footer import show_footer

# Utilities
from utils.styles import load_css, toggle_dark_mode
from utils.data_loader import load_all_data, get_heritage_sites_data, load_enhanced_heritage_sites

# Page config
st.set_page_config(
    page_title="Cultural Compass: Discover India's Heritage",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css()

# Load data (static + dynamic)
data = load_all_data()
# Load enhanced heritage CSV
data["enhanced_heritage_sites"] = load_enhanced_heritage_sites()

# Load heritage sites dynamically from Snowflake
data["heritage_sites"] = get_heritage_sites_data()
# Normalize column names to lowercase to avoid KeyError issues
data["heritage_sites"].columns = data["heritage_sites"].columns.str.lower()
data["cultural_events"].columns = data["cultural_events"].columns.str.lower()


# Sidebar: Dark mode toggle + page navigation
with st.sidebar:
    dark_mode = st.checkbox("Dark Mode", value=False)
    toggle_dark_mode(dark_mode)

    # Page navigation radio button
    page = st.radio(
        "Navigate",
        [
            "Map Explorer",
            "Cultural Calendar",
            "Trend Dashboard",
            "Story Cards",
            "Sustainability Tips"
        ]
    )

    show_sidebar(data)

# Main content
show_header()
show_hero()
show_stats_section()
show_featured_destinations(data["featured_destinations"])

# Debug info - can remove or comment out in production
if "heritage_sites" not in data:
    st.error("❌ 'heritage_sites' key is missing from data!")
    st.stop()

if data["heritage_sites"] is None:
    st.error("❌ 'heritage_sites' is None!")
    st.stop()

if not isinstance(data["heritage_sites"], pd.DataFrame):
    st.error("❌ 'heritage_sites' is not a DataFrame!")
    st.write(data["heritage_sites"])
    st.stop()

st.write("Loaded data keys:", list(data.keys()))
st.write("Heritage Sites Preview:", data.get("heritage_sites", "Not Found"))

# Show selected page content
if page == "Map Explorer":
    if data and "heritage_sites" in data:
        show_map_explorer(data["heritage_sites"])
    else:
        st.error(
            "Heritage sites data not found. Available keys: " +
            str(list(data.keys()) if data else "No data loaded.")
        )

elif page == "Cultural Calendar":
    cultural_events = data["cultural_events"]
    if isinstance(cultural_events, list):
        cultural_events = pd.DataFrame(cultural_events)

    if 'date' in cultural_events.columns:
        cultural_events['date'] = pd.to_datetime(
            cultural_events['date'], errors='coerce'
        )
    show_cultural_calendar(cultural_events)

elif page == "Trend Dashboard":
    show_trend_dashboard(
        data["yearly_trends"],
        data["monthly_trends"],
        data["demographics"],
        data["origin"],
        data["purpose"],
        data["spending"],
        data["enhanced_heritage_sites"]  # ✅ Pass enhanced dataset
    )


elif page == "Story Cards":
    show_story_cards(data["art_forms"])

elif page == "Sustainability Tips":
    show_sustainability_tips(data["sustainability_tips"])

# Footer
show_footer()
