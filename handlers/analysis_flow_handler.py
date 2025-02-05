from typing import List, Dict


# class designed for handling the Predefined Flows and implement the logic behind each flow. 
class AnalysisFlowHandler:

    def __init__(self, predefined_flows: List[Dict]):
        self.analysis_flows = predefined_flows
    
    def apply(self, analysis_flow_id: int, data: List[str]) -> List[str]:
                 
        steps = self.analysis_flows.get(analysis_flow_id).get("Steps", [])
        processed_data = data.copy()
        
        for step in steps:
            if step["Name"] == "Remove short items":
                processed_data = [item for item in processed_data if len(item) >= 5]
            elif step["Name"] == "Remove spaces":
                processed_data = [item.replace(" ", "") for item in processed_data]
            elif step["Name"] == "Convert to lowercase":
                processed_data = [item.lower() for item in processed_data]
            elif step["Name"] == "Remove numbers":
                processed_data = ["".join(filter(lambda c: not c.isdigit(), item)) for item in processed_data]
            elif step["Name"] == "Remove special characters":
                processed_data = ["".join(filter(str.isalnum, item)) for item in processed_data]
            elif step["Name"] == "Trim whitespace":
                processed_data = [item.strip() for item in processed_data]
            elif step["Name"] == "Tokenize words":
                processed_data = [word for item in processed_data for word in item.split()]
            elif step["Name"] == "Filter stopwords":
                stopwords = {"the", "is", "in", "and", "to", "a"}
                processed_data = [word for word in processed_data if word.lower() not in stopwords]
            elif step["Name"] == "Stem words":
                processed_data = [item[:-1] if len(item) > 3 else item for item in processed_data]  # Simple stemming
            elif step["Name"] == "Remove duplicates":
                processed_data = list(set(processed_data))
            elif step["Name"] == "Sort alphabetically":
                processed_data = sorted(processed_data)
            elif step["Name"] == "Limit to 10 items":
                processed_data = processed_data[:10]
        
        return processed_data
    
    def exists(self, analysis_flow_id: int) -> bool:
        return analysis_flow_id in self.analysis_flows
