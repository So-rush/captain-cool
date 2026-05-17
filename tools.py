def get_matchup_stats(venue: str, batsman: str, bowler_type: str) -> dict:
    """
    Simulate fetching historical data based on venue, batsman, and bowler type.
    """
    # Simple simulated logic based on inputs
    venue_lower = venue.lower()
    bowler_type_lower = bowler_type.lower()
    
    # Simulate average score
    average_score = 45.5
    if venue_lower == "wankhede":
        average_score = 55.0
    elif venue_lower == "chepauk":
        average_score = 30.0

    # Simulate batsman weakness
    batsman_weakness = "struggles against spin"
    if bowler_type_lower == "pace":
        batsman_weakness = "struggles against express pace and bounce"
    elif bowler_type_lower == "spin":
        batsman_weakness = "struggles against quality spin, especially googly"

    # Simulate dew impact
    dew_impact = "high" if venue_lower in ["wankhede", "chinnaswamy", "eden gardens"] else "low"
    
    return {
        "average_score": average_score,
        "batsman_weakness": batsman_weakness,
        "dew_impact": dew_impact
    }
