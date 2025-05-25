import streamlit as st
import snowflake.connector
import pandas as pd
import numpy as np


@st.cache_data(ttl=3600)
def get_heritage_sites_data():
    try:
        conn = snowflake.connector.connect(
            user=st.secrets["snowflake"]["user"],
            password=st.secrets["snowflake"]["password"],
            account=st.secrets["snowflake"]["account"],
            warehouse=st.secrets["snowflake"]["warehouse"],
            database=st.secrets["snowflake"]["database"],
            schema=st.secrets["snowflake"]["schema"]
        )
        cs = conn.cursor()

        query = """
        SELECT
            C1 AS state,
            C2 AS site_name,
            C3 AS category,
            C4 AS year_built,
            C5 AS visitors_per_year,
            C6 AS popularity,
            C7 AS best_month_to_visit,
            C8 AS unesco_status,
            C13 AS entry_fee,
            C14 AS description,
            C15 AS festival,
            C16 AS famous_art,
            C9 AS latitude,
            C10 AS longitude
        FROM VISITORS
        """
        cs.execute(query)
        results = cs.fetchall()
        columns = [desc[0] for desc in cs.description]
        df = pd.DataFrame(results, columns=columns)
        df.columns = [c.lower() for c in df.columns]

        # Clean up coordinates immediately
        df["Latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
        df["Longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
        df["Visitors_Per_Year"] = pd.to_numeric(df["Visitors_Per_Year"], errors="coerce")

        if df.empty:
            st.warning("⚠️ No data fetched from Snowflake VISITORS table. Using fallback CSV.")
            df = pd.read_csv("indian_heritage_sites_extended.csv")

        return df

    except Exception as e:
        st.error(f"❌ Snowflake error: {e}")
        st.warning("⚠️ Using fallback CSV instead.")
        try:
            return pd.read_csv("indian_heritage_sites_extended.csv")
        except Exception as file_error:
            st.error(f"❌ Failed to load fallback CSV: {file_error}")
            return pd.DataFrame()

    finally:
        try:
            cs.close()
            conn.close()
        except Exception:
            pass


@st.cache_data
def load_heritage_sites():
    # Sample data for heritage sites
    data = {
        'name': [
            'Hampi', 'Majuli Island', 'Chettinad', 'Khajuraho', 'Ziro Valley',
            'Shekhawati', 'Champaner', 'Orchha', 'Unakoti', 'Lepakshi',
            'Kumbhalgarh', 'Dhanushkodi', 'Mawlynnong', 'Spiti Valley', 'Tawang'
        ],
        'state': [
            'Karnataka', 'Assam', 'Tamil Nadu', 'Madhya Pradesh', 'Arunachal Pradesh',
            'Rajasthan', 'Gujarat', 'Madhya Pradesh', 'Tripura', 'Andhra Pradesh',
            'Rajasthan', 'Tamil Nadu', 'Meghalaya', 'Himachal Pradesh', 'Arunachal Pradesh'
        ],
        'category': [
            'Architecture', 'Cultural Landscape', 'Heritage', 'Architecture', 'Tribal Culture',
            'Frescoes', 'Architecture', 'Architecture', 'Rock Carvings', 'Temple',
            'Fort', 'Ghost Town', 'Clean Village', 'Monastery', 'Monastery'
        ],
        'visitors': [
            150000, 20000, 35000, 200000, 15000,
            25000, 45000, 120000, 10000, 50000,
            80000, 30000, 25000, 40000, 35000
        ],
        'lat': [
            15.3350, 26.9524, 10.5434, 24.8318, 27.6374,
            27.6147, 22.4866, 25.3518, 24.3130, 13.8079,
            25.1539, 9.1550, 25.3015, 32.2460, 27.5859
        ],
        'lon': [
            76.4600, 94.1756, 78.8267, 79.9199, 93.8316,
            75.1398, 73.5166, 78.6412, 91.8956, 77.6152,
            73.5861, 79.4183, 91.5811, 78.0349, 91.8594
        ],
        'popularity': [
            'Medium', 'Low', 'Low', 'High', 'Low',
            'Low', 'Medium', 'Medium', 'Low', 'Medium',
            'Medium', 'Low', 'Low', 'Medium', 'Medium'
        ],
        'description': [
            'Ancient ruins of Vijayanagara Empire with stunning temples and monuments.',
            'World\'s largest river island with unique Assamese culture and Vaishnavite monasteries.',
            'Region known for palatial mansions of the Chettiar community with unique architecture.',
            'Famous for exquisitely carved temples with erotic sculptures from 950-1050 CE.',
            'Home to the Apatani tribe with distinctive cultural practices and beautiful landscapes.',
            'Open-air art gallery with painted havelis featuring colorful frescoes.',
            'UNESCO World Heritage site with pre-Mughal Islamic architecture.',
            'Medieval city with grand palaces, temples, and cenotaphs by the Betwa River.',
            'Ancient Shaivite pilgrimage site with massive rock-cut sculptures.',
            'Temple complex with magnificent sculptures, paintings, and architectural marvels.',
            'Second longest wall in the world after the Great Wall of China, with impressive fortifications.',
            'Abandoned town at the tip of Rameswaram Island with ruins and pristine beaches.',
            'Known as the cleanest village in Asia with unique living root bridges.',
            'Cold desert mountain valley with ancient Buddhist monasteries and stunning landscapes.',
            'Home to the 400-year-old Tawang Monastery, the largest in India and second largest in the world.'
        ],
        'best_time': [
            'October to March', 'November to March', 'December to March', 'October to March', 'March to October',
            'October to March', 'November to February', 'October to March', 'October to March', 'November to February',
            'October to March', 'October to May', 'September to May', 'June to September', 'March to October'
        ],
        'unesco_status': [
            'World Heritage Site', 'None', 'None', 'World Heritage Site', 'None',
            'Tentative List', 'World Heritage Site', 'Tentative List', 'None', 'None',
            'World Heritage Site', 'None', 'None', 'None', 'None'
        ],
        'activities': [
            'Temple Tours, Coracle Rides, Rock Climbing', 'Cultural Performances, Boat Rides, Birdwatching',
            'Heritage Walks, Mansion Tours, Culinary Experiences', 'Temple Tours, Light & Sound Show, Nature Walks',
            'Tribal Village Tours, Trekking, Photography', 'Haveli Tours, Fresco Viewing, Heritage Walks',
            'Archaeological Exploration, Photography, Hiking', 'Palace Tours, River Rafting, Bird Sanctuary Visit',
            'Rock Carving Tours, Trekking, Photography', 'Temple Tours, Art Appreciation, Village Walks',
            'Fort Tours, Wall Hikes, Sunset Viewing', 'Ghost Town Exploration, Beach Walks, Photography',
            'Village Tours, Root Bridge Walks, Waterfall Visits', 'Monastery Visits, Trekking, Stargazing',
            'Monastery Tours, Lake Visits, Mountain Trekking'
        ]
    }
    return pd.DataFrame(data)


@st.cache_data
def load_cultural_events():
    # Sample data for cultural events
    data = {
        'name': [
            'Hornbill Festival', 'Pushkar Camel Fair', 'Hemis Festival', 'Onam', 'Bihu',
            'Ziro Music Festival', 'Kumbh Mela', 'Rann Utsav', 'Konark Dance Festival', 'Pongal',
            'Jaisalmer Desert Festival', 'Khajuraho Dance Festival', 'Holi in Mathura', 'Thrissur Pooram',
            'Losar Festival', 'Ganesh Chaturthi in Mumbai', 'Durga Puja in Kolkata', 'Diwali in Varanasi',
            'Hampi Utsav', 'Sangai Festival',
            'Mysuru Dasara', 'Lathmar Holi Barsana', 'Teej Festival', 'Nagaur Fair', 'Chapchar Kut',
            'Chithirai Festival', 'Surajkund Mela', 'Desi Mahotsav', 'Bhakti Festival', 'Rath Yatra',
            # New 10 events
            'Bastar Dussehra', 'Karni Mata Festival', 'Meenakshi Tirukalyanam', 'Thrissur Pooram', 'Vibrant Gujarat',
            'Magh Bihu', 'Phool Dei Festival', 'Chapchar Kut', 'Gangaur Festival', 'Tarnetar Fair'
        ],
        'state': [
            'Nagaland', 'Rajasthan', 'Ladakh', 'Kerala', 'Assam',
            'Arunachal Pradesh', 'Uttar Pradesh', 'Gujarat', 'Odisha', 'Tamil Nadu',
            'Rajasthan', 'Madhya Pradesh', 'Uttar Pradesh', 'Kerala',
            'Sikkim', 'Maharashtra', 'West Bengal', 'Uttar Pradesh',
            'Karnataka', 'Manipur',
            'Karnataka', 'Uttar Pradesh', 'Rajasthan', 'Rajasthan', 'Mizoram',
            'Tamil Nadu', 'Haryana', 'Delhi', 'Maharashtra', 'Odisha',
            # Added states
            'Chhattisgarh', 'Rajasthan', 'Tamil Nadu', 'Kerala', 'Gujarat',
            'Assam', 'Uttarakhand', 'Mizoram', 'Rajasthan', 'Gujarat'
        ],
        'month': [
            'December', 'November', 'July', 'August', 'April',
            'September', 'January', 'December', 'December', 'January',
            'February', 'February', 'March', 'April',
            'February', 'September', 'October', 'November',
            'November', 'November',
            'October', 'March', 'August', 'January', 'March',
            'April', 'February', 'November', 'November', 'July',
            # Added months
            'October', 'March', 'April', 'April', 'January',
            'January', 'March', 'March', 'March', 'August'
        ],
        'date': [
            '2023-12-01', '2023-11-15', '2023-07-10', '2023-08-20', '2023-04-14',
            '2023-09-22', '2024-01-15', '2023-12-10', '2023-12-01', '2024-01-14',
            '2024-02-05', '2024-02-20', '2024-03-25', '2024-04-15',
            '2024-02-10', '2023-09-19', '2023-10-20', '2023-11-12',
            '2023-11-03', '2023-11-21',
            '2023-10-05', '2024-03-17', '2023-08-01', '2024-01-10', '2024-03-15',
            '2024-04-10', '2024-02-15', '2023-11-25', '2023-11-10', '2023-07-10',
            # Added dates
            '2023-10-12', '2024-03-21', '2024-04-15', '2024-04-15', '2024-01-15',
            '2024-01-14', '2024-03-05', '2024-03-18', '2024-03-22', '2024-08-10'
        ],
        'description': [
            'Celebrates the heritage of Naga tribes with music, dance, and traditional games.',
            'Vibrant fair featuring camel trading, folk performances, and cultural activities.',
            'Colorful Buddhist festival with masked dances at Hemis Monastery.',
            'Harvest festival with elaborate feasts, boat races, and floral decorations.',
            'Assamese New Year celebration with traditional dance, music, and feasts.',
            'Outdoor music festival showcasing indie artists against scenic backdrop.',
            'World\'s largest religious gathering with ritual bathing in sacred rivers.',
            'Cultural festival in the white desert with folk performances and crafts.',
            'Classical dance festival against the backdrop of the Sun Temple.',
            'Tamil harvest festival with traditional rituals and feasts.',
            'Colorful desert festival with camel races, folk performances, and turban tying competitions.',
            'Celebration of classical Indian dances against the backdrop of magnificent temples.',
            'Experience the most vibrant Holi celebrations in the birthplace of Lord Krishna.',
            'Spectacular temple festival with decorated elephants, percussion ensembles, and fireworks.',
            'Tibetan New Year celebrations with masked dances, prayer ceremonies, and feasts.',
            'Mumbai\'s biggest festival with elaborate Ganesh idols, processions, and community celebrations.',
            'Bengal\'s grand festival with artistic pandals, cultural performances, and community feasts.',
            'Experience the Festival of Lights along the sacred ghats of Varanasi with thousands of lamps.',
            'Cultural extravaganza celebrating the glory of the Vijayanagara Empire with music and dance.',
            'Manipur\'s largest festival showcasing the state\'s rich cultural heritage and biodiversity.',
            'Royal celebration of the victory of good over evil with processions and cultural events.',
            'Traditional Holi celebrations with women playfully hitting men with sticks.',
            'Festival celebrating the monsoon with prayers for marital bliss and prosperity.',
            'One of the largest cattle fairs showcasing livestock trading and folk events.',
            'Spring festival marking the end of winter with traditional dances and feasts.',
            'Celebrates the coronation of Goddess Meenakshi with processions and rituals.',
            'Annual crafts fair displaying regional handicrafts, handlooms, and folk art.',
            'Cultural festival promoting folk music, dance, and regional cuisine.',
            'Devotional music festival featuring Bhakti and Sufi performances.',
            'Massive chariot procession of Lord Jagannath, a grand religious spectacle.',
            # New descriptions
            'A unique Dussehra celebration featuring local tribal rituals and cultural performances in Bastar.',
            'Festival honoring the Karni Mata goddess with rat worship and grand rituals.',
            'Grand temple wedding reenactment of Goddess Meenakshi and Lord Sundareswarar.',
            'Famous temple festival known for its elephant processions and vibrant percussion ensembles.',
            'Large-scale business and cultural event promoting investment and Gujarat\'s heritage.',
            'Traditional Assamese harvest festival celebrated with feasts and community bonfires.',
            'Uttarakhand’s spring festival with traditional dances, songs, and the welcoming of the harvest.',
            'Mizoram’s traditional festival celebrating the end of winter with folk music and dance.',
            'Rajasthan’s festival dedicated to Gauri (Parvati) involving folk dances and rituals for marital happiness.',
            'Folk festival with traditional wrestling, cultural shows, and a pilgrimage fair in Gujarat.'
        ],
        'image_url': [
            'hornbill.jpg', 'pushkar.jpg', 'hemis.jpg', 'onam.jpg', 'bihu.jpg',
            'ziro.jpg', 'kumbh.jpg', 'rann.jpg', 'konark.jpg', 'pongal.jpg',
            'jaisalmer.jpg', 'khajuraho_dance.jpg', 'holi.jpg', 'thrissur.jpg',
            'losar.jpg', 'ganesh.jpg', 'durga.jpg', 'diwali.jpg',
            'hampi_utsav.jpg', 'sangai.jpg',
            'mysuru_dasara.jpg', 'lathmar_holi.jpg', 'teej.jpg', 'nagaur_fair.jpg', 'chapchar_kut.jpg',
            'chithirai.jpg', 'surajkund.jpg', 'desi_mahotsav.jpg', 'bhakti_festival.jpg', 'rath_yatra.jpg',
            # New images
            'bastar_dussehra.jpg', 'karni_mata.jpg', 'meenakshi_tirukalyanam.jpg', 'thrissur_pooram2.jpg', 'vibrant_gujarat.jpg',
            'magh_bihu.jpg', 'phool_dei.jpg', 'chapchar_kut2.jpg', 'gangaur.jpg', 'tarnetar_fair.jpg'
        ],
        'duration': [
            '10 days', '8 days', '2 days', '10 days', '3 days',
            '4 days', '48 days', '4 months', '5 days', '4 days',
            '3 days', '7 days', '2 days', '36 hours',
            '15 days', '11 days', '10 days', '5 days',
            '3 days', '10 days',
            '10 days', '4 days', '3 days', '7 days', '3 days',
            '15 days', '15 days', '5 days', '3 days', '9 days',
            # New durations
            '9 days', '5 days', '1 day', '36 hours', '5 days',
            '3 days', '3 days', '3 days', '7 days', '4 days'
        ],
        'highlights': [
            'Tribal dances, Morungs (traditional huts), indigenous games, food festival',
            'Camel trading, folk music, bridal competition, longest moustache competition',
            'Masked dances, prayer ceremonies, thangka exhibitions, monastic music',
            'Snake boat races, Pookalam (floral carpets), Onam Sadya (feast), Pulikali (tiger dance)',
            'Bihu dance, community feasts, buffalo fights, egg fights, traditional games',
            'Live music performances, camping, tribal food, bamboo workshops',
            'Ritual bathing, religious discourses, processions, cultural performances',
            'Full moon nights, folk dances, camel safaris, handicraft bazaar, white desert camping',
            'Odissi, Bharatanatyam, Kathak, Manipuri, and other classical dance performances',
            'Kolam (rangoli), Jallikattu (bull taming), cooking Pongal, bonfire celebrations',
            'Camel races, turban tying competitions, Mr. Desert competition, folk performances',
            'Classical dance performances, light and sound show, craft fair, heritage walks',
            'Lathmar Holi, Widow\'s Holi, flower Holi, processions, traditional sweets',
            'Elephant processions, Panchavadyam (percussion ensemble), Elanjithara Melam, fireworks',
            'Masked dances, prayer flags, butter sculptures, monastic rituals, community feasts',
            'Idol installations, aartis, processions, community feasts, cultural performances',
            'Themed pandals, dhunuchi dance, sindoor khela, cultural performances, community feasts',
            'Ganga Aarti, Dev Deepawali, floating diyas, fireworks, cultural performances',
            'Processions, music and dance performances, puppet shows, craft exhibitions',
            'Cultural performances, indigenous sports, fashion shows, boat races, polo matches',
            'Royal processions, torchlight parades, cultural dances, heritage exhibitions',
            'Stick fights, traditional songs, folk dances, colorful attire',
            'Women swing rides, fasting rituals, songs praising Goddess Parvati',
            'Cattle trading, folk dances, turban tying, camel races',
            'Traditional dances, bamboo music, local cuisines, village fairs',
            'Temple processions, classical music, folk dances, fireworks',
            'Handicraft displays, folk music performances, cultural workshops',
            'Folk dance shows, culinary stalls, craft bazaars, cultural parades',
            'Devotional songs, spiritual talks, classical dance recitals',
            'Chariot pulling, devotional singing, massive crowds, religious fervor',
            # New highlights
            'Tribal rituals, folk dances, traditional music, local cuisine tastings',
            'Rituals involving rat worship, traditional music, fairs and processions',
            'Grand reenactment of divine wedding, traditional music, cultural dances',
            'Elephant processions, percussion ensembles, fireworks display',
            'Trade fairs, cultural performances, business seminars, handicraft exhibitions',
            'Community feasts, bonfires, traditional games, folk songs',
            'Folk dances, music performances, traditional food stalls',
            'Traditional music, folk dances, cultural parades, food festivals',
            'Folk dances, songs, rituals for marital happiness, fairs',
            'Traditional wrestling, cultural shows, local crafts, folk music'
        ]
    }
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    return df


@st.cache_data
def load_enhanced_heritage_sites():
    df = pd.read_csv("enhanced_indian_heritage_sites.csv")
    df.columns = df.columns.str.lower()
    return df


def load_all_data():
    """Load all datasets and return them in a dictionary"""
    return {
        "enhanced_heritage_sites": load_enhanced_heritage_sites()
    }

@st.cache_data
def load_tourism_trends():
    # Sample data for tourism trends
    states = [
        'Maharashtra', 'Tamil Nadu', 'Uttar Pradesh', 'Karnataka', 'Rajasthan',
        'Kerala', 'Gujarat', 'Himachal Pradesh', 'Goa', 'Madhya Pradesh',
        'Uttarakhand', 'Andhra Pradesh', 'West Bengal', 'Jammu & Kashmir', 'Odisha'
    ]
    
    # Yearly data (2018-2022)
    years = [2018, 2019, 2020, 2021, 2022]
    yearly_data = {}
    
    for state in states:
        # Generate realistic pattern with COVID dip in 2020
        base = np.random.randint(500000, 2000000)
        yearly_data[state] = [
            base + np.random.randint(-100000, 100000),  # 2018
            base * 1.1 + np.random.randint(-100000, 100000),  # 2019
            base * 0.3 + np.random.randint(-50000, 50000),   # 2020 (COVID)
            base * 0.6 + np.random.randint(-100000, 100000),  # 2021 (recovery)
            base * 0.9 + np.random.randint(-100000, 100000)   # 2022 (further recovery)
        ]
    
    # Create DataFrame for yearly trends
    yearly_df = pd.DataFrame({
        'State': np.repeat(states, len(years)),
        'Year': np.tile(years, len(states)),
        'Visitors': [yearly_data[state][i] for state in states for i in range(len(years))]
    })
    
    # Monthly data for 2022
    months = list(range(1, 13))
    monthly_data = {}
    
    for state in states:
        # Generate seasonal pattern
        base = yearly_data[state][-1] / 12  # Average monthly visitors based on 2022
        
        # Create seasonal pattern (higher in winter months for most states, except hill stations)
        if state in ['Himachal Pradesh', 'Uttarakhand', 'Jammu & Kashmir']:
            # Hill stations - peak in summer
            seasonal_factor = [0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 1.5, 1.2, 1.0, 0.9, 0.8, 0.7]
        elif state in ['Goa', 'Kerala', 'Rajasthan']:
            # Winter tourism destinations
            seasonal_factor = [1.5, 1.3, 1.0, 0.7, 0.5, 0.4, 0.5, 0.6, 0.8, 1.0, 1.3, 1.6]
        else:
            # General pattern with peaks in winter and dips in monsoon
            seasonal_factor = [1.3, 1.2, 1.0, 0.9, 0.8, 0.7, 0.6, 0.7, 0.9, 1.1, 1.3, 1.4]
        
        monthly_data[state] = [base * factor + np.random.randint(-int(base*0.1), int(base*0.1)) for factor in seasonal_factor]
    
    # Create DataFrame for monthly trends
    monthly_df = pd.DataFrame({
        'State': np.repeat(states, len(months)),
        'Month': np.tile(months, len(states)),
        'Visitors': [monthly_data[state][i-1] for state in states for i in months]
    })
    
    # Demographics data
    demographics = {
        'Age_Group': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
        'Percentage': [15, 25, 22, 18, 12, 8]
    }
    
    demographics_df = pd.DataFrame(demographics)
    
    # Origin data (domestic vs international)
    origin = {
        'Origin': ['Domestic', 'International'],
        'Percentage': [85, 15]
    }
    
    origin_df = pd.DataFrame(origin)
    
    # Purpose of visit data
    purpose = {
        'Purpose': ['Cultural/Heritage', 'Religious', 'Adventure/Nature', 'Leisure', 'Business', 'Medical'],
        'Percentage': [30, 25, 20, 15, 7, 3]
    }
    
    purpose_df = pd.DataFrame(purpose)
    
    # Spending patterns
    spending = {
        'Category': ['Accommodation', 'Food & Beverage', 'Transportation', 'Shopping', 'Activities', 'Others'],
        'Percentage': [35, 25, 15, 12, 10, 3]
    }
    
    spending_df = pd.DataFrame(spending)
    
    return yearly_df, monthly_df, demographics_df, origin_df, purpose_df, spending_df

@st.cache_data
def load_art_forms():
    # Sample data for art forms
    data = {
        'name': [
            'Madhubani', 'Kathakali', 'Gond Art', 'Phad Painting', 'Warli',
            'Pattachitra', 'Chikankari', 'Thangka', 'Chhau Dance', 'Kalbelia',
            'Bharatanatyam', 'Kalamkari', 'Bidri', 'Pashmina', 'Meenakari',
            'Kuchipudi', 'Tanjore Painting', 'Dhokra', 'Manipuri', 'Pichwai'
        ],
        'region': [
            'Bihar', 'Kerala', 'Madhya Pradesh', 'Rajasthan', 'Maharashtra',
            'Odisha', 'Uttar Pradesh', 'Ladakh', 'West Bengal', 'Rajasthan',
            'Tamil Nadu', 'Andhra Pradesh', 'Karnataka', 'Kashmir', 'Rajasthan',
            'Andhra Pradesh', 'Tamil Nadu', 'Chhattisgarh', 'Manipur', 'Rajasthan'
        ],
        'type': [
            'Painting', 'Dance', 'Painting', 'Painting', 'Painting',
            'Painting', 'Embroidery', 'Painting', 'Dance', 'Dance',
            'Dance', 'Textile Art', 'Metal Craft', 'Textile', 'Jewelry',
            'Dance', 'Painting', 'Metal Craft', 'Dance', 'Painting'
        ],
        'description': [
            'Geometric patterns and nature motifs using natural dyes on handmade paper.',
            'Classical dance-drama with elaborate costumes and makeup telling mythological stories.',
            'Tribal art with natural imagery using dots and lines in vibrant colors.',
            'Scroll paintings depicting heroic folk tales and legends.',
            'Tribal art using geometric shapes to depict daily life and rituals.',
            'Ancient cloth-based scroll painting with intricate details and mythological themes.',
            'Delicate white-on-white embroidery technique with floral patterns.',
            'Buddhist scroll paintings depicting deities and mandalas.',
            'Martial arts-inspired tribal dance with elaborate masks.',
            'Traditional dance of the Kalbelia tribe known for swirling movements.',
            'One of the oldest classical dance forms with precise footwork and expressive gestures.',
            'Hand-painted or block-printed cotton textile with natural dyes.',
            'Metal craft with silver inlay work on blackened alloy of zinc and copper.',
            'Fine wool textile made from the undercoat of Changthangi goats.',
            'Colorful enamel work on gold jewelry, especially popular in Jaipur.',
            'Classical dance form with graceful movements and expressive storytelling.',
            'Classical South Indian painting style with gold leaf overlays and gemstone inlays.',
            'Ancient lost-wax metal casting technique creating tribal figurines.',
            'Classical dance form emphasizing grace, purity, and tenderness.',
            'Traditional devotional paintings depicting scenes from Lord Krishna\'s life.'
        ],
        'image_url': [
            'madhubani.jpg', 'kathakali.jpg', 'gond.jpg', 'phad.jpg', 'warli.jpg',
            'pattachitra.jpg', 'chikankari.jpg', 'thangka.jpg', 'chhau.jpg', 'kalbelia.jpg',
            'bharatanatyam.jpg', 'kalamkari.jpg', 'bidri.jpg', 'pashmina.jpg', 'meenakari.jpg',
            'kuchipudi.jpg', 'tanjore.jpg', 'dhokra.jpg', 'manipuri.jpg', 'pichwai.jpg'
        ],
        'history': [
            'Dates back to the time of Ramayana, traditionally done by women on walls and floors.',
            'Evolved in the 17th century in Kerala, combining elements from Hindu temple art and martial arts.',
            'Ancient tribal art form of the Gond people, one of the largest tribal groups in India.',
            'Originated over 700 years ago in Rajasthan, traditionally performed by the Joshi family.',
            'Tribal art form dating back to 10th century AD, traditionally painted on mud walls.',
            'Ancient art form from Odisha dating back to 12th century, originally created for Jagannath Temple.',
            'Introduced by Noor Jehan, wife of Mughal Emperor Jahangir, in the 17th century.',
            'Buddhist religious paintings originating in the 7th century, influenced by Nepalese and Chinese art.',
            'Originated in the 18th century, combining elements of tribal, folk, and classical traditions.',
            'Traditional dance of the nomadic Kalbelia tribe, recognized by UNESCO as Intangible Cultural Heritage.',
            'One of the oldest dance forms in India, with 2000-year history, codified in Natya Shastra.',
            'Ancient art dating back 3000 years, with references in ancient scripts and Buddhist shrines.',
            'Developed in the 14th century during the Bahmani Sultanate in Bidar, Karnataka.',
            'Traditional craft dating back to the 3rd century BC, mentioned in Kashmiri poet Kalidasa\'s works.',
            'Introduced to Rajasthan by the Mughals, reached its zenith during Raja Man Singh\'s rule.',
            'Originated in Kuchipudi village of Andhra Pradesh in the 17th century as a dance-drama.',
            'Developed during the Maratha rule in Thanjavur (16th-18th centuries).',
            'One of the oldest metal crafts in India, dating back 4,000 years to the Indus Valley Civilization.',
            'Ancient dance form with roots in indigenous Lai Haraoba rituals and Vaishnavism.',
            'Developed in the 17th century in Nathdwara, Rajasthan as temple hangings.'
        ],
        'significance': [
            'Preserves rural traditions and mythology, provides livelihood to women artists.',
            'Preserves ancient stories and traditions through elaborate performances.',
            'Reflects tribal worldview and connection with nature, now gaining international recognition.',
            'Preserves oral storytelling traditions and folk legends of Rajasthan.',
            'Documents tribal life and rituals, now recognized internationally as contemporary art.',
            'Preserves mythological stories and temple art traditions of Odisha.',
            'Represents Lucknow\'s cultural heritage and provides livelihood to thousands of artisans.',
            'Important religious and cultural artifact in Tibetan Buddhism.',
            'Preserves tribal martial traditions and mythology through performance.',
            'Represents the cultural identity of the Kalbelia community, traditionally snake charmers.',
            'Embodies South Indian temple traditions and devotional expression.',
            'Preserves ancient textile traditions and mythological storytelling.',
            'Represents the syncretic Hindu-Muslim artistic traditions of the Deccan.',
            'Vital to Kashmir\'s economy and cultural identity.',
            'Represents the fusion of Mughal and Rajput artistic traditions.',
            'Preserves ancient dance-drama traditions of Andhra Pradesh.',
            'Represents the devotional art traditions of South India.',
            'Preserves tribal artistic traditions and provides livelihood to tribal communities.',
            'Embodies the gentle, devotional culture of Manipur.',
            'Preserves devotional art traditions associated with the Nathdwara temple.'
        ]
    }
    return pd.DataFrame(data)

@st.cache_data
def load_sustainability_tips():
    # Sample data for sustainability tips
    data = {
        'title': [
            'Respect Sacred Sites', 'Support Local Artisans', 'Reduce Plastic Waste',
            'Choose Eco-Friendly Accommodations', 'Learn Basic Local Phrases',
            'Dress Appropriately', 'Ask Before Photographing', 'Use Public Transport',
            'Conserve Water', 'Participate in Community Tourism',
            'Choose Responsible Tour Operators', 'Eat Local and Seasonal', 'Offset Your Carbon Footprint',
            'Respect Wildlife', 'Minimize Energy Usage', 'Support Conservation Efforts',
            'Practice Responsible Trekking', 'Respect Local Customs', 'Choose Sustainable Souvenirs',
            'Volunteer Responsibly'
        ],
        'category': [
            'Cultural Etiquette', 'Economic Impact', 'Environmental',
            'Environmental', 'Cultural Etiquette', 'Cultural Etiquette',
            'Cultural Etiquette', 'Environmental', 'Environmental', 'Community',
            'Economic Impact', 'Environmental', 'Environmental',
            'Environmental', 'Environmental', 'Conservation',
            'Environmental', 'Cultural Etiquette', 'Economic Impact',
            'Community'
        ],
        'description': [
            'Remove shoes before entering temples and cover your head in gurudwaras. Maintain silence in places of worship.',
            'Buy directly from local craftspeople to ensure they receive fair compensation for their work.',
            'Carry a reusable water bottle and cloth bag to minimize plastic waste in ecologically sensitive areas.',
            'Stay at hotels with sustainable practices like solar power, water recycling, and waste management.',
            'Learning a few words in the local language shows respect and enhances your cultural experience.',
            'Dress modestly when visiting religious sites and rural communities. Cover shoulders and knees.',
            'Always ask permission before taking photos of people, especially in tribal areas and religious ceremonies.',
            'Use trains, buses, and shared transportation to reduce your carbon footprint and experience local life.',
            'Be mindful of water usage, especially in water-scarce regions like Rajasthan.',
            'Choose tourism initiatives that involve and benefit local communities directly.',
            'Research and select tour operators with strong sustainability policies and fair employment practices.',
            'Choose locally grown, seasonal foods to reduce carbon footprint and support local farmers.',
            'Calculate and offset the carbon emissions from your travel through verified carbon offset programs.',
            'Maintain a safe distance from wildlife, never feed animals, and avoid wildlife products or experiences that exploit animals.',
            'Turn off lights, AC, and electronics when not in use, even in hotels and accommodations.',
            'Contribute to local conservation efforts through donations or participation in conservation activities.',
            'Stay on marked trails, carry out all waste, and avoid damaging vegetation during treks.',
            'Research and follow local customs regarding greetings, dining etiquette, and public behavior.',
            'Avoid souvenirs made from endangered species, ancient artifacts, or non-sustainable materials.',
            'Choose volunteer opportunities that address genuine community needs and create sustainable impact.'
        ],
        'icon': [
            'temple', 'shopping-bag', 'recycle', 'home', 'message-circle',
            'shirt', 'camera', 'bus', 'droplet', 'users',
            'compass', 'utensils', 'leaf', 'paw-print', 'lightbulb',
            'heart', 'mountain', 'hands', 'gift', 'helping-hand'
        ],
        'impact_level': [
            'High', 'High', 'Medium', 'High', 'Medium',
            'Medium', 'Medium', 'High', 'High', 'High',
            'High', 'Medium', 'Medium', 'High', 'Medium',
            'High', 'High', 'Medium', 'Medium', 'High'
        ],
        'example': [
            'The Ajmer Sharif Dargah provides head coverings for visitors who arrive unprepared.',
            'The Dastkar craft bazaars connect tourists directly with artisans, eliminating middlemen.',
            'Leh in Ladakh has banned single-use plastic to protect its fragile mountain ecosystem.',
            'CGH Earth hotels in Kerala use rainwater harvesting and solar energy across their properties.',
            'In Tamil Nadu, saying "Vanakkam" (hello) is greatly appreciated by locals.',
            'Visitors to Jama Masjid in Delhi are provided with appropriate coverings if needed.',
            'The Jarawa tribe in Andaman prohibits photography to protect their cultural integrity.',
            'Shimla\'s restriction on private vehicles in the Mall Road area has reduced pollution.',
            'Hotels in Jaisalmer often have signs reminding guests about the desert region\'s water scarcity.',
            'The Spiti Ecosphere initiative involves local families in providing authentic homestay experiences.',
            'Kipepeo in Northeast India ensures fair wages and sustainable practices in all their tours.',
            'Kerala\'s farm-to-table restaurants serve seasonal produce from within a 50-mile radius.',
            'Responsible travel companies like Intrepid offer carbon-neutral trips across India.',
            'Kanha National Park\'s strict safari regulations ensure minimal disturbance to tigers.',
            'ITC Hotels\' "Responsible Luxury" initiative includes energy-efficient building design.',
            'The Snow Leopard Conservancy in Ladakh involves tourists in conservation awareness programs.',
            'The Himalayan Mountaineering Institute promotes responsible trekking practices in Sikkim.',
            'In Varanasi, visitors are advised not to point feet toward the Ganges or religious sites.',
            'Dastkar\'s Green Shop sells only eco-friendly crafts made from sustainable materials.',
            'The Ecosphere Project in Spiti Valley offers meaningful volunteer opportunities in education and conservation.'
        ]
    }
    return pd.DataFrame(data)

@st.cache_data
def load_testimonials():
    # Sample testimonials
    data = {
        'quote': [
            'Cultural Compass helped me discover hidden gems in India that I would have never found on my own. The interactive map was particularly useful!',
            'As a solo female traveler, the cultural etiquette tips were invaluable. I felt more confident and respectful during my journey through Rajasthan.',
            'The festival calendar helped me plan my trip to coincide with Hornbill Festival in Nagaland. It was the highlight of my year!',
            'I\'ve been to India three times, but this app showed me places I\'d never heard of. Majuli Island was a revelation!',
            'The sustainability tips helped me travel more responsibly. I even found an eco-friendly homestay through one of the recommendations.'
        ],
        'author': [
            'Sarah Johnson, UK', 'Maria Garcia, Spain', 'David Chen, Canada', 
            'Emma Thompson, Australia', 'Raj Patel, USA'
        ]
    }
    return pd.DataFrame(data)

@st.cache_data
def load_featured_destinations():
    # Sample featured destinations
    data = {
        'name': [
            'Valley of Flowers', 'Majuli Island', 'Ziro Valley'
        ],
        'state': [
            'Uttarakhand', 'Assam', 'Arunachal Pradesh'
        ],
        'description': [
            'A UNESCO World Heritage Site and national park known for its meadows of endemic alpine flowers and diverse flora.',
            'The world\'s largest river island, known for its unique Assamese neo-Vaishnavite culture and monasteries called Satras.',
            'A picturesque valley home to the Apatani tribe, known for their unique agricultural techniques and distinctive cultural practices.'
        ],
        'why_visit': [
            'Experience one of the most beautiful high-altitude meadows with over 500 species of wild flowers, set against the backdrop of the Himalayas.',
            'Witness a unique way of life that harmoniously blends with nature on this ever-shrinking river island in the mighty Brahmaputra.',
            'Explore one of India\'s most pristine tribal regions with distinctive cultural practices and breathtaking landscapes.'
        ],
        'best_time': [
            'July to September', 'November to March', 'March to October'
        ],
        'image_url': [
            'valley_of_flowers.jpg', 'majuli.jpg', 'ziro.jpg'
        ]
    }
    return pd.DataFrame(data)

def load_all_data():
    """Load all datasets and return them in a dictionary"""
    heritage_sites = load_heritage_sites()
    cultural_events = load_cultural_events()
    yearly_trends, monthly_trends, demographics, origin, purpose, spending = load_tourism_trends()
    art_forms = load_art_forms()
    sustainability_tips = load_sustainability_tips()
    testimonials = load_testimonials()
    featured_destinations = load_featured_destinations()
    
    return {
        "heritage_sites": heritage_sites,
        "cultural_events": cultural_events,
        "yearly_trends": yearly_trends,
        "monthly_trends": monthly_trends,
        "demographics": demographics,
        "origin": origin,
        "purpose": purpose,
        "spending": spending,
        "art_forms": art_forms,
        "sustainability_tips": sustainability_tips,
        "testimonials": testimonials,
        "featured_destinations": featured_destinations
    }
