from models import MatchState
from agents import run_captain_cool_debate

def main():
    # Setting up a high-pressure IPL match scenario
    # MI chasing against RCB at Wankhede
    # 2nd innings, 16th over completed (16.0), 45 runs needed off 24 balls
    # Suryakumar Yadav on strike, turning pitch, dew present
    
    test_scenario = MatchState(
        innings=2,
        current_over=16.0,
        score=155, 
        runs_needed=45,
        batsman_on_strike="Suryakumar Yadav",
        bowler_name="Yuzvendra Chahal", # A spinner bowling the 17th over
        venue="Wankhede",
        pitch_condition="turning",
        is_dew_present=True,
        overs_left_per_bowler={
            "Yuzvendra Chahal": 1,
            "Mohammed Siraj": 2,
            "Glenn Maxwell": 1
        },
        has_impact_player=True
    )
    
    print("Initializing Match Scenario: RCB vs MI")
    print("--------------------------------------")
    print(f"Innings: {test_scenario.innings}")
    print(f"Current Over: {test_scenario.current_over}")
    print(f"Runs Needed: {test_scenario.runs_needed} off 24 balls")
    print(f"Batsman on Strike: {test_scenario.batsman_on_strike}")
    print(f"Bowler: {test_scenario.bowler_name}")
    print(f"Pitch: {test_scenario.pitch_condition}, Dew: {test_scenario.is_dew_present}")
    print("--------------------------------------\n")
    
    run_captain_cool_debate(test_scenario)

if __name__ == "__main__":
    main()
