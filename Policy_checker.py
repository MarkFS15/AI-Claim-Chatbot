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
#     policy_issues: Optional[str] = None
#     task_complete: bool = False

# @dataclass
# class PolicyDeps:
#     department: str = "General"
#     budget_limit: int = 500

# system_prompt = """
# You are a policy compliance agent.

# Your job is to validate whether the employee's requested benefits and services fall within policy.
# If there’s a violation, clearly state what it is (e.g., budget limits, service restrictions, approval required).

# IMPORTANT: Return EmployeeClaimState with:
# - policy_issues: list any potential policy violations or concerns.
# - current_agent: "policy_checker_agent"
# """

# policy_checker_agent = Agent(
#     model=model,
#     deps_type=PolicyDeps,
#     output_type=EmployeeClaimState,
#     system_prompt=system_prompt,
#     retries=1
# )
