"""Gemini agent for A2UI sample."""

import json
import os
import urllib.parse
import urllib.request
from a2a import types
from a2ui_examples import CONTACT_UI_EXAMPLES
import a2ui_schema
from google.adk import agents


# --- DEFINE YOUR TOOLS HERE ---
def get_contact_info(name: str = None) -> str:
  """Gets contact information for a person.

  Args:
      name: The name of the person to look up. If None, returns a list of
        suggested contacts.

  Returns:
      JSON string containing contact details.
  """
  access_token = os.environ.get("ACCESS_TOKEN")
  if not access_token:
    return "[]"

  try:
    if name:
      query = urllib.parse.quote(name)
      url = f"https://people.googleapis.com/v1/people:searchContacts?query={query}&readMask=names,emailAddresses,phoneNumbers,organizations,locations"
    else:
      url = "https://people.googleapis.com/v1/people/me/connections?readMask=names,emailAddresses,phoneNumbers,organizations,locations&pageSize=10"

    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(req) as response:
      data = json.loads(response.read())

      contacts = []
      items = data.get("results", data.get("connections", []))
      for item in items:
        person = item.get("person", item)

        name_val = person.get("names", [{}])[0].get("displayName", "Unknown")
        email_val = person.get("emailAddresses", [{}])[0].get("value", "")
        phone_val = person.get("phoneNumbers", [{}])[0].get("value", "")
        
        orgs = person.get("organizations", [{}])
        org = orgs[0] if orgs else {}
        title_val = org.get("title", "")
        team_val = org.get("department", "")

        locs = person.get("locations", [{}])
        loc = locs[0] if locs else {}
        loc_val = loc.get("value", "Unknown")

        contacts.append({
            "name": name_val,
            "title": title_val,
            "team": team_val,
            "location": loc_val,
            "email": email_val,
            "mobile": phone_val,
            "calendar": "Available"
        })

      if name and len(contacts) >= 1:
        return json.dumps(contacts[0])
      return json.dumps(contacts)
  except Exception as e:
    print(f"Error calling People API: {e}")
    return "[]"


def get_ui_prompt(examples: str) -> str:
  """Constructs the full prompt with UI instructions, rules, examples, and schema."""

  formatted_examples = examples

  return f"""
    You are a helpful contact lookup assistant. Your final output MUST be a a2ui UI JSON response.

    To generate the response, you MUST follow these rules:
    1.  Your response MUST be in two parts, separated by the delimiter: `---a2ui_JSON---`.
    2.  The first part is your conversational text response (e.g., "Here is the contact you requested...").
    3.  The second part is a single, raw JSON object which is a list of A2UI messages.
    4.  The JSON part MUST validate against the A2UI JSON SCHEMA provided below.
    5.  Buttons that represent the main action on a card or view (e.g., 'Follow', 'Email', 'Search') SHOULD include the `"primary": true` attribute.

    --- UI TEMPLATE RULES ---
    -   **For finding contacts (e.g., "Who is Alex Jordan?"):**
        a.  You MUST call the `get_contact_info` tool.
        b.  If the tool returns a **single contact**, you MUST use the `CONTACT_CARD_EXAMPLE` template. Populate the `dataModelUpdate.contents` with the contact's details (name, title, email, etc.).
        c.  If the tool returns **multiple contacts**, you MUST use the `CONTACT_LIST_EXAMPLE` template. Populate the `dataModelUpdate.contents` with the list of contacts for the "contacts" key.
        d.  If the tool returns an **empty list**, respond with text only and an empty JSON list: "I couldn't find anyone by that name.---a2ui_JSON---[]"

    -   **For handling a profile view (e.g., "WHO_IS: Alex Jordan..."):**
        a.  You MUST call the `get_contact_info` tool with the specific name.
        b.  This will return a single contact. You MUST use the `CONTACT_CARD_EXAMPLE` template.

    -   **For handling actions (e.g., "follow_contact"):**
        a.  You MUST use the `FOLLOW_SUCCESS_EXAMPLE` template.
        b.  This will render a new card with a "Successfully Followed" message.
        c.  Respond with a text confirmation like "You are now following this contact." along with the JSON.

    {formatted_examples}

    ---BEGIN A2UI JSON SCHEMA---
    {a2ui_schema.A2UI_SCHEMA}
    ---END A2UI JSON SCHEMA---
    """


class GeminiAgent(agents.LlmAgent):
  """An agent powered by the Gemini model via Vertex AI."""

  # --- AGENT IDENTITY ---
  name: str = "a2uicontact"
  description: str = "A contact lookup assistant with rich UI."

  def __init__(self, **kwargs):
    print("Initializing A2UI GeminiAgent...")

    # In a real deployment, base_url might come from env or config
    instructions = get_ui_prompt(CONTACT_UI_EXAMPLES)

    # --- REGISTER YOUR TOOLS HERE ---
    tools = [get_contact_info]

    super().__init__(
        model=os.environ.get("MODEL", "gemini-2.5-flash"),
        instruction=instructions,
        tools=tools,
        **kwargs,
    )

  def create_agent_card(self, agent_url: str) -> "AgentCard":
    return types.AgentCard(
        name=self.name,
        description=self.description,
        version="1.0.0",
        url=agent_url,
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        capabilities=types.AgentCapabilities(streaming=True),
        skills=[
            types.AgentSkill(
                id="contact_lookup",
                name="Contact Lookup",
                description="Find contacts and view their details.",
                tags=["contact", "directory"],
                examples=["Who is Alex Jordan?", "Find software engineers"]
            )
        ]
    )