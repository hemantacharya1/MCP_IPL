from dotenv import load_dotenv
load_dotenv()
from langchain_community.utilities import SQLDatabase
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


db = SQLDatabase.from_uri("sqlite:///./database.db")

class StructuredOutput(BaseModel):
    query: str = Field(..., description="The SQL query to be executed")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

llm_structured_output=llm.with_structured_output(StructuredOutput)


def final_human_response(user_query: str,result: str) -> str:
    prompt = f"""
    You are an expert at summarizing sql query results. Given the result of a SQL query,
    your task is to generate a concise and informative summary of the result.
    that answers the user's query.
    Here is the result of the SQL query: {result}
    Here is the user's query: {user_query}
    Make sure to provide a clear and concise summary that directly addresses the user's query.
    """
    llm_response = llm.invoke(prompt)
    return llm_response.dict().get("content")

def query_players_statistics(user_query: str) -> str:
    """Player's Performance Analysis based on the provided query."""
    dialect = db.dialect
    table_info = db.get_table_info()
    prompt = f"""
    You are an expert SQL query generator. Given an input question/query {user_query} for player statistics,
    your task is to generate a syntactically correct query which captures the essence of the question.
    you have access to the table structure below:
    {table_info}
    and the SQL dialect below:
    {dialect}
    Make sure to follow the table structure and SQL dialect while generating the query.
    """
    response = llm_structured_output.invoke(prompt).dict()
    sql_query = response.get("query")
    try:                
        result = db.run(sql_query)
        final_response = final_human_response(user_query,result)
        return final_response
    except Exception as e:
        return f"An error occurred while executing the query: {sql_query}. Error details: {str(e)}"
    
def query_match_analysis(user_query: str) -> str:
    """Match-level insights and comparisons based on the provided query."""
    dialect = db.dialect
    table_info = db.get_table_info()
    prompt = f"""
    You are an expert SQL query generator. Given an input question/query {user_query} for match analysis,
    your task is to generate a syntactically correct query which captures the essence of the question.
    you have access to the table structure below:
    {table_info}
    and the SQL dialect below:
    {dialect}
    Make sure to follow the table structure and SQL dialect while generating the query.
    """
    response = llm_structured_output.invoke(prompt).dict()
    sql_query = response.get("query")
    try:                
        result = db.run(sql_query)
        final_response = final_human_response(user_query,result)
        return final_response
    except Exception as e:
        return f"An error occurred while executing the query: {sql_query}. Error details: {str(e)}"
    
def query_team_performance(user_query: str) -> str:
    """Team statistics and trends based on the provided query."""
    dialect = db.dialect
    table_info = db.get_table_info()
    prompt = f"""
    You are an expert SQL query generator. Given an input question/query {user_query} for team performance,
    your task is to generate a syntactically correct query which captures the essence of the question.
    you have access to the table structure below:
    {table_info}
    and the SQL dialect below:
    {dialect}
    Make sure to follow the table structure and SQL dialect while generating the query.
    """
    response = llm_structured_output.invoke(prompt).dict()
    sql_query = response.get("query")
    try:                
        result = db.run(sql_query)
        final_response = final_human_response(user_query,result)
        return final_response
    except Exception as e:
        return f"An error occurred while executing the query: {sql_query}. Error details: {str(e)}"
    
def query_season_comparisons(user_query: str) -> str:
    """Cross-season analysis based on the provided query."""
    dialect = db.dialect
    table_info = db.get_table_info()
    prompt = f"""
    You are an expert SQL query generator. Given an input question/query {user_query} for season comparisons,
    your task is to generate a syntactically correct query which captures the essence of the question.
    you have access to the table structure below:
    {table_info}
    and the SQL dialect below:
    {dialect}
    Make sure to follow the table structure and SQL dialect while generating the query.
    """
    response = llm_structured_output.invoke(prompt).dict()
    sql_query = response.get("query")
    try:                
        result = db.run(sql_query)
        final_response = final_human_response(user_query,result)
        return final_response
    except Exception as e:
        return f"An error occurred while executing the query: {sql_query}. Error details: {str(e)}"
    
def query_head_to_head(user_query: str) -> str:
    """Team vs team historical data based on the provided query."""
    dialect = db.dialect
    table_info = db.get_table_info()
    prompt = f"""
    You are an expert SQL query generator. Given an input question/query {user_query} for head-to-head statistics,
    your task is to generate a syntactically correct query which captures the essence of the question.
    you have access to the table structure below:
    {table_info}
    and the SQL dialect below:
    {dialect}
    Make sure to follow the table structure and SQL dialect while generating the query.
    """
    response = llm_structured_output.invoke(prompt).dict()
    sql_query = response.get("query")
    try:                
        result = db.run(sql_query)
        final_response = final_human_response(user_query,result)
        return final_response
    except Exception as e:
        return f"An error occurred while executing the query: {sql_query}. Error details: {str(e)}"