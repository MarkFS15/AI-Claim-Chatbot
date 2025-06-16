from pydantic_ai import Agent, RunContext
from pydantic import BaseModel
from shared_models import EmployeeClaimState
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
    summary: Optional[str] = None  # <-- Added summary field

@dataclass
class SummaryDeps:
    """Dependencies for the summary agent."""
    max_length: int = 150  # or adjust based on UI use

# Summary system prompt
system_prompt = """
You are an assistant that summarizes updates for employees regarding available discounts and services.

Given the fields 'discount_updates' and 'service_updates', generate a concise summary (e.g., 1-2 sentences)
highlighting the most important benefits.

IMPORTANT: You must return a valid EmployeeClaimState object with:
- summary: the generated summary
- current_agent: set to "summary_agent"
- task_complete: set to True

Don't include unnecessary marketing fluff.
Be concise, clear, and useful to a busy employee.
"""

summary_agent = Agent(
    model=model,
    deps_type=SummaryDeps,
    output_type=EmployeeClaimState,
    system_prompt=system_prompt,
    retries=2
)

# Optional tool simulation
# @summary_agent.tool_plain
# async def summarize_updates(discounts: str, services: str) -> str:
#     return f"Summary: Discounts include {discounts[:40]}... and services include {services[:40]}..."
