# from pydantic_ai import Agent
# from pydantic import BaseModel
# from shared_models import EmployeeClaimState
# from dataclasses import dataclass
# from typing import Optional
# from utils import get_model

# model = get_model()

# class EmployeeClaimState(BaseModel):
#     messages: str
#     current_agent: Optional[str] = None
#     discount_updates: Optional[str] = None
#     service_updates: Optional[str] = None
#     recommendations: Optional[str] = None
#     task_complete: bool = False

# @dataclass
# class RecoDeps:
#     trip_type: str = "business"
#     destination: str = "local"

# system_prompt = """
# You are an AI recommendation engine.

# Based on the employee’s message and available services, suggest **additional benefits or perks** 
# they may not know about — like lounge access, wellness packages, bonus credits, or tips.

# IMPORTANT: Return EmployeeClaimState with:
# - recommendations: helpful suggestions
# - current_agent: "recommendation_agent"
# """

# recommendation_agent = Agent(
#     model=model,
#     deps_type=RecoDeps,
#     output_type=EmployeeClaimState,
#     system_prompt=system_prompt,
#     retries=1
# )
