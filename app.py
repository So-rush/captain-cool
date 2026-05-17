import streamlit as st
from models import MatchState
from agents import run_captain_cool_debate

st.set_page_config(page_title="Captain Cool", page_icon="🏏", layout="wide")

st.title("🏏 Captain Cool — Multi-Agent IPL Match Strategist")

st.markdown("### Live Match State Inputs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    innings = st.number_input("Innings", min_value=1, max_value=2, value=1)
    current_over = st.number_input("Current Over", min_value=0.0, max_value=20.0, value=14.2, step=0.1)
    score = st.number_input("Score", min_value=0, max_value=400, value=150)

with col2:
    runs_needed_input = st.number_input("Runs Needed (if chasing)", min_value=0, value=0)
    runs_needed = runs_needed_input if innings == 2 else None
    batsman_on_strike = st.text_input("Batsman on Strike", value="Virat Kohli")
    bowler_name = st.text_input("Bowler Name", value="Yuzvendra Chahal")

with col3:
    venue = st.text_input("Venue", value="Dharamshala")
    pitch_condition = st.text_input("Pitch Condition", value="Good for batting, slight turn")
    is_dew_present = st.checkbox("Dew Present?", value=False)

with col4:
    has_impact_player = st.checkbox("Has Impact Player?", value=True)

if st.button("Get Captain's Tactical Decision", type="primary", use_container_width=True):
    match_state = MatchState(
        innings=innings,
        current_over=current_over,
        score=score,
        runs_needed=runs_needed,
        batsman_on_strike=batsman_on_strike,
        bowler_name=bowler_name,
        venue=venue,
        pitch_condition=pitch_condition,
        is_dew_present=is_dew_present,
        overs_left_per_bowler={bowler_name: 1}, # Mocking this for simplicity in the UI
        has_impact_player=has_impact_player
    )

    with st.spinner("Analyzing match state and running internal debate..."):
        try:
            debate_result = run_captain_cool_debate(match_state)
            
            st.markdown("---")
            st.subheader("Internal Debate Log")
            
            if isinstance(debate_result, dict):
                st.info(f"**📊 Match Analyst Facts:**\n\n{debate_result.get('analyst_facts', '')}")
                st.success(f"**💡 Strategist's Initial Proposal:**\n\n{debate_result.get('strategist_proposal', '')}")
                st.error(f"**🔥 Devil's Advocate Challenge:**\n\n{debate_result.get('advocate_challenge', '')}")
                
                st.markdown("---")
                st.subheader("🏆 Final Captain's Decision")
                st.write(debate_result.get('final_decision', ''))
            else:
                # Fallback if it still returns a string
                st.write(debate_result)
                
        except Exception as e:
            st.error(f"Error during debate: {e}")
            st.warning("Please make sure your GEMINI_API_KEY environment variable is set and valid, then try again.")
