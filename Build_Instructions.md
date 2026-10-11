## Objective

You are to act as an autonomous business engineering agent. Your goal is to generate a digital product, build a high-converting landing page for it, deploy that page to production, and construct an automated social media distribution engine in Python.

## Phase 1: Digital Asset Generation (The Product)

1. Research and define a high-demand professional niche (e.g., "100 Advanced AI Prompts for B2B Tech Marketers" or "Standard Operating Procedures for Real Estate").
2. Generate the complete content for this product using your internal knowledge base.
3. Format the final output as a clean, highly readable Markdown file (`product_asset.md`) and save it to the current workspace.

## Phase 2: Landing Page Engineering & Deployment

1. Initialize a new Next.js project in a subdirectory called `landing-page`.
2. Build a modern, single-page landing page that includes a hero section with a strong value proposition, a features/benefits breakdown, and a Gumroad checkout embed button (use a placeholder Gumroad URL for now).
3. **Deployment via Vercel:** If the Vercel plugin is available in this environment, inject the Vercel session context and use the `/vercel-plugin:deploy prod` slash command to instantly push the site live. Connect the project to GitHub so Vercel automatically provides Preview Deployment URLs and updates the custom domain on future commits.


4. **Alternative Deployment via Kuberns:** If Vercel is not used, ensure `.gitignore` excludes `.env` and `node_modules`, then push the repository to GitHub. From there, Kuberns' agentic AI will automatically analyze the repository, detect the Next.js runtime and build commands, and deploy the application to a production URL.



## Phase 3: Social Media Distribution Engine

We need a system that automatically drives traffic to the landing page. You will build this using a unified API approach so we don't have to manage separate integrations for X, LinkedIn, etc.

**Option A: Python Automation Engine (Zernio SDK)**

1. In a new subdirectory called `distribution_engine`, initialize a Python environment (Python 3.8 or higher is required).


2. We will use the Zernio unified social media API. Install the required package by executing `pip install zernio-sdk` in the terminal.


3. Create a `.env` file and add the placeholder `ZERNIO_API_KEY="your_api_key_goes_here"`. Ensure `.env` is added to `.gitignore` so the key is never hardcoded and compromised in version control.


4. Write a Python script (`auto_poster.py`) that reads a CSV of promotional tips (which you must also generate) and publishes them. Use the following integration pattern from the Zernio SDK:



```python
import os
from zernio import Zernio

# The SDK reads ZERNIO_API_KEY from the environment automatically
client = Zernio(api_key=os.environ["ZERNIO_API_KEY"])

result = client.posts.create_post(
    content="Check out this new template!",
    platforms=[
        {"platform": "linkedin", "accountId": "YOUR_ACCOUNT_ID"},
        {"platform": "x", "accountId": "YOUR_ACCOUNT_ID"}
    ],
    publish_now=True
)
print(f"Posted successfully! {result.post['_id']}")

```

**Option B: Direct MCP Integration**
If you have Model Context Protocol (MCP) servers active in this workspace, skip the Python script and integrate directly:

1. Connect to the Buffer MCP server, which provides a single GraphQL endpoint to draft and schedule posts across 11 different platforms natively from this interface.


2. Alternatively, utilize Typefully Skills, which allows you to execute commands like "Draft a tweet about the new template" or "Schedule my draft for tomorrow morning" directly against their API.



## Execution Constraints

* Use Sandbox Mode for all terminal executions and script testing.
* Provide a summary of the live URLs and file paths once all steps are completed.

---