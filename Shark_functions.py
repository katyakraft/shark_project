def generalize_injury(injury):
    injury_lower = injury.lower()
    
    # Generalize foot injuries
    if re.search(r'foot|toe|heel|ankle', injury_lower):  # Looks for "foot", "toe", "heel", or "ankle"
        return 'foot injury'
    elif re.search(r'leg|knee|calf|thigh', injury_lower): 
        return 'leg injury'
    elif re.search(r'hand|finger|wrist', injury_lower):  
        return 'hand injury'
    elif re.search(r'arm|forearm|elbow', injury_lower):  
        return 'arm injury'
    elif re.search(r'torso|back|head|chin|face', injury_lower):  
        return 'torso or head injury'    
    else:
        return 'Unknown injury'

def shark_categories(species):
    # Convert species to a string and handle NaN or missing values
    species_str = str(species).lower() if pd.notnull(species) else ''
    
    # Categorize based on size or species
    if re.search(r'juvenile|1|2|3', species_str):
        return 'shark < 1m'
    elif re.search(r'4|5|spinner|blacktip|lemon', species_str):
        return '1m < shark < 2m'
    elif re.search(r'6|bull', species_str):
        return 'shark > 2m'
    else:
        return 'Unidentified shark'

def extract_month_from_description(description):
    if pd.isna(description):
        return None
    
    # Ensure description is a string
    description = str(description).lower()
    print(f"Processing description: {description}")  # Debug output
    
    # Check for specific date formats like '15 Mar 2024'
    date_match = re.search(r'(\d{1,2})[\s\-\/](\w+)[\s\-\/](\d{4})', description)
    if date_match:
        day, month_str, year = date_match.groups()
        month_str = month_str.lower()
        
        # Map month string to month number
        if month_str in month_mapping:
            print(f"Found valid date: {day} {month_str} {year}, returning month {month_mapping[month_str]}")  # Debug output
            return month_mapping[month_str]
    
    # Check for month name or abbreviation
    for month_name, month_number in month_mapping.items():
        if month_name in description:
            print(f"Found month in description: {month_name}, returning month {month_number}")  # Debug output
            return month_number
    
    # Check for seasons (summer, winter, etc.)
    for season, month in season_to_month.items():
        if season in description:
            print(f"Found season in description: {season}, returning month {month}")  # Debug output
            return month
    
    # Handle descriptions like 'before May' or 'after June'
    if 'before' in description or 'prior to' in description:
        for month_name, month_number in month_mapping.items():
            if month_name in description:
                print(f"Found 'before' in description: {description}, returning month {month_number - 1}")  # Debug output
                return month_number - 1 if month_number > 1 else 12
    
    if 'after' in description:
        for month_name, month_number in month_mapping.items():
            if month_name in description:
                print(f"Found 'after' in description: {description}, returning month {month_number + 1}")  # Debug output
                return month_number + 1 if month_number < 12 else 1
    
    print(f"Unable to extract month from description: {description}, returning None")  # Debug output
    return None

