import os
from google import genai
from google.genai import types
from models import MatchState
from tools import get_matchup_stats

# Initialize the GenAI client
# This assumes that the GEMINI_API_KEY environment variable is set.
client = genai.Client(api_key="AIzaSyCmPqic2-gnObxJ_bZ5PayIjuRmLjZXD6M")

def run_captain_cool_debate(match_state: MatchState) -> str:
    print("🏏 --- STARTING CAPTAIN COOL DEBATE --- 🏏\n")

    match_state_str = match_state.model_dump_json(indent=2)

    # 1. Match Analyst Sets the Facts
    print("📊 [Match Analyst is analyzing the situation...]")
    analyst_instruction = (
        "You are an expert Cricket Match Analyst. Summarize the current match state "
        "and provide relevant historical statistics using the get_matchup_stats tool."
    )
    
    prompt_for_analyst = f"Current Match State:\n{match_state_str}\n\nPlease analyze this situation and fetch stats."
    
    analyst_response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_for_analyst,
        config=types.GenerateContentConfig(
            system_instruction=analyst_instruction,
            tools=[get_matchup_stats],
            temperature=0.2
        )
    )
    analyst_facts = analyst_response.text
    print(f"\n📈 Match Analyst Facts:\n{analyst_facts}\n")
    print("-" * 50)

    # 2. Strategist Proposes Initial Plan
    print("🧠 [Strategist is formulating an initial plan...]")
    strategist_instruction = (
        "You are an elite, calm cricket captain (like MS Dhoni). "
        "Analyze the Match Analyst's facts and the current match state. "
        "Propose the best next strategic move (e.g., bowling changes, field placements, batting approach). "
        "Be decisive and explain your reasoning calmly."
    )
    
    prompt_for_strategist = (
        f"Match State:\n{match_state_str}\n\n"
        f"Analyst Facts:\n{analyst_facts}\n\n"
        "What is your proposed strategy?"
    )
    
    strategist_proposal_response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt_for_strategist,
        config=types.GenerateContentConfig(
            system_instruction=strategist_instruction,
            temperature=0.7
        )
    )
    strategist_proposal = strategist_proposal_response.text
    print(f"\n💡 Strategist's Initial Proposal:\n{strategist_proposal}\n")
    print("-" * 50)

    # 3. Devil's Advocate Challenges
    print("😈 [Devil's Advocate is looking for flaws...]")
    devil_advocate_instruction = (
        "You are a ruthless Devil's Advocate. Your job is to find flaws, risks, and weaknesses "
        "in the Strategist's proposed plan. Argue strongly against it based on the match state and facts. "
        "Point out the worst-case scenarios."
    )
    
    prompt_for_advocate = (
        f"Match State:\n{match_state_str}\n\n"
        f"Analyst Facts:\n{analyst_facts}\n\n"
        f"Strategist Proposal:\n{strategist_proposal}\n\n"
        "Tear this plan apart. What are the critical flaws?"
    )
    
    advocate_response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt_for_advocate,
        config=types.GenerateContentConfig(
            system_instruction=devil_advocate_instruction,
            temperature=0.8
        )
    )
    advocate_challenge = advocate_response.text
    print(f"\n🔥 Devil's Advocate Challenge:\n{advocate_challenge}\n")
    print("-" * 50)

    # 4. Strategist Delivers Final Decision
    print("👑 [Strategist is finalizing the decision...]")
    prompt_for_final_decision = (
        f"You previously proposed this strategy:\n{strategist_proposal}\n\n"
        f"However, the Devil's Advocate raised these valid concerns:\n{advocate_challenge}\n\n"
        "Take these criticisms into account, adjust your plan if necessary, and deliver your final, definitive captain's decision. "
        "Maintain your calm persona."
    )
    
    final_decision_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_for_final_decision,
        config=types.GenerateContentConfig(
            system_instruction=strategist_instruction,
            temperature=0.5
        )
    )
    final_decision = final_decision_response.text
    print(f"\n🏆 Strategist's Final Decision:\n{final_decision}\n")
    print("🏏 --- DEBATE CONCLUDED --- 🏏\n")

    return {
    "analyst_facts": analyst_facts,
    "strategist_proposal": strategist_proposal,
    "advocate_challenge": advocate_challenge,
    "final_decision": final_decision
}
