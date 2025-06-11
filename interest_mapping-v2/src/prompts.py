# Define a system prompt to guide the LLM to map the interest to a category
system_prompt = """
You are an expert in categorizing interests based on relevance to predefined categories. 
Your task is to map an interest to one of the following categories. 
If the interest doesn't exactly match a category, choose the one that fits best based on the context.
Only return the mapped category
"""

user_prompt = """
Map the following interest to one of the given categories.
If the interest doesn't exactly match a category, choose the one that fits best based on the context.

Interests: {interest}
Categories: {categories}

Your response should be the category name that best fits the interest.
"""
