import pandas as pd
from dotenv import load_dotenv
import yaml
from pathlib import Path
from typing import Type, Optional
import os
from pydantic import BaseModel
from openai import OpenAI
from src.prompts import system_prompt, user_prompt

def extract_interests(json_data):
    return json_data['Psychographic Targeting']['Interests']

def load_categories_from_tsv(file_path):
    df = pd.read_csv(file_path, sep='\t')
    df_cleaned = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    categories = df_cleaned.columns.tolist()
    
    return categories


load_dotenv()

def load_config(file_path: str = None) -> dict:
    file_path = Path(file_path) if file_path else Path("configs/config.yaml")

    if not file_path.exists():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            return data if data is not None else {}
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file '{file_path}': {e}")


config = load_config()

def llm_call(
    interest: list,
    categories: list,
    pydantic_model: Optional[Type[BaseModel]] = None,
    temperature: float = config["llm"]["temperature"],
) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    if pydantic_model:
        completion = client.beta.chat.completions.parse(
            model=config["llm"]["config_list"][0]["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format=pydantic_model,
        )
    else:
        completion = client.chat.completions.create(
            model=config["llm"]["config_list"][0]["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt.format(interest = interest, categories=categories)},
            ],
            temperature=temperature,
        )
    return completion.choices[0].message.content


def map_interests_to_categories(interests: list, categories: list) -> list:
    """
    This function takes a list of interests and categories, and returns a list of mapped categories 
    using the LLM call.
    
    Args:
        interests (list): A list of interests to be mapped.
        categories (list): A list of categories to choose from.
    
    Returns:
        list: A list of mapped categories corresponding to each interest.
    """
    mapped_categories = []
    for interest in interests:
        mapped_categories.append(llm_call(interest, categories))
    
    return mapped_categories

def get_category_row(csv_file, category_name):
    df = pd.read_csv(csv_file, sep='\t')
    df[df.columns[0]] = df[df.columns[0]].str.strip().str.lower()  # strip spaces and convert to lowercase
    
    category_name_clean = category_name.strip().lower()
    
    category_row = df[df[df.columns[0]] == category_name_clean]
    
    if category_row.empty:
        print(f"Warning: Category '{category_name}' not found in the CSV file.")
        return None 
    
    return category_row

def extract_top_5_categories(category_row):
    
    if category_row is None:
        return []  
    
    scores = category_row.iloc[0, 1:].values  
    columns = category_row.columns[1:]  
    
    score_column_pairs = list(zip(columns, scores))
    sorted_score_column_pairs = sorted(score_column_pairs, key=lambda x: x[1], reverse=True)
    
    top_5_categories = [pair[0] for pair in sorted_score_column_pairs[:5]]
    
    return top_5_categories


def process_multiple_categories(csv_file, category_list):
    all_top_categories = []
    for category in category_list:
        category_row = get_category_row(csv_file, category)
        if category_row is not None:
            top_categories = extract_top_5_categories(category_row)
            all_top_categories.extend(top_categories)
    return all_top_categories


def get_unique_categories(all_categories):
    return list(set(all_categories))


def append_interests_to_persona(persona, new_interests):
    current_interests = persona["Psychographic Targeting"]["Interests"]
    
    current_interests.extend(new_interests)
    
    persona["Psychographic Targeting"]["Interests"] = list(set(current_interests))
    
    return persona
