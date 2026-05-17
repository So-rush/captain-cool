from typing import Dict, Optional
from pydantic import BaseModel

class MatchState(BaseModel):
    innings: int
    current_over: float
    score: int
    runs_needed: Optional[int] = None
    batsman_on_strike: str
    bowler_name: str
    venue: str
    pitch_condition: str
    is_dew_present: bool
    overs_left_per_bowler: Dict[str, int]
    has_impact_player: bool
