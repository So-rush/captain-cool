import streamlit as st
from agents import run_captain_cool_debate
from models import MatchState
import time

# Premium UI Configuration
st.set_page_config(
    page_title="Captain Cool — IPL Strategist",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to make it look incredibly premium
st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1 { color: #f8fafc; font-family: 'Segoe UI', sans-serif; font-weight: 800; }
    .stButton>button {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px;
        width: 100%;
        border: none;
        font-size: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
    }
    .agent-box {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 5px solid;
    }
    .analyst-box { background-color: #1e293b; border-left-color: #3b82f6; border: 1px solid #334155; }
    .strategist-box { background-color: #1e293b; border-left-color: #10b981; border: 1px solid #334155; }
    .advocate-box { background-color: #1e293b; border-left-color: #f59e0b; border: 1px solid #334155; }
    .decision-box { background-color: #1e3a8a; border-left-color: #ef4444; border: 1px solid #3b82f6; }
    .agent-title { font-weight: 700; font-size: 18px; margin-bottom: 8px; color: #ffffff; display: flex; align-items: center; gap: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 Captain Cool — Multi-Agent IPL Match Strategist")
st.caption("Powered by Google Gemini 2.5 Flash & Antigravity Agentic Framework")
st.markdown("---")

# App layout split into Inputs (Left) and Brain Room (Right)
col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("📊 Live Match Parameters")
    
    with st.container():
        venue = st.selectbox("Venue", ["Himachal Pradesh Cricket Association Stadium, Dharamshala", "Wankhede Stadium, Mumbai", "M. Chinnaswamy Stadium, Bengaluru"])
        
        c1, c2 = st.columns(2)
        with c1:
            innings = st.number_input("Innings", min_value=1, max_value=2, value=1)
            score = st.number_input("Current Score", min_value=0, value=150)
        with c2:
            current_over = st.number_input("Current Over", min_value=0.0, max_value=20.0, value=14.2, step=0.1)
            wickets = st.number_input("Wickets Down", min_value=0, max_value=10, value=2)
            
        c3, c4 = st.columns(2)
        with c3:
            batsman = st.text_input("Batsman on Strike", value="Virat Kohli")
        with c4:
            bowler = st.text_input("Current Bowler", value="Yuzvendra Chahal")
            
        c5, c6 = st.columns(2)
        with c5:
            pitch = st.text_input("Pitch Condition", value="Good for batting, slight turn")
        with c6:
            dew = st.checkbox("Dew Present?", value=False)
            
        impact_player = st.checkbox("Has Impact Player Available?", value=True)

    submit_button = st.button("Get Captain's Tactical Decision")

with col2:
    st.subheader("🧠 Brain Room: Agentic Debate Loop")
    
    if submit_button:
        # Create standard MatchState model
        match_context = MatchState(
            innings=innings,
            current_over=float(current_over),
            score=score,
            wickets=wickets,
            batsman_on_strike=batsman,
            bowler_name=bowler,
            venue=venue,
            pitch_condition=pitch,
            is_dew_present=dew,
            overs_left_per_bowler={bowler: 1, "Siraj": 2, "Maxwell": 1},
            has_impact_player=impact_player
        )
        
        status_text = st.empty()
        
        # Step 1: Analyst Node
        status_text.status("🕵️ Match Analyst parsing situational metrics...")
        time.sleep(1) 
        
        # Call backend
        try:
            # Run the backend agent engine loop
            debate_output = run_captain_cool_debate(match_context)
            status_text.empty()
            
            # Render Analyst Card
            st.markdown(f"""
                <div class="agent-box analyst-box">
                    <div class="agent-title">📊 Match Analyst Insights</div>
                    <p style="color: #cbd5e1; margin: 0;">{debate_output.get('analyst_facts', 'Processing matchups...')}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Render Strategist Card
            st.markdown(f"""
                <div class="agent-box strategist-box">
                    <div class="agent-title">💡 Strategist Tactical Proposal</div>
                    <p style="color: #cbd5e1; margin: 0;">{debate_output.get('strategist_proposal', 'Formulating blueprint...')}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Render Devil's Advocate Card
            st.markdown(f"""
                <div class="agent-box advocate-box">
                    <div class="agent-title">🔥 Devil's Advocate Stress-Test</div>
                    <p style="color: #cbd5e1; margin: 0;">{debate_output.get('advocate_challenge', 'Sifting for vulnerabilities...')}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Render Final Decision Card
            st.markdown(f"""
                <div class="agent-box decision-box">
                    <div class="agent-title">🎯 Ultimate Captain's Decree</div>
                    <p style="color: #e2e8f0; margin: 0; font-weight: 600;">{debate_output.get('final_decision', 'Finalizing play...')}</p>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            status_text.empty()
            st.error(f"Execution Error: {str(e)}")
    else:
        st.info("Awaiting input parameters. Click the tactical decision button to initiate the Gemini Agent reasoning cycle.")