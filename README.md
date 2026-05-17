# 🏏 Captain Cool — Multi-Agent IPL Match Strategist

**Captain Cool** is an agentic AI system that acts as a virtual IPL captain—making real-time, high-stakes tactical decisions in live matches (e.g., bowling changes, field setups, impact player timing) with the strategic mind of legendary captains like MS Dhoni or Rohit Sharma.

Built completely during a high-speed, 3-hour vibe-coding session inside **Google Antigravity** using the official **Google GenAI SDK** and powered by **Gemini 2.5 Flash**.

---

## 🚀 Key Features & Hackathon Requirements Met

### 🧠 1. Three-Agent Collaborative Architecture (Mandatory)
The system orchestrates a multi-turn reasoning loop across three distinct, specialized Gemini-powered agents, ensuring deep collaboration rather than a single chatbot model wearing multiple hats:
* **🕵️ Match Analyst:** Parses the live match state, pitch conditions, venue context, and executes specialized tools to find historical trend baselines.
* **💡 Strategist:** Acts as the team captain. Formulates the core tactical blueprint (e.g., spinning choke, aggressive pace match-ups) using authentic cricketing logic.
* **🔥 Devil's Advocate:** Stress-tests the captain's plan. Actively challenges assumptions by factoring in constraints like boundary sizes, ground dimensions, and heavy dew factors.

### 🛠️ 2. True Gemini Function Calling (Mandatory)
The system leverages native tool use via the Google GenAI SDK. The **Match Analyst** agent dynamically calls local data tools (`get_matchup_stats`) to fetch real historic trends (such as batsman averages against specific bowling variations at a particular venue) to feed data into the strategy room.

### 🔄 3. Multi-Turn Reasoning Loop (Mandatory)
The application doesn't just return a raw response; it unrolls the internal debate. The Strategist proposes an action, the Devil's Advocate highlights a key weakness, the Strategist refines the execution, and a final definitive captain's decree is reached.

### 📢 4. Cricket-Language Explainability (Mandatory)
Decisions are rendered in authentic cricketing vernacular ("the leggie is wasted against a left-handed pinch-hitter on a short boundary with dew slicking the ball") instead of sterile machine learning metrics, making it instantly readable for fans and coaches alike.

---

## 🛠️ Tech Stack

* **Core Orchestration:** Google GenAI Python SDK (`google-genai`)
* **Model:** `gemini-2.5-flash` (Optimized for fast multi-turn loops and tool-use precision)
* **IDE Framework:** Google Antigravity (Agentic workspace tracking, prompts prototyping, and auto-compositions)
* **Frontend Dashboard:** Streamlit (Premium dark-mode dashboard separating live data inputs and the agentic debate room layout)

---

## 📦 Project Structure

```text
captain_cool/
│
├── .antigravity/          # Google Antigravity environment traces
├── app.py                 # Premium Streamlit web frontend & UI layouts
├── agents.py              # Multi-agent definition, system prompts & debate loops
├── models.py              # Pydantic data schemas defining rigid match states
├── tools.py               # Matchup data analytics tools used for Gemini Function Calling
└── README.md              # Documentation
