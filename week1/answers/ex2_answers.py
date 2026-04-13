"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "Llama 3.3 didn't output the tool format correctly, switched to Qwen 3"  # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True  # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-5cfe7d9e-a7cc-40df-9fff-81afa188f132_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "The Haymarket Vaults is confirmed for 160 guests tonight. Generate a promotional flyer with the theme 'Edinburgh AI Meetup, tech professionals, modern venue'."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user asked to check The Bow Bar for 160 vegan guests. The tool response says the capacity is 80, which is less than the required 160. So it doesn't meet the capacity constraint. The vegan requirement is met, but since the capacity isn't, the overall status is "full" and meets_all_constraints is false.

Now, the user wants to check another venue if The Bow Bar doesn't work. The next step is to pick another pub from the known list. The known venues are The Albanach
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False  # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let's see. The user wants a venue for 300 people with vegan options. The known venues are The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one:\n\n- The Albanach: Capacity 180 (too small), vegan available.\n- The Haymarket Vaults: Capacity 160 (too small), vegan available.\n- The Guilford Arms: Capacity 200 (still too small), no vegan options.\n- The Bow Bar: Capacity 80 (way too small), vegan available but status is full.\n\nNone of the venues can handle 300 people. The largest capacity is 200 at The Guilford Arms, but they don't have vegan options. The others are even smaller. So, I need to inform the user that none of the known venues meet their requirements. They might need to look for another place outside the provided list or adjust their capacity or dietary needs.\n</think>\n\nNone of the known Edinburgh venues can accommodate 300 guests with vegan options. The maximum capacity among listed venues is 200 at The Guilford Arms (which lacks vegan options), while all other venues have capacities below 180. Would you like to:\n1. Consider adjusting the guest count or dietary requirements?\n2. Explore non-listed venues?\n3. Get help with alternative event planning options?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False  # True or False

SCENARIO_3_RESPONSE = "Okay, the user is asking about the last train from Edinburgh Waverley to London tonight. Let me check the tools provided.\n\nLooking at the functions available: check_pub_availability, get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. The functions are for checking pub availability, weather, catering costs, and generating flyers. \n\nSince there's no tool for train times, I can't use any of the provided functions. I need to inform the user that I don't have access to that information. I should apologize and suggest they check a train service website or app for the most accurate details.\n</think>\n\nI don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:\n1. The ScotRail website/app\n2. National Rail Enquiries (www.nationalrail.co.uk)\n3. Train service apps like Citymapper or Google Maps\n\nWould you like me to help with anything related to Edinburgh venues, weather, or event planning instead?"

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
This is definetly an acceptable behavior. the agent failed to acomplish the task and immediately attempted to notify the user about the failure,
providing alternative questions that it can answer with the tools available.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph structure is very flexible --- just a loop between the agent thinking and tool calling. It let's
the agent to address unexpected difficulties, but also risks that it will make a wrong decision or go off-topic.

The RASA CALM on the other hand provides rails for the agent to follow and enforces. Moreover, 
it explicitly highlights the tool to get the input from the user, ensuring the agent stays on track and doesn't hallucinate.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
FILL ME IN
"""
