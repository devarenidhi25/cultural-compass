import streamlit as st


def show_header():
    """Display the app header"""
    st.markdown("""
    <div class="header">
        <h1>Cultural Compass: Discover India's Heritage</h1>
        <p>
            Explore the rich tapestry of India's art, culture, and heritage
            through an interactive journey
        </p>
    </div>
    """, unsafe_allow_html=True)
