import streamlit as st
import pandas as pd
import calendar
from datetime import datetime


def render_calendar_styles():
    st.markdown("""
    <style>
        .calendar-container {
            border: 1px solid #ddd;
            border-radius: 12px;
            overflow: hidden;
            margin-top: 20px;
            font-family: sans-serif;
        }
        .calendar-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 20px;
            background-color: #f1f3f4;
            font-weight: 600;
            font-size: 18px;
            border-bottom: 1px solid #ddd;
        }
        .calendar-grid {
            display: flex;
            flex-direction: column;
        }
        .calendar-week {
            display: flex;
        }
        .calendar-day-header, .calendar-day {
            flex: 1;
            min-height: 100px;
            border: 1px solid #eee;
            box-sizing: border-box;
            padding: 6px;
        }
        .calendar-day-header {
            background: #f8f9fa;
            text-align: center;
            font-weight: bold;
        }
        .calendar-day .day-number {
            font-weight: bold;
        }
        .calendar-day.today {
            background-color: #e3f2fd;
            border: 2px solid #42a5f5;
        }
        .calendar-event {
            background-color: #34a853;
            color: white;
            padding: 2px 6px;
            font-size: 12px;
            border-radius: 4px;
            margin-top: 4px;
            display: inline-block;
            position: relative;
        }
        .calendar-event:hover::after {
            content: attr(data-description);
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            color: black;
            padding: 8px 10px;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            white-space: pre-wrap;
            width: 200px;
            z-index: 100;
            font-size: 12px;
        }
    </style>
    """, unsafe_allow_html=True)


def show_cultural_calendar(cultural_events):
    st.markdown("<h2>Cultural Calendar</h2>", unsafe_allow_html=True)
    st.markdown("Discover upcoming festivals and cultural events across India.")

    if not isinstance(cultural_events['date'].iloc[0], pd.Timestamp):
        cultural_events['date'] = pd.to_datetime(cultural_events['date'])

    render_calendar_styles()

    now = datetime.now()

    # --- Month and Year Selectors ---
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            selected_month = st.selectbox("Select Month", list(calendar.month_name)[1:], index=now.month - 1)
            selected_month_idx = list(calendar.month_name).index(selected_month)
        with col2:
            years = sorted(cultural_events['date'].dt.year.unique())
            # Set index safely: use now.year if available, else default to the last year
            default_year_index = years.index(now.year) if now.year in years else len(years) - 1
            selected_year = st.selectbox("Select Year", years, index=default_year_index)


    # Filter events
    month_events = cultural_events[
        (cultural_events['date'].dt.month == selected_month_idx) &
        (cultural_events['date'].dt.year == selected_year)
    ]
    cal = calendar.monthcalendar(selected_year, selected_month_idx)
    today = datetime.now()
    is_current_month = today.month == selected_month_idx and today.year == selected_year

    # Render header and grid
    html = f"""
    <div class="calendar-container">
        <div class="calendar-header">
            <div>{selected_month} {selected_year}</div>
        </div>
        <div class="calendar-grid">
            <div class="calendar-week">
    """

    for day_name in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
        html += f'<div class="calendar-day-header">{day_name}</div>'
    html += "</div>"

    for week in cal:
        html += '<div class="calendar-week">'
        for day in week:
            if day == 0:
                html += '<div class="calendar-day"></div>'
            else:
                is_today = is_current_month and day == today.day
                css_classes = "calendar-day"
                if is_today:
                    css_classes += " today"

                day_html = f'<div class="{css_classes}">'
                day_html += f'<div class="day-number">{day}</div>'

                day_events = month_events[month_events['date'].dt.day == day]
                for _, event in day_events.iterrows():
                    name = event['name']
                    desc = event['description'][:150].replace('"', "'")
                    day_html += f'<div class="calendar-event" data-description="{desc}">{name}</div>'

                day_html += '</div>'
                html += day_html
        html += "</div>"

    html += "</div></div>"
    st.markdown(html, unsafe_allow_html=True)

    # Event list
    if not month_events.empty:
        st.markdown("<h3>Events this month</h3>", unsafe_allow_html=True)
        for _, event in month_events.iterrows():
            st.markdown(f"""
                <div class="card" style="padding:10px; margin:10px 0; border:1px solid #eee; border-radius:8px;">
                    <strong>{event['name']}</strong> - {event['date'].strftime('%d %b %Y')}<br>
                    <em>{event['state']}</em><br>
                    Duration: {event['duration']}<br>
                    Description: {event['description']}<br>
                    Highlights: {event['highlights']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info(f"No events found for {selected_month} {selected_year}")


