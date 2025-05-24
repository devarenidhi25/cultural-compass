import streamlit as st
import time

def show_stats_section():
    """Display the key statistics section with animated counters"""
    st.markdown("<h2>India's Cultural Heritage at a Glance</h2>", unsafe_allow_html=True)
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    # Create placeholders for the stats
    with stats_col1:
        stats_1 = st.empty()
    
    with stats_col2:
        stats_2 = st.empty()
    
    with stats_col3:
        stats_3 = st.empty()
    
    with stats_col4:
        stats_4 = st.empty()
    
    # Animate the counters
    for i in range(0, 41, 2):  # UNESCO Sites (40)
        stats_1.markdown(f"""
        <div class="stats-card counter-animation">
            <div class="stats-number">{i}</div>
            <div class="stats-label">UNESCO World Heritage Sites</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)
    
    for i in range(0, 1001, 50):  # Festivals (1000+)
        stats_2.markdown(f"""
        <div class="stats-card counter-animation">
            <div class="stats-number">{i}+</div>
            <div class="stats-label">Cultural Festivals</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)
    
    for i in range(0, 3001, 150):  # Years of Civilization (3000+)
        stats_3.markdown(f"""
        <div class="stats-card counter-animation">
            <div class="stats-number">{i}+</div>
            <div class="stats-label">Years of Civilization</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)
    
    for i in range(0, 23, 1):  # Official Languages (22)
        stats_4.markdown(f"""
        <div class="stats-card counter-animation">
            <div class="stats-number">{i}</div>
            <div class="stats-label">Official Languages</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)
