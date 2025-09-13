from fastmcp import FastMCP
from agent import query_players_statistics,query_head_to_head,query_team_performance,query_season_comparisons,query_match_analysis

mcp = FastMCP("FastMCP-IPL")

@mcp.tool
def query_players_stats(query:str)->str:
    """Player's Performance Analysis Tool"""
    return query_players_statistics(query)

@mcp.tool
def match_analysis(query:str)->str:
    """Match-level insights and comparisons"""
    return query_match_analysis(query)

@mcp.tool
def team_performance(query:str)->str:
    """Team statistics and trends"""
    return query_team_performance(query)

@mcp.tool
def season_comparisons(query:str)->str:
    """Cross-season analysis"""
    return query_season_comparisons(query)

@mcp.tool
def head_to_head(query:str)->str:
    """Team vs team historical data Tool"""
    return query_head_to_head(query)

if __name__ == "__main__":
    mcp.run()