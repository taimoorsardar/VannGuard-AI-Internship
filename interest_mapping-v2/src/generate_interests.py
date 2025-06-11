from src.utils import (
    extract_interests, 
    load_categories_from_tsv, 
    map_interests_to_categories, 
    process_multiple_categories,
    get_unique_categories,
    append_interests_to_persona
    )
from src.constants import CSV_FILE
def process_persona_and_update(persona: dict) -> dict:
    # Step 1: Extract interests from persona
    interests = extract_interests(persona)
    
    # Step 2: Load all possible categories from the TSV file
    categories = load_categories_from_tsv(CSV_FILE)
    
    # Step 3: Map interests to LLM-inferred categories
    mapped_categories = map_interests_to_categories(interests, categories)
    
    # Step 4: Use those mapped categories to get relevant rows from the CSV
    top_categories = process_multiple_categories(CSV_FILE, mapped_categories)
    
    # Step 5: Get unique ones
    unique_top_categories = get_unique_categories(top_categories)
    
    # Step 6: Append to the original persona
    updated_persona = append_interests_to_persona(persona, unique_top_categories)
    
    return updated_persona
