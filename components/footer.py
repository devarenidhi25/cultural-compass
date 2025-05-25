import streamlit as st


def show_footer():
    """Display the footer"""
    st.markdown("""
    <div style="background-color: #1A3A5A; padding: 2rem; border-radius: 15px;
                margin-top: 2rem; color: white; text-align: center;">
        <h3 style="color: white;">
                Cultural Compass: Discover India's Heritage</h3>
        <p>Explore, Experience, and Preserve India's Cultural Legacy</p>
        <div style="display: flex;
                justify-content: center; gap: 20px; margin: 20px 0;">
            <a href="#" style="color: white;
                text-decoration: none;">About</a>
            <a href="#" style="color: white;
                text-decoration: none;">Contact</a>
            <a href="#" style="color: white;
                text-decoration: none;">Privacy Policy</a>
            <a href="#" style="color: white;
                text-decoration: none;">Terms of Use</a>
        </div>
        <p style="font-size: 0.9rem;">
                Created with ❤️ for promoting sustainable tourism and cultural
                preservation</p>
        <p style="font-size: 0.8rem;">
                © 2025 Cultural Compass. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)
