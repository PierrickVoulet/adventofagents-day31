"""A2UI Prompt Builder and Templates.

This module contains the UI templates (A2UI JSON) and the logic to inject UI-specific 
instructions and schemas into the agent's system prompt.
"""

from a2ui_schema import A2UI_SCHEMA

# ------------------------------------------------------------------------------
# 1. UI EXAMPLES (TEMPLATES)
# These constants define the data structure and component layout for specific UI surfaces.
# ------------------------------------------------------------------------------

WEATHER_UI_EXAMPLE = """
---BEGIN WEATHER_CARD_EXAMPLE---
[
  { 
    "beginRendering": { 
      "surfaceId": "weather-surface", 
      "root": "root-card", 
      "styles": { "primaryColor": "#003366", "font": "Roboto" } 
    } 
  },
  { 
    "surfaceUpdate": {
      "surfaceId": "weather-surface",
      "components": [
        { "id": "root-card", "component": { "Card": { "child": "main-layout" } } },
        { 
          "id": "main-layout", 
          "component": { 
            "Column": { 
              "children": { "explicitList": ["broadcast-header", "divider-main", "content-row"] } 
            } 
          } 
        },
        
        { 
          "id": "broadcast-header", 
          "component": { 
            "Row": { 
              "children": { "explicitList": ["location-heading"] },
              "distribution": "start"
            } 
          } 
        },
        { "id": "location-heading", "component": { "Text": { "usageHint": "h2", "text": { "path": "location" } } } },
        
        { "id": "divider-main", "component": { "Divider": { "axis": "horizontal" } } },
        
        { 
          "id": "content-row", 
          "component": { 
            "Row": { 
              "children": { "explicitList": ["stats-column", "icon-container"] },
              "distribution": "spaceBetween",
              "alignment": "center"
            } 
          } 
        },
        
        { 
          "id": "stats-column", 
          "weight": 1,
          "component": { 
            "Column": { 
              "children": { "explicitList": ["temp-text", "condition-text", "pun-text"] } 
            } 
          } 
        },
        { "id": "temp-text", "component": { "Text": { "usageHint": "h1", "text": { "path": "temperature" } } } },
        { "id": "condition-text", "component": { "Text": { "usageHint": "body", "text": { "path": "description" } } } },
        { "id": "pun-text", "component": { "Text": { "usageHint": "body", "text": { "path": "pun" }, "styles": { "italic": true, "textColor": "#555555" } } } },
        
        { 
          "id": "icon-container", 
          "component": { 
            "Image": { 
              "url": { "path": "weatherIconUrl" }, 
              "usageHint": "icon", 
              "fit": "contain" 
            } 
          } 
        }
      ]
    } 
  },
  { 
    "dataModelUpdate": {
      "surfaceId": "weather-surface",
      "path": "/",
      "contents": [
        { "key": "location", "valueString": "New York, NY" },
        { "key": "temperature", "valueString": "72°" },
        { "key": "description", "valueString": "Partly Cloudy" },
        { "key": "pun", "valueString": "I'm 'cloud' nine after seeing this weather!" },
        { "key": "weatherIconUrl", "valueString": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/24px.svg" }
      ]
    } 
  }
]
---END WEATHER_CARD_EXAMPLE---
"""

FORECAST_UI_EXAMPLE = """
---BEGIN FORECAST_CARD_EXAMPLE---
[
  { 
    "beginRendering": { 
      "surfaceId": "forecast-surface", 
      "root": "root-card", 
      "styles": { "primaryColor": "#003366", "font": "Roboto" } 
    } 
  },
  { 
    "surfaceUpdate": {
      "surfaceId": "forecast-surface",
      "components": [
        { "id": "root-card", "component": { "Card": { "child": "main-layout" } } },
        { 
          "id": "main-layout", 
          "component": { 
            "Column": { 
              "children": { "explicitList": ["location-heading", "divider-main", "forecast-list"] } 
            } 
          } 
        },
        { 
          "id": "location-heading", 
          "component": { 
            "Text": { "usageHint": "h2", "text": { "path": "location" } } 
          } 
        },
        { "id": "divider-main", "component": { "Divider": { "axis": "horizontal" } } },
        { 
          "id": "forecast-list", 
          "component": { 
            "Column": { 
              "children": { "explicitList": ["day-1-row", "day-2-row", "day-3-row"] } 
            } 
          } 
        },
        
        { 
          "id": "day-1-row", 
          "component": { 
            "Row": { 
              "children": { "explicitList": ["day-1-name", "day-1-temp", "day-1-icon"] },
              "distribution": "spaceBetween",
              "alignment": "center"
            } 
          } 
        },
        { "id": "day-1-name", "weight": 1, "component": { "Text": { "usageHint": "body", "text": { "path": "day1Name" } } } },
        { "id": "day-1-temp", "weight": 1, "component": { "Text": { "usageHint": "h3", "text": { "path": "day1Temp" } } } },
        { "id": "day-1-icon", "component": { "Image": { "url": { "path": "day1IconUrl" }, "usageHint": "icon", "fit": "contain" } } },
        
        { 
          "id": "day-2-row", 
          "component": { 
            "Row": { 
              "children": { "explicitList": ["day-2-name", "day-2-temp", "day-2-icon"] },
              "distribution": "spaceBetween",
              "alignment": "center"
            } 
          } 
        },
        { "id": "day-2-name", "weight": 1, "component": { "Text": { "usageHint": "body", "text": { "path": "day2Name" } } } },
        { "id": "day-2-temp", "weight": 1, "component": { "Text": { "usageHint": "h3", "text": { "path": "day2Temp" } } } },
        { "id": "day-2-icon", "component": { "Image": { "url": { "path": "day2IconUrl" }, "usageHint": "icon", "fit": "contain" } } },
        
        { 
          "id": "day-3-row", 
          "component": { 
            "Row": { 
              "children": { "explicitList": ["day-3-name", "day-3-temp", "day-3-icon"] },
              "distribution": "spaceBetween",
              "alignment": "center"
            } 
          } 
        },
        { "id": "day-3-name", "weight": 1, "component": { "Text": { "usageHint": "body", "text": { "path": "day3Name" } } } },
        { "id": "day-3-temp", "weight": 1, "component": { "Text": { "usageHint": "h3", "text": { "path": "day3Temp" } } } },
        { "id": "day-3-icon", "component": { "Image": { "url": { "path": "day3IconUrl" }, "usageHint": "icon", "fit": "contain" } } }
      ]
    } 
  },
  { 
    "dataModelUpdate": {
      "surfaceId": "forecast-surface",
      "path": "/",
      "contents": [
        { "key": "location", "valueString": "New York, NY" },
        { "key": "day1Name", "valueString": "Today" },
        { "key": "day1Temp", "valueString": "72°" },
        { "key": "day1IconUrl", "valueString": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/wb_sunny/default/48px.svg" },
        { "key": "day2Name", "valueString": "Day 2" },
        { "key": "day2Temp", "valueString": "68°" },
        { "key": "day2IconUrl", "valueString": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg" },
        { "key": "day3Name", "valueString": "Day 3" },
        { "key": "day3Temp", "valueString": "75°" },
        { "key": "day3IconUrl", "valueString": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/wb_sunny/default/48px.svg" }
      ]
    } 
  }
]
---END FORECAST_CARD_EXAMPLE---
"""

# ------------------------------------------------------------------------------
# 2. PROMPT GENERATOR
# ------------------------------------------------------------------------------

def get_ui_instruction(base_instruction: str) -> str:
    """Combines a base agent instruction with A2UI formatting rules and schemas.
    
    Args:
        base_instruction: The primary persona and task description for the agent.
        
    Returns:
        A comprehensive system prompt including UI requirements and icon rules.
    """
    return f"""
    {base_instruction}

    Your final output MAY contain a a2ui UI JSON response. 
    
    CRITICAL RULES:
    1. If you are providing a weather report or status update after a tool call, you MUST provide the A2UI UI JSON response.
    2. If you are only responding to general conversation or asking a question, DO NOT include the JSON or the delimiter.

    To generate the response:
    1.  Provide your conversational text first.
    2.  If providing a UI, append the delimiter `---a2ui_JSON---` followed by the JSON.
    3.  The JSON MUST be a list of A2UI messages and validate against the schema provided below.

    --- UI TEMPLATE RULES ---
    -   When providing a single-day weather report, you MUST use the `WEATHER_CARD_EXAMPLE` template.
    -   When providing a multi-day forecast, you MUST use the `FORECAST_CARD_EXAMPLE` template. You MUST duplicate the row structures (`day-X-row`, `day-X-name`, `day-X-temp`, `day-X-icon`) to match the exact number of days in the requested forecast.
    -   **TEMPERATURE FORMATTING:** You MUST populate the `temperature` (or `dayXTemp`) key as a STRING. It MUST include the degree symbol (e.g., "72°" or "25°C"). Do not use raw numbers.
    -   Populate the `location`, `description`, `pun`, and any `dayXName` keys based on the tool output or your knowledge of the location.
    
    --- DYNAMIC ICON RULES ---
    -   You MUST populate the `weatherIconUrl` (or `dayXIconUrl`) key by selecting one of these exact URLs based on the condition:
        -   **Sunny/Clear:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/wb_sunny/default/48px.svg`
        -   **Rainy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/rainy/default/48px.svg`
        -   **Cloudy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg`
        -   **Snowy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/ac_unit/default/48px.svg`
        -   **Stormy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/thunderstorm/default/48px.svg`
        -   **Default:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg`

    {WEATHER_UI_EXAMPLE}
    
    {FORECAST_UI_EXAMPLE}

    ---BEGIN A2UI JSON SCHEMA---
    {A2UI_SCHEMA}
    ---END A2UI JSON SCHEMA---
    """
