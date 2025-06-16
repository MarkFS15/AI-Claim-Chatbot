from pydantic_ai import Agent, RunContext
from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_model

model = get_model()

# Shared state between agents
class EmployeeClaimState(BaseModel):
    """Shared state containing employee query and information results."""
    messages: str
    current_agent: Optional[str] = None
    task_complete: bool = False
    discount_updates: Optional[str] = None
    service_updates: Optional[str] = None

@dataclass
class ClaimRequestDeps:
    """Dependencies for the employee claim request agent."""
    category: str = "general"  # e.g., 'flights', 'hotels', 'meals'
    urgency_level: int = 3     # 1 = low, 5 = high

system_prompt = """
You are an assistant for a corporate AI claiming system.
Your job is to help employees stay informed about the **latest discounts, promotions, and services** available 
for company activities or business trips.

Your response must always include:
- Relevant **discounts or benefits** for employees (e.g., travel deals, hotel perks, food subsidies)
- New **services or corporate partnerships** the company has enabled
- Information specific to their **requested category**, if provided

IMPORTANT: You must return a valid EmployeeClaimState object with:
- messages: keep the original user query
- current_agent: set to "claim_assistant"
- discount_updates: summarize available discounts/promotions
- service_updates: describe available services or updates
- task_complete: set to False

Be thorough and clear. Avoid unnecessary details unrelated to employee benefits.
"""

claim_assistant = Agent(
    model=model,
    deps_type=ClaimRequestDeps,
    output_type=EmployeeClaimState,
    system_prompt=system_prompt,
    retries=2
)

# Example tool if you want to simulate integration later:
# @claim_assistant.tool_plain
# async def fetch_corporate_discounts(category: str) -> str:
#     """Simulate a corporate discounts fetch for the given category."""
#     return f"Mock discounts found for category: {category}"
