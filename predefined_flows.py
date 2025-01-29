# Predefined Analysis flows 

predefined_flows = {
    1: {
        "Id": 1,
        "Steps": [
            {"Name": "Remove short items", "Description": "Remove items with less than 5 characters"},
            {"Name": "Remove spaces", "Description": "Remove spaces from items"}
        ]
    },
    2: {
        "Id": 2,
        "Steps": [
            {"Name": "Convert to lowercase", "Description": "Convert all text to lowercase"},
            {"Name": "Remove numbers", "Description": "Remove numerical characters from items"}
        ]
    },
    3: {
        "Id": 3,
        "Steps": [
            {"Name": "Remove special characters", "Description": "Remove symbols like @, #, $ from items"},
            {"Name": "Trim whitespace", "Description": "Trim leading and trailing whitespace"}
        ]
    },
    4: {
        "Id": 4,
        "Steps": [
            {"Name": "Tokenize words", "Description": "Split text into words"},
            {"Name": "Filter stopwords", "Description": "Remove common stopwords like 'the', 'is', etc."}
        ]
    },
    5: {
        "Id": 5,
        "Steps": [
            {"Name": "Stem words", "Description": "Reduce words to their root form"},
            {"Name": "Remove duplicates", "Description": "Remove duplicate items from the list"}
        ]
    }
}

def get_predefined_flows():
    return predefined_flows
