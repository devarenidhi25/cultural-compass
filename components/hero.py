import streamlit as st


def show_hero():
    st.image("images/heritage_hero.jpg", use_container_width=True, caption="Discover India's Cultural Tapestry")
    st.markdown("""
    <div style="text-align: center; margin-top: -20px;">
        <h1>Discover India's Cultural Tapestry</h1>
        <p>Explore ancient traditions, vibrant festivals, and hidden cultural gems across the subcontinent</p>
        <a href="#" style="display: inline-block; background-color: #FF4B4B; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Start Exploring</a>
    </div>
    """, unsafe_allow_html=True)
