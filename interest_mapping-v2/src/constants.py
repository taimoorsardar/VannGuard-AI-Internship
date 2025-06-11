CSV_FILE = "data/inputs/topic_mapping_classification_results.tsv"

json_data = '''
{
    "Demographics": {
        "Age": {
            "From": 25,
            "To": 45
        },
        "Education": "College Degree",
        "Family Size": "0-Recently started a family",
        "Gender": "Male & Female",
        "Income": {
            "From": "Mid",
            "To": "High"
        },
        "Marital Status": "Single or Married",
        "Occupation": "Professionals, Athletes, and Health-Conscious Individuals with Disposable Income"
    },
    "General": {
        "Description": "A health-conscious individual who values efficiency, innovation, and long-term wellness investments..."
    },
    "Locations": {
        "Exclude": [],
        "Include": [
            "National (various regions with strong access to e-commerce and health tech services)"
        ]
    },
    "Psychographic Targeting": {
        "Interests": [
            "Physical Fitness",
            "Nutrition and Hydration",
            "Recovery and Performance",
            "Mental Health and Stress Management",
            "Biohacking",
            "Wearable Tech",
            "Health Tech",
            "Smart Home Devices",
            "Tech Reviews and Trends",
            "Sports",
            "Self-Improvement",
            "High-End Lifestyle Products",
            "Online Wellness Communities"
        ],
        "Personality Sliders": {
            "Active-Sedentary": 0.8,
            "Extroverted-Introverted": 0.6,
            "Follower-Trendsetter": 0.7,
            "Serious-Playful": 0.6,
            "Spender-Saver": 0.4
        },
        "Preferred Browsing Method": "Web",
        "Preferred Buying Method": "E-commerce (Health & Wellness Online Stores, Amazon, Brand Websites)"
    },
    "Health and Wellness Focus": {
        "Needs": [
            "Health Optimization",
            "Convenience and Efficiency",
            "Cutting-Edge Technology",
            "Sustainability"
        ],
        "Concerns": [
            "Price",
            "Effectiveness",
            "Durability and Maintenance",
            "Compatibility and User-Friendliness"
        ],
        "Motivations": [
            "Health and Performance Enhancement",
            "Embracing Innovative Health Solutions",
            "Long-Term Health Investment",
            "Efficiency and Productivity",
            "Environmental Impact"
        ]
    },
    "Social Media": {
        "Content Preferences": "Informative health content, high-quality visuals, fitness tips, product reviews, and expert insights",
        "Engagement Style": "Engages with interactive content, watches product demos, and participates in health and wellness discussions",
        "Posting Frequency": "Moderate to Frequent (weekly posts, story engagement)",
        "Preferred Platform": "Instagram, YouTube, and Health/Wellness Communities"
    }
}
'''
