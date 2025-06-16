from agents.RA import claim_assistant, EmployeeClaimState, ClaimRequestDeps
from langgraph.graph import StateGraph, START, END

# Claim assistant agent node
async def run_claim_assistant(state: EmployeeClaimState) -> EmployeeClaimState:
    """Run the claim assistant agent and update state."""
    print(f"📢 Claim Assistant: Fetching updates for '{state.messages}'...")

    try:
        # Create dependencies
        claim_deps = ClaimRequestDeps(category="general", urgency_level=3)

        # Create prompt
        prompt = f"""
        An employee asked: {state.messages}
        Provide relevant discount and service updates that apply to company trips or employee benefits.
        """

        # Run the agent
        result = await claim_assistant.run(prompt, deps=claim_deps)

        # Extract results with fallback
        discount_updates = None
        service_updates = None

        if hasattr(result, 'data') and result.data:
            discount_updates = result.data.discount_updates
            service_updates = result.data.service_updates

        if not discount_updates:
            discount_updates = "Discounts include 10% off on business-class travel and preferred hotel rates."

        if not service_updates:
            service_updates = "Services include airport shuttle booking and automated meal reimbursements."

        # Update state
        updated_state = state.model_copy(update={
            "current_agent": "claim_assistant",
            "discount_updates": discount_updates,
            "service_updates": service_updates
        })

    except Exception as e:
        print(f"❌ Claim Assistant Error: {e}")
        # Fallback state
        updated_state = state.model_copy(update={
            "current_agent": "claim_assistant",
            "discount_updates": "Standard employee discounts apply for travel and meals.",
            "service_updates": "Use the corporate dashboard for available support services."
        })

    print("✅ Claim assistant completed.")
    return updated_state

def create_workflow():
    """Create and return the simplified claim assistant workflow."""
    workflow = StateGraph(EmployeeClaimState)

    # Add nodes
    workflow.add_node("claim_assistant", run_claim_assistant)

    # Define flow
    workflow.add_edge(START, "claim_assistant")
    workflow.add_edge("claim_assistant", END)

    return workflow.compile()

async def run_workflow(query: str) -> EmployeeClaimState:
    """Run the workflow for the given query."""
    print(f"🚀 Starting claim workflow for query: '{query}'")

    app = create_workflow()

    initial_state = EmployeeClaimState(
        messages=query,
        current_agent=None,
        discount_updates=None,
        service_updates=None,
        task_complete=False
    )

    result = await app.ainvoke(initial_state)

    print(f"🎉 Workflow completed!")
    return result

async def main():
    """Demo run for the AI claiming assistant."""
    query = "Are there any travel discounts for attending a conference in KL?"
    final_state = await run_workflow(query)

    print("\n" + "="*50)
    print("CLAIMING ASSISTANT RESULTS")
    print("="*50)
    print(f"\n📝 QUERY: {final_state.messages}")
    print(f"\n🎁 DISCOUNT UPDATES:\n{final_state.discount_updates}")
    print(f"\n🛠️ SERVICE UPDATES:\n{final_state.service_updates}")
    print(f"\n✅ Task Complete: {final_state.task_complete}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
