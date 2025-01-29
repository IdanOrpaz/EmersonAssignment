from predefined_flows import get_predefined_flows
from fastapi import APIRouter
from handlers.stackoverflow_handler import fetch_stackoverflow_data
from handlers.github_handler import fetch_github_data
from handlers.analysis_flow_handler import AnalysisFlowHandler
from typing import List


router = APIRouter()

analysis_flow_handle = AnalysisFlowHandler(get_predefined_flows()) 


@router.get("/", response_model=List[str])
def analyze(data_source_name: str, analysis_flow_id: int = None) -> List[str]:
    
    if data_source_name == "Stackoverflow":
        data = fetch_stackoverflow_data()
    elif data_source_name == "Github":
        data = fetch_github_data()
    else:
        return ["Invalid data source name, data source name doesn't exist."]
    
    if analysis_flow_id is not None:
        if not analysis_flow_handle.exists(analysis_flow_id):
            data =  ["Invalid analysis flow ID, analysis flow ID doesn't exist."]
        else: 
            data = analysis_flow_handle.apply(analysis_flow_id, data)

    return data


