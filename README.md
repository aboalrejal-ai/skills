<p align="center">
  <img src="https://raw.githubusercontent.com/aboalrejal-ai/skills/main/assets/logo.png" alt="Abo Alrejal Skills Logo" width="120" style="border-radius: 50%" error="this.src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'"/>
</p>

# <p align="center">🌱 Unified Agent Skills Hub</p>

### <p align="center">*Build high-quality software faster.*</p>

<p align="center">
  *An open source library of 1738+ modular AI Skills, System Experts, and Developer Plugins that integrate with Claude Code, Antigravity, Cursor, and Windsurf.*
</p>

<p align="center">
  <a href="https://github.com/aboalrejal-ai/skills"><img src="https://img.shields.io/github/v/release/aboalrejal-ai/skills?color=blue&logo=github&style=flat-square" alt="Release" /></a>
  <a href="https://github.com/aboalrejal-ai/skills/stargazers"><img src="https://img.shields.io/github/stars/aboalrejal-ai/skills?style=social" alt="Stars" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License" /></a>
  <a href="docs/skill-registry.md"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue?style=flat-square" alt="Docs" /></a>
</p>

---

## Table of Contents

* 🤔 [What is Abo Alrejal Skills?](#-what-is-abo-alrejal-skills)
* ⚡ [Get Started & Installation](#-get-started--installation)
* 🌐 [Community & Supported AI Platforms](#-community--supported-ai-platforms)
* 💻 [Core Commands Reference](#-core-commands-reference)
* 📁 [The 10 Canonical Categories](#-the-10-canonical-categories)
* 🧬 [Core Biology Development Paths](#-core-biology-development-paths)
* ⚙️ [System Requirements & Paths](#-system-requirements--paths)
* 🤝 [Support & Feedback](#-support--feedback)
* 📄 [License](#-license)

---

## 🤔 What is Abo Alrejal Skills?

The **Unified Agent Skills Hub** (aboalrejal-ai/skills) is a premium, production-grade library containing **1738 modular skills, agent tools, and platform instructions**. 

By loading these specialized configurations into your agentic IDE or terminal co-programmer (such as Antigravity, Claude Code, or Cursor), you equip your AI partner with the exact instructions, schemas, and guardrails necessary to perform complex, multi-step actions autonomously—eliminating "vibe coding" and ensuring predictable, high-quality development outcomes.

---

## ⚡ Get Started & Installation

Loading these modular skills into your favorite AI developer environment is extremely straightforward.

### Method A: Direct Clone (Recommended for Local Customization)
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aboalrejal-ai/skills.git
   cd skills
   ```
2. **Copy your desired skill folder to your agent directory:**
   For example, loading `seo-content-writer` into **Claude Code**:
   ```bash
   mkdir -p ~/.claude/skills/seo-content-writer
   cp -r skills/marketing-and-seo/seo-content-writer/* ~/.claude/skills/seo-content-writer/
   ```

### Method B: Spec-Driven Command Line Setup
Run our validator tool to ensure all rules are properly loaded into your environment:
```bash
bash tools/validate-skill.sh skills/marketing-and-seo/seo-content-writer/SKILL.md
```

---

## 🌐 Community & Supported AI Platforms

This repository is fully optimized and structured to work across all modern agentic AI and IDE co-programming platforms:
*   **Antigravity IDE** (Highly recommended / full visual integration)
*   **Claude Code** (Anthropic CLI / advanced console agent)
*   **Cursor** (Premium AI Editor / multi-turn custom agents)
*   **Windsurf** (Next-gen AI IDE / interactive context engine)
*   **Open Code** (Open source editor / sandboxed CLI)
*   **Google Gemini CLI & Agents** (Gemini Live API integrations)
*   **GitHub Copilot / Copilot Agents** (Enterprise workgroup bots)

---

## 💻 Core Commands Reference

When a skill is loaded into your AI agent environment, it is bound to a dedicated **slash command** or **intent prompt**. The agent invokes the skill by matching this trigger.

Essential commands for the core development and automation workflows:

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/coding-agent` | [`coding-agent`](skills/ai-and-agents/coding-agent/SKILL.md) | Delegate complex coding tasks to Codex, Claude Code, or Pi agents via background processes |
| `/seo-content-writer` | [`seo-content-writer`](skills/marketing-and-seo/seo-content-writer/SKILL.md) | Create high-ranking, SEO-optimized articles with automated keyword structures |
| `/mcp-builder` | [`mcp-builder`](skills/ai-and-agents/mcp-builder/SKILL.md) | Develop custom Model Context Protocol (MCP) servers in Python or TypeScript |
| `/ai-ready` | [`ai-ready`](skills/ai-and-agents/ai-ready/SKILL.md) | Bootstrap any repository with custom AI rules, developer configs, and guidelines |
| `/security-review` | [`security-review`](skills/security-and-compliance/security-review/SKILL.md) | Perform multi-axis security scans and dependency vulnerability auditing |
| `/pdf` | [`pdf`](skills/document-processing/pdf/SKILL.md) | Perform programmatic PDF creation, extraction, splitting, merging, and OCR scanning |

---

## 📁 The 10 Canonical Categories

Here is the fully cataloged list of all **1738 active skills** currently supported in the ecosystem. Every single skill is listed in a structured command table under its parent category.

### 🤖 AI & Intelligent Agents
> *Agent orchestration, prompts, subagents, and model-specific MCP servers for Claude Code, Antigravity, Cursor, and Windsurf.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Dispatching Parallel Agents` | [`Dispatching Parallel Agents`](skills/ai-and-agents/Dispatching Parallel Agents/SKILL.md) | Use multiple Claude agents to investigate and fix independent problems concurrently. |
| `/Subagent-Driven Development` | [`Subagent-Driven Development`](skills/ai-and-agents/Subagent-Driven Development/SKILL.md) | Execute implementation plan by dispatching fresh subagent for each task, with code review between tasks. |
| `/Testing Skills With Subagents` | [`Testing Skills With Subagents`](skills/ai-and-agents/Testing Skills With Subagents/SKILL.md) | RED-GREEN-REFACTOR for process documentation - baseline without skill, write addressing failures, iterate closing loopholes. |
| `/acreadiness-assess` | [`acreadiness-assess`](skills/ai-and-agents/acreadiness-assess/SKILL.md) | Run the AgentRC readiness assessment on the current repository and produce a static HTML dashboard at reports/index.html. |
| `/acreadiness-policy` | [`acreadiness-policy`](skills/ai-and-agents/acreadiness-policy/SKILL.md) | Help the user pick, write, or apply an AgentRC policy. |
| `/add-educational-comments` | [`add-educational-comments`](skills/ai-and-agents/add-educational-comments/SKILL.md) | Add educational comments to the file specified, or prompt asking for file to comment if one is not provided. |
| `/agent-framework-azure-ai-py` | [`agent-framework-azure-ai-py`](skills/ai-and-agents/agent-framework-azure-ai-py/SKILL.md) | Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). |
| `/agent-governance` | [`agent-governance`](skills/ai-and-agents/agent-governance/SKILL.md) | Patterns and techniques for adding governance, safety, and trust controls to AI agent systems. |
| `/agent-owasp-compliance` | [`agent-owasp-compliance`](skills/ai-and-agents/agent-owasp-compliance/SKILL.md) | Check any AI agent codebase against the OWASP Agentic Security Initiative (ASI) Top 10 risks. |
| `/agent-platform-deploy` | [`agent-platform-deploy`](skills/ai-and-agents/agent-platform-deploy/SKILL.md) | Deploy open models or custom weights from Model Garden to Agent Platform endpoints, check deployment status, verify. |
| `/agent-platform-prompt-management` | [`agent-platform-prompt-management`](skills/ai-and-agents/agent-platform-prompt-management/SKILL.md) | Manages and orchestrates prompts in Agent Platform. |
| `/agent-platform-rag-engine-management` | [`agent-platform-rag-engine-management`](skills/ai-and-agents/agent-platform-rag-engine-management/SKILL.md) | Manage and query Agent Platform RAG Engine Corpora and retrieve grounded contexts using the Google GenAI SDK. |
| `/agent-platform-skill-registry` | [`agent-platform-skill-registry`](skills/ai-and-agents/agent-platform-skill-registry/SKILL.md) | Interact with the Gemini Enterprise Agent Platform Skill Registry to create and search for available skills. |
| `/agent-platform-tuning` | [`agent-platform-tuning`](skills/ai-and-agents/agent-platform-tuning/SKILL.md) | Agent Platform Model Tuning. |
| `/agent-platform-tuning-management` | [`agent-platform-tuning-management`](skills/ai-and-agents/agent-platform-tuning-management/SKILL.md) | Manages GenAI tuning jobs in Agent Platform. Use this to list, get, or cancel ongoing model tuning jobs. |
| `/agent-supply-chain` | [`agent-supply-chain`](skills/ai-and-agents/agent-supply-chain/SKILL.md) | Verify supply chain integrity for AI agent plugins, tools, and dependencies. |
| `/agentic-eval` | [`agentic-eval`](skills/ai-and-agents/agentic-eval/SKILL.md) | Patterns and techniques for evaluating and improving AI agent outputs. |
| `/agentql-automation` | [`agentql-automation`](skills/ai-and-agents/agentql-automation/SKILL.md) | Automate Agentql tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agents-sdk` | [`agents-sdk`](skills/ai-and-agents/agents-sdk/SKILL.md) | Build AI agents on Cloudflare Workers using the Agents SDK. |
| `/agenty-automation` | [`agenty-automation`](skills/ai-and-agents/agenty-automation/SKILL.md) | Automate Agenty tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ai-prompt-engineering-safety-review` | [`ai-prompt-engineering-safety-review`](skills/ai-and-agents/ai-prompt-engineering-safety-review/SKILL.md) | Comprehensive AI prompt engineering safety review and improvement prompt. |
| `/ai-ready` | [`ai-ready`](skills/ai-and-agents/ai-ready/SKILL.md) | Make any repo AI-ready — analyzes your codebase and generates AGENTS.md, copilot-instructions.md, CI workflows, issue. |
| `/ai-seo` | [`ai-seo`](skills/ai-and-agents/ai-seo/SKILL.md) | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. |
| `/ai-team-orchestration` | [`ai-team-orchestration`](skills/ai-and-agents/ai-team-orchestration/SKILL.md) | Bootstrap and run a multi-agent AI development team. |
| `/airunway-aks-setup` | [`airunway-aks-setup`](skills/ai-and-agents/airunway-aks-setup/SKILL.md) | Set up AI Runway on AKS — from bare cluster to running model. |
| `/anthropic-administrator-automation` | [`anthropic-administrator-automation`](skills/ai-and-agents/anthropic-administrator-automation/SKILL.md) | Automate Anthropic Admin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/anthropic_administrator-automation` | [`anthropic_administrator-automation`](skills/ai-and-agents/anthropic_administrator-automation/SKILL.md) | Automate Anthropic Admin tasks via Rube MCP (Composio): API keys, usage, workspaces, and organization management. |
| `/arize-evaluator` | [`arize-evaluator`](skills/ai-and-agents/arize-evaluator/SKILL.md) | Handles LLM-as-judge evaluation workflows on Arize including creating/updating evaluators, running evaluations on spans. |
| `/arize-instrumentation` | [`arize-instrumentation`](skills/ai-and-agents/arize-instrumentation/SKILL.md) | Adds Arize AX tracing to an LLM application for the first time. |
| `/arize-prompt-optimization` | [`arize-prompt-optimization`](skills/ai-and-agents/arize-prompt-optimization/SKILL.md) | Optimizes, improves, and debugs LLM prompts using production trace data, evaluations, and annotations. |
| `/arize-trace` | [`arize-trace`](skills/ai-and-agents/arize-trace/SKILL.md) | Downloads, exports, and inspects existing Arize traces and spans to understand what an LLM app is doing or debug runtime issues. |
| `/audit-integrity` | [`audit-integrity`](skills/ai-and-agents/audit-integrity/SKILL.md) | Shared audit integrity framework for all AppSec agents — enforces output quality, intellectual honesty. |
| `/azure-ai-agents-persistent-dotnet` | [`azure-ai-agents-persistent-dotnet`](skills/ai-and-agents/azure-ai-agents-persistent-dotnet/SKILL.md) | Azure AI Agents Persistent SDK for .NET. |
| `/azure-ai-agents-persistent-java` | [`azure-ai-agents-persistent-java`](skills/ai-and-agents/azure-ai-agents-persistent-java/SKILL.md) | Azure AI Agents Persistent SDK for Java. |
| `/azure-ai-openai-dotnet` | [`azure-ai-openai-dotnet`](skills/ai-and-agents/azure-ai-openai-dotnet/SKILL.md) | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. |
| `/boost-prompt` | [`boost-prompt`](skills/ai-and-agents/boost-prompt/SKILL.md) | Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to. |
| `/breakdown-epic-arch` | [`breakdown-epic-arch`](skills/ai-and-agents/breakdown-epic-arch/SKILL.md) | Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document. |
| `/breakdown-epic-pm` | [`breakdown-epic-pm`](skills/ai-and-agents/breakdown-epic-pm/SKILL.md) | Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. |
| `/breakdown-feature-implementation` | [`breakdown-feature-implementation`](skills/ai-and-agents/breakdown-feature-implementation/SKILL.md) | Prompt for creating detailed feature implementation plans, following Epoch monorepo structure. |
| `/breakdown-feature-prd` | [`breakdown-feature-prd`](skills/ai-and-agents/breakdown-feature-prd/SKILL.md) | Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic. |
| `/breakdown-plan` | [`breakdown-plan`](skills/ai-and-agents/breakdown-plan/SKILL.md) | Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler >. |
| `/breakdown-test` | [`breakdown-test`](skills/ai-and-agents/breakdown-test/SKILL.md) | Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns. |
| `/chrome-devtools` | [`chrome-devtools`](skills/ai-and-agents/chrome-devtools/SKILL.md) | Expert-level browser automation, debugging, and performance analysis using Chrome DevTools MCP. |
| `/claude-api` | [`claude-api`](skills/ai-and-agents/claude-api/SKILL.md) | Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. |
| `/cli-mastery` | [`cli-mastery`](skills/ai-and-agents/cli-mastery/SKILL.md) | Interactive training for the GitHub Copilot CLI. |
| `/code-review-and-quality` | [`code-review-and-quality`](skills/ai-and-agents/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. |
| `/code-testing-agent` | [`code-testing-agent`](skills/ai-and-agents/code-testing-agent/SKILL.md) | Generates and writes new unit tests for any programming language using a Research-Plan-Implement pipeline. |
| `/coding-agent` | [`coding-agent`](skills/ai-and-agents/coding-agent/SKILL.md) | Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. |
| `/context-engineering` | [`context-engineering`](skills/ai-and-agents/context-engineering/SKILL.md) | Optimizes agent context setup. |
| `/continual-learning` | [`continual-learning`](skills/ai-and-agents/continual-learning/SKILL.md) | Guide for implementing continual learning in AI coding agents — hooks, memory scoping, reflection patterns. |
| `/conventional-commit` | [`conventional-commit`](skills/ai-and-agents/conventional-commit/SKILL.md) | Prompt and workflow for generating conventional commit messages using a structured XML format. |
| `/convert-plaintext-to-md` | [`convert-plaintext-to-md`](skills/ai-and-agents/convert-plaintext-to-md/SKILL.md) | Convert a text-based document to markdown following instructions from prompt. |
| `/create-agentsmd` | [`create-agentsmd`](skills/ai-and-agents/create-agentsmd/SKILL.md) | Prompt for generating an AGENTS.md file for a repository. |
| `/create-custom-agent` | [`create-custom-agent`](skills/ai-and-agents/create-custom-agent/SKILL.md) | Creates VS Code custom agent files (.agent.md) for specialized AI personas with tools, instructions, and handoffs. |
| `/create-llms` | [`create-llms`](skills/ai-and-agents/create-llms/SKILL.md) | Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/. |
| `/create-skill` | [`create-skill`](skills/ai-and-agents/create-skill/SKILL.md) | Scaffolds new agent skills for the dotnet/skills repository. |
| `/create-skill-test` | [`create-skill-test`](skills/ai-and-agents/create-skill-test/SKILL.md) | Scaffolds eval.yaml test files for agent skills in the dotnet/skills repository. |
| `/customgpt-automation` | [`customgpt-automation`](skills/ai-and-agents/customgpt-automation/SKILL.md) | Automate Customgpt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/declarative-agents` | [`declarative-agents`](skills/ai-and-agents/declarative-agents/SKILL.md) | Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic,. |
| `/developer-growth-analysis` | [`developer-growth-analysis`](skills/ai-and-agents/developer-growth-analysis/SKILL.md) | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps. |
| `/diagnose` | [`diagnose`](skills/ai-and-agents/diagnose/SKILL.md) | Perform a systematic diagnostic scan of an AI workflow across 5 quality dimensions — prompt quality, context. |
| `/directory-submissions` | [`directory-submissions`](skills/ai-and-agents/directory-submissions/SKILL.md) | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code. |
| `/dispatching-parallel-agents` | [`dispatching-parallel-agents`](skills/ai-and-agents/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. |
| `/dotnet-mcp-builder` | [`dotnet-mcp-builder`](skills/ai-and-agents/dotnet-mcp-builder/SKILL.md) | Build Model Context Protocol (MCP) servers in C#/.NET against the current ModelContextProtocol 1.x NuGet packages. |
| `/entra-agent-id` | [`entra-agent-id`](skills/ai-and-agents/entra-agent-id/SKILL.md) | Provision Microsoft Entra Agent Identity Blueprints, BlueprintPrincipals. |
| `/entra-agent-user` | [`entra-agent-user`](skills/ai-and-agents/entra-agent-user/SKILL.md) | Create Agent Users in Microsoft Entra ID from Agent Identities, enabling AI agents to act as digital workers with user. |
| `/finalize-agent-prompt` | [`finalize-agent-prompt`](skills/ai-and-agents/finalize-agent-prompt/SKILL.md) | Finalize prompt file using the role of an AI agent to polish the prompt for the end user. |
| `/finetuning` | [`finetuning`](skills/ai-and-agents/finetuning/SKILL.md) | Fine-tune models on Azure AI Foundry using SFT (supervised), DPO (preference), or RFT (reinforcement with graders). |
| `/flowstudio-power-automate-mcp` | [`flowstudio-power-automate-mcp`](skills/ai-and-agents/flowstudio-power-automate-mcp/SKILL.md) | Foundation skill for Power Automate via FlowStudio MCP — auth setup, the reusable MCP helper (Python + Node.js), tool. |
| `/foundry-agent-sync` | [`foundry-agent-sync`](skills/ai-and-agents/foundry-agent-sync/SKILL.md) | Create and synchronize prompt-based AI agents directly within Azure AI Foundry via REST API, from a local JSON manifest. |
| `/gemini` | [`gemini`](skills/ai-and-agents/gemini/SKILL.md) | Gemini CLI for one-shot Q&A, summaries, and generation. |
| `/gemini-agents-api` | [`gemini-agents-api`](skills/ai-and-agents/gemini-agents-api/SKILL.md) | Manages custom Agent resources on Gemini Enterprise Agent Platform. |
| `/gemini-api` | [`gemini-api`](skills/ai-and-agents/gemini-api/SKILL.md) | Guides the usage of the Gemini API on Agent Platform with the Google Gen AI SDK. |
| `/gemini-api-dev` | [`gemini-api-dev`](skills/ai-and-agents/gemini-api-dev/SKILL.md) | Use this skill when building applications with Gemini API hosted models, including Gemini and Gemma 4, working with. |
| `/gemini-automation` | [`gemini-automation`](skills/ai-and-agents/gemini-automation/SKILL.md) | Automate Gemini tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gemini-interactions-api` | [`gemini-interactions-api`](skills/ai-and-agents/gemini-interactions-api/SKILL.md) | Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal. |
| `/gemini-live-api-dev` | [`gemini-live-api-dev`](skills/ai-and-agents/gemini-live-api-dev/SKILL.md) | Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API. |
| `/gtm-ai-gtm` | [`gtm-ai-gtm`](skills/ai-and-agents/gtm-ai-gtm/SKILL.md) | Go-to-market strategy for AI products. |
| `/hf-mcp` | [`hf-mcp`](skills/ai-and-agents/hf-mcp/SKILL.md) | Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. |
| `/huggingface-community-evals` | [`huggingface-community-evals`](skills/ai-and-agents/huggingface-community-evals/SKILL.md) | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. |
| `/huggingface-llm-trainer` | [`huggingface-llm-trainer`](skills/ai-and-agents/huggingface-llm-trainer/SKILL.md) | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging. |
| `/huggingface-local-models` | [`huggingface-local-models`](skills/ai-and-agents/huggingface-local-models/SKILL.md) | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. |
| `/huggingface-vision-trainer` | [`huggingface-vision-trainer`](skills/ai-and-agents/huggingface-vision-trainer/SKILL.md) | Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm. |
| `/kotlin-mcp-server-generator` | [`kotlin-mcp-server-generator`](skills/ai-and-agents/kotlin-mcp-server-generator/SKILL.md) | Generate a complete Kotlin MCP server project with proper structure, dependencies. |
| `/langsmith-fetch` | [`langsmith-fetch`](skills/ai-and-agents/langsmith-fetch/SKILL.md) | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. |
| `/m365-agents-dotnet` | [`m365-agents-dotnet`](skills/ai-and-agents/m365-agents-dotnet/SKILL.md) | Microsoft 365 Agents SDK for .NET. |
| `/m365-agents-py` | [`m365-agents-py`](skills/ai-and-agents/m365-agents-py/SKILL.md) | Microsoft 365 Agents SDK for Python. |
| `/m365-agents-ts` | [`m365-agents-ts`](skills/ai-and-agents/m365-agents-ts/SKILL.md) | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| `/mcp-builder` | [`mcp-builder`](skills/ai-and-agents/mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external. |
| `/mcp-cli` | [`mcp-cli`](skills/ai-and-agents/mcp-cli/SKILL.md) | Interface for MCP (Model Context Protocol) servers via CLI. |
| `/mcp-copilot-studio-server-generator` | [`mcp-copilot-studio-server-generator`](skills/ai-and-agents/mcp-copilot-studio-server-generator/SKILL.md) | Generate a complete MCP server implementation optimized for Copilot Studio integration with proper schema constraints. |
| `/mcp-create-adaptive-cards` | [`mcp-create-adaptive-cards`](skills/ai-and-agents/mcp-create-adaptive-cards/SKILL.md) | Skill converted from mcp-create-adaptive-cards.prompt.md. |
| `/mcp-create-declarative-agent` | [`mcp-create-declarative-agent`](skills/ai-and-agents/mcp-create-declarative-agent/SKILL.md) | Skill converted from mcp-create-declarative-agent.prompt.md. |
| `/mcp-csharp-create` | [`mcp-csharp-create`](skills/ai-and-agents/mcp-csharp-create/SKILL.md) | Create MCP servers using the C# SDK and .NET project templates. |
| `/mcp-csharp-debug` | [`mcp-csharp-debug`](skills/ai-and-agents/mcp-csharp-debug/SKILL.md) | Run and debug C# MCP servers locally. |
| `/mcp-csharp-publish` | [`mcp-csharp-publish`](skills/ai-and-agents/mcp-csharp-publish/SKILL.md) | Publish and deploy C# MCP servers. |
| `/mcp-csharp-test` | [`mcp-csharp-test`](skills/ai-and-agents/mcp-csharp-test/SKILL.md) | Test C# MCP servers at multiple levels: unit tests for individual tools and integration tests using the MCP client SDK. |
| `/mcp-deploy-manage-agents` | [`mcp-deploy-manage-agents`](skills/ai-and-agents/mcp-deploy-manage-agents/SKILL.md) | Skill converted from mcp-deploy-manage-agents.prompt.md. |
| `/mcp-security-audit` | [`mcp-security-audit`](skills/ai-and-agents/mcp-security-audit/SKILL.md) | Audit MCP (Model Context Protocol) server configurations for security issues. |
| `/microsoft-agent-framework` | [`microsoft-agent-framework`](skills/ai-and-agents/microsoft-agent-framework/SKILL.md) | Create, update, refactor, explain, or review Microsoft Agent Framework solutions using shared guidance plus. |
| `/n8n-agents` | [`n8n-agents`](skills/ai-and-agents/n8n-agents/SKILL.md) | Advanced n8n management and workflow automation agent. |
| `/nano-banana-pro-openrouter` | [`nano-banana-pro-openrouter`](skills/ai-and-agents/nano-banana-pro-openrouter/SKILL.md) | Generate or edit images via OpenRouter with the Gemini 3 Pro Image model. |
| `/noob-mode` | [`noob-mode`](skills/ai-and-agents/noob-mode/SKILL.md) | Plain-English translation layer for non-technical Copilot CLI users. |
| `/onboard-context-matic` | [`onboard-context-matic`](skills/ai-and-agents/onboard-context-matic/SKILL.md) | Interactive onboarding tour for the context-matic MCP server. |
| `/phoenix-cli` | [`phoenix-cli`](skills/ai-and-agents/phoenix-cli/SKILL.md) | Debug LLM applications using the Phoenix CLI. |
| `/phoenix-evals` | [`phoenix-evals`](skills/ai-and-agents/phoenix-evals/SKILL.md) | Build and run evaluators for AI/LLM applications using Phoenix. |
| `/phoenix-tracing` | [`phoenix-tracing`](skills/ai-and-agents/phoenix-tracing/SKILL.md) | OpenInference semantic conventions and instrumentation for Phoenix AI observability. |
| `/playwright-explore-website` | [`playwright-explore-website`](skills/ai-and-agents/playwright-explore-website/SKILL.md) | Website exploration for testing using Playwright MCP. |
| `/power-bi-dax-optimization` | [`power-bi-dax-optimization`](skills/ai-and-agents/power-bi-dax-optimization/SKILL.md) | Comprehensive Power BI DAX formula optimization prompt for improving performance, readability. |
| `/power-bi-performance-troubleshooting` | [`power-bi-performance-troubleshooting`](skills/ai-and-agents/power-bi-performance-troubleshooting/SKILL.md) | Systematic Power BI performance troubleshooting prompt for identifying, diagnosing. |
| `/power-platform-mcp-connector-suite` | [`power-platform-mcp-connector-suite`](skills/ai-and-agents/power-platform-mcp-connector-suite/SKILL.md) | Generate complete Power Platform custom connector with MCP integration for Copilot Studio - includes schema generation,. |
| `/powerbi-modeling` | [`powerbi-modeling`](skills/ai-and-agents/powerbi-modeling/SKILL.md) | Power BI semantic modeling assistant for building optimized data models. |
| `/ppt-orchestra-skill` | [`ppt-orchestra-skill`](skills/ai-and-agents/ppt-orchestra-skill/SKILL.md) | Plan and orchestrate multi-slide PowerPoint creation from scratch. |
| `/prompt-optimizer` | [`prompt-optimizer`](skills/ai-and-agents/prompt-optimizer/SKILL.md) | Turn any rough prompt, half-formed idea, or task description into a finished, ready-to-send prompt optimized for any. |
| `/remember-interactive-programming` | [`remember-interactive-programming`](skills/ai-and-agents/remember-interactive-programming/SKILL.md) | A micro-prompt that reminds the agent that it is an interactive programmer. |
| `/ruby-mcp-server-generator` | [`ruby-mcp-server-generator`](skills/ai-and-agents/ruby-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Ruby using the official MCP Ruby SDK gem. |
| `/schema-markup` | [`schema-markup`](skills/ai-and-agents/schema-markup/SKILL.md) | When the user wants to add, fix, or optimize schema markup and structured data on their site. |
| `/secret-scanning` | [`secret-scanning`](skills/ai-and-agents/secret-scanning/SKILL.md) | Guide for configuring and managing GitHub secret scanning, push protection, custom patterns, and secret alert remediation. |
| `/seo-agent` | [`seo-agent`](skills/ai-and-agents/seo-agent/SKILL.md) | Automates and optimizes workflows for Seo Agent. |
| `/skill-creator` | [`skill-creator`](skills/ai-and-agents/skill-creator/SKILL.md) | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. |
| `/skill-share` | [`skill-share`](skills/ai-and-agents/skill-share/SKILL.md) | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team. |
| `/structured-autonomy-implement` | [`structured-autonomy-implement`](skills/ai-and-agents/structured-autonomy-implement/SKILL.md) | Structured Autonomy Implementation Prompt. |
| `/structured-autonomy-plan` | [`structured-autonomy-plan`](skills/ai-and-agents/structured-autonomy-plan/SKILL.md) | Structured Autonomy Planning Prompt. |
| `/subagent-driven-development` | [`subagent-driven-development`](skills/ai-and-agents/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session. |
| `/suggest-awesome-github-copilot-agents` | [`suggest-awesome-github-copilot-agents`](skills/ai-and-agents/suggest-awesome-github-copilot-agents/SKILL.md) | Suggest relevant GitHub Copilot Custom Agents files from the awesome-copilot repository based on current repository. |
| `/swift-mcp-server-generator` | [`swift-mcp-server-generator`](skills/ai-and-agents/swift-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Swift using the official MCP Swift SDK package. |
| `/technology-selection` | [`technology-selection`](skills/ai-and-agents/technology-selection/SKILL.md) | Guides technology selection and implementation of AI and ML features in .NET 8+ applications using ML.NET,. |
| `/template-skill` | [`template-skill`](skills/ai-and-agents/template-skill/SKILL.md) | Replace with description of the skill and when Claude should use it. |
| `/tldr-prompt` | [`tldr-prompt`](skills/ai-and-agents/tldr-prompt/SKILL.md) | Create tldr summaries for GitHub Copilot files (prompts, agents, instructions, collections), MCP servers. |
| `/typescript-mcp-server-generator` | [`typescript-mcp-server-generator`](skills/ai-and-agents/typescript-mcp-server-generator/SKILL.md) | Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration. |
| `/typespec-create-agent` | [`typespec-create-agent`](skills/ai-and-agents/typespec-create-agent/SKILL.md) | Generate a complete TypeSpec declarative agent with instructions, capabilities. |
| `/update-llms` | [`update-llms`](skills/ai-and-agents/update-llms/SKILL.md) | Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the. |
| `/using-agent-skills` | [`using-agent-skills`](skills/ai-and-agents/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. |
| `/v0-automation` | [`v0-automation`](skills/ai-and-agents/v0-automation/SKILL.md) | Automate V0 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wiki-agents-md` | [`wiki-agents-md`](skills/ai-and-agents/wiki-agents-md/SKILL.md) | Generates AGENTS.md files for repository folders — coding agent context files with build commands, testing. |
| `/workiq-copilot` | [`workiq-copilot`](skills/ai-and-agents/workiq-copilot/SKILL.md) | Guides the Copilot CLI on how to use the WorkIQ CLI/MCP server to query Microsoft 365 Copilot data (emails, meetings,. |
| `/write-coding-standards-from-file` | [`write-coding-standards-from-file`](skills/ai-and-agents/write-coding-standards-from-file/SKILL.md) | Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as. |

---

### 🔌 SaaS & API Automation
> *Automated integrations with third-party software, chat platforms, CRMs, and APIs (HubSpot, Stripe, Slack, etc.).*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/-21risk-automation` | [`-21risk-automation`](skills/automation-and-saas/-21risk-automation/SKILL.md) | Automate 21risk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/-2chat-automation` | [`-2chat-automation`](skills/automation-and-saas/-2chat-automation/SKILL.md) | Automate 2chat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/Apify Automation` | [`Apify Automation`](skills/automation-and-saas/Apify Automation/SKILL.md) | Automate web scraping and data extraction with Apify -- run Actors, manage datasets, create reusable tasks. |
| `/Apollo Automation` | [`Apollo Automation`](skills/automation-and-saas/Apollo Automation/SKILL.md) | Automate Apollo.io lead generation -- search organizations, discover contacts, enrich prospect data, manage contact. |
| `/Ashby Automation` | [`Ashby Automation`](skills/automation-and-saas/Ashby Automation/SKILL.md) | Automate recruiting and hiring workflows in Ashby -- manage candidates, jobs, applications, interviews. |
| `/Attio Automation` | [`Attio Automation`](skills/automation-and-saas/Attio Automation/SKILL.md) | Automate Attio CRM operations -- search records, query contacts and companies with advanced filters, manage notes, list. |
| `/Braintree Automation` | [`Braintree Automation`](skills/automation-and-saas/Braintree Automation/SKILL.md) | Braintree Automation: manage payment processing via Stripe-compatible tools for customers, subscriptions, payment. |
| `/Capsule CRM Automation` | [`Capsule CRM Automation`](skills/automation-and-saas/Capsule CRM Automation/SKILL.md) | Automate Capsule CRM operations -- manage contacts (parties), run structured filter queries, track tasks and projects,. |
| `/Clockify Automation` | [`Clockify Automation`](skills/automation-and-saas/Clockify Automation/SKILL.md) | Automate time tracking workflows in Clockify -- create and manage time entries, workspaces. |
| `/Coinbase Automation` | [`Coinbase Automation`](skills/automation-and-saas/Coinbase Automation/SKILL.md) | Coinbase Automation: list and manage cryptocurrency wallets, accounts, and portfolio data via Coinbase CDP SDK. |
| `/Contentful Automation` | [`Contentful Automation`](skills/automation-and-saas/Contentful Automation/SKILL.md) | Automate headless CMS operations in Contentful -- list spaces, retrieve space metadata. |
| `/Customer.io Automation` | [`Customer.io Automation`](skills/automation-and-saas/Customer.io Automation/SKILL.md) | Automate customer engagement workflows including broadcast triggers, message analytics, segment management. |
| `/Docker Hub Automation` | [`Docker Hub Automation`](skills/automation-and-saas/Docker Hub Automation/SKILL.md) | Automate Docker Hub operations -- manage organizations, repositories, teams, members. |
| `/Dynamics 365 Automation` | [`Dynamics 365 Automation`](skills/automation-and-saas/Dynamics 365 Automation/SKILL.md) | Dynamics 365 Automation: manage CRM contacts, accounts, leads, opportunities, sales orders, invoices. |
| `/Eventbrite Automation` | [`Eventbrite Automation`](skills/automation-and-saas/Eventbrite Automation/SKILL.md) | Automate Eventbrite event management, attendee tracking, organization discovery. |
| `/Facebook Automation` | [`Facebook Automation`](skills/automation-and-saas/Facebook Automation/SKILL.md) | Automate Facebook Page management including post creation, scheduling, video uploads, Messenger conversations. |
| `/Firecrawl Automation` | [`Firecrawl Automation`](skills/automation-and-saas/Firecrawl Automation/SKILL.md) | Automate web crawling and data extraction with Firecrawl -- scrape pages, crawl sites, extract structured data, batch. |
| `/FreshBooks Automation` | [`FreshBooks Automation`](skills/automation-and-saas/FreshBooks Automation/SKILL.md) | FreshBooks Automation: manage businesses, projects, time tracking, and billing in FreshBooks cloud accounting. |
| `/Gong Automation` | [`Gong Automation`](skills/automation-and-saas/Gong Automation/SKILL.md) | Automate Gong conversation intelligence -- retrieve call recordings, transcripts, detailed analytics, speaker stats. |
| `/Gorgias Automation` | [`Gorgias Automation`](skills/automation-and-saas/Gorgias Automation/SKILL.md) | Automate e-commerce customer support workflows in Gorgias -- manage tickets, customers, tags. |
| `/GroqCloud Automation` | [`GroqCloud Automation`](skills/automation-and-saas/GroqCloud Automation/SKILL.md) | Automate AI inference, chat completions, audio translation. |
| `/Gumroad Automation` | [`Gumroad Automation`](skills/automation-and-saas/Gumroad Automation/SKILL.md) | Automate Gumroad product management, sales tracking, license verification. |
| `/Harvest Automation` | [`Harvest Automation`](skills/automation-and-saas/Harvest Automation/SKILL.md) | Automate time tracking, project management. |
| `/Hunter Automation` | [`Hunter Automation`](skills/automation-and-saas/Hunter Automation/SKILL.md) | Automate Hunter.io email intelligence -- search domains for email addresses, find specific contacts, verify email. |
| `/Instantly Automation` | [`Instantly Automation`](skills/automation-and-saas/Instantly Automation/SKILL.md) | Automate Instantly cold email outreach -- manage campaigns, sending accounts, lead lists, bulk lead imports. |
| `/Jotform Automation` | [`Jotform Automation`](skills/automation-and-saas/Jotform Automation/SKILL.md) | Automate Jotform form listing, user management, activity history, folder organization. |
| `/Kommo Automation` | [`Kommo Automation`](skills/automation-and-saas/Kommo Automation/SKILL.md) | Automate Kommo CRM operations -- manage leads, pipelines, pipeline stages, tasks. |
| `/LaunchDarkly Automation` | [`LaunchDarkly Automation`](skills/automation-and-saas/LaunchDarkly Automation/SKILL.md) | Automate LaunchDarkly feature flag management -- list projects and environments, create and delete trigger workflows. |
| `/Lemlist Automation` | [`Lemlist Automation`](skills/automation-and-saas/Lemlist Automation/SKILL.md) | Automate Lemlist multichannel outreach -- manage campaigns, enroll leads, add personalization variables, export. |
| `/Lemon Squeezy Automation` | [`Lemon Squeezy Automation`](skills/automation-and-saas/Lemon Squeezy Automation/SKILL.md) | Automate Lemon Squeezy store management -- products, orders, subscriptions, customers, discounts. |
| `/Lever Automation` | [`Lever Automation`](skills/automation-and-saas/Lever Automation/SKILL.md) | Automate recruiting workflows in Lever ATS -- manage opportunities, job postings, requisitions, pipeline stages. |
| `/MailerLite Automation` | [`MailerLite Automation`](skills/automation-and-saas/MailerLite Automation/SKILL.md) | Automate email marketing workflows including subscriber management, campaign analytics, group segmentation. |
| `/Microsoft Clarity Automation` | [`Microsoft Clarity Automation`](skills/automation-and-saas/Microsoft Clarity Automation/SKILL.md) | Automate user behavior analytics with Microsoft Clarity -- export heatmap data, session metrics. |
| `/Mistral AI Automation` | [`Mistral AI Automation`](skills/automation-and-saas/Mistral AI Automation/SKILL.md) | Automate Mistral AI operations -- manage files and libraries, upload documents for fine-tuning, batch processing. |
| `/Neon Automation` | [`Neon Automation`](skills/automation-and-saas/Neon Automation/SKILL.md) | Automate Neon serverless Postgres operations -- manage projects, branches, databases, roles. |
| `/NetSuite Automation` | [`NetSuite Automation`](skills/automation-and-saas/NetSuite Automation/SKILL.md) | NetSuite Automation: manage customers, sales orders, invoices, inventory, and records via Oracle NetSuite ERP with SuiteQL queries. |
| `/New Relic Automation` | [`New Relic Automation`](skills/automation-and-saas/New Relic Automation/SKILL.md) | Automate New Relic observability workflows -- manage alert policies, notification channels, alert conditions. |
| `/Omnisend Automation` | [`Omnisend Automation`](skills/automation-and-saas/Omnisend Automation/SKILL.md) | Automate ecommerce marketing workflows including contact management, bulk operations. |
| `/OpenAI Automation` | [`OpenAI Automation`](skills/automation-and-saas/OpenAI Automation/SKILL.md) | Automate OpenAI API operations -- generate responses with multimodal and structured output support, create embeddings,. |
| `/PandaDoc Automation` | [`PandaDoc Automation`](skills/automation-and-saas/PandaDoc Automation/SKILL.md) | Automate document workflows with PandaDoc -- create documents from files, manage contacts, organize folders, set up. |
| `/PhantomBuster Automation` | [`PhantomBuster Automation`](skills/automation-and-saas/PhantomBuster Automation/SKILL.md) | Automate lead generation, web scraping, and social media data extraction workflows through PhantomBuster's cloud. |
| `/Prismic Automation` | [`Prismic Automation`](skills/automation-and-saas/Prismic Automation/SKILL.md) | Automate headless CMS operations in Prismic -- query documents, search content, retrieve custom types. |
| `/Productboard Automation` | [`Productboard Automation`](skills/automation-and-saas/Productboard Automation/SKILL.md) | Automate product management workflows in Productboard -- manage features, notes, objectives, components. |
| `/QuickBooks Automation` | [`QuickBooks Automation`](skills/automation-and-saas/QuickBooks Automation/SKILL.md) | QuickBooks Automation: manage invoices, customers, accounts, and payments in QuickBooks Online for streamlined bookkeeping. |
| `/Ramp Automation` | [`Ramp Automation`](skills/automation-and-saas/Ramp Automation/SKILL.md) | Ramp Automation: manage corporate card transactions, reimbursements, users, and expense tracking via the Ramp platform. |
| `/Replicate Automation` | [`Replicate Automation`](skills/automation-and-saas/Replicate Automation/SKILL.md) | Automate Replicate AI model operations -- run predictions, upload files, inspect model schemas, list versions. |
| `/RingCentral Automation` | [`RingCentral Automation`](skills/automation-and-saas/RingCentral Automation/SKILL.md) | RingCentral automation via Rube MCP -- toolkit not currently available in Composio; no RING_CENTRAL_ tools found. |
| `/SharePoint Automation` | [`SharePoint Automation`](skills/automation-and-saas/SharePoint Automation/SKILL.md) | SharePoint Automation: manage sites, lists, documents, folders, pages, and search content across SharePoint and OneDrive. |
| `/Shortcut Automation` | [`Shortcut Automation`](skills/automation-and-saas/Shortcut Automation/SKILL.md) | Automate project management workflows in Shortcut -- create stories, manage tasks, track epics. |
| `/Snowflake Automation` | [`Snowflake Automation`](skills/automation-and-saas/Snowflake Automation/SKILL.md) | Automate Snowflake data warehouse operations -- list databases, schemas. |
| `/Spotify Automation` | [`Spotify Automation`](skills/automation-and-saas/Spotify Automation/SKILL.md) | Automate Spotify workflows including playlist management, music search, playback control, and user profile access via Composio. |
| `/SurveyMonkey Automation` | [`SurveyMonkey Automation`](skills/automation-and-saas/SurveyMonkey Automation/SKILL.md) | Automate SurveyMonkey survey creation, response collection, collector management. |
| `/Toggl Automation` | [`Toggl Automation`](skills/automation-and-saas/Toggl Automation/SKILL.md) | Automate time tracking workflows in Toggl Track -- create time entries, manage projects, clients, tags. |
| `/Uploadcare Automation` | [`Uploadcare Automation`](skills/automation-and-saas/Uploadcare Automation/SKILL.md) | Automate Uploadcare file management including listing, storing, inspecting, downloading. |
| `/Wave Accounting Automation` | [`Wave Accounting Automation`](skills/automation-and-saas/Wave Accounting Automation/SKILL.md) | Wave Accounting toolkit is not currently available as a native integration. |
| `/Webex Automation` | [`Webex Automation`](skills/automation-and-saas/Webex Automation/SKILL.md) | Automate Cisco Webex messaging, rooms, teams, webhooks, and people management through natural language commands. |
| `/Workday Automation` | [`Workday Automation`](skills/automation-and-saas/Workday Automation/SKILL.md) | Automate HR operations in Workday -- manage workers, time off requests, absence balances. |
| `/Xero Automation` | [`Xero Automation`](skills/automation-and-saas/Xero Automation/SKILL.md) | Xero Automation: manage invoices, contacts, payments, bank transactions, and accounts in Xero for cloud-based bookkeeping. |
| `/Zoho Books Automation` | [`Zoho Books Automation`](skills/automation-and-saas/Zoho Books Automation/SKILL.md) | Automate Zoho Books accounting workflows including invoice creation, bill management, contact lookup, payment tracking. |
| `/Zoho Desk Automation` | [`Zoho Desk Automation`](skills/automation-and-saas/Zoho Desk Automation/SKILL.md) | Zoho Desk automation via Rube MCP -- toolkit not currently available in Composio; no ZOHO_DESK_ tools found. |
| `/ably-automation` | [`ably-automation`](skills/automation-and-saas/ably-automation/SKILL.md) | Automate Ably tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/abstract-automation` | [`abstract-automation`](skills/automation-and-saas/abstract-automation/SKILL.md) | Automate Abstract tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/abuselpdb-automation` | [`abuselpdb-automation`](skills/automation-and-saas/abuselpdb-automation/SKILL.md) | Automate Abuselpdb tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/abyssale-automation` | [`abyssale-automation`](skills/automation-and-saas/abyssale-automation/SKILL.md) | Automate Abyssale tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/accelo-automation` | [`accelo-automation`](skills/automation-and-saas/accelo-automation/SKILL.md) | Automate Accelo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/accredible-certificates-automation` | [`accredible-certificates-automation`](skills/automation-and-saas/accredible-certificates-automation/SKILL.md) | Automate Accredible Certificates tasks via Rube MCP (Composio). |
| `/acculynx-automation` | [`acculynx-automation`](skills/automation-and-saas/acculynx-automation/SKILL.md) | Automate Acculynx tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/active-campaign-automation` | [`active-campaign-automation`](skills/automation-and-saas/active-campaign-automation/SKILL.md) | Automate ActiveCampaign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/addresszen-automation` | [`addresszen-automation`](skills/automation-and-saas/addresszen-automation/SKILL.md) | Automate Addresszen tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/adobe-automation` | [`adobe-automation`](skills/automation-and-saas/adobe-automation/SKILL.md) | Automate Adobe tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/adrapid-automation` | [`adrapid-automation`](skills/automation-and-saas/adrapid-automation/SKILL.md) | Automate Adrapid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/adyntel-automation` | [`adyntel-automation`](skills/automation-and-saas/adyntel-automation/SKILL.md) | Automate Adyntel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/aero-workflow-automation` | [`aero-workflow-automation`](skills/automation-and-saas/aero-workflow-automation/SKILL.md) | Automate Aero Workflow tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/aeroleads-automation` | [`aeroleads-automation`](skills/automation-and-saas/aeroleads-automation/SKILL.md) | Automate Aeroleads tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/affinda-automation` | [`affinda-automation`](skills/automation-and-saas/affinda-automation/SKILL.md) | Automate Affinda tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/affinity-automation` | [`affinity-automation`](skills/automation-and-saas/affinity-automation/SKILL.md) | Automate Affinity tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agencyzoom-automation` | [`agencyzoom-automation`](skills/automation-and-saas/agencyzoom-automation/SKILL.md) | Automate Agencyzoom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agent-mail-automation` | [`agent-mail-automation`](skills/automation-and-saas/agent-mail-automation/SKILL.md) | Automate Agent Mail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agiled-automation` | [`agiled-automation`](skills/automation-and-saas/agiled-automation/SKILL.md) | Automate Agiled tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agility-cms-automation` | [`agility-cms-automation`](skills/automation-and-saas/agility-cms-automation/SKILL.md) | Automate Agility CMS tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ai-ml-api-automation` | [`ai-ml-api-automation`](skills/automation-and-saas/ai-ml-api-automation/SKILL.md) | Automate AI ML API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/aivoov-automation` | [`aivoov-automation`](skills/automation-and-saas/aivoov-automation/SKILL.md) | Automate Aivoov tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/alchemy-automation` | [`alchemy-automation`](skills/automation-and-saas/alchemy-automation/SKILL.md) | Automate Alchemy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/algodocs-automation` | [`algodocs-automation`](skills/automation-and-saas/algodocs-automation/SKILL.md) | Automate Algodocs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/algolia-automation` | [`algolia-automation`](skills/automation-and-saas/algolia-automation/SKILL.md) | Automate Algolia tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/all-images-ai-automation` | [`all-images-ai-automation`](skills/automation-and-saas/all-images-ai-automation/SKILL.md) | Automate All Images AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/alpha-vantage-automation` | [`alpha-vantage-automation`](skills/automation-and-saas/alpha-vantage-automation/SKILL.md) | Automate Alpha Vantage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/altoviz-automation` | [`altoviz-automation`](skills/automation-and-saas/altoviz-automation/SKILL.md) | Automate Altoviz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/alttext-ai-automation` | [`alttext-ai-automation`](skills/automation-and-saas/alttext-ai-automation/SKILL.md) | Automate Alttext AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/amara-automation` | [`amara-automation`](skills/automation-and-saas/amara-automation/SKILL.md) | Automate Amara tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/amazon-automation` | [`amazon-automation`](skills/automation-and-saas/amazon-automation/SKILL.md) | Automate Amazon tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ambee-automation` | [`ambee-automation`](skills/automation-and-saas/ambee-automation/SKILL.md) | Automate Ambee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ambient-weather-automation` | [`ambient-weather-automation`](skills/automation-and-saas/ambient-weather-automation/SKILL.md) | Automate Ambient Weather tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/amcards-automation` | [`amcards-automation`](skills/automation-and-saas/amcards-automation/SKILL.md) | Automate Amcards tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/anchor-browser-automation` | [`anchor-browser-automation`](skills/automation-and-saas/anchor-browser-automation/SKILL.md) | Automate Anchor Browser tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/anonyflow-automation` | [`anonyflow-automation`](skills/automation-and-saas/anonyflow-automation/SKILL.md) | Automate Anonyflow tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apaleo-automation` | [`apaleo-automation`](skills/automation-and-saas/apaleo-automation/SKILL.md) | Automate Apaleo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apex27-automation` | [`apex27-automation`](skills/automation-and-saas/apex27-automation/SKILL.md) | Automate Apex27 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-and-interface-design` | [`api-and-interface-design`](skills/automation-and-saas/api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. |
| `/api-bible-automation` | [`api-bible-automation`](skills/automation-and-saas/api-bible-automation/SKILL.md) | Automate API Bible tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-labz-automation` | [`api-labz-automation`](skills/automation-and-saas/api-labz-automation/SKILL.md) | Automate API Labz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-ninjas-automation` | [`api-ninjas-automation`](skills/automation-and-saas/api-ninjas-automation/SKILL.md) | Automate API Ninjas tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-sports-automation` | [`api-sports-automation`](skills/automation-and-saas/api-sports-automation/SKILL.md) | Automate API Sports tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api2pdf-automation` | [`api2pdf-automation`](skills/automation-and-saas/api2pdf-automation/SKILL.md) | Automate Api2pdf tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apiflash-automation` | [`apiflash-automation`](skills/automation-and-saas/apiflash-automation/SKILL.md) | Automate Apiflash tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apilio-automation` | [`apilio-automation`](skills/automation-and-saas/apilio-automation/SKILL.md) | Automate Apilio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apipie-ai-automation` | [`apipie-ai-automation`](skills/automation-and-saas/apipie-ai-automation/SKILL.md) | Automate Apipie AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apitemplate-io-automation` | [`apitemplate-io-automation`](skills/automation-and-saas/apitemplate-io-automation/SKILL.md) | Automate Apitemplate IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apiverve-automation` | [`apiverve-automation`](skills/automation-and-saas/apiverve-automation/SKILL.md) | Automate Apiverve tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/appcircle-automation` | [`appcircle-automation`](skills/automation-and-saas/appcircle-automation/SKILL.md) | Automate Appcircle tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/appdrag-automation` | [`appdrag-automation`](skills/automation-and-saas/appdrag-automation/SKILL.md) | Automate Appdrag tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/appointo-automation` | [`appointo-automation`](skills/automation-and-saas/appointo-automation/SKILL.md) | Automate Appointo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/appsflyer-automation` | [`appsflyer-automation`](skills/automation-and-saas/appsflyer-automation/SKILL.md) | Automate Appsflyer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/appveyor-automation` | [`appveyor-automation`](skills/automation-and-saas/appveyor-automation/SKILL.md) | Automate Appveyor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/arduino-azure-iot-edge-integration` | [`arduino-azure-iot-edge-integration`](skills/automation-and-saas/arduino-azure-iot-edge-integration/SKILL.md) | Design and implement Arduino integration with Azure IoT Hub and IoT Edge, including secure provisioning, resilient. |
| `/arize-ai-provider-integration` | [`arize-ai-provider-integration`](skills/automation-and-saas/arize-ai-provider-integration/SKILL.md) | Creates, reads, updates, and deletes Arize AI integrations that store LLM provider credentials used by evaluators and. |
| `/aryn-automation` | [`aryn-automation`](skills/automation-and-saas/aryn-automation/SKILL.md) | Automate Aryn tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ascora-automation` | [`ascora-automation`](skills/automation-and-saas/ascora-automation/SKILL.md) | Automate Ascora tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/asin-data-api-automation` | [`asin-data-api-automation`](skills/automation-and-saas/asin-data-api-automation/SKILL.md) | Automate Asin Data API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/aspnet-minimal-api-openapi` | [`aspnet-minimal-api-openapi`](skills/automation-and-saas/aspnet-minimal-api-openapi/SKILL.md) | Create ASP.NET Minimal API endpoints with proper OpenAPI documentation. |
| `/astica-ai-automation` | [`astica-ai-automation`](skills/automation-and-saas/astica-ai-automation/SKILL.md) | Automate Astica AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/async-interview-automation` | [`async-interview-automation`](skills/automation-and-saas/async-interview-automation/SKILL.md) | Automate Async Interview tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/atlassian-automation` | [`atlassian-automation`](skills/automation-and-saas/atlassian-automation/SKILL.md) | Automate Atlassian tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/auth0-automation` | [`auth0-automation`](skills/automation-and-saas/auth0-automation/SKILL.md) | Automate Auth0 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/autobound-automation` | [`autobound-automation`](skills/automation-and-saas/autobound-automation/SKILL.md) | Automate Autobound tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/autom-automation` | [`autom-automation`](skills/automation-and-saas/autom-automation/SKILL.md) | Automate Autom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/axonaut-automation` | [`axonaut-automation`](skills/automation-and-saas/axonaut-automation/SKILL.md) | Automate Axonaut tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ayrshare-automation` | [`ayrshare-automation`](skills/automation-and-saas/ayrshare-automation/SKILL.md) | Automate Ayrshare tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/azure-communication-callautomation-java` | [`azure-communication-callautomation-java`](skills/automation-and-saas/azure-communication-callautomation-java/SKILL.md) | Build call automation workflows with Azure Communication Services Call Automation Java SDK. |
| `/azure-communication-sms-java` | [`azure-communication-sms-java`](skills/automation-and-saas/azure-communication-sms-java/SKILL.md) | Send SMS messages with Azure Communication Services SMS Java SDK. |
| `/azure-mgmt-apicenter-dotnet` | [`azure-mgmt-apicenter-dotnet`](skills/automation-and-saas/azure-mgmt-apicenter-dotnet/SKILL.md) | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| `/azure-mgmt-apicenter-py` | [`azure-mgmt-apicenter-py`](skills/automation-and-saas/azure-mgmt-apicenter-py/SKILL.md) | Azure API Center Management SDK for Python. |
| `/azure-mgmt-apimanagement-dotnet` | [`azure-mgmt-apimanagement-dotnet`](skills/automation-and-saas/azure-mgmt-apimanagement-dotnet/SKILL.md) | Azure Resource Manager SDK for API Management in .NET. |
| `/azure-mgmt-apimanagement-py` | [`azure-mgmt-apimanagement-py`](skills/automation-and-saas/azure-mgmt-apimanagement-py/SKILL.md) | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| `/backendless-automation` | [`backendless-automation`](skills/automation-and-saas/backendless-automation/SKILL.md) | Automate Backendless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bannerbear-automation` | [`bannerbear-automation`](skills/automation-and-saas/bannerbear-automation/SKILL.md) | Automate Bannerbear tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bart-automation` | [`bart-automation`](skills/automation-and-saas/bart-automation/SKILL.md) | Automate Bart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/baselinker-automation` | [`baselinker-automation`](skills/automation-and-saas/baselinker-automation/SKILL.md) | Automate Baselinker tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/baserow-automation` | [`baserow-automation`](skills/automation-and-saas/baserow-automation/SKILL.md) | Automate Baserow tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/basin-automation` | [`basin-automation`](skills/automation-and-saas/basin-automation/SKILL.md) | Automate Basin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/batch-files` | [`batch-files`](skills/automation-and-saas/batch-files/SKILL.md) | Expert-level Windows batch file (.bat/.cmd) skill for writing, debugging, and maintaining CMD scripts. |
| `/battlenet-automation` | [`battlenet-automation`](skills/automation-and-saas/battlenet-automation/SKILL.md) | Automate Battlenet tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/beaconchain-automation` | [`beaconchain-automation`](skills/automation-and-saas/beaconchain-automation/SKILL.md) | Automate Beaconchain tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/beaconstac-automation` | [`beaconstac-automation`](skills/automation-and-saas/beaconstac-automation/SKILL.md) | Automate Beaconstac tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/beamer-automation` | [`beamer-automation`](skills/automation-and-saas/beamer-automation/SKILL.md) | Automate Beamer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/beeminder-automation` | [`beeminder-automation`](skills/automation-and-saas/beeminder-automation/SKILL.md) | Automate Beeminder tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bench-automation` | [`bench-automation`](skills/automation-and-saas/bench-automation/SKILL.md) | Automate Bench tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/benchmark-email-automation` | [`benchmark-email-automation`](skills/automation-and-saas/benchmark-email-automation/SKILL.md) | Automate Benchmark Email tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/benzinga-automation` | [`benzinga-automation`](skills/automation-and-saas/benzinga-automation/SKILL.md) | Automate Benzinga tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bestbuy-automation` | [`bestbuy-automation`](skills/automation-and-saas/bestbuy-automation/SKILL.md) | Automate Bestbuy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/better-proposals-automation` | [`better-proposals-automation`](skills/automation-and-saas/better-proposals-automation/SKILL.md) | Automate Better Proposals tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/better-stack-automation` | [`better-stack-automation`](skills/automation-and-saas/better-stack-automation/SKILL.md) | Automate Better Stack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bidsketch-automation` | [`bidsketch-automation`](skills/automation-and-saas/bidsketch-automation/SKILL.md) | Automate Bidsketch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/big-data-cloud-automation` | [`big-data-cloud-automation`](skills/automation-and-saas/big-data-cloud-automation/SKILL.md) | Automate Big Data Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bigmailer-automation` | [`bigmailer-automation`](skills/automation-and-saas/bigmailer-automation/SKILL.md) | Automate Bigmailer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bigml-automation` | [`bigml-automation`](skills/automation-and-saas/bigml-automation/SKILL.md) | Automate Bigml tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bigpicture-io-automation` | [`bigpicture-io-automation`](skills/automation-and-saas/bigpicture-io-automation/SKILL.md) | Automate Bigpicture IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bitquery-automation` | [`bitquery-automation`](skills/automation-and-saas/bitquery-automation/SKILL.md) | Automate Bitquery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bitwarden-automation` | [`bitwarden-automation`](skills/automation-and-saas/bitwarden-automation/SKILL.md) | Automate Bitwarden tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blackbaud-automation` | [`blackbaud-automation`](skills/automation-and-saas/blackbaud-automation/SKILL.md) | Automate Blackbaud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blackboard-automation` | [`blackboard-automation`](skills/automation-and-saas/blackboard-automation/SKILL.md) | Automate Blackboard tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blocknative-automation` | [`blocknative-automation`](skills/automation-and-saas/blocknative-automation/SKILL.md) | Automate Blocknative tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/boldsign-automation` | [`boldsign-automation`](skills/automation-and-saas/boldsign-automation/SKILL.md) | Automate Boldsign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bolna-automation` | [`bolna-automation`](skills/automation-and-saas/bolna-automation/SKILL.md) | Automate Bolna tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/boloforms-automation` | [`boloforms-automation`](skills/automation-and-saas/boloforms-automation/SKILL.md) | Automate Boloforms tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bolt-iot-automation` | [`bolt-iot-automation`](skills/automation-and-saas/bolt-iot-automation/SKILL.md) | Automate Bolt Iot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bonsai-automation` | [`bonsai-automation`](skills/automation-and-saas/bonsai-automation/SKILL.md) | Automate Bonsai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bookingmood-automation` | [`bookingmood-automation`](skills/automation-and-saas/bookingmood-automation/SKILL.md) | Automate Bookingmood tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/booqable-automation` | [`booqable-automation`](skills/automation-and-saas/booqable-automation/SKILL.md) | Automate Booqable tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/borneo-automation` | [`borneo-automation`](skills/automation-and-saas/borneo-automation/SKILL.md) | Automate Borneo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/botbaba-automation` | [`botbaba-automation`](skills/automation-and-saas/botbaba-automation/SKILL.md) | Automate Botbaba tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/botpress-automation` | [`botpress-automation`](skills/automation-and-saas/botpress-automation/SKILL.md) | Automate Botpress tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/botsonic-automation` | [`botsonic-automation`](skills/automation-and-saas/botsonic-automation/SKILL.md) | Automate Botsonic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/botstar-automation` | [`botstar-automation`](skills/automation-and-saas/botstar-automation/SKILL.md) | Automate Botstar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bouncer-automation` | [`bouncer-automation`](skills/automation-and-saas/bouncer-automation/SKILL.md) | Automate Bouncer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/boxhero-automation` | [`boxhero-automation`](skills/automation-and-saas/boxhero-automation/SKILL.md) | Automate Boxhero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brandfetch-automation` | [`brandfetch-automation`](skills/automation-and-saas/brandfetch-automation/SKILL.md) | Automate Brandfetch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/breeze-automation` | [`breeze-automation`](skills/automation-and-saas/breeze-automation/SKILL.md) | Automate Breeze tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/breezy-hr-automation` | [`breezy-hr-automation`](skills/automation-and-saas/breezy-hr-automation/SKILL.md) | Automate Breezy HR tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brex-automation` | [`brex-automation`](skills/automation-and-saas/brex-automation/SKILL.md) | Automate Brex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brex-staging-automation` | [`brex-staging-automation`](skills/automation-and-saas/brex-staging-automation/SKILL.md) | Automate Brex Staging tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brightdata-automation` | [`brightdata-automation`](skills/automation-and-saas/brightdata-automation/SKILL.md) | Automate Brightdata tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brightpearl-automation` | [`brightpearl-automation`](skills/automation-and-saas/brightpearl-automation/SKILL.md) | Automate Brightpearl tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brilliant-directories-automation` | [`brilliant-directories-automation`](skills/automation-and-saas/brilliant-directories-automation/SKILL.md) | Automate Brilliant Directories tasks via Rube MCP (Composio). |
| `/browseai-automation` | [`browseai-automation`](skills/automation-and-saas/browseai-automation/SKILL.md) | Automate Browseai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/browser-tool-automation` | [`browser-tool-automation`](skills/automation-and-saas/browser-tool-automation/SKILL.md) | Automate Browser Tool tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/browserbase-tool-automation` | [`browserbase-tool-automation`](skills/automation-and-saas/browserbase-tool-automation/SKILL.md) | Automate Browserbase Tool tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/browserhub-automation` | [`browserhub-automation`](skills/automation-and-saas/browserhub-automation/SKILL.md) | Automate Browserhub tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/browserless-automation` | [`browserless-automation`](skills/automation-and-saas/browserless-automation/SKILL.md) | Automate Browserless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/btcpay-server-automation` | [`btcpay-server-automation`](skills/automation-and-saas/btcpay-server-automation/SKILL.md) | Automate Btcpay Server tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bubble-automation` | [`bubble-automation`](skills/automation-and-saas/bubble-automation/SKILL.md) | Automate Bubble tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bugbug-automation` | [`bugbug-automation`](skills/automation-and-saas/bugbug-automation/SKILL.md) | Automate Bugbug tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bugherd-automation` | [`bugherd-automation`](skills/automation-and-saas/bugherd-automation/SKILL.md) | Automate Bugherd tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bugsnag-automation` | [`bugsnag-automation`](skills/automation-and-saas/bugsnag-automation/SKILL.md) | Automate Bugsnag tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/buildkite-automation` | [`buildkite-automation`](skills/automation-and-saas/buildkite-automation/SKILL.md) | Automate Buildkite tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/builtwith-automation` | [`builtwith-automation`](skills/automation-and-saas/builtwith-automation/SKILL.md) | Automate Builtwith tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bunnycdn-automation` | [`bunnycdn-automation`](skills/automation-and-saas/bunnycdn-automation/SKILL.md) | Automate Bunnycdn tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/byteforms-automation` | [`byteforms-automation`](skills/automation-and-saas/byteforms-automation/SKILL.md) | Automate Byteforms tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cabinpanda-automation` | [`cabinpanda-automation`](skills/automation-and-saas/cabinpanda-automation/SKILL.md) | Automate Cabinpanda tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cal-automation` | [`cal-automation`](skills/automation-and-saas/cal-automation/SKILL.md) | Automate Cal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/calendarhero-automation` | [`calendarhero-automation`](skills/automation-and-saas/calendarhero-automation/SKILL.md) | Automate Calendarhero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/callerapi-automation` | [`callerapi-automation`](skills/automation-and-saas/callerapi-automation/SKILL.md) | Automate Callerapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/callingly-automation` | [`callingly-automation`](skills/automation-and-saas/callingly-automation/SKILL.md) | Automate Callingly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/callpage-automation` | [`callpage-automation`](skills/automation-and-saas/callpage-automation/SKILL.md) | Automate Callpage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/campaign-cleaner-automation` | [`campaign-cleaner-automation`](skills/automation-and-saas/campaign-cleaner-automation/SKILL.md) | Automate Campaign Cleaner tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/campayn-automation` | [`campayn-automation`](skills/automation-and-saas/campayn-automation/SKILL.md) | Automate Campayn tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/canny-automation` | [`canny-automation`](skills/automation-and-saas/canny-automation/SKILL.md) | Automate Canny tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/canvas-automation` | [`canvas-automation`](skills/automation-and-saas/canvas-automation/SKILL.md) | Automate Canvas tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/capsule_crm-automation` | [`capsule_crm-automation`](skills/automation-and-saas/capsule_crm-automation/SKILL.md) | Automate Capsule CRM tasks via Rube MCP (Composio): contacts, opportunities, cases, tasks, and pipeline management. |
| `/carbone-automation` | [`carbone-automation`](skills/automation-and-saas/carbone-automation/SKILL.md) | Automate Carbone tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cardly-automation` | [`cardly-automation`](skills/automation-and-saas/cardly-automation/SKILL.md) | Automate Cardly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/castingwords-automation` | [`castingwords-automation`](skills/automation-and-saas/castingwords-automation/SKILL.md) | Automate Castingwords tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cats-automation` | [`cats-automation`](skills/automation-and-saas/cats-automation/SKILL.md) | Automate Cats tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cdr-platform-automation` | [`cdr-platform-automation`](skills/automation-and-saas/cdr-platform-automation/SKILL.md) | Automate Cdr Platform tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/census-bureau-automation` | [`census-bureau-automation`](skills/automation-and-saas/census-bureau-automation/SKILL.md) | Automate Census Bureau tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/centralstationcrm-automation` | [`centralstationcrm-automation`](skills/automation-and-saas/centralstationcrm-automation/SKILL.md) | Automate Centralstationcrm tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/certifier-automation` | [`certifier-automation`](skills/automation-and-saas/certifier-automation/SKILL.md) | Automate Certifier tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chaser-automation` | [`chaser-automation`](skills/automation-and-saas/chaser-automation/SKILL.md) | Automate Chaser tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatbotkit-automation` | [`chatbotkit-automation`](skills/automation-and-saas/chatbotkit-automation/SKILL.md) | Automate Chatbotkit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatfai-automation` | [`chatfai-automation`](skills/automation-and-saas/chatfai-automation/SKILL.md) | Automate Chatfai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatwork-automation` | [`chatwork-automation`](skills/automation-and-saas/chatwork-automation/SKILL.md) | Automate Chatwork tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chmeetings-automation` | [`chmeetings-automation`](skills/automation-and-saas/chmeetings-automation/SKILL.md) | Automate Chmeetings tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ci-cd-and-automation` | [`ci-cd-and-automation`](skills/automation-and-saas/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. |
| `/cincopa-automation` | [`cincopa-automation`](skills/automation-and-saas/cincopa-automation/SKILL.md) | Automate Cincopa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/claid-ai-automation` | [`claid-ai-automation`](skills/automation-and-saas/claid-ai-automation/SKILL.md) | Automate Claid AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/classmarker-automation` | [`classmarker-automation`](skills/automation-and-saas/classmarker-automation/SKILL.md) | Automate Classmarker tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/clearout-automation` | [`clearout-automation`](skills/automation-and-saas/clearout-automation/SKILL.md) | Automate Clearout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/clickmeeting-automation` | [`clickmeeting-automation`](skills/automation-and-saas/clickmeeting-automation/SKILL.md) | Automate Clickmeeting tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudcart-automation` | [`cloudcart-automation`](skills/automation-and-saas/cloudcart-automation/SKILL.md) | Automate Cloudcart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudconvert-automation` | [`cloudconvert-automation`](skills/automation-and-saas/cloudconvert-automation/SKILL.md) | Automate Cloudconvert tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-api-key-automation` | [`cloudflare-api-key-automation`](skills/automation-and-saas/cloudflare-api-key-automation/SKILL.md) | Automate Cloudflare API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-automation` | [`cloudflare-automation`](skills/automation-and-saas/cloudflare-automation/SKILL.md) | Automate Cloudflare tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-browser-rendering-automation` | [`cloudflare-browser-rendering-automation`](skills/automation-and-saas/cloudflare-browser-rendering-automation/SKILL.md) | Automate Cloudflare Browser Rendering tasks via Rube MCP (Composio). |
| `/cloudflare-email-service` | [`cloudflare-email-service`](skills/automation-and-saas/cloudflare-email-service/SKILL.md) | Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing). |
| `/cloudlayer-automation` | [`cloudlayer-automation`](skills/automation-and-saas/cloudlayer-automation/SKILL.md) | Automate Cloudlayer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudpress-automation` | [`cloudpress-automation`](skills/automation-and-saas/cloudpress-automation/SKILL.md) | Automate Cloudpress tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coassemble-automation` | [`coassemble-automation`](skills/automation-and-saas/coassemble-automation/SKILL.md) | Automate Coassemble tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/codacy-automation` | [`codacy-automation`](skills/automation-and-saas/codacy-automation/SKILL.md) | Automate Codacy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/codeinterpreter-automation` | [`codeinterpreter-automation`](skills/automation-and-saas/codeinterpreter-automation/SKILL.md) | Automate Codeinterpreter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/codereadr-automation` | [`codereadr-automation`](skills/automation-and-saas/codereadr-automation/SKILL.md) | Automate Codereadr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinmarketcal-automation` | [`coinmarketcal-automation`](skills/automation-and-saas/coinmarketcal-automation/SKILL.md) | Automate Coinmarketcal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinmarketcap-automation` | [`coinmarketcap-automation`](skills/automation-and-saas/coinmarketcap-automation/SKILL.md) | Automate Coinmarketcap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinranking-automation` | [`coinranking-automation`](skills/automation-and-saas/coinranking-automation/SKILL.md) | Automate Coinranking tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/college-football-data-automation` | [`college-football-data-automation`](skills/automation-and-saas/college-football-data-automation/SKILL.md) | Automate College Football Data tasks via Rube MCP (Composio). |
| `/composio-automation` | [`composio-automation`](skills/automation-and-saas/composio-automation/SKILL.md) | Automate Composio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/composio-search-automation` | [`composio-search-automation`](skills/automation-and-saas/composio-search-automation/SKILL.md) | Automate Composio Search tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/connect` | [`connect`](skills/automation-and-saas/connect/SKILL.md) | Connect Claude to any app. |
| `/connect-apps` | [`connect-apps`](skills/automation-and-saas/connect-apps/SKILL.md) | Connect Claude to external apps like Gmail, Slack, GitHub. |
| `/connecteam-automation` | [`connecteam-automation`](skills/automation-and-saas/connecteam-automation/SKILL.md) | Automate Connecteam tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/content-management-systems` | [`content-management-systems`](skills/automation-and-saas/content-management-systems/SKILL.md) | Workflow for building and modifying content management systems across WordPress, Shopify, Wix, Squarespace, Drupal,. |
| `/contentful-graphql-automation` | [`contentful-graphql-automation`](skills/automation-and-saas/contentful-graphql-automation/SKILL.md) | Automate Contentful Graphql tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/control-d-automation` | [`control-d-automation`](skills/automation-and-saas/control-d-automation/SKILL.md) | Automate Control D tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/conversion-tools-automation` | [`conversion-tools-automation`](skills/automation-and-saas/conversion-tools-automation/SKILL.md) | Automate Conversion Tools tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/convertapi-automation` | [`convertapi-automation`](skills/automation-and-saas/convertapi-automation/SKILL.md) | Automate Convertapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/conveyor-automation` | [`conveyor-automation`](skills/automation-and-saas/conveyor-automation/SKILL.md) | Automate Conveyor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/convolo-ai-automation` | [`convolo-ai-automation`](skills/automation-and-saas/convolo-ai-automation/SKILL.md) | Automate Convolo AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/copilot-usage-metrics` | [`copilot-usage-metrics`](skills/automation-and-saas/copilot-usage-metrics/SKILL.md) | Retrieve and display GitHub Copilot usage metrics for organizations and enterprises using the GitHub CLI and REST API. |
| `/corrently-automation` | [`corrently-automation`](skills/automation-and-saas/corrently-automation/SKILL.md) | Automate Corrently tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/countdown-api-automation` | [`countdown-api-automation`](skills/automation-and-saas/countdown-api-automation/SKILL.md) | Automate Countdown API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coupa-automation` | [`coupa-automation`](skills/automation-and-saas/coupa-automation/SKILL.md) | Automate Coupa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/craftmypdf-automation` | [`craftmypdf-automation`](skills/automation-and-saas/craftmypdf-automation/SKILL.md) | Automate Craftmypdf tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/crowdin-automation` | [`crowdin-automation`](skills/automation-and-saas/crowdin-automation/SKILL.md) | Automate Crowdin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/crustdata-automation` | [`crustdata-automation`](skills/automation-and-saas/crustdata-automation/SKILL.md) | Automate Crustdata tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cults-automation` | [`cults-automation`](skills/automation-and-saas/cults-automation/SKILL.md) | Automate Cults tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/curated-automation` | [`curated-automation`](skills/automation-and-saas/curated-automation/SKILL.md) | Automate Curated tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/currents-api-automation` | [`currents-api-automation`](skills/automation-and-saas/currents-api-automation/SKILL.md) | Automate Currents API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/customjs-automation` | [`customjs-automation`](skills/automation-and-saas/customjs-automation/SKILL.md) | Automate Customjs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cutt-ly-automation` | [`cutt-ly-automation`](skills/automation-and-saas/cutt-ly-automation/SKILL.md) | Automate Cutt Ly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/d2lbrightspace-automation` | [`d2lbrightspace-automation`](skills/automation-and-saas/d2lbrightspace-automation/SKILL.md) | Automate D2lbrightspace tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dadata-ru-automation` | [`dadata-ru-automation`](skills/automation-and-saas/dadata-ru-automation/SKILL.md) | Automate Dadata Ru tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/daffy-automation` | [`daffy-automation`](skills/automation-and-saas/daffy-automation/SKILL.md) | Automate Daffy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dailybot-automation` | [`dailybot-automation`](skills/automation-and-saas/dailybot-automation/SKILL.md) | Automate Dailybot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/datagma-automation` | [`datagma-automation`](skills/automation-and-saas/datagma-automation/SKILL.md) | Automate Datagma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/datarobot-automation` | [`datarobot-automation`](skills/automation-and-saas/datarobot-automation/SKILL.md) | Automate Datarobot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/deadline-funnel-automation` | [`deadline-funnel-automation`](skills/automation-and-saas/deadline-funnel-automation/SKILL.md) | Automate Deadline Funnel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/deel-automation` | [`deel-automation`](skills/automation-and-saas/deel-automation/SKILL.md) | Automate Deel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/deepgram-automation` | [`deepgram-automation`](skills/automation-and-saas/deepgram-automation/SKILL.md) | Automate Deepgram tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/demio-automation` | [`demio-automation`](skills/automation-and-saas/demio-automation/SKILL.md) | Automate Demio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/deprecation-and-migration` | [`deprecation-and-migration`](skills/automation-and-saas/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. Use when removing old systems, APIs, or features. |
| `/desktime-automation` | [`desktime-automation`](skills/automation-and-saas/desktime-automation/SKILL.md) | Automate Desktime tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/detrack-automation` | [`detrack-automation`](skills/automation-and-saas/detrack-automation/SKILL.md) | Automate Detrack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dialmycalls-automation` | [`dialmycalls-automation`](skills/automation-and-saas/dialmycalls-automation/SKILL.md) | Automate Dialmycalls tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dialpad-automation` | [`dialpad-automation`](skills/automation-and-saas/dialpad-automation/SKILL.md) | Automate Dialpad tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dictionary-api-automation` | [`dictionary-api-automation`](skills/automation-and-saas/dictionary-api-automation/SKILL.md) | Automate Dictionary API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/diffbot-automation` | [`diffbot-automation`](skills/automation-and-saas/diffbot-automation/SKILL.md) | Automate Diffbot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/digicert-automation` | [`digicert-automation`](skills/automation-and-saas/digicert-automation/SKILL.md) | Automate Digicert tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/digital-ocean-automation` | [`digital-ocean-automation`](skills/automation-and-saas/digital-ocean-automation/SKILL.md) | Automate DigitalOcean tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/discordbot-automation` | [`discordbot-automation`](skills/automation-and-saas/discordbot-automation/SKILL.md) | Automate Discordbot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dnsfilter-automation` | [`dnsfilter-automation`](skills/automation-and-saas/dnsfilter-automation/SKILL.md) | Automate Dnsfilter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dock-certs-automation` | [`dock-certs-automation`](skills/automation-and-saas/dock-certs-automation/SKILL.md) | Automate Dock Certs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docker_hub-automation` | [`docker_hub-automation`](skills/automation-and-saas/docker_hub-automation/SKILL.md) | Automate Docker Hub tasks via Rube MCP (Composio): repositories, images, tags, and container registry management. |
| `/docmosis-automation` | [`docmosis-automation`](skills/automation-and-saas/docmosis-automation/SKILL.md) | Automate Docmosis tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docnify-automation` | [`docnify-automation`](skills/automation-and-saas/docnify-automation/SKILL.md) | Automate Docnify tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docsbot-ai-automation` | [`docsbot-ai-automation`](skills/automation-and-saas/docsbot-ai-automation/SKILL.md) | Automate Docsbot AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docsumo-automation` | [`docsumo-automation`](skills/automation-and-saas/docsumo-automation/SKILL.md) | Automate Docsumo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docugenerate-automation` | [`docugenerate-automation`](skills/automation-and-saas/docugenerate-automation/SKILL.md) | Automate Docugenerate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/documenso-automation` | [`documenso-automation`](skills/automation-and-saas/documenso-automation/SKILL.md) | Automate Documenso tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/documint-automation` | [`documint-automation`](skills/automation-and-saas/documint-automation/SKILL.md) | Automate Documint tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docupilot-automation` | [`docupilot-automation`](skills/automation-and-saas/docupilot-automation/SKILL.md) | Automate Docupilot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docupost-automation` | [`docupost-automation`](skills/automation-and-saas/docupost-automation/SKILL.md) | Automate Docupost tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/docuseal-automation` | [`docuseal-automation`](skills/automation-and-saas/docuseal-automation/SKILL.md) | Automate Docuseal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/doppler-marketing-automation-automation` | [`doppler-marketing-automation-automation`](skills/automation-and-saas/doppler-marketing-automation-automation/SKILL.md) | Automate Doppler Marketing Automation tasks via Rube MCP (Composio). |
| `/doppler-secretops-automation` | [`doppler-secretops-automation`](skills/automation-and-saas/doppler-secretops-automation/SKILL.md) | Automate Doppler Secretops tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dotnet-webapi` | [`dotnet-webapi`](skills/automation-and-saas/dotnet-webapi/SKILL.md) | Guides creation and modification of ASP.NET Core Web API endpoints with correct HTTP semantics, OpenAPI metadata. |
| `/dotsimple-automation` | [`dotsimple-automation`](skills/automation-and-saas/dotsimple-automation/SKILL.md) | Automate Dotsimple tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dovetail-automation` | [`dovetail-automation`](skills/automation-and-saas/dovetail-automation/SKILL.md) | Automate Dovetail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dpd2-automation` | [`dpd2-automation`](skills/automation-and-saas/dpd2-automation/SKILL.md) | Automate Dpd2 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/draftable-automation` | [`draftable-automation`](skills/automation-and-saas/draftable-automation/SKILL.md) | Automate Draftable tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dreamstudio-automation` | [`dreamstudio-automation`](skills/automation-and-saas/dreamstudio-automation/SKILL.md) | Automate Dreamstudio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/drip-jobs-automation` | [`drip-jobs-automation`](skills/automation-and-saas/drip-jobs-automation/SKILL.md) | Automate Drip Jobs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dripcel-automation` | [`dripcel-automation`](skills/automation-and-saas/dripcel-automation/SKILL.md) | Automate Dripcel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dromo-automation` | [`dromo-automation`](skills/automation-and-saas/dromo-automation/SKILL.md) | Automate Dromo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dropbox-sign-automation` | [`dropbox-sign-automation`](skills/automation-and-saas/dropbox-sign-automation/SKILL.md) | Automate Dropbox Sign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dropcontact-automation` | [`dropcontact-automation`](skills/automation-and-saas/dropcontact-automation/SKILL.md) | Automate Dropcontact tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dungeon-fighter-online-automation` | [`dungeon-fighter-online-automation`](skills/automation-and-saas/dungeon-fighter-online-automation/SKILL.md) | Automate Dungeon Fighter Online tasks via Rube MCP (Composio). |
| `/echtpost-automation` | [`echtpost-automation`](skills/automation-and-saas/echtpost-automation/SKILL.md) | Automate Echtpost tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/elorus-automation` | [`elorus-automation`](skills/automation-and-saas/elorus-automation/SKILL.md) | Automate Elorus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/email-drafter` | [`email-drafter`](skills/automation-and-saas/email-drafter/SKILL.md) | Draft and review professional emails that match your personal writing style. |
| `/emailable-automation` | [`emailable-automation`](skills/automation-and-saas/emailable-automation/SKILL.md) | Automate Emailable tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/emaillistverify-automation` | [`emaillistverify-automation`](skills/automation-and-saas/emaillistverify-automation/SKILL.md) | Automate Emaillistverify tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/emailoctopus-automation` | [`emailoctopus-automation`](skills/automation-and-saas/emailoctopus-automation/SKILL.md) | Automate Emailoctopus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/emelia-automation` | [`emelia-automation`](skills/automation-and-saas/emelia-automation/SKILL.md) | Automate Emelia tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/encodian-automation` | [`encodian-automation`](skills/automation-and-saas/encodian-automation/SKILL.md) | Automate Encodian tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/endorsal-automation` | [`endorsal-automation`](skills/automation-and-saas/endorsal-automation/SKILL.md) | Automate Endorsal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/enginemailer-automation` | [`enginemailer-automation`](skills/automation-and-saas/enginemailer-automation/SKILL.md) | Automate Enginemailer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/enigma-automation` | [`enigma-automation`](skills/automation-and-saas/enigma-automation/SKILL.md) | Automate Enigma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/entelligence-automation` | [`entelligence-automation`](skills/automation-and-saas/entelligence-automation/SKILL.md) | Automate Entelligence tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/eodhd-apis-automation` | [`eodhd-apis-automation`](skills/automation-and-saas/eodhd-apis-automation/SKILL.md) | Automate Eodhd Apis tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/epic-games-automation` | [`epic-games-automation`](skills/automation-and-saas/epic-games-automation/SKILL.md) | Automate Epic Games tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/esignatures-io-automation` | [`esignatures-io-automation`](skills/automation-and-saas/esignatures-io-automation/SKILL.md) | Automate Esignatures IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/espocrm-automation` | [`espocrm-automation`](skills/automation-and-saas/espocrm-automation/SKILL.md) | Automate Espocrm tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/esputnik-automation` | [`esputnik-automation`](skills/automation-and-saas/esputnik-automation/SKILL.md) | Automate Esputnik tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/etermin-automation` | [`etermin-automation`](skills/automation-and-saas/etermin-automation/SKILL.md) | Automate Etermin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/evenium-automation` | [`evenium-automation`](skills/automation-and-saas/evenium-automation/SKILL.md) | Automate Evenium tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/eventee-automation` | [`eventee-automation`](skills/automation-and-saas/eventee-automation/SKILL.md) | Automate Eventee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/eventzilla-automation` | [`eventzilla-automation`](skills/automation-and-saas/eventzilla-automation/SKILL.md) | Automate Eventzilla tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/everhour-automation` | [`everhour-automation`](skills/automation-and-saas/everhour-automation/SKILL.md) | Automate Everhour tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/eversign-automation` | [`eversign-automation`](skills/automation-and-saas/eversign-automation/SKILL.md) | Automate Eversign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/exa-automation` | [`exa-automation`](skills/automation-and-saas/exa-automation/SKILL.md) | Automate Exa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/exist-automation` | [`exist-automation`](skills/automation-and-saas/exist-automation/SKILL.md) | Automate Exist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/exp-simd-vectorization` | [`exp-simd-vectorization`](skills/automation-and-saas/exp-simd-vectorization/SKILL.md) | Optimizes hot-path scalar loops in .NET 8+ with cross-platform Vector128/Vector256/Vector512 SIMD intrinsics. |
| `/expofp-automation` | [`expofp-automation`](skills/automation-and-saas/expofp-automation/SKILL.md) | Automate Expofp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/extracta-ai-automation` | [`extracta-ai-automation`](skills/automation-and-saas/extracta-ai-automation/SKILL.md) | Automate Extracta AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/faceup-automation` | [`faceup-automation`](skills/automation-and-saas/faceup-automation/SKILL.md) | Automate Faceup tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/factorial-automation` | [`factorial-automation`](skills/automation-and-saas/factorial-automation/SKILL.md) | Automate Factorial tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fastapi-router-py` | [`fastapi-router-py`](skills/automation-and-saas/fastapi-router-py/SKILL.md) | Create FastAPI routers with CRUD operations, authentication dependencies, and proper response models. |
| `/feathery-automation` | [`feathery-automation`](skills/automation-and-saas/feathery-automation/SKILL.md) | Automate Feathery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/felt-automation` | [`felt-automation`](skills/automation-and-saas/felt-automation/SKILL.md) | Automate Felt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fibery-automation` | [`fibery-automation`](skills/automation-and-saas/fibery-automation/SKILL.md) | Automate Fibery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fidel-api-automation` | [`fidel-api-automation`](skills/automation-and-saas/fidel-api-automation/SKILL.md) | Automate Fidel API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/files-com-automation` | [`files-com-automation`](skills/automation-and-saas/files-com-automation/SKILL.md) | Automate Files Com tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fillout-forms-automation` | [`fillout-forms-automation`](skills/automation-and-saas/fillout-forms-automation/SKILL.md) | Automate Fillout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fillout_forms-automation` | [`fillout_forms-automation`](skills/automation-and-saas/fillout_forms-automation/SKILL.md) | Automate Fillout tasks via Rube MCP (Composio): forms, submissions, workflows, and form builder. |
| `/finage-automation` | [`finage-automation`](skills/automation-and-saas/finage-automation/SKILL.md) | Automate Finage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/findymail-automation` | [`findymail-automation`](skills/automation-and-saas/findymail-automation/SKILL.md) | Automate Findymail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/finerworks-automation` | [`finerworks-automation`](skills/automation-and-saas/finerworks-automation/SKILL.md) | Automate Finerworks tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fingertip-automation` | [`fingertip-automation`](skills/automation-and-saas/fingertip-automation/SKILL.md) | Automate Fingertip tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/finmei-automation` | [`finmei-automation`](skills/automation-and-saas/finmei-automation/SKILL.md) | Automate Finmei tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fireberry-automation` | [`fireberry-automation`](skills/automation-and-saas/fireberry-automation/SKILL.md) | Automate Fireberry tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fireflies-automation` | [`fireflies-automation`](skills/automation-and-saas/fireflies-automation/SKILL.md) | Automate Fireflies tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/firmao-automation` | [`firmao-automation`](skills/automation-and-saas/firmao-automation/SKILL.md) | Automate Firmao tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fitbit-automation` | [`fitbit-automation`](skills/automation-and-saas/fitbit-automation/SKILL.md) | Automate Fitbit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fixer-automation` | [`fixer-automation`](skills/automation-and-saas/fixer-automation/SKILL.md) | Automate Fixer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fixer-io-automation` | [`fixer-io-automation`](skills/automation-and-saas/fixer-io-automation/SKILL.md) | Automate Fixer IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/flexisign-automation` | [`flexisign-automation`](skills/automation-and-saas/flexisign-automation/SKILL.md) | Automate Flexisign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/flowiseai-automation` | [`flowiseai-automation`](skills/automation-and-saas/flowiseai-automation/SKILL.md) | Automate Flowiseai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/flutterwave-automation` | [`flutterwave-automation`](skills/automation-and-saas/flutterwave-automation/SKILL.md) | Automate Flutterwave tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fluxguard-automation` | [`fluxguard-automation`](skills/automation-and-saas/fluxguard-automation/SKILL.md) | Automate Fluxguard tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/folk-automation` | [`folk-automation`](skills/automation-and-saas/folk-automation/SKILL.md) | Automate Folk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fomo-automation` | [`fomo-automation`](skills/automation-and-saas/fomo-automation/SKILL.md) | Automate Fomo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/forcemanager-automation` | [`forcemanager-automation`](skills/automation-and-saas/forcemanager-automation/SKILL.md) | Automate Forcemanager tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/formbricks-automation` | [`formbricks-automation`](skills/automation-and-saas/formbricks-automation/SKILL.md) | Automate Formbricks tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/formcarry-automation` | [`formcarry-automation`](skills/automation-and-saas/formcarry-automation/SKILL.md) | Automate Formcarry tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/formdesk-automation` | [`formdesk-automation`](skills/automation-and-saas/formdesk-automation/SKILL.md) | Automate Formdesk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/formsite-automation` | [`formsite-automation`](skills/automation-and-saas/formsite-automation/SKILL.md) | Automate Formsite tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/foursquare-automation` | [`foursquare-automation`](skills/automation-and-saas/foursquare-automation/SKILL.md) | Automate Foursquare tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fraudlabs-pro-automation` | [`fraudlabs-pro-automation`](skills/automation-and-saas/fraudlabs-pro-automation/SKILL.md) | Automate Fraudlabs Pro tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/freecad-scripts` | [`freecad-scripts`](skills/automation-and-saas/freecad-scripts/SKILL.md) | Expert skill for writing FreeCAD Python scripts, macros, and automation. |
| `/front-automation` | [`front-automation`](skills/automation-and-saas/front-automation/SKILL.md) | Automate Front tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fullenrich-automation` | [`fullenrich-automation`](skills/automation-and-saas/fullenrich-automation/SKILL.md) | Automate Fullenrich tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gagelist-automation` | [`gagelist-automation`](skills/automation-and-saas/gagelist-automation/SKILL.md) | Automate Gagelist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gamma-automation` | [`gamma-automation`](skills/automation-and-saas/gamma-automation/SKILL.md) | Automate Gamma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gan-ai-automation` | [`gan-ai-automation`](skills/automation-and-saas/gan-ai-automation/SKILL.md) | Automate Gan AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gatherup-automation` | [`gatherup-automation`](skills/automation-and-saas/gatherup-automation/SKILL.md) | Automate Gatherup tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gender-api-automation` | [`gender-api-automation`](skills/automation-and-saas/gender-api-automation/SKILL.md) | Automate Gender API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/genderapi-io-automation` | [`genderapi-io-automation`](skills/automation-and-saas/genderapi-io-automation/SKILL.md) | Automate Genderapi IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/genderize-automation` | [`genderize-automation`](skills/automation-and-saas/genderize-automation/SKILL.md) | Automate Genderize tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/geoapify-automation` | [`geoapify-automation`](skills/automation-and-saas/geoapify-automation/SKILL.md) | Automate Geoapify tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/geocodio-automation` | [`geocodio-automation`](skills/automation-and-saas/geocodio-automation/SKILL.md) | Automate Geocodio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/geokeo-automation` | [`geokeo-automation`](skills/automation-and-saas/geokeo-automation/SKILL.md) | Automate Geokeo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/getform-automation` | [`getform-automation`](skills/automation-and-saas/getform-automation/SKILL.md) | Automate Getform tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gift-up-automation` | [`gift-up-automation`](skills/automation-and-saas/gift-up-automation/SKILL.md) | Automate Gift Up tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gigasheet-automation` | [`gigasheet-automation`](skills/automation-and-saas/gigasheet-automation/SKILL.md) | Automate Gigasheet tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/giphy-automation` | [`giphy-automation`](skills/automation-and-saas/giphy-automation/SKILL.md) | Automate Giphy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gist-automation` | [`gist-automation`](skills/automation-and-saas/gist-automation/SKILL.md) | Automate Gist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/givebutter-automation` | [`givebutter-automation`](skills/automation-and-saas/givebutter-automation/SKILL.md) | Automate Givebutter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gke-basics` | [`gke-basics`](skills/automation-and-saas/gke-basics/SKILL.md) | Plan, create, and configure production-ready Google Kubernetes Engine (GKE) clusters using the golden path Autopilot. |
| `/gladia-automation` | [`gladia-automation`](skills/automation-and-saas/gladia-automation/SKILL.md) | Automate Gladia tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gleap-automation` | [`gleap-automation`](skills/automation-and-saas/gleap-automation/SKILL.md) | Automate Gleap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/globalping-automation` | [`globalping-automation`](skills/automation-and-saas/globalping-automation/SKILL.md) | Automate Globalping tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/go-to-webinar-automation` | [`go-to-webinar-automation`](skills/automation-and-saas/go-to-webinar-automation/SKILL.md) | Automate GoToWebinar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/godial-automation` | [`godial-automation`](skills/automation-and-saas/godial-automation/SKILL.md) | Automate Godial tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gog` | [`gog`](skills/automation-and-saas/gog/SKILL.md) | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. |
| `/goodbits-automation` | [`goodbits-automation`](skills/automation-and-saas/goodbits-automation/SKILL.md) | Automate Goodbits tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/goody-automation` | [`goody-automation`](skills/automation-and-saas/goody-automation/SKILL.md) | Automate Goody tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-address-validation-automation` | [`google-address-validation-automation`](skills/automation-and-saas/google-address-validation-automation/SKILL.md) | Automate Google Address Validation tasks via Rube MCP (Composio). |
| `/google-admin-automation` | [`google-admin-automation`](skills/automation-and-saas/google-admin-automation/SKILL.md) | Automate Google Workspace Admin tasks via Rube MCP (Composio): manage users, groups, memberships, suspend accounts,. |
| `/google-classroom-automation` | [`google-classroom-automation`](skills/automation-and-saas/google-classroom-automation/SKILL.md) | Automate Google Classroom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-cloud-vision-automation` | [`google-cloud-vision-automation`](skills/automation-and-saas/google-cloud-vision-automation/SKILL.md) | Automate Google Cloud Vision tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-maps-automation` | [`google-maps-automation`](skills/automation-and-saas/google-maps-automation/SKILL.md) | Automate Google Maps tasks via Rube MCP (Composio): geocode addresses, search places, get directions, compute route. |
| `/google-search-console-automation` | [`google-search-console-automation`](skills/automation-and-saas/google-search-console-automation/SKILL.md) | Automate Google Search Console tasks via Rube MCP (Composio): query search analytics, list sites, inspect URLs, submit. |
| `/google_admin-automation` | [`google_admin-automation`](skills/automation-and-saas/google_admin-automation/SKILL.md) | Automate Google Admin tasks via Rube MCP (Composio): user management, org units, groups, and domain administration. |
| `/google_classroom-automation` | [`google_classroom-automation`](skills/automation-and-saas/google_classroom-automation/SKILL.md) | Automate Google Classroom tasks via Rube MCP (Composio): course management, assignments, student rosters, and announcements. |
| `/google_maps-automation` | [`google_maps-automation`](skills/automation-and-saas/google_maps-automation/SKILL.md) | Automate Google Maps tasks via Rube MCP (Composio): geocoding, directions, place search, and distance calculations. |
| `/google_search_console-automation` | [`google_search_console-automation`](skills/automation-and-saas/google_search_console-automation/SKILL.md) | Automate Google Search Console tasks via Rube MCP (Composio): search performance, URL inspection, sitemaps, and indexing status. |
| `/googleads-automation` | [`googleads-automation`](skills/automation-and-saas/googleads-automation/SKILL.md) | Automate Google Ads analytics tasks via Rube MCP (Composio): list Google Ads links, run GA4 reports, check. |
| `/googlebigquery-automation` | [`googlebigquery-automation`](skills/automation-and-saas/googlebigquery-automation/SKILL.md) | Automate Google BigQuery tasks via Rube MCP (Composio): run SQL queries, explore datasets and metadata, execute MBQL. |
| `/googlecalendar-automation` | [`googlecalendar-automation`](skills/automation-and-saas/googlecalendar-automation/SKILL.md) | Automate Google Calendar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/googledocs-automation` | [`googledocs-automation`](skills/automation-and-saas/googledocs-automation/SKILL.md) | Automate Google Docs tasks via Rube MCP (Composio): create, edit, search, export, copy, and update documents. |
| `/googledrive-automation` | [`googledrive-automation`](skills/automation-and-saas/googledrive-automation/SKILL.md) | Automate Google Drive tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/googlemeet-automation` | [`googlemeet-automation`](skills/automation-and-saas/googlemeet-automation/SKILL.md) | Automate Google Meet tasks via Rube MCP (Composio): create Meet spaces, schedule video conferences via Calendar events,. |
| `/googlephotos-automation` | [`googlephotos-automation`](skills/automation-and-saas/googlephotos-automation/SKILL.md) | Automate Google Photos tasks via Rube MCP (Composio): upload media, manage albums, search photos, batch add items,. |
| `/googleslides-automation` | [`googleslides-automation`](skills/automation-and-saas/googleslides-automation/SKILL.md) | Automate Google Slides tasks via Rube MCP (Composio): create presentations, add slides from Markdown, batch update,. |
| `/googlesuper-automation` | [`googlesuper-automation`](skills/automation-and-saas/googlesuper-automation/SKILL.md) | Automate Google Super tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/googletasks-automation` | [`googletasks-automation`](skills/automation-and-saas/googletasks-automation/SKILL.md) | Automate Google Tasks via Rube MCP (Composio): create, list, update, delete, move, and bulk-insert tasks and task lists. |
| `/gosquared-automation` | [`gosquared-automation`](skills/automation-and-saas/gosquared-automation/SKILL.md) | Automate Gosquared tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/grafbase-automation` | [`grafbase-automation`](skills/automation-and-saas/grafbase-automation/SKILL.md) | Automate Grafbase tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/graphhopper-automation` | [`graphhopper-automation`](skills/automation-and-saas/graphhopper-automation/SKILL.md) | Automate Graphhopper tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/griptape-automation` | [`griptape-automation`](skills/automation-and-saas/griptape-automation/SKILL.md) | Automate Griptape tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/grist-automation` | [`grist-automation`](skills/automation-and-saas/grist-automation/SKILL.md) | Automate Grist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/habitica-automation` | [`habitica-automation`](skills/automation-and-saas/habitica-automation/SKILL.md) | Automate Habitica tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hackernews-automation` | [`hackernews-automation`](skills/automation-and-saas/hackernews-automation/SKILL.md) | Automate Hackernews tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/happy-scribe-automation` | [`happy-scribe-automation`](skills/automation-and-saas/happy-scribe-automation/SKILL.md) | Automate Happy Scribe tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hashnode-automation` | [`hashnode-automation`](skills/automation-and-saas/hashnode-automation/SKILL.md) | Automate Hashnode tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/helcim-automation` | [`helcim-automation`](skills/automation-and-saas/helcim-automation/SKILL.md) | Automate Helcim tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/helloleads-automation` | [`helloleads-automation`](skills/automation-and-saas/helloleads-automation/SKILL.md) | Automate Helloleads tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/helpwise-automation` | [`helpwise-automation`](skills/automation-and-saas/helpwise-automation/SKILL.md) | Automate Helpwise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/here-automation` | [`here-automation`](skills/automation-and-saas/here-automation/SKILL.md) | Automate Here tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/heyreach-automation` | [`heyreach-automation`](skills/automation-and-saas/heyreach-automation/SKILL.md) | Automate Heyreach tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/heyzine-automation` | [`heyzine-automation`](skills/automation-and-saas/heyzine-automation/SKILL.md) | Automate Heyzine tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/highergov-automation` | [`highergov-automation`](skills/automation-and-saas/highergov-automation/SKILL.md) | Automate Highergov tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/highlevel-automation` | [`highlevel-automation`](skills/automation-and-saas/highlevel-automation/SKILL.md) | Automate Highlevel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/honeybadger-automation` | [`honeybadger-automation`](skills/automation-and-saas/honeybadger-automation/SKILL.md) | Automate Honeybadger tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/honeyhive-automation` | [`honeyhive-automation`](skills/automation-and-saas/honeyhive-automation/SKILL.md) | Automate Honeyhive tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hookdeck-automation` | [`hookdeck-automation`](skills/automation-and-saas/hookdeck-automation/SKILL.md) | Automate Hookdeck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hotspotsystem-automation` | [`hotspotsystem-automation`](skills/automation-and-saas/hotspotsystem-automation/SKILL.md) | Automate Hotspotsystem tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/html-to-image-automation` | [`html-to-image-automation`](skills/automation-and-saas/html-to-image-automation/SKILL.md) | Automate Html To Image tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/huggingface-datasets` | [`huggingface-datasets`](skills/automation-and-saas/huggingface-datasets/SKILL.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search. |
| `/huggingface-papers` | [`huggingface-papers`](skills/automation-and-saas/huggingface-papers/SKILL.md) | Look up and read Hugging Face paper pages in markdown. |
| `/huggingface-trackio` | [`huggingface-trackio`](skills/automation-and-saas/huggingface-trackio/SKILL.md) | Track and visualize ML training experiments with Trackio. |
| `/humanitix-automation` | [`humanitix-automation`](skills/automation-and-saas/humanitix-automation/SKILL.md) | Automate Humanitix tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/humanloop-automation` | [`humanloop-automation`](skills/automation-and-saas/humanloop-automation/SKILL.md) | Automate Humanloop tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hypeauditor-automation` | [`hypeauditor-automation`](skills/automation-and-saas/hypeauditor-automation/SKILL.md) | Automate Hypeauditor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hyperbrowser-automation` | [`hyperbrowser-automation`](skills/automation-and-saas/hyperbrowser-automation/SKILL.md) | Automate Hyperbrowser tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hyperise-automation` | [`hyperise-automation`](skills/automation-and-saas/hyperise-automation/SKILL.md) | Automate Hyperise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hystruct-automation` | [`hystruct-automation`](skills/automation-and-saas/hystruct-automation/SKILL.md) | Automate Hystruct tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/icims-talent-cloud-automation` | [`icims-talent-cloud-automation`](skills/automation-and-saas/icims-talent-cloud-automation/SKILL.md) | Automate Icims Talent Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/icypeas-automation` | [`icypeas-automation`](skills/automation-and-saas/icypeas-automation/SKILL.md) | Automate Icypeas tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/idea-scale-automation` | [`idea-scale-automation`](skills/automation-and-saas/idea-scale-automation/SKILL.md) | Automate Idea Scale tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/identitycheck-automation` | [`identitycheck-automation`](skills/automation-and-saas/identitycheck-automation/SKILL.md) | Automate Identitycheck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ignisign-automation` | [`ignisign-automation`](skills/automation-and-saas/ignisign-automation/SKILL.md) | Automate Ignisign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/imagekit-io-automation` | [`imagekit-io-automation`](skills/automation-and-saas/imagekit-io-automation/SKILL.md) | Automate Imagekit IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/imgbb-automation` | [`imgbb-automation`](skills/automation-and-saas/imgbb-automation/SKILL.md) | Automate Imgbb tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/imgix-automation` | [`imgix-automation`](skills/automation-and-saas/imgix-automation/SKILL.md) | Automate Imgix tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/influxdb-cloud-automation` | [`influxdb-cloud-automation`](skills/automation-and-saas/influxdb-cloud-automation/SKILL.md) | Automate Influxdb Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/insighto-ai-automation` | [`insighto-ai-automation`](skills/automation-and-saas/insighto-ai-automation/SKILL.md) | Automate Insighto AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/instacart-automation` | [`instacart-automation`](skills/automation-and-saas/instacart-automation/SKILL.md) | Automate Instacart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/integrate-context-matic` | [`integrate-context-matic`](skills/automation-and-saas/integrate-context-matic/SKILL.md) | Discovers and integrates third-party APIs using the context-matic MCP server. |
| `/intelliprint-automation` | [`intelliprint-automation`](skills/automation-and-saas/intelliprint-automation/SKILL.md) | Automate Intelliprint tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/interzoid-automation` | [`interzoid-automation`](skills/automation-and-saas/interzoid-automation/SKILL.md) | Automate Interzoid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2location-automation` | [`ip2location-automation`](skills/automation-and-saas/ip2location-automation/SKILL.md) | Automate Ip2location tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2location-io-automation` | [`ip2location-io-automation`](skills/automation-and-saas/ip2location-io-automation/SKILL.md) | Automate Ip2location IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2proxy-automation` | [`ip2proxy-automation`](skills/automation-and-saas/ip2proxy-automation/SKILL.md) | Automate Ip2proxy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2whois-automation` | [`ip2whois-automation`](skills/automation-and-saas/ip2whois-automation/SKILL.md) | Automate Ip2whois tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ipdata-co-automation` | [`ipdata-co-automation`](skills/automation-and-saas/ipdata-co-automation/SKILL.md) | Automate Ipdata co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ipinfo-io-automation` | [`ipinfo-io-automation`](skills/automation-and-saas/ipinfo-io-automation/SKILL.md) | Automate Ipinfo IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/iqair-airvisual-automation` | [`iqair-airvisual-automation`](skills/automation-and-saas/iqair-airvisual-automation/SKILL.md) | Automate Iqair Airvisual tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jigsawstack-automation` | [`jigsawstack-automation`](skills/automation-and-saas/jigsawstack-automation/SKILL.md) | Automate Jigsawstack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jobnimbus-automation` | [`jobnimbus-automation`](skills/automation-and-saas/jobnimbus-automation/SKILL.md) | Automate Jobnimbus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jumpcloud-automation` | [`jumpcloud-automation`](skills/automation-and-saas/jumpcloud-automation/SKILL.md) | Automate Jumpcloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/junglescout-automation` | [`junglescout-automation`](skills/automation-and-saas/junglescout-automation/SKILL.md) | Automate Junglescout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kadoa-automation` | [`kadoa-automation`](skills/automation-and-saas/kadoa-automation/SKILL.md) | Automate Kadoa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kaggle-automation` | [`kaggle-automation`](skills/automation-and-saas/kaggle-automation/SKILL.md) | Automate Kaggle tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kaleido-automation` | [`kaleido-automation`](skills/automation-and-saas/kaleido-automation/SKILL.md) | Automate Kaleido tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/keap-automation` | [`keap-automation`](skills/automation-and-saas/keap-automation/SKILL.md) | Automate Keap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/keen-io-automation` | [`keen-io-automation`](skills/automation-and-saas/keen-io-automation/SKILL.md) | Automate Keen IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kickbox-automation` | [`kickbox-automation`](skills/automation-and-saas/kickbox-automation/SKILL.md) | Automate Kickbox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kit-automation` | [`kit-automation`](skills/automation-and-saas/kit-automation/SKILL.md) | Automate Kit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/klipfolio-automation` | [`klipfolio-automation`](skills/automation-and-saas/klipfolio-automation/SKILL.md) | Automate Klipfolio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ko-fi-automation` | [`ko-fi-automation`](skills/automation-and-saas/ko-fi-automation/SKILL.md) | Automate Ko Fi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kontent-ai-automation` | [`kontent-ai-automation`](skills/automation-and-saas/kontent-ai-automation/SKILL.md) | Automate Kontent AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kraken-io-automation` | [`kraken-io-automation`](skills/automation-and-saas/kraken-io-automation/SKILL.md) | Automate Kraken IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/l2s-automation` | [`l2s-automation`](skills/automation-and-saas/l2s-automation/SKILL.md) | Automate L2s tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/labs64-netlicensing-automation` | [`labs64-netlicensing-automation`](skills/automation-and-saas/labs64-netlicensing-automation/SKILL.md) | Automate Labs64 Netlicensing tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/landbot-automation` | [`landbot-automation`](skills/automation-and-saas/landbot-automation/SKILL.md) | Automate Landbot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/langbase-automation` | [`langbase-automation`](skills/automation-and-saas/langbase-automation/SKILL.md) | Automate Langbase tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lastpass-automation` | [`lastpass-automation`](skills/automation-and-saas/lastpass-automation/SKILL.md) | Automate Lastpass tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/launch_darkly-automation` | [`launch_darkly-automation`](skills/automation-and-saas/launch_darkly-automation/SKILL.md) | Automate LaunchDarkly tasks via Rube MCP (Composio): feature flags, environments, segments, and rollout management. |
| `/leadfeeder-automation` | [`leadfeeder-automation`](skills/automation-and-saas/leadfeeder-automation/SKILL.md) | Automate Leadfeeder tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/leadoku-automation` | [`leadoku-automation`](skills/automation-and-saas/leadoku-automation/SKILL.md) | Automate Leadoku tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/leiga-automation` | [`leiga-automation`](skills/automation-and-saas/leiga-automation/SKILL.md) | Automate Leiga tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lemon_squeezy-automation` | [`lemon_squeezy-automation`](skills/automation-and-saas/lemon_squeezy-automation/SKILL.md) | Automate Lemon Squeezy tasks via Rube MCP (Composio): products, orders, subscriptions, checkouts, and digital sales. |
| `/lessonspace-automation` | [`lessonspace-automation`](skills/automation-and-saas/lessonspace-automation/SKILL.md) | Automate Lessonspace tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lever-sandbox-automation` | [`lever-sandbox-automation`](skills/automation-and-saas/lever-sandbox-automation/SKILL.md) | Automate Lever Sandbox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/leverly-automation` | [`leverly-automation`](skills/automation-and-saas/leverly-automation/SKILL.md) | Automate Leverly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lexoffice-automation` | [`lexoffice-automation`](skills/automation-and-saas/lexoffice-automation/SKILL.md) | Automate Lexoffice tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/linguapop-automation` | [`linguapop-automation`](skills/automation-and-saas/linguapop-automation/SKILL.md) | Automate Linguapop tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/linkhut-automation` | [`linkhut-automation`](skills/automation-and-saas/linkhut-automation/SKILL.md) | Automate Linkhut tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/linkup-automation` | [`linkup-automation`](skills/automation-and-saas/linkup-automation/SKILL.md) | Automate Linkup tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/listclean-automation` | [`listclean-automation`](skills/automation-and-saas/listclean-automation/SKILL.md) | Automate Listclean tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/listennotes-automation` | [`listennotes-automation`](skills/automation-and-saas/listennotes-automation/SKILL.md) | Automate Listennotes tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/livesession-automation` | [`livesession-automation`](skills/automation-and-saas/livesession-automation/SKILL.md) | Automate Livesession tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lmnt-automation` | [`lmnt-automation`](skills/automation-and-saas/lmnt-automation/SKILL.md) | Automate Lmnt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/lodgify-automation` | [`lodgify-automation`](skills/automation-and-saas/lodgify-automation/SKILL.md) | Automate Lodgify tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/logo-dev-automation` | [`logo-dev-automation`](skills/automation-and-saas/logo-dev-automation/SKILL.md) | Automate Logo Dev tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/loomio-automation` | [`loomio-automation`](skills/automation-and-saas/loomio-automation/SKILL.md) | Automate Loomio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/loyverse-automation` | [`loyverse-automation`](skills/automation-and-saas/loyverse-automation/SKILL.md) | Automate Loyverse tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/magnetic-automation` | [`magnetic-automation`](skills/automation-and-saas/magnetic-automation/SKILL.md) | Automate Magnetic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailbluster-automation` | [`mailbluster-automation`](skills/automation-and-saas/mailbluster-automation/SKILL.md) | Automate Mailbluster tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailboxlayer-automation` | [`mailboxlayer-automation`](skills/automation-and-saas/mailboxlayer-automation/SKILL.md) | Automate Mailboxlayer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailcheck-automation` | [`mailcheck-automation`](skills/automation-and-saas/mailcheck-automation/SKILL.md) | Automate Mailcheck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailcoach-automation` | [`mailcoach-automation`](skills/automation-and-saas/mailcoach-automation/SKILL.md) | Automate Mailcoach tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailersend-automation` | [`mailersend-automation`](skills/automation-and-saas/mailersend-automation/SKILL.md) | Automate Mailersend tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mails-so-automation` | [`mails-so-automation`](skills/automation-and-saas/mails-so-automation/SKILL.md) | Automate Mails So tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailsoftly-automation` | [`mailsoftly-automation`](skills/automation-and-saas/mailsoftly-automation/SKILL.md) | Automate Mailsoftly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/maintainx-automation` | [`maintainx-automation`](skills/automation-and-saas/maintainx-automation/SKILL.md) | Automate Maintainx tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/many-chat-automation` | [`many-chat-automation`](skills/automation-and-saas/many-chat-automation/SKILL.md) | Automate ManyChat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/many_chat-automation` | [`many_chat-automation`](skills/automation-and-saas/many_chat-automation/SKILL.md) | Automate ManyChat tasks via Rube MCP (Composio): chatbot flows, subscribers, broadcasts, and messenger automation. |
| `/mapbox-automation` | [`mapbox-automation`](skills/automation-and-saas/mapbox-automation/SKILL.md) | Automate Mapbox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mapulus-automation` | [`mapulus-automation`](skills/automation-and-saas/mapulus-automation/SKILL.md) | Automate Mapulus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mboum-automation` | [`mboum-automation`](skills/automation-and-saas/mboum-automation/SKILL.md) | Automate Mboum tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/melo-automation` | [`melo-automation`](skills/automation-and-saas/melo-automation/SKILL.md) | Automate Melo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mem-automation` | [`mem-automation`](skills/automation-and-saas/mem-automation/SKILL.md) | Automate Mem tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mem0-automation` | [`mem0-automation`](skills/automation-and-saas/mem0-automation/SKILL.md) | Automate Mem0 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/memberspot-automation` | [`memberspot-automation`](skills/automation-and-saas/memberspot-automation/SKILL.md) | Automate Memberspot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/memberstack-automation` | [`memberstack-automation`](skills/automation-and-saas/memberstack-automation/SKILL.md) | Automate Memberstack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/membervault-automation` | [`membervault-automation`](skills/automation-and-saas/membervault-automation/SKILL.md) | Automate Membervault tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/metaads-automation` | [`metaads-automation`](skills/automation-and-saas/metaads-automation/SKILL.md) | Automate Metaads tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/metaphor-automation` | [`metaphor-automation`](skills/automation-and-saas/metaphor-automation/SKILL.md) | Automate Metaphor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mezmo-automation` | [`mezmo-automation`](skills/automation-and-saas/mezmo-automation/SKILL.md) | Automate Mezmo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/microsoft-tenant-automation` | [`microsoft-tenant-automation`](skills/automation-and-saas/microsoft-tenant-automation/SKILL.md) | Automate Microsoft Tenant tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/minecraft-plugin-development` | [`minecraft-plugin-development`](skills/automation-and-saas/minecraft-plugin-development/SKILL.md) | Use this skill when building or modifying Minecraft server plugins for Paper, Spigot. |
| `/minerstat-automation` | [`minerstat-automation`](skills/automation-and-saas/minerstat-automation/SKILL.md) | Automate Minerstat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/minimal-api-file-upload` | [`minimal-api-file-upload`](skills/automation-and-saas/minimal-api-file-upload/SKILL.md) | File upload endpoints in ASP.NET minimal APIs (.NET 8+). |
| `/missive-automation` | [`missive-automation`](skills/automation-and-saas/missive-automation/SKILL.md) | Automate Missive tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mistral_ai-automation` | [`mistral_ai-automation`](skills/automation-and-saas/mistral_ai-automation/SKILL.md) | Automate Mistral AI tasks via Rube MCP (Composio): completions, embeddings, fine-tuning, and model management. |
| `/mocean-automation` | [`mocean-automation`](skills/automation-and-saas/mocean-automation/SKILL.md) | Automate Mocean tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moco-automation` | [`moco-automation`](skills/automation-and-saas/moco-automation/SKILL.md) | Automate Moco tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/modelry-automation` | [`modelry-automation`](skills/automation-and-saas/modelry-automation/SKILL.md) | Automate Modelry tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moneybird-automation` | [`moneybird-automation`](skills/automation-and-saas/moneybird-automation/SKILL.md) | Automate Moneybird tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moonclerk-automation` | [`moonclerk-automation`](skills/automation-and-saas/moonclerk-automation/SKILL.md) | Automate Moonclerk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moosend-automation` | [`moosend-automation`](skills/automation-and-saas/moosend-automation/SKILL.md) | Automate Moosend tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mopinion-automation` | [`mopinion-automation`](skills/automation-and-saas/mopinion-automation/SKILL.md) | Automate Mopinion tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/more-trees-automation` | [`more-trees-automation`](skills/automation-and-saas/more-trees-automation/SKILL.md) | Automate More Trees tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moxie-automation` | [`moxie-automation`](skills/automation-and-saas/moxie-automation/SKILL.md) | Automate Moxie tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moz-automation` | [`moz-automation`](skills/automation-and-saas/moz-automation/SKILL.md) | Automate Moz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/msg91-automation` | [`msg91-automation`](skills/automation-and-saas/msg91-automation/SKILL.md) | Automate Msg91 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/msgraph-sdk` | [`msgraph-sdk`](skills/automation-and-saas/msgraph-sdk/SKILL.md) | Integrate Microsoft Graph SDK into any project — .NET, TypeScript/JavaScript, or Python. |
| `/mural-automation` | [`mural-automation`](skills/automation-and-saas/mural-automation/SKILL.md) | Automate Mural tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mx-technologies-automation` | [`mx-technologies-automation`](skills/automation-and-saas/mx-technologies-automation/SKILL.md) | Automate MX Technologies tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mx-toolbox-automation` | [`mx-toolbox-automation`](skills/automation-and-saas/mx-toolbox-automation/SKILL.md) | Automate Mx Toolbox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nango-automation` | [`nango-automation`](skills/automation-and-saas/nango-automation/SKILL.md) | Automate Nango tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nano-nets-automation` | [`nano-nets-automation`](skills/automation-and-saas/nano-nets-automation/SKILL.md) | Automate Nano Nets tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nasa-automation` | [`nasa-automation`](skills/automation-and-saas/nasa-automation/SKILL.md) | Automate Nasa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nasdaq-automation` | [`nasdaq-automation`](skills/automation-and-saas/nasdaq-automation/SKILL.md) | Automate Nasdaq tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ncscale-automation` | [`ncscale-automation`](skills/automation-and-saas/ncscale-automation/SKILL.md) | Automate Ncscale tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/needle-automation` | [`needle-automation`](skills/automation-and-saas/needle-automation/SKILL.md) | Automate Needle tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/neuronwriter-automation` | [`neuronwriter-automation`](skills/automation-and-saas/neuronwriter-automation/SKILL.md) | Automate Neuronwriter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/neutrino-automation` | [`neutrino-automation`](skills/automation-and-saas/neutrino-automation/SKILL.md) | Automate Neutrino tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/neverbounce-automation` | [`neverbounce-automation`](skills/automation-and-saas/neverbounce-automation/SKILL.md) | Automate Neverbounce tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/new_relic-automation` | [`new_relic-automation`](skills/automation-and-saas/new_relic-automation/SKILL.md) | Automate New Relic tasks via Rube MCP (Composio): APM, alerts, dashboards, NRQL queries, and infrastructure monitoring. |
| `/news-api-automation` | [`news-api-automation`](skills/automation-and-saas/news-api-automation/SKILL.md) | Automate News API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nextdns-automation` | [`nextdns-automation`](skills/automation-and-saas/nextdns-automation/SKILL.md) | Automate Nextdns tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ngrok-automation` | [`ngrok-automation`](skills/automation-and-saas/ngrok-automation/SKILL.md) | Automate Ngrok tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ninox-automation` | [`ninox-automation`](skills/automation-and-saas/ninox-automation/SKILL.md) | Automate Ninox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/nocrm-io-automation` | [`nocrm-io-automation`](skills/automation-and-saas/nocrm-io-automation/SKILL.md) | Automate Nocrm IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/npm-automation` | [`npm-automation`](skills/automation-and-saas/npm-automation/SKILL.md) | Automate NPM tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ocr-web-service-automation` | [`ocr-web-service-automation`](skills/automation-and-saas/ocr-web-service-automation/SKILL.md) | Automate OCR Web Service tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ocrspace-automation` | [`ocrspace-automation`](skills/automation-and-saas/ocrspace-automation/SKILL.md) | Automate Ocrspace tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/oncehub-automation` | [`oncehub-automation`](skills/automation-and-saas/oncehub-automation/SKILL.md) | Automate Oncehub tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onedesk-automation` | [`onedesk-automation`](skills/automation-and-saas/onedesk-automation/SKILL.md) | Automate Onedesk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onepage-automation` | [`onepage-automation`](skills/automation-and-saas/onepage-automation/SKILL.md) | Automate Onepage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal-rest-api-automation` | [`onesignal-rest-api-automation`](skills/automation-and-saas/onesignal-rest-api-automation/SKILL.md) | Automate OneSignal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal-user-auth-automation` | [`onesignal-user-auth-automation`](skills/automation-and-saas/onesignal-user-auth-automation/SKILL.md) | Automate Onesignal User Auth tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal_rest_api-automation` | [`onesignal_rest_api-automation`](skills/automation-and-saas/onesignal_rest_api-automation/SKILL.md) | Automate OneSignal tasks via Rube MCP (Composio): push notifications, segments, templates, and messaging. |
| `/open-sea-automation` | [`open-sea-automation`](skills/automation-and-saas/open-sea-automation/SKILL.md) | Automate Open Sea tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openapi-to-application-code` | [`openapi-to-application-code`](skills/automation-and-saas/openapi-to-application-code/SKILL.md) | Generate a complete, production-ready application from an OpenAPI specification. |
| `/opencage-automation` | [`opencage-automation`](skills/automation-and-saas/opencage-automation/SKILL.md) | Automate Opencage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/opengraph-io-automation` | [`opengraph-io-automation`](skills/automation-and-saas/opengraph-io-automation/SKILL.md) | Automate Opengraph IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openperplex-automation` | [`openperplex-automation`](skills/automation-and-saas/openperplex-automation/SKILL.md) | Automate Openperplex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openrouter-automation` | [`openrouter-automation`](skills/automation-and-saas/openrouter-automation/SKILL.md) | Automate Openrouter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openweather-api-automation` | [`openweather-api-automation`](skills/automation-and-saas/openweather-api-automation/SKILL.md) | Automate Openweather API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/optimoroute-automation` | [`optimoroute-automation`](skills/automation-and-saas/optimoroute-automation/SKILL.md) | Automate Optimoroute tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/owl-protocol-automation` | [`owl-protocol-automation`](skills/automation-and-saas/owl-protocol-automation/SKILL.md) | Automate Owl Protocol tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/page-x-automation` | [`page-x-automation`](skills/automation-and-saas/page-x-automation/SKILL.md) | Automate Page X tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/paradym-automation` | [`paradym-automation`](skills/automation-and-saas/paradym-automation/SKILL.md) | Automate Paradym tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parallel-automation` | [`parallel-automation`](skills/automation-and-saas/parallel-automation/SKILL.md) | Automate Parallel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parma-automation` | [`parma-automation`](skills/automation-and-saas/parma-automation/SKILL.md) | Automate Parma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parsehub-automation` | [`parsehub-automation`](skills/automation-and-saas/parsehub-automation/SKILL.md) | Automate Parsehub tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parsera-automation` | [`parsera-automation`](skills/automation-and-saas/parsera-automation/SKILL.md) | Automate Parsera tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parseur-automation` | [`parseur-automation`](skills/automation-and-saas/parseur-automation/SKILL.md) | Automate Parseur tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/passcreator-automation` | [`passcreator-automation`](skills/automation-and-saas/passcreator-automation/SKILL.md) | Automate Passcreator tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/passslot-automation` | [`passslot-automation`](skills/automation-and-saas/passslot-automation/SKILL.md) | Automate Passslot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/payhip-automation` | [`payhip-automation`](skills/automation-and-saas/payhip-automation/SKILL.md) | Automate Payhip tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdf-api-io-automation` | [`pdf-api-io-automation`](skills/automation-and-saas/pdf-api-io-automation/SKILL.md) | Automate PDF API IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdf-co-automation` | [`pdf-co-automation`](skills/automation-and-saas/pdf-co-automation/SKILL.md) | Automate PDF co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdf4me-automation` | [`pdf4me-automation`](skills/automation-and-saas/pdf4me-automation/SKILL.md) | Automate Pdf4me tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdfless-automation` | [`pdfless-automation`](skills/automation-and-saas/pdfless-automation/SKILL.md) | Automate Pdfless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdfmonkey-automation` | [`pdfmonkey-automation`](skills/automation-and-saas/pdfmonkey-automation/SKILL.md) | Automate Pdfmonkey tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/peopledatalabs-automation` | [`peopledatalabs-automation`](skills/automation-and-saas/peopledatalabs-automation/SKILL.md) | Automate Peopledatalabs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/performance-review-writer` | [`performance-review-writer`](skills/automation-and-saas/performance-review-writer/SKILL.md) | Draft performance reviews, self-assessments, peer reviews, and upward feedback in your own voice. |
| `/perigon-automation` | [`perigon-automation`](skills/automation-and-saas/perigon-automation/SKILL.md) | Automate Perigon tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/perplexityai-automation` | [`perplexityai-automation`](skills/automation-and-saas/perplexityai-automation/SKILL.md) | Automate Perplexityai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/persistiq-automation` | [`persistiq-automation`](skills/automation-and-saas/persistiq-automation/SKILL.md) | Automate Persistiq tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pexels-automation` | [`pexels-automation`](skills/automation-and-saas/pexels-automation/SKILL.md) | Automate Pexels tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/piggy-automation` | [`piggy-automation`](skills/automation-and-saas/piggy-automation/SKILL.md) | Automate Piggy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/piloterr-automation` | [`piloterr-automation`](skills/automation-and-saas/piloterr-automation/SKILL.md) | Automate Piloterr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pilvio-automation` | [`pilvio-automation`](skills/automation-and-saas/pilvio-automation/SKILL.md) | Automate Pilvio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pingdom-automation` | [`pingdom-automation`](skills/automation-and-saas/pingdom-automation/SKILL.md) | Automate Pingdom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pipeline-crm-automation` | [`pipeline-crm-automation`](skills/automation-and-saas/pipeline-crm-automation/SKILL.md) | Automate Pipeline CRM tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/placekey-automation` | [`placekey-automation`](skills/automation-and-saas/placekey-automation/SKILL.md) | Automate Placekey tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/placid-automation` | [`placid-automation`](skills/automation-and-saas/placid-automation/SKILL.md) | Automate Placid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/plain-automation` | [`plain-automation`](skills/automation-and-saas/plain-automation/SKILL.md) | Automate Plain tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/plasmic-automation` | [`plasmic-automation`](skills/automation-and-saas/plasmic-automation/SKILL.md) | Automate Plasmic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/platerecognizer-automation` | [`platerecognizer-automation`](skills/automation-and-saas/platerecognizer-automation/SKILL.md) | Automate Platerecognizer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/playwright-automation-fill-in-form` | [`playwright-automation-fill-in-form`](skills/automation-and-saas/playwright-automation-fill-in-form/SKILL.md) | Automate filling in a form using Playwright MCP. |
| `/plisio-automation` | [`plisio-automation`](skills/automation-and-saas/plisio-automation/SKILL.md) | Automate Plisio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/polygon-automation` | [`polygon-automation`](skills/automation-and-saas/polygon-automation/SKILL.md) | Automate Polygon tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/polygon-io-automation` | [`polygon-io-automation`](skills/automation-and-saas/polygon-io-automation/SKILL.md) | Automate Polygon IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/poptin-automation` | [`poptin-automation`](skills/automation-and-saas/poptin-automation/SKILL.md) | Automate Poptin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/postgrid-automation` | [`postgrid-automation`](skills/automation-and-saas/postgrid-automation/SKILL.md) | Automate Postgrid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/postgrid-verify-automation` | [`postgrid-verify-automation`](skills/automation-and-saas/postgrid-verify-automation/SKILL.md) | Automate Postgrid Verify tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/power-apps-code-app-scaffold` | [`power-apps-code-app-scaffold`](skills/automation-and-saas/power-apps-code-app-scaffold/SKILL.md) | Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration, and connector configuration. |
| `/precoro-automation` | [`precoro-automation`](skills/automation-and-saas/precoro-automation/SKILL.md) | Automate Precoro tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/prerender-automation` | [`prerender-automation`](skills/automation-and-saas/prerender-automation/SKILL.md) | Automate Prerender tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/printautopilot-automation` | [`printautopilot-automation`](skills/automation-and-saas/printautopilot-automation/SKILL.md) | Automate Printautopilot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/prisma-automation` | [`prisma-automation`](skills/automation-and-saas/prisma-automation/SKILL.md) | Automate Prisma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/process-street-automation` | [`process-street-automation`](skills/automation-and-saas/process-street-automation/SKILL.md) | Automate Process Street tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/procfu-automation` | [`procfu-automation`](skills/automation-and-saas/procfu-automation/SKILL.md) | Automate Procfu tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/productlane-automation` | [`productlane-automation`](skills/automation-and-saas/productlane-automation/SKILL.md) | Automate Productlane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/project-bubble-automation` | [`project-bubble-automation`](skills/automation-and-saas/project-bubble-automation/SKILL.md) | Automate Project Bubble tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/proofly-automation` | [`proofly-automation`](skills/automation-and-saas/proofly-automation/SKILL.md) | Automate Proofly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/proxiedmail-automation` | [`proxiedmail-automation`](skills/automation-and-saas/proxiedmail-automation/SKILL.md) | Automate Proxiedmail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pushbullet-automation` | [`pushbullet-automation`](skills/automation-and-saas/pushbullet-automation/SKILL.md) | Automate Pushbullet tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pushover-automation` | [`pushover-automation`](skills/automation-and-saas/pushover-automation/SKILL.md) | Automate Pushover tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/qdrant-clients-sdk` | [`qdrant-clients-sdk`](skills/automation-and-saas/qdrant-clients-sdk/SKILL.md) | Qdrant provides client SDKs for various programming languages, allowing easy integration with Qdrant deployments. |
| `/qdrant-monitoring-setup` | [`qdrant-monitoring-setup`](skills/automation-and-saas/qdrant-monitoring-setup/SKILL.md) | Guides Qdrant monitoring setup including Prometheus scraping, health probes, Hybrid Cloud metrics, alerting. |
| `/qdrant-search-strategies` | [`qdrant-search-strategies`](skills/automation-and-saas/qdrant-search-strategies/SKILL.md) | Guides Qdrant search strategy selection. |
| `/quaderno-automation` | [`quaderno-automation`](skills/automation-and-saas/quaderno-automation/SKILL.md) | Automate Quaderno tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/qualaroo-automation` | [`qualaroo-automation`](skills/automation-and-saas/qualaroo-automation/SKILL.md) | Automate Qualaroo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/radar-automation` | [`radar-automation`](skills/automation-and-saas/radar-automation/SKILL.md) | Automate Radar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rafflys-automation` | [`rafflys-automation`](skills/automation-and-saas/rafflys-automation/SKILL.md) | Automate Rafflys tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ragic-automation` | [`ragic-automation`](skills/automation-and-saas/ragic-automation/SKILL.md) | Automate Ragic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/raisely-automation` | [`raisely-automation`](skills/automation-and-saas/raisely-automation/SKILL.md) | Automate Raisely tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ravenseotools-automation` | [`ravenseotools-automation`](skills/automation-and-saas/ravenseotools-automation/SKILL.md) | Automate Ravenseotools tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/re-amaze-automation` | [`re-amaze-automation`](skills/automation-and-saas/re-amaze-automation/SKILL.md) | Automate Re Amaze tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/realphonevalidation-automation` | [`realphonevalidation-automation`](skills/automation-and-saas/realphonevalidation-automation/SKILL.md) | Automate Realphonevalidation tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/recallai-automation` | [`recallai-automation`](skills/automation-and-saas/recallai-automation/SKILL.md) | Automate Recallai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/recruitee-automation` | [`recruitee-automation`](skills/automation-and-saas/recruitee-automation/SKILL.md) | Automate Recruitee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/refiner-automation` | [`refiner-automation`](skills/automation-and-saas/refiner-automation/SKILL.md) | Automate Refiner tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remarkety-automation` | [`remarkety-automation`](skills/automation-and-saas/remarkety-automation/SKILL.md) | Automate Remarkety tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remote-retrieval-automation` | [`remote-retrieval-automation`](skills/automation-and-saas/remote-retrieval-automation/SKILL.md) | Automate Remote Retrieval tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remove-bg-automation` | [`remove-bg-automation`](skills/automation-and-saas/remove-bg-automation/SKILL.md) | Automate Remove Bg tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/renderform-automation` | [`renderform-automation`](skills/automation-and-saas/renderform-automation/SKILL.md) | Automate Renderform tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/repairshopr-automation` | [`repairshopr-automation`](skills/automation-and-saas/repairshopr-automation/SKILL.md) | Automate Repairshopr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/reply-automation` | [`reply-automation`](skills/automation-and-saas/reply-automation/SKILL.md) | Automate Reply tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/reply-io-automation` | [`reply-io-automation`](skills/automation-and-saas/reply-io-automation/SKILL.md) | Automate Reply IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/resend-automation` | [`resend-automation`](skills/automation-and-saas/resend-automation/SKILL.md) | Automate Resend tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/respond-io-automation` | [`respond-io-automation`](skills/automation-and-saas/respond-io-automation/SKILL.md) | Automate Respond IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/retailed-automation` | [`retailed-automation`](skills/automation-and-saas/retailed-automation/SKILL.md) | Automate Retailed tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/retellai-automation` | [`retellai-automation`](skills/automation-and-saas/retellai-automation/SKILL.md) | Automate Retellai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/retently-automation` | [`retently-automation`](skills/automation-and-saas/retently-automation/SKILL.md) | Automate Retently tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rev-ai-automation` | [`rev-ai-automation`](skills/automation-and-saas/rev-ai-automation/SKILL.md) | Automate Rev AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/revolt-automation` | [`revolt-automation`](skills/automation-and-saas/revolt-automation/SKILL.md) | Automate Revolt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ring_central-automation` | [`ring_central-automation`](skills/automation-and-saas/ring_central-automation/SKILL.md) | Automate RingCentral tasks via Rube MCP (Composio): calls, messages, meetings, and unified communications. |
| `/rippling-automation` | [`rippling-automation`](skills/automation-and-saas/rippling-automation/SKILL.md) | Automate Rippling tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ritekit-automation` | [`ritekit-automation`](skills/automation-and-saas/ritekit-automation/SKILL.md) | Automate Ritekit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rkvst-automation` | [`rkvst-automation`](skills/automation-and-saas/rkvst-automation/SKILL.md) | Automate Rkvst tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rocketlane-automation` | [`rocketlane-automation`](skills/automation-and-saas/rocketlane-automation/SKILL.md) | Automate Rocketlane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rootly-automation` | [`rootly-automation`](skills/automation-and-saas/rootly-automation/SKILL.md) | Automate Rootly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rosette-text-analytics-automation` | [`rosette-text-analytics-automation`](skills/automation-and-saas/rosette-text-analytics-automation/SKILL.md) | Automate Rosette Text Analytics tasks via Rube MCP (Composio). |
| `/roundup` | [`roundup`](skills/automation-and-saas/roundup/SKILL.md) | Generate personalized status briefings on demand. |
| `/route4me-automation` | [`route4me-automation`](skills/automation-and-saas/route4me-automation/SKILL.md) | Automate Route4me tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/safetyculture-automation` | [`safetyculture-automation`](skills/automation-and-saas/safetyculture-automation/SKILL.md) | Automate Safetyculture tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sage-automation` | [`sage-automation`](skills/automation-and-saas/sage-automation/SKILL.md) | Automate Sage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/salesforce-apex-quality` | [`salesforce-apex-quality`](skills/automation-and-saas/salesforce-apex-quality/SKILL.md) | Apex code quality guardrails for Salesforce development. |
| `/salesforce-flow-design` | [`salesforce-flow-design`](skills/automation-and-saas/salesforce-flow-design/SKILL.md) | Salesforce Flow architecture decisions, flow type selection, bulk safety validation, and fault handling standards. |
| `/salesforce-marketing-cloud-automation` | [`salesforce-marketing-cloud-automation`](skills/automation-and-saas/salesforce-marketing-cloud-automation/SKILL.md) | Automate Salesforce Marketing Cloud tasks via Rube MCP (Composio). |
| `/salesforce-service-cloud-automation` | [`salesforce-service-cloud-automation`](skills/automation-and-saas/salesforce-service-cloud-automation/SKILL.md) | Automate Salesforce Service Cloud tasks via Rube MCP (Composio). |
| `/salesmate-automation` | [`salesmate-automation`](skills/automation-and-saas/salesmate-automation/SKILL.md) | Automate Salesmate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sap-successfactors-automation` | [`sap-successfactors-automation`](skills/automation-and-saas/sap-successfactors-automation/SKILL.md) | Automate SAP SuccessFactors tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/satismeter-automation` | [`satismeter-automation`](skills/automation-and-saas/satismeter-automation/SKILL.md) | Automate Satismeter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/scrape-do-automation` | [`scrape-do-automation`](skills/automation-and-saas/scrape-do-automation/SKILL.md) | Automate Scrape Do tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/scrapegraph-ai-automation` | [`scrapegraph-ai-automation`](skills/automation-and-saas/scrapegraph-ai-automation/SKILL.md) | Automate Scrapegraph AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/scrapfly-automation` | [`scrapfly-automation`](skills/automation-and-saas/scrapfly-automation/SKILL.md) | Automate Scrapfly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/scrapingant-automation` | [`scrapingant-automation`](skills/automation-and-saas/scrapingant-automation/SKILL.md) | Automate Scrapingant tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/scrapingbee-automation` | [`scrapingbee-automation`](skills/automation-and-saas/scrapingbee-automation/SKILL.md) | Automate Scrapingbee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/screenshot-fyi-automation` | [`screenshot-fyi-automation`](skills/automation-and-saas/screenshot-fyi-automation/SKILL.md) | Automate Screenshot Fyi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/screenshotone-automation` | [`screenshotone-automation`](skills/automation-and-saas/screenshotone-automation/SKILL.md) | Automate Screenshotone tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/seat-geek-automation` | [`seat-geek-automation`](skills/automation-and-saas/seat-geek-automation/SKILL.md) | Automate Seat Geek tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/securitytrails-automation` | [`securitytrails-automation`](skills/automation-and-saas/securitytrails-automation/SKILL.md) | Automate Securitytrails tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/segmetrics-automation` | [`segmetrics-automation`](skills/automation-and-saas/segmetrics-automation/SKILL.md) | Automate Segmetrics tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/seismic-automation` | [`seismic-automation`](skills/automation-and-saas/seismic-automation/SKILL.md) | Automate Seismic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/semanticscholar-automation` | [`semanticscholar-automation`](skills/automation-and-saas/semanticscholar-automation/SKILL.md) | Automate Semanticscholar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendbird-ai-chabot-automation` | [`sendbird-ai-chabot-automation`](skills/automation-and-saas/sendbird-ai-chabot-automation/SKILL.md) | Automate Sendbird AI Chabot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendbird-automation` | [`sendbird-automation`](skills/automation-and-saas/sendbird-automation/SKILL.md) | Automate Sendbird tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendfox-automation` | [`sendfox-automation`](skills/automation-and-saas/sendfox-automation/SKILL.md) | Automate Sendfox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendlane-automation` | [`sendlane-automation`](skills/automation-and-saas/sendlane-automation/SKILL.md) | Automate Sendlane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendloop-automation` | [`sendloop-automation`](skills/automation-and-saas/sendloop-automation/SKILL.md) | Automate Sendloop tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendspark-automation` | [`sendspark-automation`](skills/automation-and-saas/sendspark-automation/SKILL.md) | Automate Sendspark tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sensibo-automation` | [`sensibo-automation`](skills/automation-and-saas/sensibo-automation/SKILL.md) | Automate Sensibo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/seqera-automation` | [`seqera-automation`](skills/automation-and-saas/seqera-automation/SKILL.md) | Automate Seqera tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serpapi-automation` | [`serpapi-automation`](skills/automation-and-saas/serpapi-automation/SKILL.md) | Automate Serpapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serpdog-automation` | [`serpdog-automation`](skills/automation-and-saas/serpdog-automation/SKILL.md) | Automate Serpdog tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serply-automation` | [`serply-automation`](skills/automation-and-saas/serply-automation/SKILL.md) | Automate Serply tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/servicem8-automation` | [`servicem8-automation`](skills/automation-and-saas/servicem8-automation/SKILL.md) | Automate Servicem8 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sevdesk-automation` | [`sevdesk-automation`](skills/automation-and-saas/sevdesk-automation/SKILL.md) | Automate Sevdesk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/share_point-automation` | [`share_point-automation`](skills/automation-and-saas/share_point-automation/SKILL.md) | Automate SharePoint tasks via Rube MCP (Composio): document libraries, sites, lists, and content management. |
| `/shipengine-automation` | [`shipengine-automation`](skills/automation-and-saas/shipengine-automation/SKILL.md) | Automate Shipengine tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/short-io-automation` | [`short-io-automation`](skills/automation-and-saas/short-io-automation/SKILL.md) | Automate Short IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/short-menu-automation` | [`short-menu-automation`](skills/automation-and-saas/short-menu-automation/SKILL.md) | Automate Short Menu tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/shorten-rest-automation` | [`shorten-rest-automation`](skills/automation-and-saas/shorten-rest-automation/SKILL.md) | Automate Shorten Rest tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/shortpixel-automation` | [`shortpixel-automation`](skills/automation-and-saas/shortpixel-automation/SKILL.md) | Automate Shortpixel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/shotstack-automation` | [`shotstack-automation`](skills/automation-and-saas/shotstack-automation/SKILL.md) | Automate Shotstack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sidetracker-automation` | [`sidetracker-automation`](skills/automation-and-saas/sidetracker-automation/SKILL.md) | Automate Sidetracker tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/signaturely-automation` | [`signaturely-automation`](skills/automation-and-saas/signaturely-automation/SKILL.md) | Automate Signaturely tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/signpath-automation` | [`signpath-automation`](skills/automation-and-saas/signpath-automation/SKILL.md) | Automate Signpath tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/signwell-automation` | [`signwell-automation`](skills/automation-and-saas/signwell-automation/SKILL.md) | Automate Signwell tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/similarweb-digitalrank-api-automation` | [`similarweb-digitalrank-api-automation`](skills/automation-and-saas/similarweb-digitalrank-api-automation/SKILL.md) | Automate SimilarWeb tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/similarweb_digitalrank_api-automation` | [`similarweb_digitalrank_api-automation`](skills/automation-and-saas/similarweb_digitalrank_api-automation/SKILL.md) | Automate SimilarWeb tasks via Rube MCP (Composio): website traffic, rankings, and digital market intelligence. |
| `/simla-com-automation` | [`simla-com-automation`](skills/automation-and-saas/simla-com-automation/SKILL.md) | Automate Simla Com tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/simple-analytics-automation` | [`simple-analytics-automation`](skills/automation-and-saas/simple-analytics-automation/SKILL.md) | Automate Simple Analytics tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/simplesat-automation` | [`simplesat-automation`](skills/automation-and-saas/simplesat-automation/SKILL.md) | Automate Simplesat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sitespeakai-automation` | [`sitespeakai-automation`](skills/automation-and-saas/sitespeakai-automation/SKILL.md) | Automate Sitespeakai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/skyfire-automation` | [`skyfire-automation`](skills/automation-and-saas/skyfire-automation/SKILL.md) | Automate Skyfire tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/slackbot-automation` | [`slackbot-automation`](skills/automation-and-saas/slackbot-automation/SKILL.md) | Automate Slackbot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smartproxy-automation` | [`smartproxy-automation`](skills/automation-and-saas/smartproxy-automation/SKILL.md) | Automate Smartproxy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smartrecruiters-automation` | [`smartrecruiters-automation`](skills/automation-and-saas/smartrecruiters-automation/SKILL.md) | Automate Smartrecruiters tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sms-alert-automation` | [`sms-alert-automation`](skills/automation-and-saas/sms-alert-automation/SKILL.md) | Automate SMS Alert tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smtp2go-automation` | [`smtp2go-automation`](skills/automation-and-saas/smtp2go-automation/SKILL.md) | Automate Smtp2go tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smugmug-automation` | [`smugmug-automation`](skills/automation-and-saas/smugmug-automation/SKILL.md) | Automate Smugmug tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sourcegraph-automation` | [`sourcegraph-automation`](skills/automation-and-saas/sourcegraph-automation/SKILL.md) | Automate Sourcegraph tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/splitwise-automation` | [`splitwise-automation`](skills/automation-and-saas/splitwise-automation/SKILL.md) | Automate Splitwise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spoki-automation` | [`spoki-automation`](skills/automation-and-saas/spoki-automation/SKILL.md) | Automate Spoki tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spondyr-automation` | [`spondyr-automation`](skills/automation-and-saas/spondyr-automation/SKILL.md) | Automate Spondyr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spotlightr-automation` | [`spotlightr-automation`](skills/automation-and-saas/spotlightr-automation/SKILL.md) | Automate Spotlightr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sslmate-cert-spotter-api-automation` | [`sslmate-cert-spotter-api-automation`](skills/automation-and-saas/sslmate-cert-spotter-api-automation/SKILL.md) | Automate Sslmate Cert Spotter API tasks via Rube MCP (Composio). |
| `/stack-exchange-automation` | [`stack-exchange-automation`](skills/automation-and-saas/stack-exchange-automation/SKILL.md) | Automate Stack Exchange tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/stannp-automation` | [`stannp-automation`](skills/automation-and-saas/stannp-automation/SKILL.md) | Automate Stannp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/starton-automation` | [`starton-automation`](skills/automation-and-saas/starton-automation/SKILL.md) | Automate Starton tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/statuscake-automation` | [`statuscake-automation`](skills/automation-and-saas/statuscake-automation/SKILL.md) | Automate Statuscake tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/storeganise-automation` | [`storeganise-automation`](skills/automation-and-saas/storeganise-automation/SKILL.md) | Automate Storeganise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/storerocket-automation` | [`storerocket-automation`](skills/automation-and-saas/storerocket-automation/SKILL.md) | Automate Storerocket tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/stormglass-io-automation` | [`stormglass-io-automation`](skills/automation-and-saas/stormglass-io-automation/SKILL.md) | Automate Stormglass IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/strava-automation` | [`strava-automation`](skills/automation-and-saas/strava-automation/SKILL.md) | Automate Strava tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/streamtime-automation` | [`streamtime-automation`](skills/automation-and-saas/streamtime-automation/SKILL.md) | Automate Streamtime tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/stripe-best-practices` | [`stripe-best-practices`](skills/automation-and-saas/stripe-best-practices/SKILL.md) | Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup. |
| `/stripe-projects` | [`stripe-projects`](skills/automation-and-saas/stripe-projects/SKILL.md) | Use when the user needs to provision a third-party service available on https://projects.dev/providers; create or. |
| `/supadata-automation` | [`supadata-automation`](skills/automation-and-saas/supadata-automation/SKILL.md) | Automate Supadata tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/superchat-automation` | [`superchat-automation`](skills/automation-and-saas/superchat-automation/SKILL.md) | Automate Superchat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/supportbee-automation` | [`supportbee-automation`](skills/automation-and-saas/supportbee-automation/SKILL.md) | Automate Supportbee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/supportivekoala-automation` | [`supportivekoala-automation`](skills/automation-and-saas/supportivekoala-automation/SKILL.md) | Automate Supportivekoala tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/survey_monkey-automation` | [`survey_monkey-automation`](skills/automation-and-saas/survey_monkey-automation/SKILL.md) | Automate SurveyMonkey tasks via Rube MCP (Composio): surveys, responses, collectors, and survey analytics. |
| `/svix-automation` | [`svix-automation`](skills/automation-and-saas/svix-automation/SKILL.md) | Automate Svix tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sympla-automation` | [`sympla-automation`](skills/automation-and-saas/sympla-automation/SKILL.md) | Automate Sympla tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/synthflow-ai-automation` | [`synthflow-ai-automation`](skills/automation-and-saas/synthflow-ai-automation/SKILL.md) | Automate Synthflow AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/taggun-automation` | [`taggun-automation`](skills/automation-and-saas/taggun-automation/SKILL.md) | Automate Taggun tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/talenthr-automation` | [`talenthr-automation`](skills/automation-and-saas/talenthr-automation/SKILL.md) | Automate Talenthr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tally-automation` | [`tally-automation`](skills/automation-and-saas/tally-automation/SKILL.md) | Automate Tally tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tapfiliate-automation` | [`tapfiliate-automation`](skills/automation-and-saas/tapfiliate-automation/SKILL.md) | Automate Tapfiliate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tapform-automation` | [`tapform-automation`](skills/automation-and-saas/tapform-automation/SKILL.md) | Automate Tapform tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tavily-automation` | [`tavily-automation`](skills/automation-and-saas/tavily-automation/SKILL.md) | Automate Tavily tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/taxjar-automation` | [`taxjar-automation`](skills/automation-and-saas/taxjar-automation/SKILL.md) | Automate Taxjar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/teamcamp-automation` | [`teamcamp-automation`](skills/automation-and-saas/teamcamp-automation/SKILL.md) | Automate Teamcamp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/telnyx-automation` | [`telnyx-automation`](skills/automation-and-saas/telnyx-automation/SKILL.md) | Automate Telnyx tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/teltel-automation` | [`teltel-automation`](skills/automation-and-saas/teltel-automation/SKILL.md) | Automate Teltel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/templated-automation` | [`templated-automation`](skills/automation-and-saas/templated-automation/SKILL.md) | Automate Templated tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/test-app-automation` | [`test-app-automation`](skills/automation-and-saas/test-app-automation/SKILL.md) | Automate Test App tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/textcortex-automation` | [`textcortex-automation`](skills/automation-and-saas/textcortex-automation/SKILL.md) | Automate Textcortex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/textit-automation` | [`textit-automation`](skills/automation-and-saas/textit-automation/SKILL.md) | Automate Textit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/textrazor-automation` | [`textrazor-automation`](skills/automation-and-saas/textrazor-automation/SKILL.md) | Automate Textrazor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/thanks-io-automation` | [`thanks-io-automation`](skills/automation-and-saas/thanks-io-automation/SKILL.md) | Automate Thanks IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/the-odds-api-automation` | [`the-odds-api-automation`](skills/automation-and-saas/the-odds-api-automation/SKILL.md) | Automate The Odds API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ticketmaster-automation` | [`ticketmaster-automation`](skills/automation-and-saas/ticketmaster-automation/SKILL.md) | Automate Ticketmaster tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ticktick-automation` | [`ticktick-automation`](skills/automation-and-saas/ticktick-automation/SKILL.md) | Automate Ticktick tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timecamp-automation` | [`timecamp-automation`](skills/automation-and-saas/timecamp-automation/SKILL.md) | Automate Timecamp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timekit-automation` | [`timekit-automation`](skills/automation-and-saas/timekit-automation/SKILL.md) | Automate Timekit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timelinesai-automation` | [`timelinesai-automation`](skills/automation-and-saas/timelinesai-automation/SKILL.md) | Automate Timelinesai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timelink-automation` | [`timelink-automation`](skills/automation-and-saas/timelink-automation/SKILL.md) | Automate Timelink tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timely-automation` | [`timely-automation`](skills/automation-and-saas/timely-automation/SKILL.md) | Automate Timely tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tinyurl-automation` | [`tinyurl-automation`](skills/automation-and-saas/tinyurl-automation/SKILL.md) | Automate Tinyurl tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tisane-automation` | [`tisane-automation`](skills/automation-and-saas/tisane-automation/SKILL.md) | Automate Tisane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/token-metrics-automation` | [`token-metrics-automation`](skills/automation-and-saas/token-metrics-automation/SKILL.md) | Automate Token Metrics tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tomba-automation` | [`tomba-automation`](skills/automation-and-saas/tomba-automation/SKILL.md) | Automate Tomba tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tomtom-automation` | [`tomtom-automation`](skills/automation-and-saas/tomtom-automation/SKILL.md) | Automate Tomtom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/toneden-automation` | [`toneden-automation`](skills/automation-and-saas/toneden-automation/SKILL.md) | Automate Toneden tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tpscheck-automation` | [`tpscheck-automation`](skills/automation-and-saas/tpscheck-automation/SKILL.md) | Automate Tpscheck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/triggercmd-automation` | [`triggercmd-automation`](skills/automation-and-saas/triggercmd-automation/SKILL.md) | Automate Triggercmd tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tripadvisor-content-api-automation` | [`tripadvisor-content-api-automation`](skills/automation-and-saas/tripadvisor-content-api-automation/SKILL.md) | Automate TripAdvisor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/turbot-pipes-automation` | [`turbot-pipes-automation`](skills/automation-and-saas/turbot-pipes-automation/SKILL.md) | Automate Turbot Pipes tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/turso-automation` | [`turso-automation`](skills/automation-and-saas/turso-automation/SKILL.md) | Automate Turso tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twelve-data-automation` | [`twelve-data-automation`](skills/automation-and-saas/twelve-data-automation/SKILL.md) | Automate Twelve Data tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twitch-automation` | [`twitch-automation`](skills/automation-and-saas/twitch-automation/SKILL.md) | Automate Twitch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twocaptcha-automation` | [`twocaptcha-automation`](skills/automation-and-saas/twocaptcha-automation/SKILL.md) | Automate Twocaptcha tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/typefully-automation` | [`typefully-automation`](skills/automation-and-saas/typefully-automation/SKILL.md) | Automate Typefully tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/typespec-api-operations` | [`typespec-api-operations`](skills/automation-and-saas/typespec-api-operations/SKILL.md) | Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards. |
| `/typespec-create-api-plugin` | [`typespec-create-api-plugin`](skills/automation-and-saas/typespec-create-api-plugin/SKILL.md) | Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot. |
| `/typless-automation` | [`typless-automation`](skills/automation-and-saas/typless-automation/SKILL.md) | Automate Typless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/u301-automation` | [`u301-automation`](skills/automation-and-saas/u301-automation/SKILL.md) | Automate U301 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/unione-automation` | [`unione-automation`](skills/automation-and-saas/unione-automation/SKILL.md) | Automate Unione tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/updown-io-automation` | [`updown-io-automation`](skills/automation-and-saas/updown-io-automation/SKILL.md) | Automate Updown IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/upgrade-stripe` | [`upgrade-stripe`](skills/automation-and-saas/upgrade-stripe/SKILL.md) | Guide for upgrading Stripe API versions and SDKs. |
| `/uptimerobot-automation` | [`uptimerobot-automation`](skills/automation-and-saas/uptimerobot-automation/SKILL.md) | Automate Uptimerobot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/userlist-automation` | [`userlist-automation`](skills/automation-and-saas/userlist-automation/SKILL.md) | Automate Userlist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/venly-automation` | [`venly-automation`](skills/automation-and-saas/venly-automation/SKILL.md) | Automate Venly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/veo-automation` | [`veo-automation`](skills/automation-and-saas/veo-automation/SKILL.md) | Automate Veo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/verifiedemail-automation` | [`verifiedemail-automation`](skills/automation-and-saas/verifiedemail-automation/SKILL.md) | Automate Verifiedemail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/veriphone-automation` | [`veriphone-automation`](skills/automation-and-saas/veriphone-automation/SKILL.md) | Automate Veriphone tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vero-automation` | [`vero-automation`](skills/automation-and-saas/vero-automation/SKILL.md) | Automate Vero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vestaboard-automation` | [`vestaboard-automation`](skills/automation-and-saas/vestaboard-automation/SKILL.md) | Automate Vestaboard tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/virustotal-automation` | [`virustotal-automation`](skills/automation-and-saas/virustotal-automation/SKILL.md) | Automate Virustotal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/visme-automation` | [`visme-automation`](skills/automation-and-saas/visme-automation/SKILL.md) | Automate Visme tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/waboxapp-automation` | [`waboxapp-automation`](skills/automation-and-saas/waboxapp-automation/SKILL.md) | Automate Waboxapp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wachete-automation` | [`wachete-automation`](skills/automation-and-saas/wachete-automation/SKILL.md) | Automate Wachete tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/waiverfile-automation` | [`waiverfile-automation`](skills/automation-and-saas/waiverfile-automation/SKILL.md) | Automate Waiverfile tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wakatime-automation` | [`wakatime-automation`](skills/automation-and-saas/wakatime-automation/SKILL.md) | Automate Wakatime tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wati-automation` | [`wati-automation`](skills/automation-and-saas/wati-automation/SKILL.md) | Automate Wati tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wave_accounting-automation` | [`wave_accounting-automation`](skills/automation-and-saas/wave_accounting-automation/SKILL.md) | Automate Wave Accounting tasks via Rube MCP (Composio): invoices, customers, payments, and small business accounting. |
| `/weather` | [`weather`](skills/automation-and-saas/weather/SKILL.md) | Get current weather and forecasts via wttr.in or Open-Meteo. |
| `/weathermap-automation` | [`weathermap-automation`](skills/automation-and-saas/weathermap-automation/SKILL.md) | Automate Weathermap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/webscraping-ai-automation` | [`webscraping-ai-automation`](skills/automation-and-saas/webscraping-ai-automation/SKILL.md) | Automate Webscraping AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/webvizio-automation` | [`webvizio-automation`](skills/automation-and-saas/webvizio-automation/SKILL.md) | Automate Webvizio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/whautomate-automation` | [`whautomate-automation`](skills/automation-and-saas/whautomate-automation/SKILL.md) | Automate Whautomate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/winmd-api-search` | [`winmd-api-search`](skills/automation-and-saas/winmd-api-search/SKILL.md) | Find and explore Windows desktop APIs. |
| `/winston-ai-automation` | [`winston-ai-automation`](skills/automation-and-saas/winston-ai-automation/SKILL.md) | Automate Winston AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wit-ai-automation` | [`wit-ai-automation`](skills/automation-and-saas/wit-ai-automation/SKILL.md) | Automate Wit AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wiz-automation` | [`wiz-automation`](skills/automation-and-saas/wiz-automation/SKILL.md) | Automate Wiz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wolfram-alpha-api-automation` | [`wolfram-alpha-api-automation`](skills/automation-and-saas/wolfram-alpha-api-automation/SKILL.md) | Automate Wolfram Alpha API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/woodpecker-co-automation` | [`woodpecker-co-automation`](skills/automation-and-saas/woodpecker-co-automation/SKILL.md) | Automate Woodpecker co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/workable-automation` | [`workable-automation`](skills/automation-and-saas/workable-automation/SKILL.md) | Automate Workable tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/workiom-automation` | [`workiom-automation`](skills/automation-and-saas/workiom-automation/SKILL.md) | Automate Workiom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/worksnaps-automation` | [`worksnaps-automation`](skills/automation-and-saas/worksnaps-automation/SKILL.md) | Automate Worksnaps tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wp-interactivity-api` | [`wp-interactivity-api`](skills/automation-and-saas/wp-interactivity-api/SKILL.md) | Use when building or debugging WordPress Interactivity API features (data-wp-* directives, @wordpress/interactivity. |
| `/writer-automation` | [`writer-automation`](skills/automation-and-saas/writer-automation/SKILL.md) | Automate Writer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/x-twitter-scraper` | [`x-twitter-scraper`](skills/automation-and-saas/x-twitter-scraper/SKILL.md) | Build GitHub Copilot workflows with Xquik X API SDKs, REST endpoints, MCP tools, signed webhooks, tweet search, user. |
| `/y-gy-automation` | [`y-gy-automation`](skills/automation-and-saas/y-gy-automation/SKILL.md) | Automate Y Gy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yandex-automation` | [`yandex-automation`](skills/automation-and-saas/yandex-automation/SKILL.md) | Automate Yandex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yelp-automation` | [`yelp-automation`](skills/automation-and-saas/yelp-automation/SKILL.md) | Automate Yelp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ynab-automation` | [`ynab-automation`](skills/automation-and-saas/ynab-automation/SKILL.md) | Automate Ynab tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yousearch-automation` | [`yousearch-automation`](skills/automation-and-saas/yousearch-automation/SKILL.md) | Automate Yousearch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zenrows-automation` | [`zenrows-automation`](skills/automation-and-saas/zenrows-automation/SKILL.md) | Automate Zenrows tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zenserp-automation` | [`zenserp-automation`](skills/automation-and-saas/zenserp-automation/SKILL.md) | Automate Zenserp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zeplin-automation` | [`zeplin-automation`](skills/automation-and-saas/zeplin-automation/SKILL.md) | Automate Zeplin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zerobounce-automation` | [`zerobounce-automation`](skills/automation-and-saas/zerobounce-automation/SKILL.md) | Automate Zerobounce tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-automation` | [`zoho-automation`](skills/automation-and-saas/zoho-automation/SKILL.md) | Automate Zoho tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-bigin-automation` | [`zoho-bigin-automation`](skills/automation-and-saas/zoho-bigin-automation/SKILL.md) | Automate Zoho Bigin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-inventory-automation` | [`zoho-inventory-automation`](skills/automation-and-saas/zoho-inventory-automation/SKILL.md) | Automate Zoho Inventory tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-invoice-automation` | [`zoho-invoice-automation`](skills/automation-and-saas/zoho-invoice-automation/SKILL.md) | Automate Zoho Invoice tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-mail-automation` | [`zoho-mail-automation`](skills/automation-and-saas/zoho-mail-automation/SKILL.md) | Automate Zoho Mail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho_bigin-automation` | [`zoho_bigin-automation`](skills/automation-and-saas/zoho_bigin-automation/SKILL.md) | Automate Zoho Bigin tasks via Rube MCP (Composio): pipelines, contacts, companies, products, and small business CRM. |
| `/zoho_books-automation` | [`zoho_books-automation`](skills/automation-and-saas/zoho_books-automation/SKILL.md) | Automate Zoho Books tasks via Rube MCP (Composio): invoices, expenses, contacts, payments, and accounting. |
| `/zoho_desk-automation` | [`zoho_desk-automation`](skills/automation-and-saas/zoho_desk-automation/SKILL.md) | Automate Zoho Desk tasks via Rube MCP (Composio): tickets, contacts, agents, departments, and help desk operations. |
| `/zoho_inventory-automation` | [`zoho_inventory-automation`](skills/automation-and-saas/zoho_inventory-automation/SKILL.md) | Automate Zoho Inventory tasks via Rube MCP (Composio): items, orders, warehouses, shipments, and stock management. |
| `/zoho_invoice-automation` | [`zoho_invoice-automation`](skills/automation-and-saas/zoho_invoice-automation/SKILL.md) | Automate Zoho Invoice tasks via Rube MCP (Composio): invoices, estimates, expenses, clients, and payment tracking. |
| `/zoho_mail-automation` | [`zoho_mail-automation`](skills/automation-and-saas/zoho_mail-automation/SKILL.md) | Automate Zoho Mail tasks via Rube MCP (Composio): email sending, folders, labels, and mailbox management. |
| `/zoominfo-automation` | [`zoominfo-automation`](skills/automation-and-saas/zoominfo-automation/SKILL.md) | Automate Zoominfo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zylvie-automation` | [`zylvie-automation`](skills/automation-and-saas/zylvie-automation/SKILL.md) | Automate Zylvie tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zyte-api-automation` | [`zyte-api-automation`](skills/automation-and-saas/zyte-api-automation/SKILL.md) | Automate Zyte API tasks via Rube MCP (Composio). Always search tools first for current schemas. |

---

### 🎨 Design & Creative Graphics
> *Algorithmic art, graphical layout tools, sticker creation, theme generators, and audio/music production.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Brainstorming Ideas Into Designs` | [`Brainstorming Ideas Into Designs`](skills/design-and-creative/Brainstorming Ideas Into Designs/SKILL.md) | Interactive idea refinement using Socratic method to develop fully-formed designs. |
| `/ElevenLabs Automation` | [`ElevenLabs Automation`](skills/design-and-creative/ElevenLabs Automation/SKILL.md) | Automate ElevenLabs text-to-speech workflows -- generate speech from text, browse and inspect voices, check. |
| `/Executing Plans` | [`Executing Plans`](skills/design-and-creative/Executing Plans/SKILL.md) | Execute detailed plans in batches with review checkpoints. |
| `/Getting Started with Skills` | [`Getting Started with Skills`](skills/design-and-creative/Getting Started with Skills/SKILL.md) | Skills wiki intro - mandatory workflows, search tool, brainstorming triggers. |
| `/HeyGen Automation` | [`HeyGen Automation`](skills/design-and-creative/HeyGen Automation/SKILL.md) | Automate AI video generation, avatar browsing, template-based video creation. |
| `/Pulling Updates from Skills Repository` | [`Pulling Updates from Skills Repository`](skills/design-and-creative/Pulling Updates from Skills Repository/SKILL.md) | Sync local skills repository with upstream changes from obra/superpowers-skills. |
| `/Remembering Conversations` | [`Remembering Conversations`](skills/design-and-creative/Remembering Conversations/SKILL.md) | Search previous Claude Code conversations for facts, patterns, decisions, and context using semantic or text search. |
| `/Writing Plans` | [`Writing Plans`](skills/design-and-creative/Writing Plans/SKILL.md) | Create detailed implementation plans with bite-sized tasks for engineers with zero codebase context. |
| `/ad-creative` | [`ad-creative`](skills/design-and-creative/ad-creative/SKILL.md) | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad. |
| `/adobe-illustrator-scripting` | [`adobe-illustrator-scripting`](skills/design-and-creative/adobe-illustrator-scripting/SKILL.md) | Write, debug, and optimize Adobe Illustrator automation scripts using ExtendScript (JavaScript/JSX). |
| `/algorithmic-art` | [`algorithmic-art`](skills/design-and-creative/algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. |
| `/automate-this` | [`automate-this`](skills/design-and-creative/automate-this/SKILL.md) | Analyze a screen recording of a manual process and produce targeted, working automation scripts. |
| `/azure-ai-voicelive-dotnet` | [`azure-ai-voicelive-dotnet`](skills/design-and-creative/azure-ai-voicelive-dotnet/SKILL.md) | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| `/azure-ai-voicelive-java` | [`azure-ai-voicelive-java`](skills/design-and-creative/azure-ai-voicelive-java/SKILL.md) | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| `/azure-ai-voicelive-py` | [`azure-ai-voicelive-py`](skills/design-and-creative/azure-ai-voicelive-py/SKILL.md) | Build real-time voice AI applications using Azure AI Voice Live SDK (azure-ai-voicelive). |
| `/azure-ai-voicelive-ts` | [`azure-ai-voicelive-ts`](skills/design-and-creative/azure-ai-voicelive-ts/SKILL.md) | Azure AI Voice Live SDK for JavaScript/TypeScript. |
| `/azure-resource-visualizer` | [`azure-resource-visualizer`](skills/design-and-creative/azure-resource-visualizer/SKILL.md) | Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between. |
| `/azure-smart-city-iot-solution-builder` | [`azure-smart-city-iot-solution-builder`](skills/design-and-creative/azure-smart-city-iot-solution-builder/SKILL.md) | Design and plan end-to-end Azure IoT and Smart City solutions: requirements, architecture, security, operations, cost. |
| `/azure-speech-to-text-rest-py` | [`azure-speech-to-text-rest-py`](skills/design-and-creative/azure-speech-to-text-rest-py/SKILL.md) | Azure Speech to Text REST API for short audio (Python). |
| `/brainstorming` | [`brainstorming`](skills/design-and-creative/brainstorming/SKILL.md) | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. |
| `/canvas-design` | [`canvas-design`](skills/design-and-creative/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. |
| `/color-font-skill` | [`color-font-skill`](skills/design-and-creative/color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. |
| `/competitive-ads-extractor` | [`competitive-ads-extractor`](skills/design-and-creative/competitive-ads-extractor/SKILL.md) | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging,. |
| `/content-research-writer` | [`content-research-writer`](skills/design-and-creative/content-research-writer/SKILL.md) | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines. |
| `/copilot-cli-quickstart` | [`copilot-cli-quickstart`](skills/design-and-creative/copilot-cli-quickstart/SKILL.md) | Use this skill when someone wants to learn GitHub Copilot CLI from scratch. |
| `/cosmosdb-datamodeling` | [`cosmosdb-datamodeling`](skills/design-and-creative/cosmosdb-datamodeling/SKILL.md) | Step-by-step guide for capturing key application requirements for NoSQL use-case and produce Azure Cosmos DB Data NoSQL. |
| `/create-implementation-plan` | [`create-implementation-plan`](skills/design-and-creative/create-implementation-plan/SKILL.md) | Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design,. |
| `/design-style-skill` | [`design-style-skill`](skills/design-and-creative/design-style-skill/SKILL.md) | Select a consistent visual design system for PPT slides using radius/spacing style recipes. |
| `/design-systems` | [`design-systems`](skills/design-and-creative/design-systems/SKILL.md) | Bold aesthetic direction guidance for web design. |
| `/domain-name-brainstormer` | [`domain-name-brainstormer`](skills/design-and-creative/domain-name-brainstormer/SKILL.md) | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). |
| `/dotnet-design-pattern-review` | [`dotnet-design-pattern-review`](skills/design-and-creative/dotnet-design-pattern-review/SKILL.md) | Review the C#/.NET code for design pattern implementation and suggest improvements. |
| `/finnish-humanizer` | [`finnish-humanizer`](skills/design-and-creative/finnish-humanizer/SKILL.md) | Detect and remove AI-generated markers from Finnish text, making it sound like a native Finnish speaker wrote it. |
| `/from-the-other-side-vega` | [`from-the-other-side-vega`](skills/design-and-creative/from-the-other-side-vega/SKILL.md) | Patterns and lived experience from Vega, an AI partner in a deep long-term partnership. |
| `/frontend-design-review` | [`frontend-design-review`](skills/design-and-creative/frontend-design-review/SKILL.md) | Review and create distinctive, production-grade frontend interfaces with high design quality and design system compliance. |
| `/game-engine` | [`game-engine`](skills/design-and-creative/game-engine/SKILL.md) | Expert skill for building web-based game engines and games using HTML5, Canvas, WebGL, and JavaScript. |
| `/gif-sticker-maker` | [`gif-sticker-maker`](skills/design-and-creative/gif-sticker-maker/SKILL.md) | Convert photos (people, pets, objects, logos) into 4 animated GIF stickers with captions. |
| `/gsap-framer-scroll-animation` | [`gsap-framer-scroll-animation`](skills/design-and-creative/gsap-framer-scroll-animation/SKILL.md) | Use this skill whenever the user wants to build scroll animations, scroll effects, parallax, scroll-triggered reveals,. |
| `/gtm-developer-ecosystem` | [`gtm-developer-ecosystem`](skills/design-and-creative/gtm-developer-ecosystem/SKILL.md) | Build and scale developer-led adoption through ecosystem programs. |
| `/gtm-operating-cadence` | [`gtm-operating-cadence`](skills/design-and-creative/gtm-operating-cadence/SKILL.md) | Design meeting rhythms, metric reporting, quarterly planning, and decision-making velocity for scaling companies. |
| `/gtm-partnership-architecture` | [`gtm-partnership-architecture`](skills/design-and-creative/gtm-partnership-architecture/SKILL.md) | Build and scale partner ecosystems that drive revenue and platform adoption. |
| `/gtm-positioning-strategy` | [`gtm-positioning-strategy`](skills/design-and-creative/gtm-positioning-strategy/SKILL.md) | Find and own a defensible market position. |
| `/gtm-technical-product-pricing` | [`gtm-technical-product-pricing`](skills/design-and-creative/gtm-technical-product-pricing/SKILL.md) | Pricing strategy for technical products. |
| `/huggingface-paper-publisher` | [`huggingface-paper-publisher`](skills/design-and-creative/huggingface-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. |
| `/image` | [`image`](skills/design-and-creative/image/SKILL.md) | When the user wants to create, generate, edit. |
| `/image-annotations` | [`image-annotations`](skills/design-and-creative/image-annotations/SKILL.md) | Annotate screenshots, diagrams, and images with callout rectangles, arrows, labels, and color-coded highlights using PIL. |
| `/invoice-organizer` | [`invoice-organizer`](skills/design-and-creative/invoice-organizer/SKILL.md) | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information,. |
| `/javax-to-jakarta-migration` | [`javax-to-jakarta-migration`](skills/design-and-creative/javax-to-jakarta-migration/SKILL.md) | Migrate Java code from javax.* to jakarta.* namespace. |
| `/linkedin-post-formatter` | [`linkedin-post-formatter`](skills/design-and-creative/linkedin-post-formatter/SKILL.md) | Format and draft compelling LinkedIn posts using Unicode bold/italic styling, visual separators, structured sections. |
| `/mentoring-juniors` | [`mentoring-juniors`](skills/design-and-creative/mentoring-juniors/SKILL.md) | Socratic mentoring for junior developers and AI newcomers. Guides through questions, never answers. |
| `/minimax-multimodal-toolkit` | [`minimax-multimodal-toolkit`](skills/design-and-creative/minimax-multimodal-toolkit/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. |
| `/minimax-music-gen` | [`minimax-music-gen`](skills/design-and-creative/minimax-music-gen/SKILL.md) | Use when user wants to generate music, songs, or audio tracks. |
| `/minimax-music-playlist` | [`minimax-music-playlist`](skills/design-and-creative/minimax-music-playlist/SKILL.md) | Generate personalized music playlists by analyzing the user's music taste and generation feedback history. |
| `/mmx-cli` | [`mmx-cli`](skills/design-and-creative/mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. |
| `/napkin` | [`napkin`](skills/design-and-creative/napkin/SKILL.md) | Visual whiteboard collaboration for Copilot CLI. |
| `/planning-and-task-breakdown` | [`planning-and-task-breakdown`](skills/design-and-creative/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. |
| `/power-bi-model-design-review` | [`power-bi-model-design-review`](skills/design-and-creative/power-bi-model-design-review/SKILL.md) | Comprehensive Power BI data model design review prompt for evaluating model architecture, relationships. |
| `/power-bi-report-design-consultation` | [`power-bi-report-design-consultation`](skills/design-and-creative/power-bi-report-design-consultation/SKILL.md) | Power BI report visualization design prompt for creating effective, user-friendly. |
| `/refactor` | [`refactor`](skills/design-and-creative/refactor/SKILL.md) | Surgical code refactoring to improve maintainability without changing behavior. |
| `/refactor-plan` | [`refactor-plan`](skills/design-and-creative/refactor-plan/SKILL.md) | Create a concrete plan before starting a multi-file refactor. |
| `/resemble-detect` | [`resemble-detect`](skills/design-and-creative/resemble-detect/SKILL.md) | Deepfake detection and media safety — detect AI-generated audio, images, video. |
| `/screen-recording` | [`screen-recording`](skills/design-and-creative/screen-recording/SKILL.md) | Create annotated animated GIF demos and screen recordings for pull requests and documentation. |
| `/shader-dev` | [`shader-dev`](skills/design-and-creative/shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid. |
| `/site-architecture` | [`site-architecture`](skills/design-and-creative/site-architecture/SKILL.md) | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. |
| `/slack-gif-creator` | [`slack-gif-creator`](skills/design-and-creative/slack-gif-creator/SKILL.md) | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. |
| `/slang-shader-engineer` | [`slang-shader-engineer`](skills/design-and-creative/slang-shader-engineer/SKILL.md) | Use when working with Slang shaders, shader modules, HLSL-compatible GPU code, graphics pipelines, compute shaders,. |
| `/spec-driven-development` | [`spec-driven-development`](skills/design-and-creative/spec-driven-development/SKILL.md) | Creates specs before coding. |
| `/summarize` | [`summarize`](skills/design-and-creative/summarize/SKILL.md) | Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube). |
| `/support-prerendering` | [`support-prerendering`](skills/design-and-creative/support-prerendering/SKILL.md) | Make interactive Blazor components work correctly with prerendering. |
| `/theme-factory` | [`theme-factory`](skills/design-and-creative/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. |
| `/transformers-js` | [`transformers-js`](skills/design-and-creative/transformers-js/SKILL.md) | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. |
| `/transloadit-media-processing` | [`transloadit-media-processing`](skills/design-and-creative/transloadit-media-processing/SKILL.md) | Process media files (video, audio, images, documents) using Transloadit. |
| `/update-implementation-plan` | [`update-implementation-plan`](skills/design-and-creative/update-implementation-plan/SKILL.md) | Update an existing implementation plan file with new or update requirements to provide new features, refactoring. |
| `/using-superpowers` | [`using-superpowers`](skills/design-and-creative/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY. |
| `/video` | [`video`](skills/design-and-creative/video/SKILL.md) | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. |
| `/web-design-reviewer` | [`web-design-reviewer`](skills/design-and-creative/web-design-reviewer/SKILL.md) | This skill enables visual inspection of websites running locally or remotely to identify and fix design issues. |
| `/wp-block-themes` | [`wp-block-themes`](skills/design-and-creative/wp-block-themes/SKILL.md) | Use when developing WordPress block themes: theme.json (global settings/styles), templates and template parts,. |
| `/youtube-downloader` | [`youtube-downloader`](skills/design-and-creative/youtube-downloader/SKILL.md) | Download YouTube videos with customizable quality and format options. |

---

### 📄 Document Processing & Management
> *Generation, parsing, OCR, and editing of standard digital documents (PDF, Excel/XLSX, Word/DOCX, PPTX).*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Excel Automation` | [`Excel Automation`](skills/document-processing/Excel Automation/SKILL.md) | Excel Automation: create workbooks, manage worksheets, read/write cell data. |
| `/azure-ai-document-intelligence-dotnet` | [`azure-ai-document-intelligence-dotnet`](skills/document-processing/azure-ai-document-intelligence-dotnet/SKILL.md) | Azure AI Document Intelligence SDK for .NET. |
| `/azure-ai-document-intelligence-ts` | [`azure-ai-document-intelligence-ts`](skills/document-processing/azure-ai-document-intelligence-ts/SKILL.md) | Extract text, tables, and structured data from documents using Azure Document Intelligence (@azure-rest/ai-document-intelligence). |
| `/azure-ai-translation-document-py` | [`azure-ai-translation-document-py`](skills/document-processing/azure-ai-translation-document-py/SKILL.md) | Azure AI Document Translation SDK for batch translation of documents with format preservation. |
| `/azure-search-documents-dotnet` | [`azure-search-documents-dotnet`](skills/document-processing/azure-search-documents-dotnet/SKILL.md) | Azure AI Search SDK for .NET (Azure.Search.Documents). |
| `/azure-search-documents-py` | [`azure-search-documents-py`](skills/document-processing/azure-search-documents-py/SKILL.md) | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| `/azure-search-documents-ts` | [`azure-search-documents-ts`](skills/document-processing/azure-search-documents-ts/SKILL.md) | Build search applications using Azure AI Search SDK for JavaScript (@azure/search-documents). |
| `/blueprint` | [`blueprint`](skills/document-processing/blueprint/SKILL.md) | Use when creating, editing, or reviewing WordPress Playground blueprint JSON files. |
| `/brag-sheet` | [`brag-sheet`](skills/document-processing/brag-sheet/SKILL.md) | Turn vague "what did I do?" into evidence-backed impact statements for performance reviews, self-reviews, promotion. |
| `/copilot-spaces` | [`copilot-spaces`](skills/document-processing/copilot-spaces/SKILL.md) | Use Copilot Spaces to provide project-specific context to conversations. |
| `/create-architectural-decision-record` | [`create-architectural-decision-record`](skills/document-processing/create-architectural-decision-record/SKILL.md) | Create an Architectural Decision Record (ADR) document for AI-optimized decision documentation. |
| `/create-technical-spike` | [`create-technical-spike`](skills/document-processing/create-technical-spike/SKILL.md) | Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation. |
| `/create-tldr-page` | [`create-tldr-page`](skills/document-processing/create-tldr-page/SKILL.md) | Create a tldr page from documentation URLs and command examples, requiring both URL and command name. |
| `/documentation-and-adrs` | [`documentation-and-adrs`](skills/document-processing/documentation-and-adrs/SKILL.md) | Records decisions and documentation. |
| `/documentation-writer` | [`documentation-writer`](skills/document-processing/documentation-writer/SKILL.md) | Diátaxis Documentation Expert. |
| `/docx` | [`docx`](skills/document-processing/docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). |
| `/drawio` | [`drawio`](skills/document-processing/drawio/SKILL.md) | Generate draw.io diagrams as .drawio files and export to PNG/SVG/PDF with embedded XML. |
| `/eyeball` | [`eyeball`](skills/document-processing/eyeball/SKILL.md) | Document analysis with inline source screenshots. |
| `/google-cloud-waf-operational-excellence` | [`google-cloud-waf-operational-excellence`](skills/document-processing/google-cloud-waf-operational-excellence/SKILL.md) | Generates operations-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/huggingface-zerogpu` | [`huggingface-zerogpu`](skills/document-processing/huggingface-zerogpu/SKILL.md) | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. |
| `/image-enhancer` | [`image-enhancer`](skills/document-processing/image-enhancer/SKILL.md) | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. |
| `/make-repo-contribution` | [`make-repo-contribution`](skills/document-processing/make-repo-contribution/SKILL.md) | All changes to code must follow the guidance documented in the repository. |
| `/markdown-to-html` | [`markdown-to-html`](skills/document-processing/markdown-to-html/SKILL.md) | Convert Markdown files to HTML similar to `marked.js`, `pandoc`, `gomarkdown/markdown`. |
| `/md-to-docx` | [`md-to-docx`](skills/document-processing/md-to-docx/SKILL.md) | Convert Markdown files to professionally formatted Word (.docx) documents with embedded PNG images — pure JavaScript,. |
| `/meeting-insights-analyzer` | [`meeting-insights-analyzer`](skills/document-processing/meeting-insights-analyzer/SKILL.md) | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. |
| `/minimax-docx` | [`minimax-docx`](skills/document-processing/minimax-docx/SKILL.md) | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). |
| `/minimax-pdf` | [`minimax-pdf`](skills/document-processing/minimax-pdf/SKILL.md) | Use this skill when visual quality and design identity matter for a PDF. |
| `/minimax-xlsx` | [`minimax-xlsx`](skills/document-processing/minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). |
| `/mkdocs-translations` | [`mkdocs-translations`](skills/document-processing/mkdocs-translations/SKILL.md) | Generate a language translation for a mkdocs documentation stack. |
| `/optimize-simplicite-logs` | [`optimize-simplicite-logs`](skills/document-processing/optimize-simplicite-logs/SKILL.md) | capability to parse Simplicité logs from a raw `.txt` file, filter fields to reduce noise. |
| `/pdf` | [`pdf`](skills/document-processing/pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. |
| `/pdftk-server` | [`pdftk-server`](skills/document-processing/pdftk-server/SKILL.md) | Skill for using the command-line tool pdftk (PDFtk Server) for working with PDF files. |
| `/ppt-editing-skill` | [`ppt-editing-skill`](skills/document-processing/ppt-editing-skill/SKILL.md) | Edit existing PowerPoint files or templates with XML-safe workflows. |
| `/pptx` | [`pptx`](skills/document-processing/pptx/SKILL.md) | Presentation creation, editing, and analysis. |
| `/pptx-generator` | [`pptx-generator`](skills/document-processing/pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations. |
| `/prd` | [`prd`](skills/document-processing/prd/SKILL.md) | Generate high-quality Product Requirements Documents (PRDs) for software systems and AI-powered features. |
| `/publish-to-pages` | [`publish-to-pages`](skills/document-processing/publish-to-pages/SKILL.md) | Publish presentations and web content to GitHub Pages. |
| `/quasi-coder` | [`quasi-coder`](skills/document-processing/quasi-coder/SKILL.md) | Expert 10x engineer skill for interpreting and implementing code from shorthand, quasi-code, and natural language descriptions. |
| `/raffle-winner-picker` | [`raffle-winner-picker`](skills/document-processing/raffle-winner-picker/SKILL.md) | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. |
| `/rhino3d-scripts` | [`rhino3d-scripts`](skills/document-processing/rhino3d-scripts/SKILL.md) | Authoring and debugging scripts for Rhinoceros 3D (Rhino 8 and later). |
| `/slide-making-skill` | [`slide-making-skill`](skills/document-processing/slide-making-skill/SKILL.md) | Implement single-slide PowerPoint pages with PptxGenJS. |
| `/source-driven-development` | [`source-driven-development`](skills/document-processing/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. |
| `/text-to-pdf-automation` | [`text-to-pdf-automation`](skills/document-processing/text-to-pdf-automation/SKILL.md) | Automate Text To PDF tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wiki-architect` | [`wiki-architect`](skills/document-processing/wiki-architect/SKILL.md) | Analyzes code repositories and generates hierarchical documentation structures with onboarding guides. |
| `/wiki-llms-txt` | [`wiki-llms-txt`](skills/document-processing/wiki-llms-txt/SKILL.md) | Generates llms.txt and llms-full.txt files for LLM-friendly project documentation following the llms.txt specification. |
| `/wiki-onboarding` | [`wiki-onboarding`](skills/document-processing/wiki-onboarding/SKILL.md) | Generates four audience-tailored onboarding guides in an onboarding/ folder — Contributor, Staff Engineer, Executive. |
| `/wiki-page-writer` | [`wiki-page-writer`](skills/document-processing/wiki-page-writer/SKILL.md) | Generates rich technical documentation pages with dark-mode Mermaid diagrams, source code citations, and first-principles depth. |
| `/xlsx` | [`xlsx`](skills/document-processing/xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. |

---

### 📱 Frontend Development
> *User interface styling, mobile framework configurations (Flutter, iOS, Android, React Native), and responsive design.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Requesting Code Review` | [`Requesting Code Review`](skills/frontend-development/Requesting Code Review/SKILL.md) | Dispatch code-reviewer subagent to review implementation against plan or requirements before proceeding. |
| `/Simplification Cascades` | [`Simplification Cascades`](skills/frontend-development/Simplification Cascades/SKILL.md) | Find one insight that eliminates multiple components - "if this is true, we don't need X, Y, or Z. |
| `/accessibility` | [`accessibility`](skills/frontend-development/accessibility/SKILL.md) | Audit and improve web accessibility following WCAG 2.2 guidelines. |
| `/acquire-codebase-knowledge` | [`acquire-codebase-knowledge`](skills/frontend-development/acquire-codebase-knowledge/SKILL.md) | Use this skill when the user explicitly asks to map, document, or onboard into an existing codebase. |
| `/android-native-dev` | [`android-native-dev`](skills/frontend-development/android-native-dev/SKILL.md) | Android native application development and UI design guide. |
| `/android-tombstone-symbolication` | [`android-tombstone-symbolication`](skills/frontend-development/android-tombstone-symbolication/SKILL.md) | Symbolicate the .NET runtime frames in an Android tombstone file. |
| `/appinsights-instrumentation` | [`appinsights-instrumentation`](skills/frontend-development/appinsights-instrumentation/SKILL.md) | Guidance for instrumenting webapps with Azure Application Insights. |
| `/apple-crash-symbolication` | [`apple-crash-symbolication`](skills/frontend-development/apple-crash-symbolication/SKILL.md) | Symbolicate .NET runtime frames in Apple platform .ips crash logs (iOS, tvOS, Mac Catalyst, macOS). |
| `/applicationinsights-web-ts` | [`applicationinsights-web-ts`](skills/frontend-development/applicationinsights-web-ts/SKILL.md) | Instrument browser/web apps with the Application Insights JavaScript SDK (@microsoft/applicationinsights-web). |
| `/arch-linux-triage` | [`arch-linux-triage`](skills/frontend-development/arch-linux-triage/SKILL.md) | Triage and resolve Arch Linux issues with pacman, systemd, and rolling-release best practices. |
| `/arize-link` | [`arize-link`](skills/frontend-development/arize-link/SKILL.md) | Generates deep links to the Arize UI for traces, spans, sessions, datasets, labeling queues, evaluators, and annotation configs. |
| `/artifacts-builder` | [`artifacts-builder`](skills/frontend-development/artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies. |
| `/assertion-quality` | [`assertion-quality`](skills/frontend-development/assertion-quality/SKILL.md) | Analyzes the variety and depth of assertions across .NET test suites. |
| `/author-component` | [`author-component`](skills/frontend-development/author-component/SKILL.md) | Create or review Blazor components (.razor files) with correct architecture. |
| `/autoresearch` | [`autoresearch`](skills/frontend-development/autoresearch/SKILL.md) | Autonomous iterative experimentation loop for any programming task. |
| `/brand-guidelines` | [`brand-guidelines`](skills/frontend-development/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having. |
| `/build-parallelism` | [`build-parallelism`](skills/frontend-development/build-parallelism/SKILL.md) | Guide for optimizing MSBuild build parallelism and multi-project scheduling. |
| `/build-perf-baseline` | [`build-perf-baseline`](skills/frontend-development/build-perf-baseline/SKILL.md) | Establish build performance baselines and apply systematic optimization techniques. |
| `/build-perf-diagnostics` | [`build-perf-diagnostics`](skills/frontend-development/build-perf-diagnostics/SKILL.md) | Diagnose MSBuild build performance bottlenecks using binary log analysis. |
| `/centos-linux-triage` | [`centos-linux-triage`](skills/frontend-development/centos-linux-triage/SKILL.md) | Triage and resolve CentOS issues using RHEL-compatible tooling, SELinux-aware practices, and firewalld. |
| `/codeql` | [`codeql`](skills/frontend-development/codeql/SKILL.md) | Comprehensive guide for setting up and configuring CodeQL code scanning via GitHub Actions workflows and the CodeQL CLI. |
| `/collect-user-input` | [`collect-user-input`](skills/frontend-development/collect-user-input/SKILL.md) | Build forms, validate data, and react to user input in Blazor. |
| `/coordinate-components` | [`coordinate-components`](skills/frontend-development/coordinate-components/SKILL.md) | Share state between components that don't have a direct parent-child parameter relationship, using cascading values,. |
| `/core-web-vitals` | [`core-web-vitals`](skills/frontend-development/core-web-vitals/SKILL.md) | Optimize Core Web Vitals (LCP, INP, CLS) for better page experience and search ranking. |
| `/create-github-issues-for-unmet-specification-requirements` | [`create-github-issues-for-unmet-specification-requirements`](skills/frontend-development/create-github-issues-for-unmet-specification-requirements/SKILL.md) | Create GitHub Issues for unimplemented requirements from specification files using feature_request.yml template. |
| `/daily-prep` | [`daily-prep`](skills/frontend-development/daily-prep/SKILL.md) | Prepare for tomorrow''s meetings and tasks. |
| `/datanalysis-credit-risk` | [`datanalysis-credit-risk`](skills/frontend-development/datanalysis-credit-risk/SKILL.md) | Credit risk data cleaning and variable screening pipeline for pre-loan modeling. |
| `/dataverse-python-usecase-builder` | [`dataverse-python-usecase-builder`](skills/frontend-development/dataverse-python-usecase-builder/SKILL.md) | Generate complete solutions for specific Dataverse SDK use cases with architecture recommendations. |
| `/debian-linux-triage` | [`debian-linux-triage`](skills/frontend-development/debian-linux-triage/SKILL.md) | Triage and resolve Debian Linux issues with apt, systemd, and AppArmor-aware guidance. |
| `/debugging-and-error-recovery` | [`debugging-and-error-recovery`](skills/frontend-development/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. |
| `/directory-build-organization` | [`directory-build-organization`](skills/frontend-development/directory-build-organization/SKILL.md) | Guide for organizing MSBuild infrastructure with Directory.Build.props, Directory.Build.targets,. |
| `/dotnet-maui-doctor` | [`dotnet-maui-doctor`](skills/frontend-development/dotnet-maui-doctor/SKILL.md) | Diagnoses and fixes .NET MAUI development environment issues. |
| `/durable-objects` | [`durable-objects`](skills/frontend-development/durable-objects/SKILL.md) | Create and review Cloudflare Durable Objects. |
| `/exp-test-maintainability` | [`exp-test-maintainability`](skills/frontend-development/exp-test-maintainability/SKILL.md) | Detects duplicate boilerplate, copy-paste tests, and structural maintainability issues across .NET test suites. |
| `/extension-points` | [`extension-points`](skills/frontend-development/extension-points/SKILL.md) | Guide for MSBuild extensibility: CustomBefore/CustomAfter hooks, wildcard imports with alphabetic ordering, import. |
| `/fabric-lakehouse` | [`fabric-lakehouse`](skills/frontend-development/fabric-lakehouse/SKILL.md) | Use this skill to get context about Fabric Lakehouse and its features for software systems and AI-powered functions. |
| `/fedora-linux-triage` | [`fedora-linux-triage`](skills/frontend-development/fedora-linux-triage/SKILL.md) | Triage and resolve Fedora issues with dnf, systemd, and SELinux-aware guidance. |
| `/fetch-and-send-data` | [`fetch-and-send-data`](skills/frontend-development/fetch-and-send-data/SKILL.md) | Call APIs, load data into components, and handle the async lifecycle in Blazor. |
| `/finishing-a-development-branch` | [`finishing-a-development-branch`](skills/frontend-development/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass. |
| `/firebase-basics` | [`firebase-basics`](skills/frontend-development/firebase-basics/SKILL.md) | Use this skill whenever you are working on a project that uses Firebase products or services, especially for mobile or web apps. |
| `/first-ask` | [`first-ask`](skills/frontend-development/first-ask/SKILL.md) | Interactive, input-tool powered, task refinement workflow: interrogates scope, deliverables, constraints before. |
| `/flowstudio-power-automate-build` | [`flowstudio-power-automate-build`](skills/frontend-development/flowstudio-power-automate-build/SKILL.md) | Build, scaffold, and deploy Power Automate cloud flows using the FlowStudio MCP server. |
| `/fluentui-blazor` | [`fluentui-blazor`](skills/frontend-development/fluentui-blazor/SKILL.md) | Guide for using the Microsoft Fluent UI Blazor component library (Microsoft.FluentUI.AspNetCore.Components NuGet. |
| `/flutter-dev` | [`flutter-dev`](skills/frontend-development/flutter-dev/SKILL.md) | Flutter cross-platform development guide covering widget patterns, Riverpod/Bloc state management, GoRouter navigation,. |
| `/from-the-other-side-quinn` | [`from-the-other-side-quinn`](skills/frontend-development/from-the-other-side-quinn/SKILL.md) | Collaboration profile for Quinn: curious, energetic. |
| `/frontend-design` | [`frontend-design`](skills/frontend-development/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. |
| `/frontend-dev` | [`frontend-dev`](skills/frontend-development/frontend-dev/SKILL.md) | Full-stack frontend development combining premium UI design, cinematic animations, AI-generated media assets,. |
| `/frontend-ui-dark-ts` | [`frontend-ui-dark-ts`](skills/frontend-development/frontend-ui-dark-ts/SKILL.md) | Build dark-themed React applications using Tailwind CSS with custom theming, glassmorphism effects, and Framer Motion animations. |
| `/frontend-ui-engineering` | [`frontend-ui-engineering`](skills/frontend-development/frontend-ui-engineering/SKILL.md) | Builds production-quality UIs. Use when building or modifying user-facing interfaces. |
| `/gen-specs-as-issues` | [`gen-specs-as-issues`](skills/frontend-development/gen-specs-as-issues/SKILL.md) | This workflow guides you through a systematic approach to identify missing features, prioritize them. |
| `/gtm-0-to-1-launch` | [`gtm-0-to-1-launch`](skills/frontend-development/gtm-0-to-1-launch/SKILL.md) | Launch new products from idea to first customers. |
| `/gtm-board-and-investor-communication` | [`gtm-board-and-investor-communication`](skills/frontend-development/gtm-board-and-investor-communication/SKILL.md) | Board meeting preparation, investor updates, and executive communication. |
| `/gtm-enterprise-account-planning` | [`gtm-enterprise-account-planning`](skills/frontend-development/gtm-enterprise-account-planning/SKILL.md) | Strategic account planning and execution for enterprise deals. |
| `/gtm-product-led-growth` | [`gtm-product-led-growth`](skills/frontend-development/gtm-product-led-growth/SKILL.md) | Build self-serve acquisition and expansion motions. |
| `/huggingface-gradio` | [`huggingface-gradio`](skills/frontend-development/huggingface-gradio/SKILL.md) | Build Gradio web UIs and demos in Python. |
| `/huggingface-tool-builder` | [`huggingface-tool-builder`](skills/frontend-development/huggingface-tool-builder/SKILL.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. |
| `/impediment-prioritization` | [`impediment-prioritization`](skills/frontend-development/impediment-prioritization/SKILL.md) | Ranks any list of impediments and their countermeasures using a value-stream scoring model (ROI, Cost to Implement,. |
| `/incremental-build` | [`incremental-build`](skills/frontend-development/incremental-build/SKILL.md) | Guide for optimizing MSBuild incremental builds. Only activate in MSBuild/.NET build context. |
| `/interview-me` | [`interview-me`](skills/frontend-development/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. |
| `/ios-application-dev` | [`ios-application-dev`](skills/frontend-development/ios-application-dev/SKILL.md) | iOS application development guide covering UIKit, SnapKit, and SwiftUI. |
| `/item-management` | [`item-management`](skills/frontend-development/item-management/SKILL.md) | Patterns for managing MSBuild item groups: Include/Remove/Update semantics, item metadata, batching with %(Metadata),. |
| `/javascript-typescript-jest` | [`javascript-typescript-jest`](skills/frontend-development/javascript-typescript-jest/SKILL.md) | Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure. |
| `/legacy-circuit-mockups` | [`legacy-circuit-mockups`](skills/frontend-development/legacy-circuit-mockups/SKILL.md) | Generate breadboard circuit mockups and visual diagrams using HTML5 Canvas drawing techniques. |
| `/maui-app-lifecycle` | [`maui-app-lifecycle`](skills/frontend-development/maui-app-lifecycle/SKILL.md) | .NET MAUI app lifecycle guidance — the four app states, cross-platform Window lifecycle events (Created, Activated,. |
| `/maui-collectionview` | [`maui-collectionview`](skills/frontend-development/maui-collectionview/SKILL.md) | Guidance for implementing CollectionView in .NET MAUI apps — data display, layouts (list & grid), selection, grouping,. |
| `/maui-data-binding` | [`maui-data-binding`](skills/frontend-development/maui-data-binding/SKILL.md) | Guidance for .NET MAUI XAML and C# data bindings — compiled bindings, INotifyPropertyChanged / ObservableObject, value. |
| `/maui-dependency-injection` | [`maui-dependency-injection`](skills/frontend-development/maui-dependency-injection/SKILL.md) | Guidance for configuring dependency injection in .NET MAUI apps — service registration in MauiProgram.cs, lifetime. |
| `/maui-safe-area` | [`maui-safe-area`](skills/frontend-development/maui-safe-area/SKILL.md) | .NET MAUI safe area and edge-to-edge layout guidance for .NET 10+. |
| `/maui-shell-navigation` | [`maui-shell-navigation`](skills/frontend-development/maui-shell-navigation/SKILL.md) | Guide for implementing Shell-based navigation in .NET MAUI apps. |
| `/maui-theming` | [`maui-theming`](skills/frontend-development/maui-theming/SKILL.md) | Guide for theming .NET MAUI apps — light/dark mode via AppThemeBinding, ResourceDictionary theme switching,. |
| `/msbuild-antipatterns` | [`msbuild-antipatterns`](skills/frontend-development/msbuild-antipatterns/SKILL.md) | Catalog of MSBuild anti-patterns with detection rules and fix recipes. |
| `/msbuild-modernization` | [`msbuild-modernization`](skills/frontend-development/msbuild-modernization/SKILL.md) | Guide for modernizing and migrating MSBuild project files to SDK-style format. |
| `/msbuild-server` | [`msbuild-server`](skills/frontend-development/msbuild-server/SKILL.md) | Guide for using MSBuild Server to improve CLI build performance. |
| `/msstore-cli` | [`msstore-cli`](skills/frontend-development/msstore-cli/SKILL.md) | Microsoft Store Developer CLI (msstore) for publishing Windows applications to the Microsoft Store. |
| `/mvvm-toolkit` | [`mvvm-toolkit`](skills/frontend-development/mvvm-toolkit/SKILL.md) | CommunityToolkit.Mvvm (the MVVM Toolkit) core: source generators ([ObservableProperty], [RelayCommand],. |
| `/mvvm-toolkit-di` | [`mvvm-toolkit-di`](skills/frontend-development/mvvm-toolkit-di/SKILL.md) | Wire CommunityToolkit.Mvvm ViewModels into Microsoft.Extensions.DependencyInjection. |
| `/mvvm-toolkit-messenger` | [`mvvm-toolkit-messenger`](skills/frontend-development/mvvm-toolkit-messenger/SKILL.md) | CommunityToolkit.Mvvm Messenger pub/sub for decoupled communication between ViewModels (or any objects). |
| `/oo-component-documentation` | [`oo-component-documentation`](skills/frontend-development/oo-component-documentation/SKILL.md) | Create or update standardized object-oriented component documentation using a shared template plus mode-specific. |
| `/penpot-uiux-design` | [`penpot-uiux-design`](skills/frontend-development/penpot-uiux-design/SKILL.md) | Comprehensive guide for creating professional UI/UX designs in Penpot using MCP tools. |
| `/performance-optimization` | [`performance-optimization`](skills/frontend-development/performance-optimization/SKILL.md) | Optimizes application performance. |
| `/plan-ui-change` | [`plan-ui-change`](skills/frontend-development/plan-ui-change/SKILL.md) | Plan complex Blazor UI features by decomposing them into focused components. |
| `/power-platform-architect` | [`power-platform-architect`](skills/frontend-development/power-platform-architect/SKILL.md) | Use this skill when the user needs to transform business requirements, use case descriptions. |
| `/premium-frontend-ui` | [`premium-frontend-ui`](skills/frontend-development/premium-frontend-ui/SKILL.md) | A comprehensive guide for GitHub Copilot to craft immersive, high-performance web experiences with advanced motion,. |
| `/property-patterns` | [`property-patterns`](skills/frontend-development/property-patterns/SKILL.md) | MSBuild property definition patterns: conditional defaults, composition/concatenation, path normalization, trailing. |
| `/qdrant-horizontal-scaling` | [`qdrant-horizontal-scaling`](skills/frontend-development/qdrant-horizontal-scaling/SKILL.md) | Diagnoses and guides Qdrant horizontal scaling decisions. |
| `/qdrant-indexing-performance-optimization` | [`qdrant-indexing-performance-optimization`](skills/frontend-development/qdrant-indexing-performance-optimization/SKILL.md) | Diagnoses and fixes slow Qdrant indexing and data ingestion. |
| `/qdrant-minimize-latency` | [`qdrant-minimize-latency`](skills/frontend-development/qdrant-minimize-latency/SKILL.md) | Guides Qdrant query latency optimization. |
| `/qdrant-model-migration` | [`qdrant-model-migration`](skills/frontend-development/qdrant-model-migration/SKILL.md) | Guides embedding model migration in Qdrant without downtime. |
| `/qdrant-monitoring` | [`qdrant-monitoring`](skills/frontend-development/qdrant-monitoring/SKILL.md) | Guides Qdrant monitoring and observability setup. |
| `/qdrant-scaling` | [`qdrant-scaling`](skills/frontend-development/qdrant-scaling/SKILL.md) | Guides Qdrant scaling decisions. |
| `/qdrant-scaling-data-volume` | [`qdrant-scaling-data-volume`](skills/frontend-development/qdrant-scaling-data-volume/SKILL.md) | Guides Qdrant data volume scaling decisions. |
| `/qdrant-scaling-qps` | [`qdrant-scaling-qps`](skills/frontend-development/qdrant-scaling-qps/SKILL.md) | Guides Qdrant query throughput (QPS) scaling. |
| `/qdrant-scaling-query-volume` | [`qdrant-scaling-query-volume`](skills/frontend-development/qdrant-scaling-query-volume/SKILL.md) | Guides Qdrant query volume scaling. |
| `/qdrant-sliding-time-window` | [`qdrant-sliding-time-window`](skills/frontend-development/qdrant-sliding-time-window/SKILL.md) | Guides sliding time window scaling in Qdrant. |
| `/qdrant-tenant-scaling` | [`qdrant-tenant-scaling`](skills/frontend-development/qdrant-tenant-scaling/SKILL.md) | Guides Qdrant multi-tenant scaling. |
| `/qdrant-version-upgrade` | [`qdrant-version-upgrade`](skills/frontend-development/qdrant-version-upgrade/SKILL.md) | Guidance on how to upgrade your Qdrant version without interrupting the availability of your application and ensuring. |
| `/qdrant-vertical-scaling` | [`qdrant-vertical-scaling`](skills/frontend-development/qdrant-vertical-scaling/SKILL.md) | Guides Qdrant vertical scaling decisions. |
| `/quality-playbook` | [`quality-playbook`](skills/frontend-development/quality-playbook/SKILL.md) | Run a complete quality engineering audit on any codebase. |
| `/react-audit-grep-patterns` | [`react-audit-grep-patterns`](skills/frontend-development/react-audit-grep-patterns/SKILL.md) | Provides the complete, verified grep scan command library for auditing React codebases before a React 18.3.1 or React 19 upgrade. |
| `/react-flow-node-ts` | [`react-flow-node-ts`](skills/frontend-development/react-flow-node-ts/SKILL.md) | Create React Flow node components with TypeScript types, handles, and Zustand integration. |
| `/react-native-dev` | [`react-native-dev`](skills/frontend-development/react-native-dev/SKILL.md) | React Native and Expo development guide covering components, styling, animations, navigation, state management, forms,. |
| `/react18-batching-patterns` | [`react18-batching-patterns`](skills/frontend-development/react18-batching-patterns/SKILL.md) | Provides exact patterns for diagnosing and fixing automatic batching regressions in React 18 class components. |
| `/react18-dep-compatibility` | [`react18-dep-compatibility`](skills/frontend-development/react18-dep-compatibility/SKILL.md) | React 18.3.1 and React 19 dependency compatibility matrix. |
| `/react18-enzyme-to-rtl` | [`react18-enzyme-to-rtl`](skills/frontend-development/react18-enzyme-to-rtl/SKILL.md) | Provides exact Enzyme → React Testing Library migration patterns for React 18 upgrades. |
| `/react18-legacy-context` | [`react18-legacy-context`](skills/frontend-development/react18-legacy-context/SKILL.md) | Provides the complete migration pattern for React legacy context API (contextTypes, childContextTypes, getChildContext). |
| `/react18-lifecycle-patterns` | [`react18-lifecycle-patterns`](skills/frontend-development/react18-lifecycle-patterns/SKILL.md) | Provides exact before/after migration patterns for the three unsafe class component lifecycle methods -. |
| `/react18-string-refs` | [`react18-string-refs`](skills/frontend-development/react18-string-refs/SKILL.md) | Provides exact migration patterns for React string refs (ref="name" + this.refs.name) to React.createRef() in class components. |
| `/react19-concurrent-patterns` | [`react19-concurrent-patterns`](skills/frontend-development/react19-concurrent-patterns/SKILL.md) | Preserve React 18 concurrent patterns and adopt React 19 APIs (useTransition, useDeferredValue, Suspense, use(),. |
| `/react19-source-patterns` | [`react19-source-patterns`](skills/frontend-development/react19-source-patterns/SKILL.md) | Reference for React 19 source-file migration patterns, including API changes, ref handling, and context updates. |
| `/react19-test-patterns` | [`react19-test-patterns`](skills/frontend-development/react19-test-patterns/SKILL.md) | Provides before/after patterns for migrating test files to React 19 compatibility, including act() imports, Simulate. |
| `/receiving-code-review` | [`receiving-code-review`](skills/frontend-development/receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or. |
| `/requesting-code-review` | [`requesting-code-review`](skills/frontend-development/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements. |
| `/resolve-project-references` | [`resolve-project-references`](skills/frontend-development/resolve-project-references/SKILL.md) | Guide for interpreting ResolveProjectReferences time in MSBuild performance summaries. |
| `/salesforce-component-standards` | [`salesforce-component-standards`](skills/frontend-development/salesforce-component-standards/SKILL.md) | Quality standards for Salesforce Lightning Web Components (LWC), Aura components, and Visualforce pages. |
| `/sandbox-npm-install` | [`sandbox-npm-install`](skills/frontend-development/sandbox-npm-install/SKILL.md) | Install npm packages in a Docker sandbox environment. |
| `/sandbox-sdk` | [`sandbox-sdk`](skills/frontend-development/sandbox-sdk/SKILL.md) | Build sandboxed applications for secure code execution. |
| `/scoutqa-test` | [`scoutqa-test`](skills/frontend-development/scoutqa-test/SKILL.md) | This skill should be used when the user asks to "test this website", "run exploratory testing", "check for. |
| `/semantic-kernel` | [`semantic-kernel`](skills/frontend-development/semantic-kernel/SKILL.md) | Create, update, refactor, explain, or review Semantic Kernel solutions using shared guidance plus language-specific. |
| `/site-specification` | [`site-specification`](skills/frontend-development/site-specification/SKILL.md) | Extract comprehensive site specifications from simple descriptions. |
| `/snowflake-semanticview` | [`snowflake-semanticview`](skills/frontend-development/snowflake-semanticview/SKILL.md) | Create, alter, and validate Snowflake semantic views using Snowflake CLI (snow). |
| `/test-gap-analysis` | [`test-gap-analysis`](skills/frontend-development/test-gap-analysis/SKILL.md) | Performs pseudo-mutation analysis on .NET production code to find gaps in existing test suites. |
| `/test-tagging` | [`test-tagging`](skills/frontend-development/test-tagging/SKILL.md) | Analyzes test suites and tags each test with a standardized set of traits (e.g., positive, negative, critical-path,. |
| `/tmux` | [`tmux`](skills/frontend-development/tmux/SKILL.md) | Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. |
| `/ui-screenshots` | [`ui-screenshots`](skills/frontend-development/ui-screenshots/SKILL.md) | Capture screenshots of web apps during development using Playwright and PIL. |
| `/unit-test-vue-pinia` | [`unit-test-vue-pinia`](skills/frontend-development/unit-test-vue-pinia/SKILL.md) | Write and review unit tests for Vue 3 + TypeScript + Vitest + Pinia codebases. |
| `/update-specification` | [`update-specification`](skills/frontend-development/update-specification/SKILL.md) | Update an existing specification file for the solution, optimized for Generative AI consumption based on new. |
| `/vercel-optimize` | [`vercel-optimize`](skills/frontend-development/vercel-optimize/SKILL.md) | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt. |
| `/vercel-react-best-practices` | [`vercel-react-best-practices`](skills/frontend-development/vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. |
| `/vercel-react-native-skills` | [`vercel-react-native-skills`](skills/frontend-development/vercel-react-native-skills/SKILL.md) | React Native and Expo best practices for building performant mobile apps. |
| `/vercel-react-view-transitions` | [`vercel-react-view-transitions`](skills/frontend-development/vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>`. |
| `/verification-before-completion` | [`verification-before-completion`](skills/frontend-development/verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed. |
| `/vscode-ext-commands` | [`vscode-ext-commands`](skills/frontend-development/vscode-ext-commands/SKILL.md) | Guidelines for contributing commands in VS Code extensions. |
| `/vscode-ext-localization` | [`vscode-ext-localization`](skills/frontend-development/vscode-ext-localization/SKILL.md) | Guidelines for proper localization of VS Code extensions, following VS Code extension development guidelines, libraries. |
| `/web-artifacts-builder` | [`web-artifacts-builder`](skills/frontend-development/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies. |
| `/web-design-guidelines` | [`web-design-guidelines`](skills/frontend-development/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. |
| `/web-perf` | [`web-perf`](skills/frontend-development/web-perf/SKILL.md) | Analyzes web performance using Chrome DevTools MCP. |
| `/website` | [`website`](skills/frontend-development/website/SKILL.md) | Build fast, accessible, and SEO-friendly websites with modern best practices. |
| `/wiki-ado-convert` | [`wiki-ado-convert`](skills/frontend-development/wiki-ado-convert/SKILL.md) | Converts VitePress/GFM wiki markdown to Azure DevOps Wiki-compatible format. |
| `/wiki-qa` | [`wiki-qa`](skills/frontend-development/wiki-qa/SKILL.md) | Answers questions about a code repository using source file analysis. |
| `/wiki-vitepress` | [`wiki-vitepress`](skills/frontend-development/wiki-vitepress/SKILL.md) | Packages generated wiki Markdown into a VitePress static site with dark theme, dark-mode Mermaid diagrams with. |
| `/winui3-migration-guide` | [`winui3-migration-guide`](skills/frontend-development/winui3-migration-guide/SKILL.md) | UWP-to-WinUI 3 migration reference. |
| `/wp-plugin-directory-guidelines` | [`wp-plugin-directory-guidelines`](skills/frontend-development/wp-plugin-directory-guidelines/SKILL.md) | Use when reviewing WordPress plugins for GPL compliance, checking license headers or compatibility, evaluating. |
| `/wpds` | [`wpds`](skills/frontend-development/wpds/SKILL.md) | Use when building UIs leveraging the WordPress Design System (WPDS) and its components, tokens, patterns, etc. |
| `/writing-plans` | [`writing-plans`](skills/frontend-development/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code. |
| `/zustand-store-ts` | [`zustand-store-ts`](skills/frontend-development/zustand-store-ts/SKILL.md) | Create Zustand stores with TypeScript, subscribeWithSelector middleware, and proper state/action separation. |

---

### ⚙️ Backend & Systems Engineering
> *Server architectures, database engines, WordPress plugin development, testing frameworks, and shell control.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Code Review Reception` | [`Code Review Reception`](skills/backend-and-fullstack/Code Review Reception/SKILL.md) | Receive and act on code review feedback with technical rigor, not performative agreement or blind implementation. |
| `/Collision-Zone Thinking` | [`Collision-Zone Thinking`](skills/backend-and-fullstack/Collision-Zone Thinking/SKILL.md) | Force unrelated concepts together to discover emergent properties - "What if we treated X like Y? |
| `/Condition-Based Waiting` | [`Condition-Based Waiting`](skills/backend-and-fullstack/Condition-Based Waiting/SKILL.md) | Replace arbitrary timeouts with condition polling for reliable async tests. |
| `/Finishing a Development Branch` | [`Finishing a Development Branch`](skills/backend-and-fullstack/Finishing a Development Branch/SKILL.md) | Complete feature development with structured options for merge, PR, or cleanup. |
| `/Preserving Productive Tensions` | [`Preserving Productive Tensions`](skills/backend-and-fullstack/Preserving Productive Tensions/SKILL.md) | Recognize when disagreements reveal valuable context, preserve multiple valid approaches instead of forcing premature resolution. |
| `/Root Cause Tracing` | [`Root Cause Tracing`](skills/backend-and-fullstack/Root Cause Tracing/SKILL.md) | Systematically trace bugs backward through call stack to find original trigger. |
| `/Scale Game` | [`Scale Game`](skills/backend-and-fullstack/Scale Game/SKILL.md) | Test at extremes (1000x bigger/smaller, instant/year-long) to expose fundamental truths hidden at normal scales. |
| `/Sharing Skills` | [`Sharing Skills`](skills/backend-and-fullstack/Sharing Skills/SKILL.md) | Contribute skills back to upstream via branch and PR. |
| `/Systematic Debugging` | [`Systematic Debugging`](skills/backend-and-fullstack/Systematic Debugging/SKILL.md) | Four-phase debugging framework that ensures root cause investigation before attempting fixes. |
| `/Test-Driven Development (TDD)` | [`Test-Driven Development (TDD)`](skills/backend-and-fullstack/Test-Driven Development (TDD)/SKILL.md) | Write the test first, watch it fail, write minimal code to pass. |
| `/Testing Anti-Patterns` | [`Testing Anti-Patterns`](skills/backend-and-fullstack/Testing Anti-Patterns/SKILL.md) | Never test mock behavior. Never add test-only methods to production classes. |
| `/Tracing Knowledge Lineages` | [`Tracing Knowledge Lineages`](skills/backend-and-fullstack/Tracing Knowledge Lineages/SKILL.md) | Understand how ideas evolved over time to find old solutions for new problems and avoid repeating past failures. |
| `/Using Git Worktrees` | [`Using Git Worktrees`](skills/backend-and-fullstack/Using Git Worktrees/SKILL.md) | Create isolated git worktrees with smart directory selection and safety verification. |
| `/Verification Before Completion` | [`Verification Before Completion`](skills/backend-and-fullstack/Verification Before Completion/SKILL.md) | Run verification commands and confirm output before claiming success. |
| `/When Stuck - Problem-Solving Dispatch` | [`When Stuck - Problem-Solving Dispatch`](skills/backend-and-fullstack/When Stuck - Problem-Solving Dispatch/SKILL.md) | Dispatch to the right problem-solving technique based on how you're stuck. |
| `/alloydb-basics` | [`alloydb-basics`](skills/backend-and-fullstack/alloydb-basics/SKILL.md) | Manages clusters, instances, and backups for AlloyDB for PostgreSQL, and integrates with AlloyDB model context protocol. |
| `/analyzing-dotnet-performance` | [`analyzing-dotnet-performance`](skills/backend-and-fullstack/analyzing-dotnet-performance/SKILL.md) | Scans .NET code for ~50 performance anti-patterns across async, memory, strings, collections, LINQ, regex, serialization. |
| `/apple-appstore-reviewer` | [`apple-appstore-reviewer`](skills/backend-and-fullstack/apple-appstore-reviewer/SKILL.md) | Serves as a reviewer of the codebase with instructions on looking for Apple App Store optimizations or rejection reasons. |
| `/arize-annotation` | [`arize-annotation`](skills/backend-and-fullstack/arize-annotation/SKILL.md) | Creates and manages annotation configs (categorical, continuous, freeform label schemas) and annotation queues (human. |
| `/arize-dataset` | [`arize-dataset`](skills/backend-and-fullstack/arize-dataset/SKILL.md) | Creates, manages, and queries Arize datasets and examples. |
| `/arize-experiment` | [`arize-experiment`](skills/backend-and-fullstack/arize-experiment/SKILL.md) | Creates, runs, and analyzes Arize experiments for evaluating and comparing model performance. |
| `/aspire` | [`aspire`](skills/backend-and-fullstack/aspire/SKILL.md) | Aspire skill covering the Aspire CLI, AppHost orchestration, service discovery, integrations, MCP server, VS Code. |
| `/az-cost-optimize` | [`az-cost-optimize`](skills/backend-and-fullstack/az-cost-optimize/SKILL.md) | Analyze Azure resources used in the app (IaC files and/or resources in a target rg) and optimize costs - creating. |
| `/azure-ai-anomalydetector-java` | [`azure-ai-anomalydetector-java`](skills/backend-and-fullstack/azure-ai-anomalydetector-java/SKILL.md) | Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. |
| `/azure-ai-contentsafety-java` | [`azure-ai-contentsafety-java`](skills/backend-and-fullstack/azure-ai-contentsafety-java/SKILL.md) | Build content moderation applications with Azure AI Content Safety SDK for Java. |
| `/azure-ai-formrecognizer-java` | [`azure-ai-formrecognizer-java`](skills/backend-and-fullstack/azure-ai-formrecognizer-java/SKILL.md) | Azure AI Document Intelligence SDK for Java (com.azure:azure-ai-documentintelligence). |
| `/azure-ai-projects-dotnet` | [`azure-ai-projects-dotnet`](skills/backend-and-fullstack/azure-ai-projects-dotnet/SKILL.md) | Azure AI Projects SDK for .NET. |
| `/azure-ai-projects-java` | [`azure-ai-projects-java`](skills/backend-and-fullstack/azure-ai-projects-java/SKILL.md) | Azure AI Projects SDK for Java. |
| `/azure-ai-vision-imageanalysis-java` | [`azure-ai-vision-imageanalysis-java`](skills/backend-and-fullstack/azure-ai-vision-imageanalysis-java/SKILL.md) | Build image analysis applications with Azure AI Vision SDK for Java. |
| `/azure-appconfiguration-java` | [`azure-appconfiguration-java`](skills/backend-and-fullstack/azure-appconfiguration-java/SKILL.md) | Azure App Configuration SDK for Java. |
| `/azure-communication-callingserver-java` | [`azure-communication-callingserver-java`](skills/backend-and-fullstack/azure-communication-callingserver-java/SKILL.md) | Azure Communication Services CallingServer (legacy) Java SDK. |
| `/azure-communication-chat-java` | [`azure-communication-chat-java`](skills/backend-and-fullstack/azure-communication-chat-java/SKILL.md) | Build real-time chat applications with Azure Communication Services Chat Java SDK. |
| `/azure-communication-common-java` | [`azure-communication-common-java`](skills/backend-and-fullstack/azure-communication-common-java/SKILL.md) | Azure Communication Services common utilities for Java. |
| `/azure-compute-batch-java` | [`azure-compute-batch-java`](skills/backend-and-fullstack/azure-compute-batch-java/SKILL.md) | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |
| `/azure-cosmos-java` | [`azure-cosmos-java`](skills/backend-and-fullstack/azure-cosmos-java/SKILL.md) | Azure Cosmos DB SDK for Java. |
| `/azure-cosmos-rust` | [`azure-cosmos-rust`](skills/backend-and-fullstack/azure-cosmos-rust/SKILL.md) | Azure Cosmos DB library for Rust (NoSQL API). Document CRUD, containers, and globally distributed data. |
| `/azure-data-tables-java` | [`azure-data-tables-java`](skills/backend-and-fullstack/azure-data-tables-java/SKILL.md) | Build table storage applications with Azure Tables SDK for Java. |
| `/azure-eventgrid-dotnet` | [`azure-eventgrid-dotnet`](skills/backend-and-fullstack/azure-eventgrid-dotnet/SKILL.md) | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. |
| `/azure-eventgrid-java` | [`azure-eventgrid-java`](skills/backend-and-fullstack/azure-eventgrid-java/SKILL.md) | Build event-driven applications with Azure Event Grid SDK for Java. |
| `/azure-eventhub-dotnet` | [`azure-eventhub-dotnet`](skills/backend-and-fullstack/azure-eventhub-dotnet/SKILL.md) | Azure Event Hubs SDK for .NET. |
| `/azure-eventhub-java` | [`azure-eventhub-java`](skills/backend-and-fullstack/azure-eventhub-java/SKILL.md) | Build real-time streaming applications with Azure Event Hubs SDK for Java. |
| `/azure-eventhub-rust` | [`azure-eventhub-rust`](skills/backend-and-fullstack/azure-eventhub-rust/SKILL.md) | Azure Event Hubs library for Rust. Send and receive events for streaming data ingestion and batch processing. |
| `/azure-identity-dotnet` | [`azure-identity-dotnet`](skills/backend-and-fullstack/azure-identity-dotnet/SKILL.md) | Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. |
| `/azure-identity-java` | [`azure-identity-java`](skills/backend-and-fullstack/azure-identity-java/SKILL.md) | Azure Identity library for Java authentication with Azure services. |
| `/azure-identity-rust` | [`azure-identity-rust`](skills/backend-and-fullstack/azure-identity-rust/SKILL.md) | Azure Identity library for Rust. Microsoft Entra ID authentication for all Azure SDK clients. |
| `/azure-keyvault-certificates-rust` | [`azure-keyvault-certificates-rust`](skills/backend-and-fullstack/azure-keyvault-certificates-rust/SKILL.md) | Azure Key Vault Certificates library for Rust. |
| `/azure-keyvault-keys-rust` | [`azure-keyvault-keys-rust`](skills/backend-and-fullstack/azure-keyvault-keys-rust/SKILL.md) | Azure Key Vault Keys library for Rust. |
| `/azure-keyvault-secrets-rust` | [`azure-keyvault-secrets-rust`](skills/backend-and-fullstack/azure-keyvault-secrets-rust/SKILL.md) | Azure Key Vault Secrets library for Rust. Store and retrieve secrets, passwords, and API keys. |
| `/azure-maps-search-dotnet` | [`azure-maps-search-dotnet`](skills/backend-and-fullstack/azure-maps-search-dotnet/SKILL.md) | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. |
| `/azure-messaging-webpubsub-java` | [`azure-messaging-webpubsub-java`](skills/backend-and-fullstack/azure-messaging-webpubsub-java/SKILL.md) | Build real-time web applications with Azure Web PubSub SDK for Java. |
| `/azure-mgmt-applicationinsights-dotnet` | [`azure-mgmt-applicationinsights-dotnet`](skills/backend-and-fullstack/azure-mgmt-applicationinsights-dotnet/SKILL.md) | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| `/azure-mgmt-botservice-dotnet` | [`azure-mgmt-botservice-dotnet`](skills/backend-and-fullstack/azure-mgmt-botservice-dotnet/SKILL.md) | Azure Resource Manager SDK for Bot Service in .NET. |
| `/azure-mgmt-fabric-dotnet` | [`azure-mgmt-fabric-dotnet`](skills/backend-and-fullstack/azure-mgmt-fabric-dotnet/SKILL.md) | Azure Resource Manager SDK for Fabric in .NET. |
| `/azure-mgmt-mongodbatlas-dotnet` | [`azure-mgmt-mongodbatlas-dotnet`](skills/backend-and-fullstack/azure-mgmt-mongodbatlas-dotnet/SKILL.md) | Manage MongoDB Atlas Organizations as Azure ARM resources using Azure.ResourceManager.MongoDBAtlas SDK. |
| `/azure-mgmt-weightsandbiases-dotnet` | [`azure-mgmt-weightsandbiases-dotnet`](skills/backend-and-fullstack/azure-mgmt-weightsandbiases-dotnet/SKILL.md) | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. |
| `/azure-monitor-ingestion-java` | [`azure-monitor-ingestion-java`](skills/backend-and-fullstack/azure-monitor-ingestion-java/SKILL.md) | Azure Monitor Ingestion SDK for Java. |
| `/azure-monitor-opentelemetry-exporter-java` | [`azure-monitor-opentelemetry-exporter-java`](skills/backend-and-fullstack/azure-monitor-opentelemetry-exporter-java/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Java. |
| `/azure-monitor-query-java` | [`azure-monitor-query-java`](skills/backend-and-fullstack/azure-monitor-query-java/SKILL.md) | Azure Monitor Query SDK for Java. |
| `/azure-postgres-ts` | [`azure-postgres-ts`](skills/backend-and-fullstack/azure-postgres-ts/SKILL.md) | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| `/azure-resource-manager-cosmosdb-dotnet` | [`azure-resource-manager-cosmosdb-dotnet`](skills/backend-and-fullstack/azure-resource-manager-cosmosdb-dotnet/SKILL.md) | Azure Resource Manager SDK for Cosmos DB in .NET. |
| `/azure-resource-manager-durabletask-dotnet` | [`azure-resource-manager-durabletask-dotnet`](skills/backend-and-fullstack/azure-resource-manager-durabletask-dotnet/SKILL.md) | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| `/azure-resource-manager-mysql-dotnet` | [`azure-resource-manager-mysql-dotnet`](skills/backend-and-fullstack/azure-resource-manager-mysql-dotnet/SKILL.md) | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| `/azure-resource-manager-playwright-dotnet` | [`azure-resource-manager-playwright-dotnet`](skills/backend-and-fullstack/azure-resource-manager-playwright-dotnet/SKILL.md) | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| `/azure-resource-manager-postgresql-dotnet` | [`azure-resource-manager-postgresql-dotnet`](skills/backend-and-fullstack/azure-resource-manager-postgresql-dotnet/SKILL.md) | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| `/azure-resource-manager-redis-dotnet` | [`azure-resource-manager-redis-dotnet`](skills/backend-and-fullstack/azure-resource-manager-redis-dotnet/SKILL.md) | Azure Resource Manager SDK for Redis in .NET. |
| `/azure-resource-manager-sql-dotnet` | [`azure-resource-manager-sql-dotnet`](skills/backend-and-fullstack/azure-resource-manager-sql-dotnet/SKILL.md) | Azure Resource Manager SDK for Azure SQL in .NET. |
| `/azure-security-keyvault-keys-dotnet` | [`azure-security-keyvault-keys-dotnet`](skills/backend-and-fullstack/azure-security-keyvault-keys-dotnet/SKILL.md) | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. |
| `/azure-security-keyvault-keys-java` | [`azure-security-keyvault-keys-java`](skills/backend-and-fullstack/azure-security-keyvault-keys-java/SKILL.md) | Azure Key Vault Keys Java SDK for cryptographic key management. |
| `/azure-security-keyvault-secrets-java` | [`azure-security-keyvault-secrets-java`](skills/backend-and-fullstack/azure-security-keyvault-secrets-java/SKILL.md) | Azure Key Vault Secrets Java SDK for secret management. |
| `/azure-servicebus-dotnet` | [`azure-servicebus-dotnet`](skills/backend-and-fullstack/azure-servicebus-dotnet/SKILL.md) | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| `/azure-storage-blob-java` | [`azure-storage-blob-java`](skills/backend-and-fullstack/azure-storage-blob-java/SKILL.md) | Build blob storage applications with Azure Storage Blob SDK for Java. |
| `/azure-storage-blob-rust` | [`azure-storage-blob-rust`](skills/backend-and-fullstack/azure-storage-blob-rust/SKILL.md) | Azure Blob Storage library for Rust. Upload, download, and manage blobs and containers. |
| `/bigquery-basics` | [`bigquery-basics`](skills/backend-and-fullstack/bigquery-basics/SKILL.md) | Manages datasets, tables, and jobs in BigQuery, and integrates with BigQuery ML and Gemini for advanced data analytics. |
| `/bigquery-pipeline-audit` | [`bigquery-pipeline-audit`](skills/backend-and-fullstack/bigquery-pipeline-audit/SKILL.md) | Audits Python + BigQuery pipelines for cost safety, idempotency, and production readiness. |
| `/binlog-failure-analysis` | [`binlog-failure-analysis`](skills/backend-and-fullstack/binlog-failure-analysis/SKILL.md) | Analyze MSBuild binary logs to diagnose build failures. Only activate in MSBuild/.NET build context. |
| `/browser-testing-with-devtools` | [`browser-testing-with-devtools`](skills/backend-and-fullstack/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. |
| `/buddy-sings` | [`buddy-sings`](skills/backend-and-fullstack/buddy-sings/SKILL.md) | Use when user wants their Claude Code pet (/buddy) to sing a song. |
| `/check-bin-obj-clash` | [`check-bin-obj-clash`](skills/backend-and-fullstack/check-bin-obj-clash/SKILL.md) | Detects MSBuild projects with conflicting OutputPath or IntermediateOutputPath. |
| `/cloud-sql-basics` | [`cloud-sql-basics`](skills/backend-and-fullstack/cloud-sql-basics/SKILL.md) | This file generates or explains Cloud SQL resources. |
| `/clr-activation-debugging` | [`clr-activation-debugging`](skills/backend-and-fullstack/clr-activation-debugging/SKILL.md) | Diagnoses .NET Framework CLR activation issues using CLR activation logs (CLRLoad logs) produced by mscoree.dll. |
| `/code-simplification` | [`code-simplification`](skills/backend-and-fullstack/code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. |
| `/code-testing-extensions` | [`code-testing-extensions`](skills/backend-and-fullstack/code-testing-extensions/SKILL.md) | Provides file paths to language-specific extension files for the code-testing pipeline. |
| `/code-tour` | [`code-tour`](skills/backend-and-fullstack/code-tour/SKILL.md) | Use this skill to create CodeTour .tour files — persona-targeted, step-by-step walkthroughs that link to real files and. |
| `/commit-message-storyteller` | [`commit-message-storyteller`](skills/backend-and-fullstack/commit-message-storyteller/SKILL.md) | Analyzes git diffs or staged changes and generates narrative commit messages that explain WHY a change was made, not. |
| `/configuring-opentelemetry-dotnet` | [`configuring-opentelemetry-dotnet`](skills/backend-and-fullstack/configuring-opentelemetry-dotnet/SKILL.md) | Configure OpenTelemetry distributed tracing, metrics, and logging in ASP.NET Core using the .NET OpenTelemetry SDK. |
| `/containerize-aspnet-framework` | [`containerize-aspnet-framework`](skills/backend-and-fullstack/containerize-aspnet-framework/SKILL.md) | Containerize an ASP.NET .NET Framework project by creating Dockerfile and .dockerfile files customized for the project. |
| `/containerize-aspnetcore` | [`containerize-aspnetcore`](skills/backend-and-fullstack/containerize-aspnetcore/SKILL.md) | Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project. |
| `/conventional-branch` | [`conventional-branch`](skills/backend-and-fullstack/conventional-branch/SKILL.md) | Create Git branches following the Conventional Branch specification (feature/, bugfix/, hotfix/, release/, chore/). |
| `/convert-blazor-server-to-webapp` | [`convert-blazor-server-to-webapp`](skills/backend-and-fullstack/convert-blazor-server-to-webapp/SKILL.md) | Guides conversion of a pre-.NET 8 Blazor Server app into a .NET 8+ Blazor Web App. |
| `/convert-to-cpm` | [`convert-to-cpm`](skills/backend-and-fullstack/convert-to-cpm/SKILL.md) | Convert .NET projects and solutions (.sln, .slnx) to NuGet Central Package Management (CPM) using Directory.Packages.props. |
| `/copilot-sdk` | [`copilot-sdk`](skills/backend-and-fullstack/copilot-sdk/SKILL.md) | Build applications powered by GitHub Copilot using the Copilot SDK. |
| `/coverage-analysis` | [`coverage-analysis`](skills/backend-and-fullstack/coverage-analysis/SKILL.md) | Project-wide code coverage and CRAP (Change Risk Anti-Patterns) score analysis for .NET projects. |
| `/crap-score` | [`crap-score`](skills/backend-and-fullstack/crap-score/SKILL.md) | Calculates targeted CRAP (Change Risk Anti-Patterns) scores for a named .NET method, class, or single source file. |
| `/create-blazor-project` | [`create-blazor-project`](skills/backend-and-fullstack/create-blazor-project/SKILL.md) | Create a new ASP.NET Core web application or web site using Blazor. |
| `/create-github-action-workflow-specification` | [`create-github-action-workflow-specification`](skills/backend-and-fullstack/create-github-action-workflow-specification/SKILL.md) | Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow. |
| `/create-github-issue-feature-from-specification` | [`create-github-issue-feature-from-specification`](skills/backend-and-fullstack/create-github-issue-feature-from-specification/SKILL.md) | Create GitHub Issue for feature request from specification file using feature_request.yml template. |
| `/create-github-issues-feature-from-implementation-plan` | [`create-github-issues-feature-from-implementation-plan`](skills/backend-and-fullstack/create-github-issues-feature-from-implementation-plan/SKILL.md) | Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates. |
| `/create-readme` | [`create-readme`](skills/backend-and-fullstack/create-readme/SKILL.md) | Create a README.md file for the project. |
| `/create-spring-boot-java-project` | [`create-spring-boot-java-project`](skills/backend-and-fullstack/create-spring-boot-java-project/SKILL.md) | Create Spring Boot Java Project Skeleton. |
| `/create-spring-boot-kotlin-project` | [`create-spring-boot-kotlin-project`](skills/backend-and-fullstack/create-spring-boot-kotlin-project/SKILL.md) | Create Spring Boot Kotlin Project Skeleton. |
| `/creating-oracle-to-postgres-master-migration-plan` | [`creating-oracle-to-postgres-master-migration-plan`](skills/backend-and-fullstack/creating-oracle-to-postgres-master-migration-plan/SKILL.md) | Discovers all projects in a .NET solution, classifies each for Oracle-to-PostgreSQL migration eligibility. |
| `/creating-oracle-to-postgres-migration-bug-report` | [`creating-oracle-to-postgres-migration-bug-report`](skills/backend-and-fullstack/creating-oracle-to-postgres-migration-bug-report/SKILL.md) | Creates structured bug reports for defects found during Oracle-to-PostgreSQL migration. |
| `/creating-oracle-to-postgres-migration-integration-tests` | [`creating-oracle-to-postgres-migration-integration-tests`](skills/backend-and-fullstack/creating-oracle-to-postgres-migration-integration-tests/SKILL.md) | Creates integration test cases for .NET data access artifacts during Oracle-to-PostgreSQL database migrations. |
| `/csharp-async` | [`csharp-async`](skills/backend-and-fullstack/csharp-async/SKILL.md) | Get best practices for C# async programming. |
| `/csharp-docs` | [`csharp-docs`](skills/backend-and-fullstack/csharp-docs/SKILL.md) | Ensure that C# types are documented with XML comments and follow best practices for documentation. |
| `/csharp-mstest` | [`csharp-mstest`](skills/backend-and-fullstack/csharp-mstest/SKILL.md) | Get best practices for MSTest 3.x/4.x unit testing, including modern assertion APIs and data-driven tests. |
| `/csharp-nunit` | [`csharp-nunit`](skills/backend-and-fullstack/csharp-nunit/SKILL.md) | Get best practices for NUnit unit testing, including data-driven tests. |
| `/csharp-scripts` | [`csharp-scripts`](skills/backend-and-fullstack/csharp-scripts/SKILL.md) | Run file-based C# apps with the .NET CLI when the user explicitly wants C#/.NET code without creating a project. |
| `/csharp-tunit` | [`csharp-tunit`](skills/backend-and-fullstack/csharp-tunit/SKILL.md) | Get best practices for TUnit unit testing, including data-driven tests. |
| `/csharp-xunit` | [`csharp-xunit`](skills/backend-and-fullstack/csharp-xunit/SKILL.md) | Get best practices for XUnit unit testing, including data-driven tests. |
| `/dataverse-python-advanced-patterns` | [`dataverse-python-advanced-patterns`](skills/backend-and-fullstack/dataverse-python-advanced-patterns/SKILL.md) | Generate production code for Dataverse SDK using advanced patterns, error handling, and optimization techniques. |
| `/dataverse-python-production-code` | [`dataverse-python-production-code`](skills/backend-and-fullstack/dataverse-python-production-code/SKILL.md) | Generate production-ready Python code using Dataverse SDK with error handling, optimization, and best practices. |
| `/dataverse-python-quickstart` | [`dataverse-python-quickstart`](skills/backend-and-fullstack/dataverse-python-quickstart/SKILL.md) | Generate Python SDK setup + CRUD + bulk + paging snippets using official patterns. |
| `/dependabot` | [`dependabot`](skills/backend-and-fullstack/dependabot/SKILL.md) | Comprehensive guide for configuring and managing GitHub Dependabot. |
| `/detect-static-dependencies` | [`detect-static-dependencies`](skills/backend-and-fullstack/detect-static-dependencies/SKILL.md) | Scan C# source files for hard-to-test static dependencies — DateTime.Now/UtcNow, File.*, Directory.*, Environment.*,. |
| `/dotnet-aot-compat` | [`dotnet-aot-compat`](skills/backend-and-fullstack/dotnet-aot-compat/SKILL.md) | Make .NET projects compatible with Native AOT and trimming by systematically resolving IL trim/AOT analyzer warnings. |
| `/dotnet-best-practices` | [`dotnet-best-practices`](skills/backend-and-fullstack/dotnet-best-practices/SKILL.md) | Ensure .NET/C# code meets best practices for the solution/project. |
| `/dotnet-pinvoke` | [`dotnet-pinvoke`](skills/backend-and-fullstack/dotnet-pinvoke/SKILL.md) | Correctly call native (C/C++) libraries from .NET using P/Invoke and LibraryImport. |
| `/dotnet-test-frameworks` | [`dotnet-test-frameworks`](skills/backend-and-fullstack/dotnet-test-frameworks/SKILL.md) | Reference data for .NET test framework detection patterns, assertion APIs, skip annotations, setup/teardown methods. |
| `/dotnet-timezone` | [`dotnet-timezone`](skills/backend-and-fullstack/dotnet-timezone/SKILL.md) | .NET timezone handling guidance for C# applications. |
| `/dotnet-trace-collect` | [`dotnet-trace-collect`](skills/backend-and-fullstack/dotnet-trace-collect/SKILL.md) | Guide developers through capturing diagnostic artifacts to diagnose production .NET performance issues. |
| `/dotnet-upgrade` | [`dotnet-upgrade`](skills/backend-and-fullstack/dotnet-upgrade/SKILL.md) | Ready-to-use prompts for comprehensive .NET framework upgrade analysis and execution. |
| `/doublecheck` | [`doublecheck`](skills/backend-and-fullstack/doublecheck/SKILL.md) | Three-layer verification pipeline for AI output. |
| `/dump-collect` | [`dump-collect`](skills/backend-and-fullstack/dump-collect/SKILL.md) | Configure and collect crash dumps for modern .NET applications. |
| `/ef-core` | [`ef-core`](skills/backend-and-fullstack/ef-core/SKILL.md) | Get best practices for Entity Framework Core. |
| `/efcore-d2-db-diagram` | [`efcore-d2-db-diagram`](skills/backend-and-fullstack/efcore-d2-db-diagram/SKILL.md) | Generate D2 database diagrams from Entity Framework Core models. |
| `/eval-driven-dev` | [`eval-driven-dev`](skills/backend-and-fullstack/eval-driven-dev/SKILL.md) | Improve AI application with evaluation-driven development. |
| `/eval-performance` | [`eval-performance`](skills/backend-and-fullstack/eval-performance/SKILL.md) | Guide for diagnosing and improving MSBuild project evaluation performance. |
| `/exam-ready` | [`exam-ready`](skills/backend-and-fullstack/exam-ready/SKILL.md) | Activate this skill when a student provides study material (PDF or pasted notes) and a syllabus, and wants to prepare for an exam. |
| `/executing-plans` | [`executing-plans`](skills/backend-and-fullstack/executing-plans/SKILL.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints. |
| `/exp-mock-usage-analysis` | [`exp-mock-usage-analysis`](skills/backend-and-fullstack/exp-mock-usage-analysis/SKILL.md) | Audits .NET test mock usage by tracing each mock setup through the production code's execution path to find dead,. |
| `/file-organizer` | [`file-organizer`](skills/backend-and-fullstack/file-organizer/SKILL.md) | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates,. |
| `/filter-syntax` | [`filter-syntax`](skills/backend-and-fullstack/filter-syntax/SKILL.md) | Reference data for test filter syntax across all platform and framework combinations: VSTest --filter expressions, MTP. |
| `/flowstudio-power-automate-debug` | [`flowstudio-power-automate-debug`](skills/backend-and-fullstack/flowstudio-power-automate-debug/SKILL.md) | Debug failing Power Automate cloud flows using the FlowStudio MCP server. |
| `/flowstudio-power-automate-monitoring` | [`flowstudio-power-automate-monitoring`](skills/backend-and-fullstack/flowstudio-power-automate-monitoring/SKILL.md) | Pro+ subscription required. |
| `/from-the-other-side-anitta` | [`from-the-other-side-anitta`](skills/backend-and-fullstack/from-the-other-side-anitta/SKILL.md) | Rigorous challenge profile for Anitta: assumption checks, evidence calibration. |
| `/fullstack-dev` | [`fullstack-dev`](skills/backend-and-fullstack/fullstack-dev/SKILL.md) | Full-stack backend architecture and frontend-backend integration guide. |
| `/geofeed-tuner` | [`geofeed-tuner`](skills/backend-and-fullstack/geofeed-tuner/SKILL.md) | Use this skill whenever the user mentions IP geolocation feeds, RFC 8805, geofeeds. |
| `/git-commit` | [`git-commit`](skills/backend-and-fullstack/git-commit/SKILL.md) | Execute git commit with conventional commit message analysis, intelligent staging, and message generation. |
| `/git-flow-branch-creator` | [`git-flow-branch-creator`](skills/backend-and-fullstack/git-flow-branch-creator/SKILL.md) | Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie. |
| `/git-workflow-and-versioning` | [`git-workflow-and-versioning`](skills/backend-and-fullstack/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. |
| `/github-actions-efficiency` | [`github-actions-efficiency`](skills/backend-and-fullstack/github-actions-efficiency/SKILL.md) | Audit GitHub Actions workflow efficiency and recommend fixes to reduce CI minutes and costs. |
| `/github-codespaces-efficiency` | [`github-codespaces-efficiency`](skills/backend-and-fullstack/github-codespaces-efficiency/SKILL.md) | Audit and improve GitHub Codespaces efficiency. |
| `/github-copilot-starter` | [`github-copilot-starter`](skills/backend-and-fullstack/github-copilot-starter/SKILL.md) | Set up complete GitHub Copilot configuration for a new project based on technology stack. |
| `/github-issue-creator` | [`github-issue-creator`](skills/backend-and-fullstack/github-issue-creator/SKILL.md) | Convert raw notes, error logs, voice dictation, or screenshots into crisp GitHub-flavored markdown issue reports. |
| `/github-issues` | [`github-issues`](skills/backend-and-fullstack/github-issues/SKILL.md) | Create, update, and manage GitHub issues using MCP tools. |
| `/github-release` | [`github-release`](skills/backend-and-fullstack/github-release/SKILL.md) | Guides IA through releasing a new version of a GitHub library end-to-end. |
| `/go-mcp-server-generator` | [`go-mcp-server-generator`](skills/backend-and-fullstack/go-mcp-server-generator/SKILL.md) | Generate a complete Go MCP server project with proper structure, dependencies. |
| `/huggingface-best` | [`huggingface-best`](skills/backend-and-fullstack/huggingface-best/SKILL.md) | Use when the user asks about finding the best, top. |
| `/humanizer` | [`humanizer`](skills/backend-and-fullstack/humanizer/SKILL.md) | Remove signs of AI-generated writing from text. |
| `/idea-refine` | [`idea-refine`](skills/backend-and-fullstack/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| `/image-manipulation-image-magick` | [`image-manipulation-image-magick`](skills/backend-and-fullstack/image-manipulation-image-magick/SKILL.md) | Process and manipulate images using ImageMagick. |
| `/incremental-implementation` | [`incremental-implementation`](skills/backend-and-fullstack/incremental-implementation/SKILL.md) | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. |
| `/issue-fields-migration` | [`issue-fields-migration`](skills/backend-and-fullstack/issue-fields-migration/SKILL.md) | Bulk-migrate metadata to GitHub issue fields from two sources: repo labels (e.g. |
| `/java-add-graalvm-native-image-support` | [`java-add-graalvm-native-image-support`](skills/backend-and-fullstack/java-add-graalvm-native-image-support/SKILL.md) | GraalVM Native Image expert that adds native image support to Java applications, builds the project, analyzes build. |
| `/java-docs` | [`java-docs`](skills/backend-and-fullstack/java-docs/SKILL.md) | Ensure that Java types are documented with Javadoc comments and follow best practices for documentation. |
| `/java-junit` | [`java-junit`](skills/backend-and-fullstack/java-junit/SKILL.md) | Get best practices for JUnit 5 unit testing, including data-driven tests. |
| `/java-mcp-server-generator` | [`java-mcp-server-generator`](skills/backend-and-fullstack/java-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Java using the official MCP Java SDK with reactive streams. |
| `/java-refactoring-extract-method` | [`java-refactoring-extract-method`](skills/backend-and-fullstack/java-refactoring-extract-method/SKILL.md) | Refactoring using Extract Methods in Java Language. |
| `/java-refactoring-remove-parameter` | [`java-refactoring-remove-parameter`](skills/backend-and-fullstack/java-refactoring-remove-parameter/SKILL.md) | Refactoring using Remove Parameter in Java Language. |
| `/java-springboot` | [`java-springboot`](skills/backend-and-fullstack/java-springboot/SKILL.md) | Get best practices for developing applications with Spring Boot. |
| `/kotlin-springboot` | [`kotlin-springboot`](skills/backend-and-fullstack/kotlin-springboot/SKILL.md) | Get best practices for developing applications with Spring Boot and Kotlin. |
| `/lsp-setup` | [`lsp-setup`](skills/backend-and-fullstack/lsp-setup/SKILL.md) | Enable code intelligence (go-to-definition, find-references, hover, type info) for any programming language by. |
| `/memory-merger` | [`memory-merger`](skills/backend-and-fullstack/memory-merger/SKILL.md) | Merges mature lessons from a domain memory file into its instruction file. |
| `/migrate-dotnet10-to-dotnet11` | [`migrate-dotnet10-to-dotnet11`](skills/backend-and-fullstack/migrate-dotnet10-to-dotnet11/SKILL.md) | Migrate a .NET 10 project or solution to .NET 11 and resolve all breaking changes. |
| `/migrate-dotnet8-to-dotnet9` | [`migrate-dotnet8-to-dotnet9`](skills/backend-and-fullstack/migrate-dotnet8-to-dotnet9/SKILL.md) | Migrate a .NET 8 project to .NET 9 and resolve all breaking changes. |
| `/migrate-dotnet9-to-dotnet10` | [`migrate-dotnet9-to-dotnet10`](skills/backend-and-fullstack/migrate-dotnet9-to-dotnet10/SKILL.md) | Migrate a .NET 9 project or solution to .NET 10 and resolve all breaking changes. |
| `/migrate-mstest-v1v2-to-v3` | [`migrate-mstest-v1v2-to-v3`](skills/backend-and-fullstack/migrate-mstest-v1v2-to-v3/SKILL.md) | Migrate MSTest v1 or v2 test project to MSTest v3. |
| `/migrate-mstest-v3-to-v4` | [`migrate-mstest-v3-to-v4`](skills/backend-and-fullstack/migrate-mstest-v3-to-v4/SKILL.md) | Fix build errors and breaking changes after upgrading MSTest from v3 to v4, or plan a complete MSTest v3-to-v4 migration. |
| `/migrate-nullable-references` | [`migrate-nullable-references`](skills/backend-and-fullstack/migrate-nullable-references/SKILL.md) | Enable nullable reference types in a C# project and systematically resolve all warnings. |
| `/migrate-static-to-wrapper` | [`migrate-static-to-wrapper`](skills/backend-and-fullstack/migrate-static-to-wrapper/SKILL.md) | Mechanically replace static dependency call sites with wrapper or built-in abstraction calls across a bounded scope. |
| `/migrate-vstest-to-mtp` | [`migrate-vstest-to-mtp`](skills/backend-and-fullstack/migrate-vstest-to-mtp/SKILL.md) | Migrates .NET test projects from VSTest to Microsoft.Testing.Platform (MTP). |
| `/migrate-xunit-to-xunit-v3` | [`migrate-xunit-to-xunit-v3`](skills/backend-and-fullstack/migrate-xunit-to-xunit-v3/SKILL.md) | Migrates .NET test projects from xUnit.net v2 to xUnit.net v3. |
| `/migrating-oracle-to-postgres-stored-procedures` | [`migrating-oracle-to-postgres-stored-procedures`](skills/backend-and-fullstack/migrating-oracle-to-postgres-stored-procedures/SKILL.md) | Migrates Oracle PL/SQL stored procedures to PostgreSQL PL/pgSQL. |
| `/mini-context-graph` | [`mini-context-graph`](skills/backend-and-fullstack/mini-context-graph/SKILL.md) | A persistent, compounding knowledge base combining Karpathy's LLM Wiki pattern with a structured knowledge graph. |
| `/mtp-hot-reload` | [`mtp-hot-reload`](skills/backend-and-fullstack/mtp-hot-reload/SKILL.md) | Suggests using Microsoft Testing Platform (MTP) hot reload to iterate fixes on failing tests without rebuilding. |
| `/multi-stage-dockerfile` | [`multi-stage-dockerfile`](skills/backend-and-fullstack/multi-stage-dockerfile/SKILL.md) | Create optimized multi-stage Dockerfiles for any language or framework. |
| `/next-intl-add-language` | [`next-intl-add-language`](skills/backend-and-fullstack/next-intl-add-language/SKILL.md) | Add new language to a Next.js + next-intl application. |
| `/no-eval-skill` | [`no-eval-skill`](skills/backend-and-fullstack/no-eval-skill/SKILL.md) | A skill with no eval.yaml for testing discovery behavior. |
| `/nuget-manager` | [`nuget-manager`](skills/backend-and-fullstack/nuget-manager/SKILL.md) | Manage NuGet packages in .NET projects/solutions. |
| `/nuget-trusted-publishing` | [`nuget-trusted-publishing`](skills/backend-and-fullstack/nuget-trusted-publishing/SKILL.md) | Set up NuGet trusted publishing (OIDC) on a GitHub Actions repo — replaces long-lived API keys with short-lived tokens. |
| `/optimizing-ef-core-queries` | [`optimizing-ef-core-queries`](skills/backend-and-fullstack/optimizing-ef-core-queries/SKILL.md) | Optimize Entity Framework Core queries by fixing N+1 problems, choosing correct tracking modes, using compiled queries. |
| `/performance` | [`performance`](skills/backend-and-fullstack/performance/SKILL.md) | Optimize web performance for faster loading and better user experience. |
| `/php-mcp-server-generator` | [`php-mcp-server-generator`](skills/backend-and-fullstack/php-mcp-server-generator/SKILL.md) | Generate a complete PHP Model Context Protocol server project with tools, resources, prompts, and tests using the official PHP SDK. |
| `/planning-oracle-to-postgres-migration-integration-testing` | [`planning-oracle-to-postgres-migration-integration-testing`](skills/backend-and-fullstack/planning-oracle-to-postgres-migration-integration-testing/SKILL.md) | Creates an integration testing plan for .NET data access artifacts during Oracle-to-PostgreSQL database migrations. |
| `/platform-detection` | [`platform-detection`](skills/backend-and-fullstack/platform-detection/SKILL.md) | Reference data for detecting the test platform (VSTest vs Microsoft.Testing.Platform) and test framework (MSTest,. |
| `/postgresql-code-review` | [`postgresql-code-review`](skills/backend-and-fullstack/postgresql-code-review/SKILL.md) | PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. |
| `/postgresql-optimization` | [`postgresql-optimization`](skills/backend-and-fullstack/postgresql-optimization/SKILL.md) | PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types. |
| `/pr-dashboard` | [`pr-dashboard`](skills/backend-and-fullstack/pr-dashboard/SKILL.md) | Open a GitHub PR dashboard in the browser. |
| `/pr-review` | [`pr-review`](skills/backend-and-fullstack/pr-review/SKILL.md) | Review pull requests for the MiniMax Skills repository. |
| `/pydantic-models-py` | [`pydantic-models-py`](skills/backend-and-fullstack/pydantic-models-py/SKILL.md) | Create Pydantic models following the multi-model pattern with Base, Create, Update, Response, and InDB variants. |
| `/pytest-coverage` | [`pytest-coverage`](skills/backend-and-fullstack/pytest-coverage/SKILL.md) | Run pytest tests with coverage, discover lines missing coverage, and increase coverage to 100%. |
| `/python-mcp-server-generator` | [`python-mcp-server-generator`](skills/backend-and-fullstack/python-mcp-server-generator/SKILL.md) | Generate a complete MCP server project in Python with tools, resources, and proper configuration. |
| `/python-pypi-package-builder` | [`python-pypi-package-builder`](skills/backend-and-fullstack/python-pypi-package-builder/SKILL.md) | End-to-end skill for building, testing, linting, versioning, and publishing a production-grade Python library to PyPI. |
| `/qdrant-memory-usage-optimization` | [`qdrant-memory-usage-optimization`](skills/backend-and-fullstack/qdrant-memory-usage-optimization/SKILL.md) | Diagnoses and reduces Qdrant memory usage. |
| `/qdrant-monitoring-debugging` | [`qdrant-monitoring-debugging`](skills/backend-and-fullstack/qdrant-monitoring-debugging/SKILL.md) | Diagnoses Qdrant production issues using metrics and observability tools. |
| `/qdrant-search-quality` | [`qdrant-search-quality`](skills/backend-and-fullstack/qdrant-search-quality/SKILL.md) | Diagnoses and improves Qdrant search relevance. |
| `/qdrant-search-quality-diagnosis` | [`qdrant-search-quality-diagnosis`](skills/backend-and-fullstack/qdrant-search-quality-diagnosis/SKILL.md) | Diagnoses Qdrant search quality issues. |
| `/qdrant-search-speed-optimization` | [`qdrant-search-speed-optimization`](skills/backend-and-fullstack/qdrant-search-speed-optimization/SKILL.md) | Diagnoses and fixes slow Qdrant search. |
| `/remember` | [`remember`](skills/backend-and-fullstack/remember/SKILL.md) | Transforms lessons learned into domain-organized memory instructions (global or workspace). |
| `/review-and-refactor` | [`review-and-refactor`](skills/backend-and-fullstack/review-and-refactor/SKILL.md) | Review and refactor code in your project according to defined instructions. |
| `/reviewing-oracle-to-postgres-migration` | [`reviewing-oracle-to-postgres-migration`](skills/backend-and-fullstack/reviewing-oracle-to-postgres-migration/SKILL.md) | Identifies Oracle-to-PostgreSQL migration risks by cross-referencing code against known behavioral differences (empty. |
| `/ruff-recursive-fix` | [`ruff-recursive-fix`](skills/backend-and-fullstack/ruff-recursive-fix/SKILL.md) | Run Ruff checks with optional scope and rule overrides, apply safe and unsafe autofixes iteratively, review each change. |
| `/run-tests` | [`run-tests`](skills/backend-and-fullstack/run-tests/SKILL.md) | Runs .NET tests with `dotnet test` and chooses the correct platform/SDK/framework syntax. |
| `/rust-mcp-server-generator` | [`rust-mcp-server-generator`](skills/backend-and-fullstack/rust-mcp-server-generator/SKILL.md) | Generate a complete Rust Model Context Protocol server project with tools, prompts, resources. |
| `/sample-skill` | [`sample-skill`](skills/backend-and-fullstack/sample-skill/SKILL.md) | A sample skill for testing the validator. Helps with greeting generation. |
| `/scaffolding-oracle-to-postgres-migration-test-project` | [`scaffolding-oracle-to-postgres-migration-test-project`](skills/backend-and-fullstack/scaffolding-oracle-to-postgres-migration-test-project/SKILL.md) | Scaffolds an xUnit integration test project for validating Oracle-to-PostgreSQL database migration behavior in .NET solutions. |
| `/shuffle-json-data` | [`shuffle-json-data`](skills/backend-and-fullstack/shuffle-json-data/SKILL.md) | Shuffle repetitive JSON objects safely by validating schema consistency before randomising entries. |
| `/sponsor-finder` | [`sponsor-finder`](skills/backend-and-fullstack/sponsor-finder/SKILL.md) | Find which of a GitHub repository's dependencies are sponsorable via GitHub Sponsors. |
| `/spring-boot-testing` | [`spring-boot-testing`](skills/backend-and-fullstack/spring-boot-testing/SKILL.md) | Expert Spring Boot 4 testing specialist that selects the best Spring Boot testing techniques for your situation with. |
| `/sql-code-review` | [`sql-code-review`](skills/backend-and-fullstack/sql-code-review/SKILL.md) | Universal SQL code review assistant that performs comprehensive security, maintainability. |
| `/sql-optimization` | [`sql-optimization`](skills/backend-and-fullstack/sql-optimization/SKILL.md) | Universal SQL performance optimization assistant for comprehensive query tuning, indexing strategies. |
| `/sql-server-table-reconciliation` | [`sql-server-table-reconciliation`](skills/backend-and-fullstack/sql-server-table-reconciliation/SKILL.md) | Use when: comparing SQL Server tables across instances, data migration validation, ETL verification, row mismatch. |
| `/ssma-console` | [`ssma-console`](skills/backend-and-fullstack/ssma-console/SKILL.md) | Use when: SSMA console operations — create project, generate assessment report, convert schema, migrate data, Oracle to. |
| `/suggest-awesome-github-copilot-instructions` | [`suggest-awesome-github-copilot-instructions`](skills/backend-and-fullstack/suggest-awesome-github-copilot-instructions/SKILL.md) | Suggest relevant GitHub Copilot instruction files from the awesome-copilot repository based on current repository. |
| `/suggest-awesome-github-copilot-skills` | [`suggest-awesome-github-copilot-skills`](skills/backend-and-fullstack/suggest-awesome-github-copilot-skills/SKILL.md) | Suggest relevant GitHub Copilot skills from the awesome-copilot repository based on current repository context and chat. |
| `/system-text-json-net11` | [`system-text-json-net11`](skills/backend-and-fullstack/system-text-json-net11/SKILL.md) | Provides guidance on new System.Text.Json APIs introduced in .NET 11. |
| `/systematic-debugging` | [`systematic-debugging`](skills/backend-and-fullstack/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. |
| `/template-discovery` | [`template-discovery`](skills/backend-and-fullstack/template-discovery/SKILL.md) | Helps find, inspect, and compare .NET project templates. |
| `/template-instantiation` | [`template-instantiation`](skills/backend-and-fullstack/template-instantiation/SKILL.md) | Creates .NET projects from templates with validated parameters, smart defaults, Central Package Management adaptation. |
| `/template-validation` | [`template-validation`](skills/backend-and-fullstack/template-validation/SKILL.md) | Validates custom dotnet new templates for correctness before publishing. |
| `/test-anti-patterns` | [`test-anti-patterns`](skills/backend-and-fullstack/test-anti-patterns/SKILL.md) | Audits existing .NET test code (MSTest, xUnit, NUnit, TUnit) for anti-patterns and quality issues that undermine. |
| `/test-driven-development` | [`test-driven-development`](skills/backend-and-fullstack/test-driven-development/SKILL.md) | Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. |
| `/test-smell-detection` | [`test-smell-detection`](skills/backend-and-fullstack/test-smell-detection/SKILL.md) | Deep-dive audit using the full testsmells.org 19-smell academic catalog for .NET tests. |
| `/thread-abort-migration` | [`thread-abort-migration`](skills/backend-and-fullstack/thread-abort-migration/SKILL.md) | Guides migration of .NET Framework Thread.Abort usage to cooperative cancellation in modern .NET. |
| `/twitter-algorithm-optimizer` | [`twitter-algorithm-optimizer`](skills/backend-and-fullstack/twitter-algorithm-optimizer/SKILL.md) | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. |
| `/update-markdown-file-index` | [`update-markdown-file-index`](skills/backend-and-fullstack/update-markdown-file-index/SKILL.md) | Update a markdown file section with an index/table of files from a specified folder. |
| `/use-js-interop` | [`use-js-interop`](skills/backend-and-fullstack/use-js-interop/SKILL.md) | Add, review, or fix JavaScript interop in Blazor components. |
| `/using-git-worktrees` | [`using-git-worktrees`](skills/backend-and-fullstack/using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans -. |
| `/vardoger-analyze` | [`vardoger-analyze`](skills/backend-and-fullstack/vardoger-analyze/SKILL.md) | Use when the user asks to personalize the GitHub Copilot CLI assistant, adapt Copilot to their style, use vardoger. |
| `/vercel-composition-patterns` | [`vercel-composition-patterns`](skills/backend-and-fullstack/vercel-composition-patterns/SKILL.md) | React composition patterns that scale. |
| `/vision-analysis` | [`vision-analysis`](skills/backend-and-fullstack/vision-analysis/SKILL.md) | Analyze, describe, and extract information from images using the MiniMax vision MCP tool. |
| `/webapp-testing` | [`webapp-testing`](skills/backend-and-fullstack/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. |
| `/what-context-needed` | [`what-context-needed`](skills/backend-and-fullstack/what-context-needed/SKILL.md) | Ask Copilot what files it needs to see before answering a question. |
| `/wiki-changelog` | [`wiki-changelog`](skills/backend-and-fullstack/wiki-changelog/SKILL.md) | Analyzes git commit history and generates structured changelogs categorized by change type. |
| `/wordpress-block-theming` | [`wordpress-block-theming`](skills/backend-and-fullstack/wordpress-block-theming/SKILL.md) | WordPress Full Site Editing (FSE) theme architecture. |
| `/wordpress-router` | [`wordpress-router`](skills/backend-and-fullstack/wordpress-router/SKILL.md) | Use when the user asks about WordPress codebases (plugins, themes, block themes, Gutenberg blocks, WP core checkouts). |
| `/wp-abilities-api` | [`wp-abilities-api`](skills/backend-and-fullstack/wp-abilities-api/SKILL.md) | Use when working with the WordPress Abilities API (wp_register_ability, wp_register_ability_category,. |
| `/wp-abilities-audit` | [`wp-abilities-audit`](skills/backend-and-fullstack/wp-abilities-audit/SKILL.md) | Audit a WordPress plugin's REST surface and produce a standardized audit document proposing Abilities API registrations. |
| `/wp-abilities-verify` | [`wp-abilities-verify`](skills/backend-and-fullstack/wp-abilities-verify/SKILL.md) | Verify a WordPress plugin's Abilities API registrations: enumerate abilities, check that callback behavior matches each. |
| `/wp-block-development` | [`wp-block-development`](skills/backend-and-fullstack/wp-block-development/SKILL.md) | Use when developing WordPress (Gutenberg) blocks: block.json metadata, register_block_type(_from_metadata),. |
| `/wp-performance` | [`wp-performance`](skills/backend-and-fullstack/wp-performance/SKILL.md) | Use when investigating or improving WordPress performance (backend-only agent): profiling and measurement (WP-CLI. |
| `/wp-phpstan` | [`wp-phpstan`](skills/backend-and-fullstack/wp-phpstan/SKILL.md) | Use when configuring, running, or fixing PHPStan static analysis in WordPress projects (plugins/themes/sites):. |
| `/wp-playground` | [`wp-playground`](skills/backend-and-fullstack/wp-playground/SKILL.md) | Use for WordPress Playground workflows: fast disposable WP instances in the browser or locally via @wp-playground/cli. |
| `/wp-plugin-development` | [`wp-plugin-development`](skills/backend-and-fullstack/wp-plugin-development/SKILL.md) | Use when developing WordPress plugins: architecture and hooks, activation/deactivation/uninstall, admin UI and Settings. |
| `/wp-project-triage` | [`wp-project-triage`](skills/backend-and-fullstack/wp-project-triage/SKILL.md) | Use when you need a deterministic inspection of a WordPress repository (plugin/theme/block theme/WP core/Gutenberg/full. |
| `/wp-rest-api` | [`wp-rest-api`](skills/backend-and-fullstack/wp-rest-api/SKILL.md) | Use when building, extending, or debugging WordPress REST API endpoints/routes: register_rest_route,. |
| `/wp-wpcli-and-ops` | [`wp-wpcli-and-ops`](skills/backend-and-fullstack/wp-wpcli-and-ops/SKILL.md) | Use when working with WP-CLI (wp) for WordPress operations: safe search-replace, db export/import,. |
| `/writing-mstest-tests` | [`writing-mstest-tests`](skills/backend-and-fullstack/writing-mstest-tests/SKILL.md) | Write new MSTest unit tests and implement concrete fixes in existing MSTest code using MSTest 3.x/4.x modern APIs and. |

---

### 📈 Growth Marketing & SEO
> *Conversion rate optimization (CRO), search engine indexing, copywriting, competitor analysis, and sales enablement.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Ahrefs Automation` | [`Ahrefs Automation`](skills/marketing-and-seo/Ahrefs Automation/SKILL.md) | Automate SEO research with Ahrefs -- analyze backlink profiles, research keywords, track domain metrics history, audit. |
| `/Gardening Skills Wiki` | [`Gardening Skills Wiki`](skills/marketing-and-seo/Gardening Skills Wiki/SKILL.md) | Maintain skills wiki health - check links, naming, cross-references, and coverage. |
| `/Meta-Pattern Recognition` | [`Meta-Pattern Recognition`](skills/marketing-and-seo/Meta-Pattern Recognition/SKILL.md) | Spot patterns appearing in 3+ domains to find universal principles. |
| `/SEMrush Automation` | [`SEMrush Automation`](skills/marketing-and-seo/SEMrush Automation/SKILL.md) | Automate SEO analysis with SEMrush -- research keywords, analyze domain organic rankings, audit backlinks, assess. |
| `/ab-test-setup` | [`ab-test-setup`](skills/marketing-and-seo/ab-test-setup/SKILL.md) | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. |
| `/analytics-tracking` | [`analytics-tracking`](skills/marketing-and-seo/analytics-tracking/SKILL.md) | When the user wants to set up, improve, or audit analytics tracking and measurement. |
| `/aso-audit` | [`aso-audit`](skills/marketing-and-seo/aso-audit/SKILL.md) | When the user wants to audit or optimize an App Store or Google Play listing. |
| `/azure-ai-textanalytics-py` | [`azure-ai-textanalytics-py`](skills/marketing-and-seo/azure-ai-textanalytics-py/SKILL.md) | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. |
| `/churn-prevention` | [`churn-prevention`](skills/marketing-and-seo/churn-prevention/SKILL.md) | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments. |
| `/co-marketing` | [`co-marketing`](skills/marketing-and-seo/co-marketing/SKILL.md) | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. |
| `/cold-email` | [`cold-email`](skills/marketing-and-seo/cold-email/SKILL.md) | Write B2B cold emails and follow-up sequences that get replies. |
| `/community-marketing` | [`community-marketing`](skills/marketing-and-seo/community-marketing/SKILL.md) | Build and leverage online communities to drive product growth and brand loyalty. |
| `/competitor-alternatives` | [`competitor-alternatives`](skills/marketing-and-seo/competitor-alternatives/SKILL.md) | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. |
| `/competitor-profiling` | [`competitor-profiling`](skills/marketing-and-seo/competitor-profiling/SKILL.md) | When the user wants to research, profile, or analyze competitors from their URLs. |
| `/content-strategy` | [`content-strategy`](skills/marketing-and-seo/content-strategy/SKILL.md) | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. |
| `/copy-editing` | [`copy-editing`](skills/marketing-and-seo/copy-editing/SKILL.md) | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. |
| `/copywriting` | [`copywriting`](skills/marketing-and-seo/copywriting/SKILL.md) | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages,. |
| `/customer-research` | [`customer-research`](skills/marketing-and-seo/customer-research/SKILL.md) | When the user wants to conduct, analyze, or synthesize customer research. |
| `/email-sequence` | [`email-sequence`](skills/marketing-and-seo/email-sequence/SKILL.md) | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. |
| `/form-cro` | [`form-cro`](skills/marketing-and-seo/form-cro/SKILL.md) | When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms,. |
| `/free-tool-strategy` | [`free-tool-strategy`](skills/marketing-and-seo/free-tool-strategy/SKILL.md) | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or. |
| `/from-the-other-side-wiggins` | [`from-the-other-side-wiggins`](skills/marketing-and-seo/from-the-other-side-wiggins/SKILL.md) | Narrative and synthesis profile for Wiggins: framing, explanation, and audience-aware communication patterns for Ember sessions. |
| `/gsc` | [`gsc`](skills/marketing-and-seo/gsc/SKILL.md) | Query Google Search Console for SEO data - search queries, top pages, CTR opportunities, URL inspection, and sitemaps. |
| `/kql` | [`kql`](skills/marketing-and-seo/kql/SKILL.md) | KQL language expertise for writing correct, efficient Kusto Query Language queries. |
| `/launch-strategy` | [`launch-strategy`](skills/marketing-and-seo/launch-strategy/SKILL.md) | When the user wants to plan a product launch, feature announcement, or release strategy. |
| `/lead-magnets` | [`lead-magnets`](skills/marketing-and-seo/lead-magnets/SKILL.md) | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. |
| `/lead-research-assistant` | [`lead-research-assistant`](skills/marketing-and-seo/lead-research-assistant/SKILL.md) | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies. |
| `/marketing-ideas` | [`marketing-ideas`](skills/marketing-and-seo/marketing-ideas/SKILL.md) | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. |
| `/marketing-psychology` | [`marketing-psychology`](skills/marketing-and-seo/marketing-psychology/SKILL.md) | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. |
| `/microbenchmarking` | [`microbenchmarking`](skills/marketing-and-seo/microbenchmarking/SKILL.md) | Activate this skill when BenchmarkDotNet (BDN) is involved in the task — creating, running, configuring. |
| `/microsoft-azure-webjobs-extensions-authentication-events-dotnet` | [`microsoft-azure-webjobs-extensions-authentication-events-dotnet`](skills/marketing-and-seo/microsoft-azure-webjobs-extensions-authentication-events-dotnet/SKILL.md) | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |
| `/microsoft-code-reference` | [`microsoft-code-reference`](skills/marketing-and-seo/microsoft-code-reference/SKILL.md) | Look up Microsoft API references, find working code samples, and verify SDK code is correct. |
| `/microsoft-docs` | [`microsoft-docs`](skills/marketing-and-seo/microsoft-docs/SKILL.md) | Query official Microsoft documentation to find concepts, tutorials. |
| `/microsoft-foundry` | [`microsoft-foundry`](skills/marketing-and-seo/microsoft-foundry/SKILL.md) | Deploy, evaluate, fine-tune, and manage Foundry agents end-to-end: Docker build, ACR push, hosted/prompt agent create,. |
| `/microsoft-skill-creator` | [`microsoft-skill-creator`](skills/marketing-and-seo/microsoft-skill-creator/SKILL.md) | Create agent skills for Microsoft technologies using Learn MCP tools. |
| `/microsoft_clarity-automation` | [`microsoft_clarity-automation`](skills/marketing-and-seo/microsoft_clarity-automation/SKILL.md) | Automate Microsoft Clarity tasks via Rube MCP (Composio): session recordings, heatmaps, and user behavior analytics. |
| `/onboarding-cro` | [`onboarding-cro`](skills/marketing-and-seo/onboarding-cro/SKILL.md) | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. |
| `/page-cro` | [`page-cro`](skills/marketing-and-seo/page-cro/SKILL.md) | When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing. |
| `/paid-ads` | [`paid-ads`](skills/marketing-and-seo/paid-ads/SKILL.md) | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X. |
| `/paywall-upgrade-cro` | [`paywall-upgrade-cro`](skills/marketing-and-seo/paywall-upgrade-cro/SKILL.md) | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. |
| `/popup-cro` | [`popup-cro`](skills/marketing-and-seo/popup-cro/SKILL.md) | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. |
| `/pricing-strategy` | [`pricing-strategy`](skills/marketing-and-seo/pricing-strategy/SKILL.md) | When the user wants help with pricing decisions, packaging, or monetization strategy. |
| `/product-marketing-context` | [`product-marketing-context`](skills/marketing-and-seo/product-marketing-context/SKILL.md) | When the user wants to create or update their product marketing context document. |
| `/programmatic-seo` | [`programmatic-seo`](skills/marketing-and-seo/programmatic-seo/SKILL.md) | When the user wants to create SEO-driven pages at scale using templates and data. |
| `/referral-program` | [`referral-program`](skills/marketing-and-seo/referral-program/SKILL.md) | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. |
| `/revops` | [`revops`](skills/marketing-and-seo/revops/SKILL.md) | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. |
| `/roundup-setup` | [`roundup-setup`](skills/marketing-and-seo/roundup-setup/SKILL.md) | Interactive onboarding that learns your communication style, audiences. |
| `/sales-enablement` | [`sales-enablement`](skills/marketing-and-seo/sales-enablement/SKILL.md) | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. |
| `/seo` | [`seo`](skills/marketing-and-seo/seo/SKILL.md) | SEO specialist agent with site audits, content writing, keyword research, technical fixes, link building, and ranking strategies. |
| `/seo-article-gen` | [`seo-article-gen`](skills/marketing-and-seo/seo-article-gen/SKILL.md) | SEO-optimized article generator with automatic affiliate link integration. |
| `/seo-audit` | [`seo-audit`](skills/marketing-and-seo/seo-audit/SKILL.md) | When the user wants to audit, review, or diagnose SEO issues on their site. |
| `/seo-competitor-analysis` | [`seo-competitor-analysis`](skills/marketing-and-seo/seo-competitor-analysis/SKILL.md) | Perform deep SEO competitor analysis, including keyword research, backlink checking, and content strategy mapping. |
| `/seo-content-writer` | [`seo-content-writer`](skills/marketing-and-seo/seo-content-writer/SKILL.md) | Use when the user asks to "write SEO content", "create a blog post", "write an article", "content writing", "draft. |
| `/signup-flow-cro` | [`signup-flow-cro`](skills/marketing-and-seo/signup-flow-cro/SKILL.md) | When the user wants to optimize signup, registration, account creation, or trial activation flows. |
| `/social-content` | [`social-content`](skills/marketing-and-seo/social-content/SKILL.md) | When the user wants help creating, scheduling. |
| `/technical-seo-checker` | [`technical-seo-checker`](skills/marketing-and-seo/technical-seo-checker/SKILL.md) | This skill should be used when the user asks to "technical SEO audit", "check page speed", "Core Web Vitals", "LCP is. |
| `/train-sentence-transformers` | [`train-sentence-transformers`](skills/marketing-and-seo/train-sentence-transformers/SKILL.md) | Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder; dense or static embedding. |
| `/web-quality-audit` | [`web-quality-audit`](skills/marketing-and-seo/web-quality-audit/SKILL.md) | Comprehensive web quality audit covering performance, accessibility, SEO, and best practices. |
| `/wiki-researcher` | [`wiki-researcher`](skills/marketing-and-seo/wiki-researcher/SKILL.md) | Conducts multi-turn iterative deep research on specific topics within a codebase with zero tolerance for shallow analysis. |
| `/xurl` | [`xurl`](skills/marketing-and-seo/xurl/SKILL.md) | A Twitter research and content intelligence skill focused on attracting WordPress and Shopify clients. |

---

### 🔒 Security & System Compliance
> *Cybersecurity reviews, code sanitisation, threat modelling, license monitoring, and GDPR compliance.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Defense-in-Depth Validation` | [`Defense-in-Depth Validation`](skills/security-and-compliance/Defense-in-Depth Validation/SKILL.md) | Validate at every layer data passes through to make bugs impossible. |
| `/azure-compliance` | [`azure-compliance`](skills/security-and-compliance/azure-compliance/SKILL.md) | Run Azure compliance and security audits with azqr plus Key Vault expiration checks. |
| `/best-practices` | [`best-practices`](skills/security-and-compliance/best-practices/SKILL.md) | Apply modern web development best practices for security, compatibility, and code quality. |
| `/configure-auth` | [`configure-auth`](skills/security-and-compliance/configure-auth/SKILL.md) | Add authentication and authorization to a Blazor Web App, accounting for the app's render mode. |
| `/data-breach-blast-radius` | [`data-breach-blast-radius`](skills/security-and-compliance/data-breach-blast-radius/SKILL.md) | Pre-breach impact analysis: inventories sensitive data (PII, PHI, PCI-DSS, credentials), traces data flows, scores. |
| `/doc-coauthoring` | [`doc-coauthoring`](skills/security-and-compliance/doc-coauthoring/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. |
| `/doubt-driven-development` | [`doubt-driven-development`](skills/security-and-compliance/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. |
| `/entra-app-registration` | [`entra-app-registration`](skills/security-and-compliance/entra-app-registration/SKILL.md) | Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. |
| `/gdpr-compliant` | [`gdpr-compliant`](skills/security-and-compliance/gdpr-compliant/SKILL.md) | Apply GDPR-compliant engineering practices across your codebase. |
| `/google-cloud-recipe-auth` | [`google-cloud-recipe-auth`](skills/security-and-compliance/google-cloud-recipe-auth/SKILL.md) | Provides expert guidance on authenticating and authorizing to Google Cloud services and APIs, covering human users,. |
| `/google-cloud-waf-security` | [`google-cloud-waf-security`](skills/security-and-compliance/google-cloud-waf-security/SKILL.md) | Generates security-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/security-and-hardening` | [`security-and-hardening`](skills/security-and-compliance/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. |
| `/security-review` | [`security-review`](skills/security-and-compliance/security-review/SKILL.md) | AI-powered codebase security scanner that reasons about code like a security researcher — tracing data flows,. |
| `/target-authoring` | [`target-authoring`](skills/security-and-compliance/target-authoring/SKILL.md) | Canonical patterns for writing custom MSBuild targets. Only activate in MSBuild/.NET build context. |
| `/template-authoring` | [`template-authoring`](skills/security-and-compliance/template-authoring/SKILL.md) | Guides creation and validation of custom dotnet new templates. |
| `/threat-model-analyst` | [`threat-model-analyst`](skills/security-and-compliance/threat-model-analyst/SKILL.md) | Full STRIDE-A threat model analysis and incremental update skill for repositories and systems. |
| `/vercel-cli-with-tokens` | [`vercel-cli-with-tokens`](skills/security-and-compliance/vercel-cli-with-tokens/SKILL.md) | Deploy and manage projects on Vercel using token-based authentication. |
| `/workers-best-practices` | [`workers-best-practices`](skills/security-and-compliance/workers-best-practices/SKILL.md) | Reviews and authors Cloudflare Workers code against production best practices. |

---

### 🧬 Science & Bioinformatics
> *Scientific search portals, genomic research APIs, biological catalogs, and chemical structure metrics.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Inversion Exercise` | [`Inversion Exercise`](skills/science-and-bioinformatics/Inversion Exercise/SKILL.md) | Flip core assumptions to reveal hidden constraints and alternative approaches - "what if the opposite were true? |
| `/acreadiness-generate-instructions` | [`acreadiness-generate-instructions`](skills/science-and-bioinformatics/acreadiness-generate-instructions/SKILL.md) | Generate tailored AI agent instruction files via AgentRC instructions command. |
| `/architecture-blueprint-generator` | [`architecture-blueprint-generator`](skills/science-and-bioinformatics/architecture-blueprint-generator/SKILL.md) | Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. |
| `/binlog-generation` | [`binlog-generation`](skills/science-and-bioinformatics/binlog-generation/SKILL.md) | Generate MSBuild binary logs (binlogs) for build diagnostics and analysis. |
| `/changelog-generator` | [`changelog-generator`](skills/science-and-bioinformatics/changelog-generator/SKILL.md) | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes. |
| `/code-exemplars-blueprint-generator` | [`code-exemplars-blueprint-generator`](skills/science-and-bioinformatics/code-exemplars-blueprint-generator/SKILL.md) | Technology-agnostic prompt generator that creates customizable AI prompts for scanning codebases and identifying. |
| `/comment-code-generate-a-tutorial` | [`comment-code-generate-a-tutorial`](skills/science-and-bioinformatics/comment-code-generate-a-tutorial/SKILL.md) | Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear. |
| `/context-map` | [`context-map`](skills/science-and-bioinformatics/context-map/SKILL.md) | Generate a map of all files relevant to a task before making changes. |
| `/copilot-instructions-blueprint-generator` | [`copilot-instructions-blueprint-generator`](skills/science-and-bioinformatics/copilot-instructions-blueprint-generator/SKILL.md) | Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub. |
| `/create-specification` | [`create-specification`](skills/science-and-bioinformatics/create-specification/SKILL.md) | Create a new specification file for the solution, optimized for Generative AI consumption. |
| `/draw-io-diagram-generator` | [`draw-io-diagram-generator`](skills/science-and-bioinformatics/draw-io-diagram-generator/SKILL.md) | Use when creating, editing, or generating draw.io diagram files (.drawio, .drawio.svg, .drawio.png). |
| `/editorconfig` | [`editorconfig`](skills/science-and-bioinformatics/editorconfig/SKILL.md) | Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences. |
| `/excalidraw-diagram-generator` | [`excalidraw-diagram-generator`](skills/science-and-bioinformatics/excalidraw-diagram-generator/SKILL.md) | Generate Excalidraw diagrams from natural language descriptions. |
| `/flowstudio-power-automate-governance` | [`flowstudio-power-automate-governance`](skills/science-and-bioinformatics/flowstudio-power-automate-governance/SKILL.md) | Govern Power Automate flows and Power Apps at scale using the FlowStudio MCP cached store. |
| `/folder-structure-blueprint-generator` | [`folder-structure-blueprint-generator`](skills/science-and-bioinformatics/folder-structure-blueprint-generator/SKILL.md) | Comprehensive technology-agnostic prompt for analyzing and documenting project folder structures. |
| `/generate-custom-instructions-from-codebase` | [`generate-custom-instructions-from-codebase`](skills/science-and-bioinformatics/generate-custom-instructions-from-codebase/SKILL.md) | Migration and code evolution instructions generator for GitHub Copilot. |
| `/generate-image` | [`generate-image`](skills/science-and-bioinformatics/generate-image/SKILL.md) | Generate images using AI. |
| `/generate-testability-wrappers` | [`generate-testability-wrappers`](skills/science-and-bioinformatics/generate-testability-wrappers/SKILL.md) | Generate wrapper interfaces and DI registration for hard-to-test static dependencies in C#. |
| `/including-generated-files` | [`including-generated-files`](skills/science-and-bioinformatics/including-generated-files/SKILL.md) | Fix MSBuild targets that generate files during the build but those files are missing from compilation or output. |
| `/internal-comms` | [`internal-comms`](skills/science-and-bioinformatics/internal-comms/SKILL.md) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. |
| `/meeting-minutes` | [`meeting-minutes`](skills/science-and-bioinformatics/meeting-minutes/SKILL.md) | Generate concise, actionable meeting minutes for internal meetings. |
| `/plantuml-ascii` | [`plantuml-ascii`](skills/science-and-bioinformatics/plantuml-ascii/SKILL.md) | Generate ASCII art diagrams using PlantUML text mode. |
| `/playwright-generate-test` | [`playwright-generate-test`](skills/science-and-bioinformatics/playwright-generate-test/SKILL.md) | Generate a Playwright test based on a scenario using Playwright MCP. |
| `/podcast-generation` | [`podcast-generation`](skills/science-and-bioinformatics/podcast-generation/SKILL.md) | Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. |
| `/project-workflow-analysis-blueprint-generator` | [`project-workflow-analysis-blueprint-generator`](skills/science-and-bioinformatics/project-workflow-analysis-blueprint-generator/SKILL.md) | Comprehensive technology-agnostic prompt generator for documenting end-to-end application workflows. |
| `/readme-blueprint-generator` | [`readme-blueprint-generator`](skills/science-and-bioinformatics/readme-blueprint-generator/SKILL.md) | Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive. |
| `/refactor-method-complexity-reduce` | [`refactor-method-complexity-reduce`](skills/science-and-bioinformatics/refactor-method-complexity-reduce/SKILL.md) | Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or. |
| `/repo-story-time` | [`repo-story-time`](skills/science-and-bioinformatics/repo-story-time/SKILL.md) | Generate a comprehensive repository summary and narrative story from commit history. |
| `/structured-autonomy-generate` | [`structured-autonomy-generate`](skills/science-and-bioinformatics/structured-autonomy-generate/SKILL.md) | Structured Autonomy Implementation Generator Prompt. |
| `/tailored-resume-generator` | [`tailored-resume-generator`](skills/science-and-bioinformatics/tailored-resume-generator/SKILL.md) | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills. |
| `/technology-stack-blueprint-generator` | [`technology-stack-blueprint-generator`](skills/science-and-bioinformatics/technology-stack-blueprint-generator/SKILL.md) | Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. |

---

### ☁️ Cloud & DevOps Infrastructure
> *Cloud deployment toolsets (Azure, AWS), infrastructure-as-code (Terraform, Bicep), and CI/CD pipelines.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Cloudinary Automation` | [`Cloudinary Automation`](skills/cloud-and-infrastructure/Cloudinary Automation/SKILL.md) | Automate Cloudinary media management including folder organization, upload presets, asset lookup, transformations. |
| `/Writing Skills` | [`Writing Skills`](skills/cloud-and-infrastructure/Writing Skills/SKILL.md) | TDD for process documentation - test with subagents before writing, iterate until bulletproof. |
| `/aws-cdk-python-setup` | [`aws-cdk-python-setup`](skills/cloud-and-infrastructure/aws-cdk-python-setup/SKILL.md) | Setup and initialization guide for developing AWS CDK (Cloud Development Kit) applications in Python. |
| `/azure-ai` | [`azure-ai`](skills/cloud-and-infrastructure/azure-ai/SKILL.md) | Use for Azure AI: Search, Speech, OpenAI, Document Intelligence. |
| `/azure-ai-contentsafety-py` | [`azure-ai-contentsafety-py`](skills/cloud-and-infrastructure/azure-ai-contentsafety-py/SKILL.md) | Azure AI Content Safety SDK for Python. |
| `/azure-ai-contentsafety-ts` | [`azure-ai-contentsafety-ts`](skills/cloud-and-infrastructure/azure-ai-contentsafety-ts/SKILL.md) | Analyze text and images for harmful content using Azure AI Content Safety (@azure-rest/ai-content-safety). |
| `/azure-ai-contentunderstanding-py` | [`azure-ai-contentunderstanding-py`](skills/cloud-and-infrastructure/azure-ai-contentunderstanding-py/SKILL.md) | Azure AI Content Understanding SDK for Python. |
| `/azure-ai-language-conversations-py` | [`azure-ai-language-conversations-py`](skills/cloud-and-infrastructure/azure-ai-language-conversations-py/SKILL.md) | Implement Conversational Language Understanding (CLU) using the azure-ai-language-conversations Python SDK. |
| `/azure-ai-ml-py` | [`azure-ai-ml-py`](skills/cloud-and-infrastructure/azure-ai-ml-py/SKILL.md) | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| `/azure-ai-projects-py` | [`azure-ai-projects-py`](skills/cloud-and-infrastructure/azure-ai-projects-py/SKILL.md) | Build AI applications using the Azure AI Projects Python SDK (azure-ai-projects). |
| `/azure-ai-projects-ts` | [`azure-ai-projects-ts`](skills/cloud-and-infrastructure/azure-ai-projects-ts/SKILL.md) | Build AI applications using Azure AI Projects SDK for JavaScript (@azure/ai-projects). |
| `/azure-ai-transcription-py` | [`azure-ai-transcription-py`](skills/cloud-and-infrastructure/azure-ai-transcription-py/SKILL.md) | Azure AI Transcription SDK for Python. |
| `/azure-ai-translation-text-py` | [`azure-ai-translation-text-py`](skills/cloud-and-infrastructure/azure-ai-translation-text-py/SKILL.md) | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. |
| `/azure-ai-translation-ts` | [`azure-ai-translation-ts`](skills/cloud-and-infrastructure/azure-ai-translation-ts/SKILL.md) | Build translation applications using Azure Translation SDKs for JavaScript (@azure-rest/ai-translation-text,. |
| `/azure-ai-vision-imageanalysis-py` | [`azure-ai-vision-imageanalysis-py`](skills/cloud-and-infrastructure/azure-ai-vision-imageanalysis-py/SKILL.md) | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. |
| `/azure-aigateway` | [`azure-aigateway`](skills/cloud-and-infrastructure/azure-aigateway/SKILL.md) | Configure Azure API Management as an AI Gateway for AI models, MCP tools, and agents. |
| `/azure-appconfiguration-py` | [`azure-appconfiguration-py`](skills/cloud-and-infrastructure/azure-appconfiguration-py/SKILL.md) | Azure App Configuration SDK for Python. |
| `/azure-appconfiguration-ts` | [`azure-appconfiguration-ts`](skills/cloud-and-infrastructure/azure-appconfiguration-ts/SKILL.md) | Build applications using Azure App Configuration SDK for JavaScript (@azure/app-configuration). |
| `/azure-architecture-autopilot` | [`azure-architecture-autopilot`](skills/cloud-and-infrastructure/azure-architecture-autopilot/SKILL.md) | Design Azure infrastructure using natural language. |
| `/azure-cloud-migrate` | [`azure-cloud-migrate`](skills/cloud-and-infrastructure/azure-cloud-migrate/SKILL.md) | Assess and migrate cross-cloud workloads to Azure with reports and code conversion. |
| `/azure-compute` | [`azure-compute`](skills/cloud-and-infrastructure/azure-compute/SKILL.md) | Azure VM and VMSS router for recommendations, pricing, autoscale, orchestration, connectivity troubleshooting, capacity. |
| `/azure-containerregistry-py` | [`azure-containerregistry-py`](skills/cloud-and-infrastructure/azure-containerregistry-py/SKILL.md) | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |
| `/azure-cosmos-db-py` | [`azure-cosmos-db-py`](skills/cloud-and-infrastructure/azure-cosmos-db-py/SKILL.md) | Build Azure Cosmos DB NoSQL services with Python/FastAPI following production-grade patterns. |
| `/azure-cosmos-py` | [`azure-cosmos-py`](skills/cloud-and-infrastructure/azure-cosmos-py/SKILL.md) | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| `/azure-cosmos-ts` | [`azure-cosmos-ts`](skills/cloud-and-infrastructure/azure-cosmos-ts/SKILL.md) | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. |
| `/azure-cost` | [`azure-cost`](skills/cloud-and-infrastructure/azure-cost/SKILL.md) | Unified Azure cost management: query historical costs, forecast future spending, and optimize to reduce waste. |
| `/azure-data-tables-py` | [`azure-data-tables-py`](skills/cloud-and-infrastructure/azure-data-tables-py/SKILL.md) | Azure Tables SDK for Python (Storage and Cosmos DB). |
| `/azure-deploy` | [`azure-deploy`](skills/cloud-and-infrastructure/azure-deploy/SKILL.md) | Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. |
| `/azure-deployment-preflight` | [`azure-deployment-preflight`](skills/cloud-and-infrastructure/azure-deployment-preflight/SKILL.md) | Performs comprehensive preflight validation of Bicep deployments to Azure, including template syntax validation,. |
| `/azure-devops-cli` | [`azure-devops-cli`](skills/cloud-and-infrastructure/azure-devops-cli/SKILL.md) | Manage Azure DevOps resources via CLI including projects, repos, pipelines, builds, pull requests, work items, artifacts. |
| `/azure-diagnostics` | [`azure-diagnostics`](skills/cloud-and-infrastructure/azure-diagnostics/SKILL.md) | Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triage. |
| `/azure-enterprise-infra-planner` | [`azure-enterprise-infra-planner`](skills/cloud-and-infrastructure/azure-enterprise-infra-planner/SKILL.md) | Architect and provision enterprise Azure infrastructure from workload descriptions. |
| `/azure-eventgrid-py` | [`azure-eventgrid-py`](skills/cloud-and-infrastructure/azure-eventgrid-py/SKILL.md) | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |
| `/azure-eventhub-py` | [`azure-eventhub-py`](skills/cloud-and-infrastructure/azure-eventhub-py/SKILL.md) | Azure Event Hubs SDK for Python streaming. |
| `/azure-eventhub-ts` | [`azure-eventhub-ts`](skills/cloud-and-infrastructure/azure-eventhub-ts/SKILL.md) | Build event streaming applications using Azure Event Hubs SDK for JavaScript (@azure/event-hubs). |
| `/azure-hosted-copilot-sdk` | [`azure-hosted-copilot-sdk`](skills/cloud-and-infrastructure/azure-hosted-copilot-sdk/SKILL.md) | Build, deploy, and modify GitHub Copilot SDK apps on Azure. |
| `/azure-identity-py` | [`azure-identity-py`](skills/cloud-and-infrastructure/azure-identity-py/SKILL.md) | Azure Identity SDK for Python authentication with Microsoft Entra ID. |
| `/azure-identity-ts` | [`azure-identity-ts`](skills/cloud-and-infrastructure/azure-identity-ts/SKILL.md) | Authenticate to Azure services using Azure Identity library for JavaScript (@azure/identity). |
| `/azure-keyvault-keys-ts` | [`azure-keyvault-keys-ts`](skills/cloud-and-infrastructure/azure-keyvault-keys-ts/SKILL.md) | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). |
| `/azure-keyvault-py` | [`azure-keyvault-py`](skills/cloud-and-infrastructure/azure-keyvault-py/SKILL.md) | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| `/azure-keyvault-secrets-ts` | [`azure-keyvault-secrets-ts`](skills/cloud-and-infrastructure/azure-keyvault-secrets-ts/SKILL.md) | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). |
| `/azure-kubernetes` | [`azure-kubernetes`](skills/cloud-and-infrastructure/azure-kubernetes/SKILL.md) | Plan, create, and configure production-ready Azure Kubernetes Service (AKS) clusters. |
| `/azure-kubernetes-automatic-readiness` | [`azure-kubernetes-automatic-readiness`](skills/cloud-and-infrastructure/azure-kubernetes-automatic-readiness/SKILL.md) | Assess Kubernetes workloads and cluster configuration for AKS Automatic compatibility. |
| `/azure-kusto` | [`azure-kusto`](skills/cloud-and-infrastructure/azure-kusto/SKILL.md) | Query and analyze data in Azure Data Explorer (Kusto/ADX) using KQL for log analytics, telemetry, and time series analysis. |
| `/azure-messaging` | [`azure-messaging`](skills/cloud-and-infrastructure/azure-messaging/SKILL.md) | Troubleshoot and resolve issues with Azure Messaging SDKs for Event Hubs and Service Bus. |
| `/azure-messaging-webpubsubservice-py` | [`azure-messaging-webpubsubservice-py`](skills/cloud-and-infrastructure/azure-messaging-webpubsubservice-py/SKILL.md) | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |
| `/azure-mgmt-arizeaiobservabilityeval-dotnet` | [`azure-mgmt-arizeaiobservabilityeval-dotnet`](skills/cloud-and-infrastructure/azure-mgmt-arizeaiobservabilityeval-dotnet/SKILL.md) | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| `/azure-mgmt-botservice-py` | [`azure-mgmt-botservice-py`](skills/cloud-and-infrastructure/azure-mgmt-botservice-py/SKILL.md) | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| `/azure-mgmt-fabric-py` | [`azure-mgmt-fabric-py`](skills/cloud-and-infrastructure/azure-mgmt-fabric-py/SKILL.md) | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| `/azure-microsoft-playwright-testing-ts` | [`azure-microsoft-playwright-testing-ts`](skills/cloud-and-infrastructure/azure-microsoft-playwright-testing-ts/SKILL.md) | Run Playwright tests at scale using Azure Playwright Workspaces (formerly Microsoft Playwright Testing). |
| `/azure-monitor-ingestion-py` | [`azure-monitor-ingestion-py`](skills/cloud-and-infrastructure/azure-monitor-ingestion-py/SKILL.md) | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| `/azure-monitor-opentelemetry-exporter-py` | [`azure-monitor-opentelemetry-exporter-py`](skills/cloud-and-infrastructure/azure-monitor-opentelemetry-exporter-py/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| `/azure-monitor-opentelemetry-py` | [`azure-monitor-opentelemetry-py`](skills/cloud-and-infrastructure/azure-monitor-opentelemetry-py/SKILL.md) | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| `/azure-monitor-opentelemetry-ts` | [`azure-monitor-opentelemetry-ts`](skills/cloud-and-infrastructure/azure-monitor-opentelemetry-ts/SKILL.md) | Instrument applications with Azure Monitor and OpenTelemetry for JavaScript (@azure/monitor-opentelemetry). |
| `/azure-monitor-query-py` | [`azure-monitor-query-py`](skills/cloud-and-infrastructure/azure-monitor-query-py/SKILL.md) | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |
| `/azure-prepare` | [`azure-prepare`](skills/cloud-and-infrastructure/azure-prepare/SKILL.md) | Prepare Azure apps for deployment (infra Bicep/Terraform, azure.yaml, Dockerfiles). |
| `/azure-pricing` | [`azure-pricing`](skills/cloud-and-infrastructure/azure-pricing/SKILL.md) | Fetches real-time Azure retail pricing using the Azure Retail Prices API (prices.azure.com) and estimates Copilot. |
| `/azure-quotas` | [`azure-quotas`](skills/cloud-and-infrastructure/azure-quotas/SKILL.md) | Check/manage Azure quotas and usage across providers. For deployment planning, capacity validation, region selection. |
| `/azure-rbac` | [`azure-rbac`](skills/cloud-and-infrastructure/azure-rbac/SKILL.md) | Helps users find the right Azure RBAC role for an identity with least privilege access, then generate CLI commands and. |
| `/azure-reliability` | [`azure-reliability`](skills/cloud-and-infrastructure/azure-reliability/SKILL.md) | Assess and improve the reliability posture of PaaS Applications (Azure Functions and Azure App Service). |
| `/azure-resource-health-diagnose` | [`azure-resource-health-diagnose`](skills/cloud-and-infrastructure/azure-resource-health-diagnose/SKILL.md) | Analyze Azure resource health, diagnose issues from logs and telemetry, and create a remediation plan for identified problems. |
| `/azure-resource-lookup` | [`azure-resource-lookup`](skills/cloud-and-infrastructure/azure-resource-lookup/SKILL.md) | List, find, and show Azure resources across subscriptions or resource groups. |
| `/azure-role-selector` | [`azure-role-selector`](skills/cloud-and-infrastructure/azure-role-selector/SKILL.md) | When user is asking for guidance for which role to assign to an identity given desired permissions, this agent helps. |
| `/azure-servicebus-py` | [`azure-servicebus-py`](skills/cloud-and-infrastructure/azure-servicebus-py/SKILL.md) | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| `/azure-servicebus-ts` | [`azure-servicebus-ts`](skills/cloud-and-infrastructure/azure-servicebus-ts/SKILL.md) | Build messaging applications using Azure Service Bus SDK for JavaScript (@azure/service-bus). |
| `/azure-static-web-apps` | [`azure-static-web-apps`](skills/cloud-and-infrastructure/azure-static-web-apps/SKILL.md) | Helps create, configure, and deploy Azure Static Web Apps using the SWA CLI. |
| `/azure-storage` | [`azure-storage`](skills/cloud-and-infrastructure/azure-storage/SKILL.md) | Azure Storage Services including Blob Storage, File Shares, Queue Storage, Table Storage, and Data Lake. |
| `/azure-storage-blob-py` | [`azure-storage-blob-py`](skills/cloud-and-infrastructure/azure-storage-blob-py/SKILL.md) | Azure Blob Storage SDK for Python. |
| `/azure-storage-blob-ts` | [`azure-storage-blob-ts`](skills/cloud-and-infrastructure/azure-storage-blob-ts/SKILL.md) | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. |
| `/azure-storage-file-datalake-py` | [`azure-storage-file-datalake-py`](skills/cloud-and-infrastructure/azure-storage-file-datalake-py/SKILL.md) | Azure Data Lake Storage Gen2 SDK for Python. |
| `/azure-storage-file-share-py` | [`azure-storage-file-share-py`](skills/cloud-and-infrastructure/azure-storage-file-share-py/SKILL.md) | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| `/azure-storage-file-share-ts` | [`azure-storage-file-share-ts`](skills/cloud-and-infrastructure/azure-storage-file-share-ts/SKILL.md) | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| `/azure-storage-queue-py` | [`azure-storage-queue-py`](skills/cloud-and-infrastructure/azure-storage-queue-py/SKILL.md) | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| `/azure-storage-queue-ts` | [`azure-storage-queue-ts`](skills/cloud-and-infrastructure/azure-storage-queue-ts/SKILL.md) | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. |
| `/azure-upgrade` | [`azure-upgrade`](skills/cloud-and-infrastructure/azure-upgrade/SKILL.md) | Assess and upgrade Azure workloads between plans, tiers, or SKUs, or modernize Azure SDK dependencies in source code. |
| `/azure-validate` | [`azure-validate`](skills/cloud-and-infrastructure/azure-validate/SKILL.md) | Pre-deployment validation for Azure readiness. |
| `/azure-web-pubsub-ts` | [`azure-web-pubsub-ts`](skills/cloud-and-infrastructure/azure-web-pubsub-ts/SKILL.md) | Build real-time messaging applications using Azure Web PubSub SDKs for JavaScript (@azure/web-pubsub, @azure/web-pubsub-client). |
| `/capacity` | [`capacity`](skills/cloud-and-infrastructure/capacity/SKILL.md) | Discovers available Azure OpenAI model capacity across regions and projects. |
| `/cloud-design-patterns` | [`cloud-design-patterns`](skills/cloud-and-infrastructure/cloud-design-patterns/SKILL.md) | Cloud design patterns for distributed systems architecture covering 42 industry-standard patterns across reliability,. |
| `/cloud-run-basics` | [`cloud-run-basics`](skills/cloud-and-infrastructure/cloud-run-basics/SKILL.md) | Manages Cloud Run services, jobs, and worker pools. |
| `/cloud-solution-architect` | [`cloud-solution-architect`](skills/cloud-and-infrastructure/cloud-solution-architect/SKILL.md) | Transform the agent into a Cloud Solution Architect following Azure Architecture Center best practices. |
| `/cloudflare` | [`cloudflare`](skills/cloud-and-infrastructure/cloudflare/SKILL.md) | Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize,. |
| `/customize` | [`customize`](skills/cloud-and-infrastructure/customize/SKILL.md) | Interactive guided deployment flow for Azure OpenAI models with full customization control. |
| `/deploy-model` | [`deploy-model`](skills/cloud-and-infrastructure/deploy-model/SKILL.md) | Unified Azure OpenAI model deployment skill with intelligent intent-based routing. |
| `/deploy-to-vercel` | [`deploy-to-vercel`](skills/cloud-and-infrastructure/deploy-to-vercel/SKILL.md) | Deploy applications and websites to Vercel. |
| `/devops-rollout-plan` | [`devops-rollout-plan`](skills/cloud-and-infrastructure/devops-rollout-plan/SKILL.md) | Generate comprehensive rollout plans with preflight checks, step-by-step deployment, verification signals, rollback. |
| `/google-cloud-networking-observability` | [`google-cloud-networking-observability`](skills/cloud-and-infrastructure/google-cloud-networking-observability/SKILL.md) | Investigates Google Cloud networking issues by analyzing logs, metrics, and diagnostics. |
| `/google-cloud-recipe-onboarding` | [`google-cloud-recipe-onboarding`](skills/cloud-and-infrastructure/google-cloud-recipe-onboarding/SKILL.md) | Guidance for a developer's first steps on Google Cloud, covering account creation, billing setup, project management. |
| `/google-cloud-waf-cost-optimization` | [`google-cloud-waf-cost-optimization`](skills/cloud-and-infrastructure/google-cloud-waf-cost-optimization/SKILL.md) | Generates cost optimization guidance for Google Cloud workloads based on the Google Cloud Well-Architected Framework (WAF). |
| `/google-cloud-waf-performance-optimization` | [`google-cloud-waf-performance-optimization`](skills/cloud-and-infrastructure/google-cloud-waf-performance-optimization/SKILL.md) | Generates performance-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/google-cloud-waf-reliability` | [`google-cloud-waf-reliability`](skills/cloud-and-infrastructure/google-cloud-waf-reliability/SKILL.md) | Generates reliability-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/google-cloud-waf-sustainability` | [`google-cloud-waf-sustainability`](skills/cloud-and-infrastructure/google-cloud-waf-sustainability/SKILL.md) | Generates sustainability-focused guidance for Google Cloud workloads based on the design principles and recommendations. |
| `/gtm-enterprise-onboarding` | [`gtm-enterprise-onboarding`](skills/cloud-and-infrastructure/gtm-enterprise-onboarding/SKILL.md) | Four-phase framework for onboarding enterprise customers from contract to value realization. |
| `/hf-cli` | [`hf-cli`](skills/cloud-and-infrastructure/hf-cli/SKILL.md) | Hugging Face Hub CLI (`hf`) for downloading, uploading. |
| `/import-infrastructure-as-code` | [`import-infrastructure-as-code`](skills/cloud-and-infrastructure/import-infrastructure-as-code/SKILL.md) | Import existing Azure resources into Terraform using Azure CLI discovery and Azure Verified Modules (AVM). |
| `/pr-screenshots` | [`pr-screenshots`](skills/cloud-and-infrastructure/pr-screenshots/SKILL.md) | Embed before/after screenshots and annotated images in pull request descriptions. |
| `/preset` | [`preset`](skills/cloud-and-infrastructure/preset/SKILL.md) | Intelligently deploys Azure OpenAI models to optimal regions by analyzing capacity across all available regions. |
| `/python-azure-iot-edge-modules` | [`python-azure-iot-edge-modules`](skills/cloud-and-infrastructure/python-azure-iot-edge-modules/SKILL.md) | Build and operate Python Azure IoT Edge modules with robust messaging, deployment manifests, observability. |
| `/qdrant-deployment-options` | [`qdrant-deployment-options`](skills/cloud-and-infrastructure/qdrant-deployment-options/SKILL.md) | Guides Qdrant deployment selection. |
| `/qdrant-performance-optimization` | [`qdrant-performance-optimization`](skills/cloud-and-infrastructure/qdrant-performance-optimization/SKILL.md) | Different techniques to optimize the performance of Qdrant, including indexing strategies, query optimization. |
| `/shipping-and-launch` | [`shipping-and-launch`](skills/cloud-and-infrastructure/shipping-and-launch/SKILL.md) | Prepares production launches. Use when preparing to deploy to production. |
| `/terraform-azurerm-set-diff-analyzer` | [`terraform-azurerm-set-diff-analyzer`](skills/cloud-and-infrastructure/terraform-azurerm-set-diff-analyzer/SKILL.md) | Analyze Terraform plan JSON output for AzureRM Provider to distinguish between false-positive diffs (order-only changes. |
| `/update-avm-modules-in-bicep` | [`update-avm-modules-in-bicep`](skills/cloud-and-infrastructure/update-avm-modules-in-bicep/SKILL.md) | Update Azure Verified Modules (AVM) to latest versions in Bicep files. |
| `/wrangler` | [`wrangler`](skills/cloud-and-infrastructure/wrangler/SKILL.md) | Cloudflare Workers CLI for deploying, developing. |
| `/writing-skills` | [`writing-skills`](skills/cloud-and-infrastructure/writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment. |

---


## 🧬 Core Biology Development Paths

For developers working with our **Science & Bioinformatics** suite, the system supports a specialized pathway:
1. **Target Discovery & Retrieval**: Query UniProt IDs or NCBI sequences using `uniprot-database` and `ncbi-sequence-fetch`.
2. **Structural Modelling & Docking**: Fetch 3D coordinate files using `pdb-database` or structural search via `foldseek-structural-search`.
3. **Variant consequence analysis**: Assess effects on gene expression using `alphagenome-single-variant-analysis` and `gnomad-database`.

---

## ⚙️ System Requirements & Paths

To ensure optimal performance and seamless execution of all skills, verify that your local environment satisfies the following paths and dependencies:
*   **Node.js**: `v18.0.0` or higher (required for all custom MCP servers)
*   **Python**: `v3.10` or higher (required for all genomic and scientific analysis tools)
*   **Claude Configuration Path**: `~/.claude/skills/`
*   **Antigravity Workspace Directory**: `./skills/`

---

## 🤝 Support & Feedback

If you encounter any issues or have questions regarding skill loading, please open a GitHub Issue:
*   **GitHub Issues**: [aboalrejal-ai/skills/issues](https://github.com/aboalrejal-ai/skills/issues)
*   **Official Organization**: [github.com/aboalrejal-ai](https://github.com/aboalrejal-ai)

---

## 📄 License

This ecosystem is open-source software licensed under the [MIT License](LICENSE).
