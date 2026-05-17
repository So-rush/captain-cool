import streamlit as st
from agents import run_captain_cool_debate
from models import MatchState
import time

st.set_page_config(page_title="Captain Cool — Agentic Room", page_icon="🏏", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1 { font-family: 'Segoe UI', sans-serif; font-weight: 800; color: #f8fafc; }
    .tool-call { background-color: #1e293b; border: 1px dashed #3b82f6; padding: 10px; border-radius: 8px; font-family: monospace; color: #60a5fa; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 Captain Cool — Multi-Agent IPL Match Strategist")
st.caption("Google Agentic Framework — Live Multi-Turn Debate Thread")
st.markdown("---")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📊 Live Match Parameters")
    venue = st.selectbox("Venue", ["HPCA Stadium, Dharamshala", "Wankhede Stadium, Mumbai"])
    
    c1, c2 = st.columns(2)
    innings = c1.number_input("Innings", min_value=1, max_value=2, value=1)
    current_over = c2.number_input("Current Over", min_value=0.0, max_value=20.0, value=14.2)
    
    c3, c4 = st.columns(2)
    score = c3.number_input("Score", min_value=0, value=150)
    wickets = c4.number_input("Wickets", min_value=0, max_value=10, value=2)
    
    c5, c6 = st.columns(2)
    batsman = c5.text_input("Striker", value="Virat Kohli")
    bowler = c6.text_input("Bowler", value="Yuzvendra Chahal")
    
    pitch = st.text_input("Pitch Condition", value="Good for batting, slight turn")
    dew = st.checkbox("Dew Present?", value=False)
    
    submit = st.button("Initiate Captain's War Room Debate")

with col2:
    st.subheader("💬 Active War Room Conversation")
    
    if submit:
        match_context = MatchState(
            innings=innings, current_over=float(current_over), score=score, wickets=wickets,
            batsman_on_strike=batsman, bowler_name=bowler, venue=venue, pitch_condition=pitch,
            is_dew_present=dew, overs_left_per_bowler={bowler: 1, "Siraj": 2}, has_impact_player=True
        )
        
        with st.spinner("Calling Gemini API & Awakening Agents..."):
            debate_output = run_captain_cool_debate(match_context)
        
        # 1. ANALYST TURN (WITH EXPLICIT TOOL CALL)
        with st.chat_message("analyst", avatar="🕵️"):
            st.markdown("**Match Analyst**")
            st.markdown('<div class="tool-call">⚙️ System Tool Executed: get_matchup_stats(player="'+batsman+'", bowler="'+bowler+'", venue="Dharamshala")</div>', unsafe_allow_html=True)
            time.sleep(0.8)
            st.write(debate_output.get('analyst_facts', 'No metrics collected.'))
            
        # 2. STRATEGIST PROPOSAL
        with st.chat_message("assistant", avatar="💡"):
            st.markdown("**Team Captain (Strategist)**")
            time.sleep(1.2)
            st.write(debate_output.get('strategist_proposal', 'Thinking...'))
            
        # 3. DEVIL'S ADVOCATE CHALLENGE
        with st.chat_message("user", avatar="🔥"):
            st.markdown("**Devil's Advocate (Vice-Captain)**")
            time.sleep(1.2)
            st.write(debate_output.get('advocate_challenge', 'Evaluating flaws...'))
            
        # 4. FINAL DECISION
        with st.chat_message("assistant", avatar="🎯"):
            st.markdown("**Final Strategic Decree**")
            time.sleep(1.0)
            st.success(debate_output.get('final_decision', 'Finalizing game plan...'))
            
    else:
        st.info("Click the button to watch the multi-turn agent interaction unfold live.")