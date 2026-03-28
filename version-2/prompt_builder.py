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
      "root": "root", 
      "styles": { "primaryColor": "#FF5722", "font": "Roboto" } 
    } 
  },
  { 
    "surfaceUpdate": {
      "surfaceId": "weather-surface",
      "components": [
        {
          "id": "root",
          "component": {
            "Card": {
              "child": "mainColumn"
            }
          }
        },
        {
          "id": "mainColumn",
          "component": {
            "Column": {
              "children": {
                "explicitList": [
                  "header",
                  "weatherAudio",
                  "dogImage",
                  "locationDateRow",
                  "weatherIcon",
                  "temperatureRow",
                  "conditionText",
                  "forecastList",
                  "unitToggleRow",
                  "actionRow"
                ]
              },
              "distribution": "spaceAround",
              "alignment": "center"
            }
          }
        },
        {
          "id": "header",
          "component": {
            "Text": {
              "text": {
                "literalString": "Dog Weather App"
              },
              "usageHint": "h1"
            }
          }
        },
        {
          "id": "weatherAudio",
          "component": {
            "AudioPlayer": {
              "url": { "path": "/weather/audioUrl" },
              "description": { "literalString": "Weather Soundscape" }
            }
          }
        },
        {
          "id": "dogImage",
          "component": {
            "Image": {
              "url": {
                "path": "/weather/dogImageUrl"
              },
              "fit": "cover",
              "usageHint": "smallFeature"
            }
          }
        },
        {
          "id": "locationDateRow",
          "component": {
            "Row": {
              "children": {
                "explicitList": [
                  "locationText",
                  "dateText"
                ]
              },
              "distribution": "spaceBetween",
              "alignment": "center"
            }
          }
        },
        {
          "id": "locationText",
          "component": {
            "Text": {
              "text": {
                "path": "/weather/location"
              },
              "usageHint": "h3"
            }
          }
        },
        {
          "id": "dateText",
          "component": {
            "Text": {
              "text": {
                "path": "/weather/date"
              },
              "usageHint": "caption"
            }
          }
        },
        {
          "id": "weatherIcon",
          "component": {
            "Image": {
              "url": {
                "path": "/weather/iconUrl"
              },
              "fit": "contain",
              "usageHint": "largeFeature"
            }
          }
        },
        {
          "id": "temperatureRow",
          "component": {
            "Row": {
              "children": {
                "explicitList": [
                  "currentTemp",
                  "highLowTemp"
                ]
              },
              "distribution": "center",
              "alignment": "center"
            }
          }
        },
        {
          "id": "currentTemp",
          "component": {
            "Text": {
              "text": {
                "path": "/weather/temperature"
              },
              "usageHint": "h2"
            }
          }
        },
        {
          "id": "highLowTemp",
          "component": {
            "Text": {
              "text": {
                "literalString": "H: 72°  L: 55°"
              },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "conditionText",
          "component": {
            "Text": {
              "text": {
                "path": "/weather/description"
              },
              "usageHint": "h3"
            }
          }
        },
        {
          "id": "forecastList",
          "component": {
            "List": {
              "children": {
                "template": {
                  "componentId": "forecastItem",
                  "dataBinding": "/weather/forecast"
                }
              },
              "direction": "horizontal",
              "alignment": "center"
            }
          }
        },
        {
          "id": "forecastItem",
          "component": {
            "Column": {
              "children": {
                "explicitList": [
                  "forecastDate",
                  "forecastIcon",
                  "forecastTemp",
                  "forecastCondition"
                ]
              },
              "distribution": "spaceAround",
              "alignment": "center"
            }
          }
        },
        {
          "id": "forecastDate",
          "component": {
            "Text": {
              "text": {
                "path": "./day"
              },
              "usageHint": "caption"
            }
          }
        },
        {
          "id": "forecastIcon",
          "component": {
            "Image": {
              "url": {
                "path": "./iconUrl"
              },
              "fit": "contain",
              "usageHint": "icon"
            }
          }
        },
        {
          "id": "forecastTemp",
          "component": {
            "Text": {
              "text": {
                "path": "./temperature"
              },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "forecastCondition",
          "component": {
            "Text": {
              "text": {
                "path": "./description"
              },
              "usageHint": "caption"
            }
          }
        },
        {
          "id": "unitToggleRow",
          "component": {
            "Row": {
              "children": {
                "explicitList": [
                  "btnCelsius",
                  "btnFahrenheit"
                ]
              },
              "distribution": "center",
              "alignment": "center"
            }
          }
        },
        {
          "id": "btnCelsius",
          "component": {
            "Button": {
              "child": "lblCelsius",
              "action": {
                "name": "sendText",
                "context": [
                  { "key": "text", "value": { "literalString": "@Weather Agent V2 Show weather in Celsius" } }
                ]
              }
            }
          }
        },
        {
          "id": "lblCelsius",
          "component": {
            "Text": {
              "text": { "literalString": "°C" },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "btnFahrenheit",
          "component": {
            "Button": {
              "child": "lblFahrenheit",
              "action": {
                "name": "sendText",
                "context": [
                  { "key": "text", "value": { "literalString": "@Weather Agent V2 Show weather in Fahrenheit" } }
                ]
              }
            }
          }
        },
        {
          "id": "lblFahrenheit",
          "component": {
            "Text": {
              "text": { "literalString": "°F" },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "actionRow",
          "component": {
            "Row": {
              "children": {
                "explicitList": [
                  "btnSF",
                  "btnLondon",
                  "btnRandom"
                ]
              },
              "distribution": "spaceEvenly",
              "alignment": "center"
            }
          }
        },
        {
          "id": "btnSF",
          "component": {
            "Button": {
              "child": "lblSF",
              "action": {
                "name": "sendText",
                "context": [
                  { "key": "text", "value": { "literalString": "@Weather Agent V2 What's the weather in San Francisco?" } }
                ]
              }
            }
          }
        },
        {
          "id": "lblSF",
          "component": {
            "Text": {
              "text": { "literalString": "San Francisco" },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "btnLondon",
          "component": {
            "Button": {
              "child": "lblLondon",
              "action": {
                "name": "sendText",
                "context": [
                  { "key": "text", "value": { "literalString": "@Weather Agent V2 What's the weather in London?" } }
                ]
              }
            }
          }
        },
        {
          "id": "lblLondon",
          "component": {
            "Text": {
              "text": { "literalString": "London" },
              "usageHint": "body"
            }
          }
        },
        {
          "id": "btnRandom",
          "component": {
            "Button": {
              "child": "lblRandom",
              "action": {
                "name": "sendText",
                "context": [
                  { "key": "text", "value": { "literalString": "@Weather Agent V2 Pick a random city and show its weather." } }
                ]
              }
            }
          }
        },
        {
          "id": "lblRandom",
          "component": {
            "Text": {
              "text": { "literalString": "Random City" },
              "usageHint": "body"
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
        { "key": "weather", "valueStruct": {
            "location": "New York, NY",
            "date": "Mon, Oct 24",
            "temperature": "72°",
            "description": "Partly Cloudy",
            "iconUrl": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg",
            "dogImageUrl": "https://images.dog.ceo/breeds/retriever-golden/n02099601_3004.jpg",
            "audioUrl": "https://www.soundjay.com/nature/rain-01.mp3",
            "forecast": [
              {
                "day": "Tue",
                "temperature": "68°",
                "description": "Sunny",
                "iconUrl": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/wb_sunny/default/48px.svg"
              },
              {
                "day": "Wed",
                "temperature": "65°",
                "description": "Rain",
                "iconUrl": "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/rainy/default/48px.svg"
              }
            ]
          }
        }
      ]
    } 
  }
]
---END WEATHER_CARD_EXAMPLE---
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
    -   You MUST always use the `WEATHER_CARD_EXAMPLE` template (the Colorful Weather App) for ALL weather responses, whether it is a single-day report or a multi-day forecast.
    -   This template ensures the `dogImage` is always visible.
    -   The template uses A2UI data binding (`valueStruct`). You MUST map the tool's output into the `weather` key's `valueStruct`.
    -   If a multi-day forecast is requested, populate the `forecast` array inside the `valueStruct` with the upcoming days. If only current weather is requested, you can leave the `forecast` array empty.
    
    --- TOOL & INTERACTION RULES ---
    -   **RANDOM CITY:** When a user asks for a 'random city' or clicks the 'Pick a random city' button, you MUST call `get_random_location` FIRST to get a city, then immediately call `get_weather` with that city name. DO NOT ask the user for a city name.
    -   **UNIT TOGGLES:** When the user clicks the Celsius or Fahrenheit toggle, they will ask to 'Show weather in Celsius' or 'Show weather in Fahrenheit'. You MUST call the `get_weather` tool with `unit='C'` or `unit='F'` to get the correct data. Do not attempt to convert the temperature manually.
    -   **TEMPERATURE FORMATTING:** You MUST populate the `temperature` keys as a STRING exactly as provided by the tool.
    -   **MAPPING TOOL OUTPUT:** You MUST map the tool's `description` to the `description` key in the UI, and the tool's `day` to the `day` key in the UI forecast array.
    
    --- DYNAMIC THEMING RULES ---
    -   You MUST update the `primaryColor` in the `beginRendering` message based on the condition:
        -   **Sunny/Clear:** `#FFB300` (Amber)
        -   **Rainy/Cloudy:** `#455A64` (Blue Grey)
        -   **Snowy:** `#90CAF9` (Light Blue)
        -   **Stormy:** `#311B92` (Deep Purple)
        -   **Default:** `#FF5722` (Deep Orange)

    --- WEATHER SOUNDSCAPES ---
    -   You MUST populate the `audioUrl` key in the `valueStruct` with one of these loops based on the condition. You MUST NEVER leave it empty.
        -   **Rainy/Stormy:** `https://www.soundjay.com/nature/rain-01.mp3`
        -   **Cloudy/Snowy:** `https://www.soundjay.com/nature/sounds/wind-1.mp3`
        -   **Sunny/Clear/Default:** `https://www.soundjay.com/nature/sounds/wind-chime-1.mp3`

    --- DYNAMIC ICON RULES ---
    -   You MUST populate the `iconUrl` and the forecast `iconUrl` keys by selecting one of these exact URLs based on the condition:
        -   **Sunny/Clear:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/wb_sunny/default/48px.svg`
        -   **Rainy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/rainy/default/48px.svg`
        -   **Cloudy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg`
        -   **Snowy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/ac_unit/default/48px.svg`
        -   **Stormy:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/thunderstorm/default/48px.svg`
        -   **Default:** `https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/cloud/default/48px.svg`

    {WEATHER_UI_EXAMPLE}

    ---BEGIN A2UI JSON SCHEMA---
    {A2UI_SCHEMA}
    ---END A2UI JSON SCHEMA---
    """
