import streamlit as st


def load_css():
    """Load custom CSS for styling"""
    st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --saffron: #FF9933;
        --teal: #218380;
        --earth: #A67C52;
        --gold: #D4AF37;
        --navy: #1A3A5A;
        --light: #F8F8F8;
        --dark: #333333;

        /* Light mode colors */
        --background: var(--light);
        --text-color: var(--dark);
        --card-bg: white;
                --header-bg: linear-gradient(135deg, var(--saffron) 0%, \
        var(--teal) 100%);
        --header-text: white;
        --border-color: rgba(0,0,0,0.1);
        --hover-bg: rgba(0,0,0,0.05);
    }

    /* Dark mode colors */
    .dark-mode {
        --background: #121212;
        --text-color: #E0E0E0;
        --card-bg: #1E1E1E;
        --header-bg: linear-gradient(135deg, #B36B23 0%, #155957 100%);
        --header-text: #F0F0F0;
        --border-color: rgba(255,255,255,0.1);
        --hover-bg: rgba(255,255,255,0.05);
    }

    /* Base styling */
    .main {
        background-color: var(--background);
        color: var(--text-color);
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
    }

    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: var(--navy);
        font-weight: 600;
    }

    /* Header styling */
    .header {
        padding: 2rem;
        background: var(--header-bg);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: var(--header-text);
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }

    .header h1 {
        color: var(--header-text);
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

    .header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    /* Card styling */
    .card {
        color: black;
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid var(--border-color);
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }

    /* Story card styling */
    .story-card {
        height: 100%;
        overflow: hidden;
        position: relative;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        background-color: var(--card-bg);
        margin-bottom: 1.5rem;
    }
    .story-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }

    .story-card img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 15px 15px 0 0;
        transition: transform 0.5s ease;
    }

    .story-card:hover img {
        transform: scale(1.05);
    }

    .story-content {
        padding: 1.5rem;
        background-color: var(--card-bg);
        color: var(--text-color);
    }

    .story-title {
        font-weight: bold;
        color: var(--navy);
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
    }

    .story-region {
        color: var(--teal);
        font-size: 0.9rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
    }

    .story-region:before {
        content: '';
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: var(--teal);
        border-radius: 50%;
        margin-right: 8px;
    }

    .story-desc {
        font-size: 0.95rem;
        color: var(--text-color);
        line-height: 1.6;
    }

    /* Calendar styling */
    .calendar-card {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid var(--border-color);
    }

    .calendar-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }

    .calendar-date {
        background-color: var(--saffron);
        color: white;
        padding: 0.7rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
        font-size: 1.1rem;
        box-shadow: 0 4px 10px rgba(255, 153, 51, 0.3);
    }

    .calendar-content {
        flex-grow: 1;
    }

    .calendar-content h4 {
        color: var(--navy);
        margin-bottom: 0.8rem;
        font-size: 1.2rem;
    }

    /* Google Calendar style */
    .google-calendar {
        background-color: var(--card-bg);
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .calendar-header {
        background-color: var(--teal);
        color: black;
        padding: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .calendar-title {
        font-size: 1.2rem;
        font-weight: 500;
    }

    .calendar-nav {
        display: flex;
        gap: 10px;
    }

    .calendar-nav button {
        background: rgba(255,255,255,0.2);
        border: none;
        color: white;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: background 0.3s;
    }

    .calendar-nav button:hover {
        background: rgba(255,255,255,0.3);
    }

    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        border-bottom: 1px solid var(--border-color);
    }

    .calendar-day-header {
        padding: 10px;
        text-align: center;
        font-weight: 500;
        color: var(--text-color);
        border-bottom: 1px solid var(--border-color);
    }

    .calendar-day {
        min-height: 100px;
        padding: 8px;
        border-right: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        position: relative;
    }

    .calendar-day:nth-child(7n) {
        border-right: none;
    }

    .day-number {
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 5px;
        color: #333;
    }

    .calendar-event {
        background-color: #4285F4;
        color: white;
        padding: 3px 6px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-bottom: 4px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        cursor: pointer;
    }

    .calendar-event.cultural {
        background-color: #4285F4;
    }

    .calendar-event.religious {
        background-color: #EA4335;
    }

    .calendar-event.music {
        background-color: #FBBC05;
    }

    .calendar-event.harvest {
        background-color: #34A853;
    }

    .calendar-event.art {
        background-color: #8E24AA;
    }

    .calendar-event:hover {
        opacity: 0.9;
    }

    .calendar-day.today {
        background-color: rgba(66, 133, 244, 0.1);
    }

    .calendar-day.different-month {
        background-color: var(--hover-bg);
    }

    .calendar-day.different-month .day-number {
        opacity: 0.5;
    }

    /* Sustainability tip styling */
    .tip-card {
        color: black;
        background-color: #E8F4F4;
        border-left: 5px solid var(--teal);
        padding: 1.5rem;
        border-radius: 0 15px 15px 0;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }

    .tip-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    }

    .tip-title {
        color: var(--teal);
        font-weight: bold;
        margin-bottom: 0.8rem;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
    }

    .tip-title i {
        margin-right: 10px;
        font-size: 1.2rem;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--card-bg);
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }

    .stTabs [data-baseweb="tab"] {
        background-color: var(--card-bg);
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-weight: 500;
        color: var(--navy);
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--saffron) !important;
        color: white !important;
        box-shadow: 0 4px 10px rgba(255, 153, 51, 0.3);
    }

    /* Button styling */
    .stButton button {
        background-color: var(--teal);
        color: white;
        border-radius: 30px;
        padding: 0.6rem 1.5rem;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(33, 131, 128, 0.3);
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: var(--navy);
        box-shadow: 0 6px 15px rgba(26, 58, 90, 0.3);
        transform: translateY(-2px);
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: var(--card-bg);
        border-radius: 15px;
        color: var(--text-color);
    }

    /* Featured section styling */
    .featured-section {
        color: black;
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    }

    .dark-mode .featured-section {
        background: linear-gradient(135deg, #2A2A2A 0%, #1A1A1A 100%);
    }

    .featured-title {
        color: var(--navy);
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 600;
        display: flex;
        align-items: center;
    }

    .featured-title:before {
        content: '';
        display: inline-block;
        width: 15px;
        height: 15px;
        background-color: var(--saffron);
        border-radius: 50%;
        margin-right: 10px;
    }

    /* Stats card styling */
    .stats-card {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .stats-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }

    .stats-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: var(--teal);
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        color: var(--text-color);
        font-size: 1rem;
    }
    
    /* Testimonial styling */
    .testimonial {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        position: relative;
        color: var(--text-color);
    }
    
    .testimonial:before {
        content: '"';
        position: absolute;
        top: 10px;
        left: 15px;
        font-size: 4rem;
        color: rgba(33, 131, 128, 0.1);
        font-family: Georgia, serif;
    }
    
    .testimonial-content {
        padding-left: 1.5rem;
        font-style: italic;
        color: var(--text-color);
        line-height: 1.6;
    }
    
    .testimonial-author {
        margin-top: 1rem;
        font-weight: bold;
        color: var(--navy);
        display: flex;
        align-items: center;
    }
    
    .testimonial-author:before {
        content: '—';
        margin-right: 0.5rem;
        color: var(--teal);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .story-card img {
            height: 180px;
        }
        
        .card {
            padding: 1.2rem;
        }
        
        .header h1 {
            font-size: 1.8rem;
        }
        
        .header p {
            font-size: 1rem;
        }
        
        .stats-number {
            font-size: 2rem;
        }
    }
    
    /* Animation for elements */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.6s ease forwards;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--background);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--teal);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--navy);
    }
    
    /* Tooltip styling */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: var(--navy);
        color: white;
        text-align: center;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        font-size: 0.9rem;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .badge-primary {
        background-color: var(--teal);
        color: white;
    }
    
    .badge-secondary {
        background-color: var(--saffron);
        color: white;
    }
    
    .badge-tertiary {
        background-color: var(--navy);
        color: white;
    }
    
    .badge-light {
        background-color: #e9ecef;
        color: var(--navy);
    }
    
    /* Hero section */
    .hero-section {
        position: relative;
        height: 400px;
        border-radius: 15px;
        overflow: hidden;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    
    .hero-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 3rem;
    }

    .hero-title {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    .hero-subtitle {
        color: white;
        font-size: 1.5rem;
        max-width: 600px;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }

    .hero-button {
        display: inline-block;
        background-color: var(--saffron);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 30px;
        font-weight: bold;
        text-decoration: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

    .hero-button:hover {
        background-color: var(--teal);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }

    /* Feature box */
    .feature-box {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        color: var(--text-color);
    }

    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }

    .feature-icon {
        font-size: 2.5rem;
        color: var(--teal);
        margin-bottom: 1rem;
    }

    .feature-title {
        color: var(--navy);
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    .feature-text {
        color: var(--text-color);
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Map styling */
    .map-container {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Dark mode toggle */
    .dark-mode-toggle {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        padding: 0.5rem;
        border-radius: 10px;
        background-color: var(--card-bg);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .dark-mode-toggle label {
        margin-left: 0.5rem;
        color: var(--text-color);
        font-weight: 500;
    }

    /* Counter animation for stats */
    @keyframes countUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .counter-animation {
        animation: countUp 1s ease-out forwards;
    }
    </style>
    """, unsafe_allow_html=True)


def toggle_dark_mode(enable=False):
    """Toggle dark mode by adding or removing the dark-mode class"""
    if enable:
        st.markdown("""
        <script>
        document.body.classList.add('dark-mode');
        </script>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <script>
        document.body.classList.remove('dark-mode');
        </script>
        """, unsafe_allow_html=True)
