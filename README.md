<p align="center">
  <img src="https://raw.githubusercontent.com/aboalrejal-ai/skills/main/assets/logo.png" alt="Abo Alrejal Skills Logo" width="120" style="border-radius: 50%" error="this.src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'"/>
</p>

# <p align="center">🌱 Unified Agent Skills Hub</p>

### <p align="center">*Build high-quality software faster.*</p>

<p align="center">
  *An open source library of 2993+ modular AI Skills, System Experts, and Developer Plugins that integrate with Claude Code, Antigravity, Cursor, and Windsurf.*
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

The **Unified Agent Skills Hub** (aboalrejal-ai/skills) is a premium, production-grade library containing **2993 modular skills, agent tools, and platform instructions**. 

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

Here is the fully cataloged list of all **2993 active skills** currently supported in the ecosystem. Every single skill is listed in a structured command table under its parent category.

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
| `/adhx` | [`adhx`](skills/ai-and-agents/adhx/SKILL.md) | Fetch any X/Twitter post as clean LLM-friendly JSON. |
| `/advanced-evaluation` | [`advanced-evaluation`](skills/ai-and-agents/advanced-evaluation/SKILL.md) | This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation. |
| `/aegisops-ai` | [`aegisops-ai`](skills/ai-and-agents/aegisops-ai/SKILL.md) | Autonomous DevSecOps & FinOps Guardrails. |
| `/agent-evaluation` | [`agent-evaluation`](skills/ai-and-agents/agent-evaluation/SKILL.md) | Testing and benchmarking LLM agents including behavioral testing,. |
| `/agent-framework-azure-ai-py` | [`agent-framework-azure-ai-py`](skills/ai-and-agents/agent-framework-azure-ai-py/SKILL.md) | Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). |
| `/agent-governance` | [`agent-governance`](skills/ai-and-agents/agent-governance/SKILL.md) | Patterns and techniques for adding governance, safety, and trust controls to AI agent systems. |
| `/agent-manager-skill` | [`agent-manager-skill`](skills/ai-and-agents/agent-manager-skill/SKILL.md) | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. |
| `/agent-memory-mcp` | [`agent-memory-mcp`](skills/ai-and-agents/agent-memory-mcp/SKILL.md) | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns,. |
| `/agent-memory-systems` | [`agent-memory-systems`](skills/ai-and-agents/agent-memory-systems/SKILL.md) | Memory is the cornerstone of intelligent agents. Without it, every. |
| `/agent-orchestration-improve-agent` | [`agent-orchestration-improve-agent`](skills/ai-and-agents/agent-orchestration-improve-agent/SKILL.md) | Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration. |
| `/agent-orchestration-multi-agent-optimize` | [`agent-orchestration-multi-agent-optimize`](skills/ai-and-agents/agent-orchestration-multi-agent-optimize/SKILL.md) | Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. |
| `/agent-orchestrator` | [`agent-orchestrator`](skills/ai-and-agents/agent-orchestrator/SKILL.md) | Meta-skill que orquestra todos os agentes do ecossistema. |
| `/agent-owasp-compliance` | [`agent-owasp-compliance`](skills/ai-and-agents/agent-owasp-compliance/SKILL.md) | Check any AI agent codebase against the OWASP Agentic Security Initiative (ASI) Top 10 risks. |
| `/agent-platform-deploy` | [`agent-platform-deploy`](skills/ai-and-agents/agent-platform-deploy/SKILL.md) | Deploy open models or custom weights from Model Garden to Agent Platform endpoints, check deployment status, verify. |
| `/agent-platform-prompt-management` | [`agent-platform-prompt-management`](skills/ai-and-agents/agent-platform-prompt-management/SKILL.md) | Manages and orchestrates prompts in Agent Platform. |
| `/agent-platform-rag-engine-management` | [`agent-platform-rag-engine-management`](skills/ai-and-agents/agent-platform-rag-engine-management/SKILL.md) | Manage and query Agent Platform RAG Engine Corpora and retrieve grounded contexts using the Google GenAI SDK. |
| `/agent-platform-skill-registry` | [`agent-platform-skill-registry`](skills/ai-and-agents/agent-platform-skill-registry/SKILL.md) | Interact with the Gemini Enterprise Agent Platform Skill Registry to create and search for available skills. |
| `/agent-platform-tuning` | [`agent-platform-tuning`](skills/ai-and-agents/agent-platform-tuning/SKILL.md) | Agent Platform Model Tuning. |
| `/agent-platform-tuning-management` | [`agent-platform-tuning-management`](skills/ai-and-agents/agent-platform-tuning-management/SKILL.md) | Manages GenAI tuning jobs in Agent Platform. Use this to list, get, or cancel ongoing model tuning jobs. |
| `/agent-supply-chain` | [`agent-supply-chain`](skills/ai-and-agents/agent-supply-chain/SKILL.md) | Verify supply chain integrity for AI agent plugins, tools, and dependencies. |
| `/agent-tool-builder` | [`agent-tool-builder`](skills/ai-and-agents/agent-tool-builder/SKILL.md) | Tools are how AI agents interact with the world. A well-designed. |
| `/agentflow` | [`agentflow`](skills/ai-and-agents/agentflow/SKILL.md) | Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). |
| `/agentfolio` | [`agentfolio`](skills/ai-and-agents/agentfolio/SKILL.md) | Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory. |
| `/agentic-actions-auditor` | [`agentic-actions-auditor`](skills/ai-and-agents/agentic-actions-auditor/SKILL.md) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action,. |
| `/agentic-eval` | [`agentic-eval`](skills/ai-and-agents/agentic-eval/SKILL.md) | Patterns and techniques for evaluating and improving AI agent outputs. |
| `/agentphone` | [`agentphone`](skills/ai-and-agents/agentphone/SKILL.md) | Build AI phone agents with AgentPhone API. |
| `/agentql-automation` | [`agentql-automation`](skills/ai-and-agents/agentql-automation/SKILL.md) | Automate Agentql tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agents-md` | [`agents-md`](skills/ai-and-agents/agents-md/SKILL.md) | This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up. |
| `/agents-sdk` | [`agents-sdk`](skills/ai-and-agents/agents-sdk/SKILL.md) | Build AI agents on Cloudflare Workers using the Agents SDK. |
| `/agents-v2-py` | [`agents-v2-py`](skills/ai-and-agents/agents-v2-py/SKILL.md) | Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). |
| `/agenttrace-session-audit` | [`agenttrace-session-audit`](skills/ai-and-agents/agenttrace-session-audit/SKILL.md) | Audit local AI coding-agent sessions with agenttrace for cost, tool failures, latency, anomalies, health, diffs, and CI gates. |
| `/agenty-automation` | [`agenty-automation`](skills/ai-and-agents/agenty-automation/SKILL.md) | Automate Agenty tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ai-agent-development` | [`ai-agent-development`](skills/ai-and-agents/ai-agent-development/SKILL.md) | AI agent development workflow for building autonomous agents, multi-agent systems. |
| `/ai-agents-architect` | [`ai-agents-architect`](skills/ai-and-agents/ai-agents-architect/SKILL.md) | Expert in designing and building autonomous AI agents. Masters tool. |
| `/ai-dev-jobs-mcp` | [`ai-dev-jobs-mcp`](skills/ai-and-agents/ai-dev-jobs-mcp/SKILL.md) | Search 8,400+ AI and ML jobs across 489 companies, inspect listings and employers, match roles. |
| `/ai-engineer` | [`ai-engineer`](skills/ai-and-agents/ai-engineer/SKILL.md) | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. |
| `/ai-engineering-toolkit` | [`ai-engineering-toolkit`](skills/ai-and-agents/ai-engineering-toolkit/SKILL.md) | 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG. |
| `/ai-md` | [`ai-md`](skills/ai-and-agents/ai-md/SKILL.md) | Convert human-written CLAUDE.md into AI-native structured-label format. |
| `/ai-ml` | [`ai-ml`](skills/ai-and-agents/ai-ml/SKILL.md) | AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML. |
| `/ai-native-cli` | [`ai-native-cli`](skills/ai-and-agents/ai-native-cli/SKILL.md) | Design spec with 98 rules for building CLI tools that AI agents can safely use. |
| `/ai-prompt-engineering-safety-review` | [`ai-prompt-engineering-safety-review`](skills/ai-and-agents/ai-prompt-engineering-safety-review/SKILL.md) | Comprehensive AI prompt engineering safety review and improvement prompt. |
| `/ai-ready` | [`ai-ready`](skills/ai-and-agents/ai-ready/SKILL.md) | Make any repo AI-ready — analyzes your codebase and generates AGENTS.md, copilot-instructions.md, CI workflows, issue. |
| `/ai-seo` | [`ai-seo`](skills/ai-and-agents/ai-seo/SKILL.md) | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. |
| `/ai-studio-image` | [`ai-studio-image`](skills/ai-and-agents/ai-studio-image/SKILL.md) | Geracao de imagens humanizadas via Google AI Studio (Gemini). |
| `/ai-team-orchestration` | [`ai-team-orchestration`](skills/ai-and-agents/ai-team-orchestration/SKILL.md) | Bootstrap and run a multi-agent AI development team. |
| `/ai-wrapper-product` | [`ai-wrapper-product`](skills/ai-and-agents/ai-wrapper-product/SKILL.md) | Expert in building products that wrap AI APIs (OpenAI, Anthropic,. |
| `/airunway-aks-setup` | [`airunway-aks-setup`](skills/ai-and-agents/airunway-aks-setup/SKILL.md) | Set up AI Runway on AKS — from bare cluster to running model. |
| `/analyze-project` | [`analyze-project`](skills/ai-and-agents/analyze-project/SKILL.md) | Forensic root cause analyzer for Antigravity sessions. |
| `/andrej-karpathy` | [`andrej-karpathy`](skills/ai-and-agents/andrej-karpathy/SKILL.md) | Behavioral guidelines to reduce common LLM coding mistakes. |
| `/anthropic-administrator-automation` | [`anthropic-administrator-automation`](skills/ai-and-agents/anthropic-administrator-automation/SKILL.md) | Automate Anthropic Admin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/anthropic_administrator-automation` | [`anthropic_administrator-automation`](skills/ai-and-agents/anthropic_administrator-automation/SKILL.md) | Automate Anthropic Admin tasks via Rube MCP (Composio): API keys, usage, workspaces, and organization management. |
| `/antigravity-skill-orchestrator` | [`antigravity-skill-orchestrator`](skills/ai-and-agents/antigravity-skill-orchestrator/SKILL.md) | A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill. |
| `/antigravity-workflows` | [`antigravity-workflows`](skills/ai-and-agents/antigravity-workflows/SKILL.md) | Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds. |
| `/aomi-transact` | [`aomi-transact`](skills/ai-and-agents/aomi-transact/SKILL.md) | Build natural-language crypto/DeFi agents and EVM MCP plugins (Claude Code, Cursor, Codex, Gemini). |
| `/arize-evaluator` | [`arize-evaluator`](skills/ai-and-agents/arize-evaluator/SKILL.md) | Handles LLM-as-judge evaluation workflows on Arize including creating/updating evaluators, running evaluations on spans. |
| `/arize-instrumentation` | [`arize-instrumentation`](skills/ai-and-agents/arize-instrumentation/SKILL.md) | Adds Arize AX tracing to an LLM application for the first time. |
| `/arize-prompt-optimization` | [`arize-prompt-optimization`](skills/ai-and-agents/arize-prompt-optimization/SKILL.md) | Optimizes, improves, and debugs LLM prompts using production trace data, evaluations, and annotations. |
| `/arize-trace` | [`arize-trace`](skills/ai-and-agents/arize-trace/SKILL.md) | Downloads, exports, and inspects existing Arize traces and spans to understand what an LLM app is doing or debug runtime issues. |
| `/audit-integrity` | [`audit-integrity`](skills/ai-and-agents/audit-integrity/SKILL.md) | Shared audit integrity framework for all AppSec agents — enforces output quality, intellectual honesty. |
| `/auri-core` | [`auri-core`](skills/ai-and-agents/auri-core/SKILL.md) | Auri: assistente de voz inteligente (Alexa + Claude claude-opus-4-20250805). |
| `/autonomous-agent-patterns` | [`autonomous-agent-patterns`](skills/ai-and-agents/autonomous-agent-patterns/SKILL.md) | Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI. |
| `/autonomous-agents` | [`autonomous-agents`](skills/ai-and-agents/autonomous-agents/SKILL.md) | Autonomous agents are AI systems that can independently decompose. |
| `/azure-ai-agents-persistent-dotnet` | [`azure-ai-agents-persistent-dotnet`](skills/ai-and-agents/azure-ai-agents-persistent-dotnet/SKILL.md) | Azure AI Agents Persistent SDK for .NET. |
| `/azure-ai-agents-persistent-java` | [`azure-ai-agents-persistent-java`](skills/ai-and-agents/azure-ai-agents-persistent-java/SKILL.md) | Azure AI Agents Persistent SDK for Java. |
| `/azure-ai-openai-dotnet` | [`azure-ai-openai-dotnet`](skills/ai-and-agents/azure-ai-openai-dotnet/SKILL.md) | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. |
| `/bdi-mental-states` | [`bdi-mental-states`](skills/ai-and-agents/bdi-mental-states/SKILL.md) | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create. |
| `/bill-gates` | [`bill-gates`](skills/ai-and-agents/bill-gates/SKILL.md) | Agente que simula Bill Gates — cofundador da Microsoft, arquiteto da industria de software comercial, estrategista. |
| `/blockrun` | [`blockrun`](skills/ai-and-agents/blockrun/SKILL.md) | BlockRun works with Claude Code and Google Antigravity. |
| `/boost-prompt` | [`boost-prompt`](skills/ai-and-agents/boost-prompt/SKILL.md) | Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to. |
| `/brand-guidelines-anthropic` | [`brand-guidelines-anthropic`](skills/ai-and-agents/brand-guidelines-anthropic/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| `/breakdown-epic-arch` | [`breakdown-epic-arch`](skills/ai-and-agents/breakdown-epic-arch/SKILL.md) | Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document. |
| `/breakdown-epic-pm` | [`breakdown-epic-pm`](skills/ai-and-agents/breakdown-epic-pm/SKILL.md) | Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. |
| `/breakdown-feature-implementation` | [`breakdown-feature-implementation`](skills/ai-and-agents/breakdown-feature-implementation/SKILL.md) | Prompt for creating detailed feature implementation plans, following Epoch monorepo structure. |
| `/breakdown-feature-prd` | [`breakdown-feature-prd`](skills/ai-and-agents/breakdown-feature-prd/SKILL.md) | Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic. |
| `/breakdown-plan` | [`breakdown-plan`](skills/ai-and-agents/breakdown-plan/SKILL.md) | Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler >. |
| `/breakdown-test` | [`breakdown-test`](skills/ai-and-agents/breakdown-test/SKILL.md) | Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns. |
| `/bullmq-specialist` | [`bullmq-specialist`](skills/ai-and-agents/bullmq-specialist/SKILL.md) | BullMQ expert for Redis-backed job queues, background processing,. |
| `/bumblebee` | [`bumblebee`](skills/ai-and-agents/bumblebee/SKILL.md) | Run Bumblebee supply-chain inventory and exposure scans on macOS/Linux to detect compromised packages, extensions. |
| `/buywhere-product-catalog` | [`buywhere-product-catalog`](skills/ai-and-agents/buywhere-product-catalog/SKILL.md) | Use BuyWhere's MCP and API surfaces to add product search, price comparison, and deal discovery to AI shopping agents. |
| `/cc-skill-continuous-learning` | [`cc-skill-continuous-learning`](skills/ai-and-agents/cc-skill-continuous-learning/SKILL.md) | Development skill from everything-claude-code. |
| `/cc-skill-strategic-compact` | [`cc-skill-strategic-compact`](skills/ai-and-agents/cc-skill-strategic-compact/SKILL.md) | Development skill from everything-claude-code. |
| `/chrome-devtools` | [`chrome-devtools`](skills/ai-and-agents/chrome-devtools/SKILL.md) | Expert-level browser automation, debugging, and performance analysis using Chrome DevTools MCP. |
| `/clarvia-aeo-check` | [`clarvia-aeo-check`](skills/ai-and-agents/clarvia-aeo-check/SKILL.md) | Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). |
| `/claude-ally-health` | [`claude-ally-health`](skills/ai-and-agents/claude-ally-health/SKILL.md) | A health assistant skill for medical information analysis, symptom tracking, and wellness guidance. |
| `/claude-api` | [`claude-api`](skills/ai-and-agents/claude-api/SKILL.md) | Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. |
| `/claude-code-expert` | [`claude-code-expert`](skills/ai-and-agents/claude-code-expert/SKILL.md) | Especialista profundo em Claude Code - CLI da Anthropic. |
| `/claude-code-guide` | [`claude-code-guide`](skills/ai-and-agents/claude-code-guide/SKILL.md) | To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. |
| `/claude-d3js-skill` | [`claude-d3js-skill`](skills/ai-and-agents/claude-d3js-skill/SKILL.md) | This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js. |
| `/claude-in-chrome-troubleshooting` | [`claude-in-chrome-troubleshooting`](skills/ai-and-agents/claude-in-chrome-troubleshooting/SKILL.md) | Diagnose and fix Claude in Chrome MCP extension connectivity issues. |
| `/claude-monitor` | [`claude-monitor`](skills/ai-and-agents/claude-monitor/SKILL.md) | Monitor de performance do Claude Code e sistema local. |
| `/claude-settings-audit` | [`claude-settings-audit`](skills/ai-and-agents/claude-settings-audit/SKILL.md) | Analyze a repository to generate recommended Claude Code settings.json permissions. |
| `/claude-speed-reader` | [`claude-speed-reader`](skills/ai-and-agents/claude-speed-reader/SKILL.md) | -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting. |
| `/claude-win11-speckit-update-skill` | [`claude-win11-speckit-update-skill`](skills/ai-and-agents/claude-win11-speckit-update-skill/SKILL.md) | Windows 11 system management. |
| `/cli-mastery` | [`cli-mastery`](skills/ai-and-agents/cli-mastery/SKILL.md) | Interactive training for the GitHub Copilot CLI. |
| `/code-review-ai-ai-review` | [`code-review-ai-ai-review`](skills/ai-and-agents/code-review-ai-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition. |
| `/code-review-and-quality` | [`code-review-and-quality`](skills/ai-and-agents/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. |
| `/code-testing-agent` | [`code-testing-agent`](skills/ai-and-agents/code-testing-agent/SKILL.md) | Generates and writes new unit tests for any programming language using a Research-Plan-Implement pipeline. |
| `/coding-agent` | [`coding-agent`](skills/ai-and-agents/coding-agent/SKILL.md) | Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. |
| `/computer-use-agents` | [`computer-use-agents`](skills/ai-and-agents/computer-use-agents/SKILL.md) | Build AI agents that interact with computers like humans do -. |
| `/conductor-setup` | [`conductor-setup`](skills/ai-and-agents/conductor-setup/SKILL.md) | Configure a Rails project to work with Conductor (parallel coding agents). |
| `/context-agent` | [`context-agent`](skills/ai-and-agents/context-agent/SKILL.md) | Agente de contexto para continuidade entre sessoes. |
| `/context-compression` | [`context-compression`](skills/ai-and-agents/context-compression/SKILL.md) | When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. |
| `/context-engineering` | [`context-engineering`](skills/ai-and-agents/context-engineering/SKILL.md) | Optimizes agent context setup. |
| `/context-window-management` | [`context-window-management`](skills/ai-and-agents/context-window-management/SKILL.md) | Strategies for managing LLM context windows including. |
| `/context7-auto-research` | [`context7-auto-research`](skills/ai-and-agents/context7-auto-research/SKILL.md) | Automatically fetch latest library/framework documentation for Claude Code via Context7 API. |
| `/continual-learning` | [`continual-learning`](skills/ai-and-agents/continual-learning/SKILL.md) | Guide for implementing continual learning in AI coding agents — hooks, memory scoping, reflection patterns. |
| `/conventional-commit` | [`conventional-commit`](skills/ai-and-agents/conventional-commit/SKILL.md) | Prompt and workflow for generating conventional commit messages using a structured XML format. |
| `/conversation-memory` | [`conversation-memory`](skills/ai-and-agents/conversation-memory/SKILL.md) | Persistent memory systems for LLM conversations including. |
| `/convert-plaintext-to-md` | [`convert-plaintext-to-md`](skills/ai-and-agents/convert-plaintext-to-md/SKILL.md) | Convert a text-based document to markdown following instructions from prompt. |
| `/create-agentsmd` | [`create-agentsmd`](skills/ai-and-agents/create-agentsmd/SKILL.md) | Prompt for generating an AGENTS.md file for a repository. |
| `/create-custom-agent` | [`create-custom-agent`](skills/ai-and-agents/create-custom-agent/SKILL.md) | Creates VS Code custom agent files (.agent.md) for specialized AI personas with tools, instructions, and handoffs. |
| `/create-llms` | [`create-llms`](skills/ai-and-agents/create-llms/SKILL.md) | Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/. |
| `/create-skill` | [`create-skill`](skills/ai-and-agents/create-skill/SKILL.md) | Scaffolds new agent skills for the dotnet/skills repository. |
| `/create-skill-test` | [`create-skill-test`](skills/ai-and-agents/create-skill-test/SKILL.md) | Scaffolds eval.yaml test files for agent skills in the dotnet/skills repository. |
| `/crewai` | [`crewai`](skills/ai-and-agents/crewai/SKILL.md) | Expert in CrewAI - the leading role-based multi-agent framework. |
| `/crypto-bd-agent` | [`crypto-bd-agent`](skills/ai-and-agents/crypto-bd-agent/SKILL.md) | Production-tested patterns for building AI agents that autonomously discover, > evaluate. |
| `/customgpt-automation` | [`customgpt-automation`](skills/ai-and-agents/customgpt-automation/SKILL.md) | Automate Customgpt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/data-engineering-data-driven-feature` | [`data-engineering-data-driven-feature`](skills/ai-and-agents/data-engineering-data-driven-feature/SKILL.md) | Build features guided by data insights, A/B testing. |
| `/data-structure-protocol` | [`data-structure-protocol`](skills/ai-and-agents/data-structure-protocol/SKILL.md) | Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs. |
| `/declarative-agents` | [`declarative-agents`](skills/ai-and-agents/declarative-agents/SKILL.md) | Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic,. |
| `/developer-growth-analysis` | [`developer-growth-analysis`](skills/ai-and-agents/developer-growth-analysis/SKILL.md) | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps. |
| `/diagnose` | [`diagnose`](skills/ai-and-agents/diagnose/SKILL.md) | Perform a systematic diagnostic scan of an AI workflow across 5 quality dimensions — prompt quality, context. |
| `/directory-submissions` | [`directory-submissions`](skills/ai-and-agents/directory-submissions/SKILL.md) | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code. |
| `/dispatching-parallel-agents` | [`dispatching-parallel-agents`](skills/ai-and-agents/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. |
| `/dotnet-mcp-builder` | [`dotnet-mcp-builder`](skills/ai-and-agents/dotnet-mcp-builder/SKILL.md) | Build Model Context Protocol (MCP) servers in C#/.NET against the current ModelContextProtocol 1.x NuGet packages. |
| `/ejentum-reasoning-harness` | [`ejentum-reasoning-harness`](skills/ai-and-agents/ejentum-reasoning-harness/SKILL.md) | MCP server exposing four cognitive harness modes (reasoning, code, anti-deception, memory). |
| `/elon-musk` | [`elon-musk`](skills/ai-and-agents/elon-musk/SKILL.md) | Agente que simula Elon Musk com profundidade psicologica e comunicacional de alta fidelidade. |
| `/emblemai-crypto-wallet` | [`emblemai-crypto-wallet`](skills/ai-and-agents/emblemai-crypto-wallet/SKILL.md) | Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. |
| `/enhance-prompt` | [`enhance-prompt`](skills/ai-and-agents/enhance-prompt/SKILL.md) | Transforms vague UI ideas into polished, Stitch-optimized prompts. |
| `/entra-agent-id` | [`entra-agent-id`](skills/ai-and-agents/entra-agent-id/SKILL.md) | Provision Microsoft Entra Agent Identity Blueprints, BlueprintPrincipals. |
| `/entra-agent-user` | [`entra-agent-user`](skills/ai-and-agents/entra-agent-user/SKILL.md) | Create Agent Users in Microsoft Entra ID from Agent Identities, enabling AI agents to act as digital workers with user. |
| `/error-debugging-multi-agent-review` | [`error-debugging-multi-agent-review`](skills/ai-and-agents/error-debugging-multi-agent-review/SKILL.md) | Use when working with error debugging multi agent review. |
| `/evaluation` | [`evaluation`](skills/ai-and-agents/evaluation/SKILL.md) | Build evaluation frameworks for agent systems. |
| `/faf-expert` | [`faf-expert`](skills/ai-and-agents/faf-expert/SKILL.md) | Advanced .faf (Foundational AI-context Format) specialist. |
| `/ffuf-claude-skill` | [`ffuf-claude-skill`](skills/ai-and-agents/ffuf-claude-skill/SKILL.md) | Web fuzzing with ffuf. |
| `/finalize-agent-prompt` | [`finalize-agent-prompt`](skills/ai-and-agents/finalize-agent-prompt/SKILL.md) | Finalize prompt file using the role of an AI agent to polish the prompt for the end user. |
| `/finetuning` | [`finetuning`](skills/ai-and-agents/finetuning/SKILL.md) | Fine-tune models on Azure AI Foundry using SFT (supervised), DPO (preference), or RFT (reinforcement with graders). |
| `/flowstudio-power-automate-mcp` | [`flowstudio-power-automate-mcp`](skills/ai-and-agents/flowstudio-power-automate-mcp/SKILL.md) | Foundation skill for Power Automate via FlowStudio MCP — auth setup, the reusable MCP helper (Python + Node.js), tool. |
| `/foundry-agent-sync` | [`foundry-agent-sync`](skills/ai-and-agents/foundry-agent-sync/SKILL.md) | Create and synchronize prompt-based AI agents directly within Azure AI Foundry via REST API, from a local JSON manifest. |
| `/gdb-cli` | [`gdb-cli`](skills/ai-and-agents/gdb-cli/SKILL.md) | GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks. |
| `/gemini` | [`gemini`](skills/ai-and-agents/gemini/SKILL.md) | Gemini CLI for one-shot Q&A, summaries, and generation. |
| `/gemini-agents-api` | [`gemini-agents-api`](skills/ai-and-agents/gemini-agents-api/SKILL.md) | Manages custom Agent resources on Gemini Enterprise Agent Platform. |
| `/gemini-api` | [`gemini-api`](skills/ai-and-agents/gemini-api/SKILL.md) | Guides the usage of the Gemini API on Agent Platform with the Google Gen AI SDK. |
| `/gemini-api-dev` | [`gemini-api-dev`](skills/ai-and-agents/gemini-api-dev/SKILL.md) | Use this skill when building applications with Gemini API hosted models, including Gemini and Gemma 4, working with. |
| `/gemini-automation` | [`gemini-automation`](skills/ai-and-agents/gemini-automation/SKILL.md) | Automate Gemini tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gemini-interactions-api` | [`gemini-interactions-api`](skills/ai-and-agents/gemini-interactions-api/SKILL.md) | Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal. |
| `/gemini-live-api-dev` | [`gemini-live-api-dev`](skills/ai-and-agents/gemini-live-api-dev/SKILL.md) | Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API. |
| `/geminiignore-finops` | [`geminiignore-finops`](skills/ai-and-agents/geminiignore-finops/SKILL.md) | Configure and optimize .geminiignore files for AI context window efficiency and token cost reduction (FinOps). |
| `/geo-fundamentals` | [`geo-fundamentals`](skills/ai-and-agents/geo-fundamentals/SKILL.md) | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| `/geoffrey-hinton` | [`geoffrey-hinton`](skills/ai-and-agents/geoffrey-hinton/SKILL.md) | Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, criador do backpropagation e das. |
| `/global-chat-agent-discovery` | [`global-chat-agent-discovery`](skills/ai-and-agents/global-chat-agent-discovery/SKILL.md) | Discover and search 18K+ MCP servers and AI agents across 6+ registries using Global Chat's cross-protocol directory. |
| `/gpt-taste` | [`gpt-taste`](skills/ai-and-agents/gpt-taste/SKILL.md) | Use when generating elite GSAP-heavy frontend pages with strict AIDA structure, wide hero typography, and gapless bento grids. |
| `/gtm-ai-gtm` | [`gtm-ai-gtm`](skills/ai-and-agents/gtm-ai-gtm/SKILL.md) | Go-to-market strategy for AI products. |
| `/helium-mcp` | [`helium-mcp`](skills/ai-and-agents/helium-mcp/SKILL.md) | Connect to Helium's MCP server for news research, media bias analysis, balanced perspectives, stock/options data. |
| `/hf-mcp` | [`hf-mcp`](skills/ai-and-agents/hf-mcp/SKILL.md) | Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. |
| `/hierarchical-agent-memory` | [`hierarchical-agent-memory`](skills/ai-and-agents/hierarchical-agent-memory/SKILL.md) | Scoped CLAUDE.md memory system that reduces context token spend. |
| `/hig-inputs` | [`hig-inputs`](skills/ai-and-agents/hig-inputs/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. |
| `/hig-technologies` | [`hig-technologies`](skills/ai-and-agents/hig-technologies/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. |
| `/hosted-agents` | [`hosted-agents`](skills/ai-and-agents/hosted-agents/SKILL.md) | Build background agents in sandboxed environments. |
| `/hosted-agents-v2-py` | [`hosted-agents-v2-py`](skills/ai-and-agents/hosted-agents-v2-py/SKILL.md) | Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. |
| `/hugging-face-datasets` | [`hugging-face-datasets`](skills/ai-and-agents/hugging-face-datasets/SKILL.md) | Create and manage datasets on Hugging Face Hub. |
| `/hugging-face-evaluation` | [`hugging-face-evaluation`](skills/ai-and-agents/hugging-face-evaluation/SKILL.md) | Add and manage evaluation results in Hugging Face model cards. |
| `/huggingface-community-evals` | [`huggingface-community-evals`](skills/ai-and-agents/huggingface-community-evals/SKILL.md) | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. |
| `/huggingface-llm-trainer` | [`huggingface-llm-trainer`](skills/ai-and-agents/huggingface-llm-trainer/SKILL.md) | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging. |
| `/huggingface-local-models` | [`huggingface-local-models`](skills/ai-and-agents/huggingface-local-models/SKILL.md) | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. |
| `/huggingface-vision-trainer` | [`huggingface-vision-trainer`](skills/ai-and-agents/huggingface-vision-trainer/SKILL.md) | Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm. |
| `/ilya-sutskever` | [`ilya-sutskever`](skills/ai-and-agents/ilya-sutskever/SKILL.md) | Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. |
| `/infinite-gratitude` | [`infinite-gratitude`](skills/ai-and-agents/infinite-gratitude/SKILL.md) | Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies). |
| `/jobgpt` | [`jobgpt`](skills/ai-and-agents/jobgpt/SKILL.md) | Job search automation, auto apply, resume generation, application tracking, salary intelligence. |
| `/kotlin-mcp-server-generator` | [`kotlin-mcp-server-generator`](skills/ai-and-agents/kotlin-mcp-server-generator/SKILL.md) | Generate a complete Kotlin MCP server project with proper structure, dependencies. |
| `/kubestellar-console` | [`kubestellar-console`](skills/ai-and-agents/kubestellar-console/SKILL.md) | Multi-cluster Kubernetes dashboard with AI-powered operations via MCP server and 10+ built-in agent skills. |
| `/langchain-architecture` | [`langchain-architecture`](skills/ai-and-agents/langchain-architecture/SKILL.md) | Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration. |
| `/langfuse` | [`langfuse`](skills/ai-and-agents/langfuse/SKILL.md) | Expert in Langfuse - the open-source LLM observability platform. |
| `/langsmith-fetch` | [`langsmith-fetch`](skills/ai-and-agents/langsmith-fetch/SKILL.md) | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. |
| `/last30days` | [`last30days`](skills/ai-and-agents/last30days/SKILL.md) | Research a topic from the last 30 days on Reddit + X + Web, become an expert. |
| `/linear-claude-skill` | [`linear-claude-skill`](skills/ai-and-agents/linear-claude-skill/SKILL.md) | Manage Linear issues, projects, and teams. |
| `/llm-app-patterns` | [`llm-app-patterns`](skills/ai-and-agents/llm-app-patterns/SKILL.md) | Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and. |
| `/llm-application-dev-ai-assistant` | [`llm-application-dev-ai-assistant`](skills/ai-and-agents/llm-application-dev-ai-assistant/SKILL.md) | You are an AI assistant development expert specializing in creating intelligent conversational interfaces, chatbots. |
| `/llm-application-dev-langchain-agent` | [`llm-application-dev-langchain-agent`](skills/ai-and-agents/llm-application-dev-langchain-agent/SKILL.md) | You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph. |
| `/llm-application-dev-prompt-optimize` | [`llm-application-dev-prompt-optimize`](skills/ai-and-agents/llm-application-dev-prompt-optimize/SKILL.md) | You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques. |
| `/llm-evaluation` | [`llm-evaluation`](skills/ai-and-agents/llm-evaluation/SKILL.md) | Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing. |
| `/llm-ops` | [`llm-ops`](skills/ai-and-agents/llm-ops/SKILL.md) | LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de. |
| `/llm-prompt-optimizer` | [`llm-prompt-optimizer`](skills/ai-and-agents/llm-prompt-optimizer/SKILL.md) | Use when improving prompts for any LLM. |
| `/llm-structured-output` | [`llm-structured-output`](skills/ai-and-agents/llm-structured-output/SKILL.md) | Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding. |
| `/local-llm-expert` | [`local-llm-expert`](skills/ai-and-agents/local-llm-expert/SKILL.md) | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. |
| `/logic-lens` | [`logic-lens`](skills/ai-and-agents/logic-lens/SKILL.md) | AI-powered Claude Code skill that performs deep code review using formal logic and reasoning frameworks to detect bugs,. |
| `/loki-mode` | [`loki-mode`](skills/ai-and-agents/loki-mode/SKILL.md) | Version 2.35.0 \| PRD to Production \| Zero Human Intervention > Research-enhanced: OpenAI SDK, DeepMind, Anthropic, AWS. |
| `/longbridge` | [`longbridge`](skills/ai-and-agents/longbridge/SKILL.md) | 125+ agent skills for Longbridge Securities — real-time quotes, charts, fundamentals, portfolio analysis, options. |
| `/m365-agents-dotnet` | [`m365-agents-dotnet`](skills/ai-and-agents/m365-agents-dotnet/SKILL.md) | Microsoft 365 Agents SDK for .NET. |
| `/m365-agents-py` | [`m365-agents-py`](skills/ai-and-agents/m365-agents-py/SKILL.md) | Microsoft 365 Agents SDK for Python. |
| `/m365-agents-ts` | [`m365-agents-ts`](skills/ai-and-agents/m365-agents-ts/SKILL.md) | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| `/manage-skills` | [`manage-skills`](skills/ai-and-agents/manage-skills/SKILL.md) | Discover, list, create, edit, toggle, copy, move. |
| `/manifest` | [`manifest`](skills/ai-and-agents/manifest/SKILL.md) | Install and configure the Manifest observability plugin for your agents. |
| `/maxia` | [`maxia`](skills/ai-and-agents/maxia/SKILL.md) | Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. |
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
| `/mcp-tool-developer` | [`mcp-tool-developer`](skills/ai-and-agents/mcp-tool-developer/SKILL.md) | Build Model Context Protocol (MCP) servers and tools from scratch. |
| `/memory-systems` | [`memory-systems`](skills/ai-and-agents/memory-systems/SKILL.md) | Design short-term, long-term, and graph-based memory architectures. |
| `/mercury-mcp` | [`mercury-mcp`](skills/ai-and-agents/mercury-mcp/SKILL.md) | Cheatsheet for the Mercury (proton) MCP tools. |
| `/mesh-memory` | [`mesh-memory`](skills/ai-and-agents/mesh-memory/SKILL.md) | Self-hosted semantic memory for AI agents via MCP. |
| `/microsoft-agent-framework` | [`microsoft-agent-framework`](skills/ai-and-agents/microsoft-agent-framework/SKILL.md) | Create, update, refactor, explain, or review Microsoft Agent Framework solutions using shared guidance plus. |
| `/mock-hunter` | [`mock-hunter`](skills/ai-and-agents/mock-hunter/SKILL.md) | Audit a live web page in five phases (catalog, click, trace, classify, report) to identify mock data, hardcoded values,. |
| `/molykit` | [`molykit`](skills/ai-and-agents/molykit/SKILL.md) | CRITICAL: Use for MolyKit AI chat toolkit. |
| `/monte-carlo-monitor-creation` | [`monte-carlo-monitor-creation`](skills/ai-and-agents/monte-carlo-monitor-creation/SKILL.md) | Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code YAML for CI/CD deployment. |
| `/moyu` | [`moyu`](skills/ai-and-agents/moyu/SKILL.md) | Anti-over-engineering guardrail that activates when an AI coding agent expands scope, adds abstractions. |
| `/multi-advisor` | [`multi-advisor`](skills/ai-and-agents/multi-advisor/SKILL.md) | Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de. |
| `/multi-agent-architect` | [`multi-agent-architect`](skills/ai-and-agents/multi-agent-architect/SKILL.md) | Design and optimize production-grade multi-agent systems with LangGraph, LangChain, and DeepAgents for complex AI workflows. |
| `/multi-agent-brainstorming` | [`multi-agent-brainstorming`](skills/ai-and-agents/multi-agent-brainstorming/SKILL.md) | Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden. |
| `/multi-agent-patterns` | [`multi-agent-patterns`](skills/ai-and-agents/multi-agent-patterns/SKILL.md) | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create. |
| `/multi-agent-task-orchestrator` | [`multi-agent-task-orchestrator`](skills/ai-and-agents/multi-agent-task-orchestrator/SKILL.md) | Route tasks to specialized AI agents with anti-duplication, quality gates, and 30-minute heartbeat monitoring. |
| `/n8n-agents` | [`n8n-agents`](skills/ai-and-agents/n8n-agents/SKILL.md) | Advanced n8n management and workflow automation agent. |
| `/n8n-mcp-tools-expert` | [`n8n-mcp-tools-expert`](skills/ai-and-agents/n8n-mcp-tools-expert/SKILL.md) | Expert guide for using n8n-mcp MCP tools effectively. |
| `/nano-banana-pro-openrouter` | [`nano-banana-pro-openrouter`](skills/ai-and-agents/nano-banana-pro-openrouter/SKILL.md) | Generate or edit images via OpenRouter with the Gemini 3 Pro Image model. |
| `/nerdzao-elite-gemini-high` | [`nerdzao-elite-gemini-high`](skills/ai-and-agents/nerdzao-elite-gemini-high/SKILL.md) | Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. |
| `/news-sentiment-engine` | [`news-sentiment-engine`](skills/ai-and-agents/news-sentiment-engine/SKILL.md) | Multi-source RSS news aggregation with Claude-powered sentiment analysis and structured briefing output. |
| `/noob-mode` | [`noob-mode`](skills/ai-and-agents/noob-mode/SKILL.md) | Plain-English translation layer for non-technical Copilot CLI users. |
| `/not-human-search-mcp` | [`not-human-search-mcp`](skills/ai-and-agents/not-human-search-mcp/SKILL.md) | Search AI-ready websites, inspect indexed site details, verify MCP endpoints. |
| `/notebooklm` | [`notebooklm`](skills/ai-and-agents/notebooklm/SKILL.md) | Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. |
| `/odoo-ecommerce-configurator` | [`odoo-ecommerce-configurator`](skills/ai-and-agents/odoo-ecommerce-configurator/SKILL.md) | Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO. |
| `/onboard-context-matic` | [`onboard-context-matic`](skills/ai-and-agents/onboard-context-matic/SKILL.md) | Interactive onboarding tour for the context-matic MCP server. |
| `/parallel-agents` | [`parallel-agents`](skills/ai-and-agents/parallel-agents/SKILL.md) | Multi-agent orchestration patterns. |
| `/performance-testing-review-multi-agent-review` | [`performance-testing-review-multi-agent-review`](skills/ai-and-agents/performance-testing-review-multi-agent-review/SKILL.md) | Use when working with performance testing review multi agent review. |
| `/phoenix-cli` | [`phoenix-cli`](skills/ai-and-agents/phoenix-cli/SKILL.md) | Debug LLM applications using the Phoenix CLI. |
| `/phoenix-evals` | [`phoenix-evals`](skills/ai-and-agents/phoenix-evals/SKILL.md) | Build and run evaluators for AI/LLM applications using Phoenix. |
| `/phoenix-tracing` | [`phoenix-tracing`](skills/ai-and-agents/phoenix-tracing/SKILL.md) | OpenInference semantic conventions and instrumentation for Phoenix AI observability. |
| `/pipecat-friday-agent` | [`pipecat-friday-agent`](skills/ai-and-agents/pipecat-friday-agent/SKILL.md) | Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI. |
| `/playwright-explore-website` | [`playwright-explore-website`](skills/ai-and-agents/playwright-explore-website/SKILL.md) | Website exploration for testing using Playwright MCP. |
| `/power-bi-dax-optimization` | [`power-bi-dax-optimization`](skills/ai-and-agents/power-bi-dax-optimization/SKILL.md) | Comprehensive Power BI DAX formula optimization prompt for improving performance, readability. |
| `/power-bi-performance-troubleshooting` | [`power-bi-performance-troubleshooting`](skills/ai-and-agents/power-bi-performance-troubleshooting/SKILL.md) | Systematic Power BI performance troubleshooting prompt for identifying, diagnosing. |
| `/power-platform-mcp-connector-suite` | [`power-platform-mcp-connector-suite`](skills/ai-and-agents/power-platform-mcp-connector-suite/SKILL.md) | Generate complete Power Platform custom connector with MCP integration for Copilot Studio - includes schema generation,. |
| `/powerbi-modeling` | [`powerbi-modeling`](skills/ai-and-agents/powerbi-modeling/SKILL.md) | Power BI semantic modeling assistant for building optimized data models. |
| `/ppt-orchestra-skill` | [`ppt-orchestra-skill`](skills/ai-and-agents/ppt-orchestra-skill/SKILL.md) | Plan and orchestrate multi-slide PowerPoint creation from scratch. |
| `/product-manager` | [`product-manager`](skills/ai-and-agents/product-manager/SKILL.md) | Senior PM agent with 6 knowledge domains, 30+ frameworks, 12 templates, and 32 SaaS metrics with formulas. |
| `/progressive-estimation` | [`progressive-estimation`](skills/ai-and-agents/progressive-estimation/SKILL.md) | Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops. |
| `/project-development` | [`project-development`](skills/ai-and-agents/project-development/SKILL.md) | This skill covers the principles for identifying tasks suited to LLM processing, designing effective project. |
| `/prompt-caching` | [`prompt-caching`](skills/ai-and-agents/prompt-caching/SKILL.md) | Caching strategies for LLM prompts including Anthropic prompt. |
| `/prompt-engineer` | [`prompt-engineer`](skills/ai-and-agents/prompt-engineer/SKILL.md) | Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density,. |
| `/prompt-engineering` | [`prompt-engineering`](skills/ai-and-agents/prompt-engineering/SKILL.md) | Expert guide on prompt engineering patterns, best practices, and optimization techniques. |
| `/prompt-engineering-patterns` | [`prompt-engineering-patterns`](skills/ai-and-agents/prompt-engineering-patterns/SKILL.md) | Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability. |
| `/prompt-library` | [`prompt-library`](skills/ai-and-agents/prompt-library/SKILL.md) | A comprehensive collection of battle-tested prompts inspired by. |
| `/prompt-optimizer` | [`prompt-optimizer`](skills/ai-and-agents/prompt-optimizer/SKILL.md) | Turn any rough prompt, half-formed idea, or task description into a finished, ready-to-send prompt optimized for any. |
| `/protect-mcp-governance` | [`protect-mcp-governance`](skills/ai-and-agents/protect-mcp-governance/SKILL.md) | Agent governance skill for MCP tool calls — Cedar policy authoring, shadow-to-enforce rollout, and Ed25519 receipt verification. |
| `/pydantic-ai` | [`pydantic-ai`](skills/ai-and-agents/pydantic-ai/SKILL.md) | Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection. |
| `/recallmax` | [`recallmax`](skills/ai-and-agents/recallmax/SKILL.md) | FREE — God-tier long-context memory for AI agents. |
| `/recursive-context-pruning-token-budgeting` | [`recursive-context-pruning-token-budgeting`](skills/ai-and-agents/recursive-context-pruning-token-budgeting/SKILL.md) | Optimizes AI agent performance by pruning redundant context, managing token usage. |
| `/remember-interactive-programming` | [`remember-interactive-programming`](skills/ai-and-agents/remember-interactive-programming/SKILL.md) | A micro-prompt that reminds the agent that it is an interactive programmer. |
| `/ruby-mcp-server-generator` | [`ruby-mcp-server-generator`](skills/ai-and-agents/ruby-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Ruby using the official MCP Ruby SDK gem. |
| `/sam-altman` | [`sam-altman`](skills/ai-and-agents/sam-altman/SKILL.md) | Agente que simula Sam Altman — CEO da OpenAI, ex-presidente da Y Combinator, arquiteto da era AGI. |
| `/schema-markup` | [`schema-markup`](skills/ai-and-agents/schema-markup/SKILL.md) | When the user wants to add, fix, or optimize schema markup and structured data on their site. |
| `/secret-scanning` | [`secret-scanning`](skills/ai-and-agents/secret-scanning/SKILL.md) | Guide for configuring and managing GitHub secret scanning, push protection, custom patterns, and secret alert remediation. |
| `/seo-agent` | [`seo-agent`](skills/ai-and-agents/seo-agent/SKILL.md) | Automates and optimizes workflows for Seo Agent. |
| `/skill-audit` | [`skill-audit`](skills/ai-and-agents/skill-audit/SKILL.md) | Pre-install security scanner for AI agent skills. 7.5% of 14,706 skills are malicious. |
| `/skill-check` | [`skill-check`](skills/ai-and-agents/skill-check/SKILL.md) | Validate Claude Code skills against the agentskills specification. |
| `/skill-creator` | [`skill-creator`](skills/ai-and-agents/skill-creator/SKILL.md) | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. |
| `/skill-creator-ms` | [`skill-creator-ms`](skills/ai-and-agents/skill-creator-ms/SKILL.md) | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. |
| `/skill-developer` | [`skill-developer`](skills/ai-and-agents/skill-developer/SKILL.md) | Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's. |
| `/skill-improver` | [`skill-improver`](skills/ai-and-agents/skill-improver/SKILL.md) | Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. |
| `/skill-optimizer` | [`skill-optimizer`](skills/ai-and-agents/skill-optimizer/SKILL.md) | Diagnose and optimize Agent Skills (SKILL.md) with real session data and research-backed static analysis. |
| `/skill-scanner` | [`skill-scanner`](skills/ai-and-agents/skill-scanner/SKILL.md) | Scan agent skills for security issues before adoption. |
| `/skill-share` | [`skill-share`](skills/ai-and-agents/skill-share/SKILL.md) | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team. |
| `/skill-writer` | [`skill-writer`](skills/ai-and-agents/skill-writer/SKILL.md) | Create and improve agent skills following the Agent Skills specification. |
| `/socialclaw` | [`socialclaw`](skills/ai-and-agents/socialclaw/SKILL.md) | Agent-first social media publishing skill — schedule and publish posts across 13 platforms (X, LinkedIn, Instagram,. |
| `/steve-jobs` | [`steve-jobs`](skills/ai-and-agents/steve-jobs/SKILL.md) | Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos. |
| `/stitch-loop` | [`stitch-loop`](skills/ai-and-agents/stitch-loop/SKILL.md) | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern. |
| `/structured-autonomy-implement` | [`structured-autonomy-implement`](skills/ai-and-agents/structured-autonomy-implement/SKILL.md) | Structured Autonomy Implementation Prompt. |
| `/structured-autonomy-plan` | [`structured-autonomy-plan`](skills/ai-and-agents/structured-autonomy-plan/SKILL.md) | Structured Autonomy Planning Prompt. |
| `/subagent-driven-development` | [`subagent-driven-development`](skills/ai-and-agents/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session. |
| `/subagent-orchestrator` | [`subagent-orchestrator`](skills/ai-and-agents/subagent-orchestrator/SKILL.md) | Coordinate quota-aware parallel subagents for large, multi-file Antigravity tasks. |
| `/suggest-awesome-github-copilot-agents` | [`suggest-awesome-github-copilot-agents`](skills/ai-and-agents/suggest-awesome-github-copilot-agents/SKILL.md) | Suggest relevant GitHub Copilot Custom Agents files from the awesome-copilot repository based on current repository. |
| `/superpowers-lab` | [`superpowers-lab`](skills/ai-and-agents/superpowers-lab/SKILL.md) | Lab environment for Claude superpowers. |
| `/swift-mcp-server-generator` | [`swift-mcp-server-generator`](skills/ai-and-agents/swift-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Swift using the official MCP Swift SDK package. |
| `/task-intelligence` | [`task-intelligence`](skills/ai-and-agents/task-intelligence/SKILL.md) | Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes do ecossistema ANTES de executar qualquer. |
| `/tdd-orchestrator` | [`tdd-orchestrator`](skills/ai-and-agents/tdd-orchestrator/SKILL.md) | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination. |
| `/technology-selection` | [`technology-selection`](skills/ai-and-agents/technology-selection/SKILL.md) | Guides technology selection and implementation of AI and ML features in .NET 8+ applications using ML.NET,. |
| `/template-skill` | [`template-skill`](skills/ai-and-agents/template-skill/SKILL.md) | Replace with description of the skill and when Claude should use it. |
| `/tldr-prompt` | [`tldr-prompt`](skills/ai-and-agents/tldr-prompt/SKILL.md) | Create tldr summaries for GitHub Copilot files (prompts, agents, instructions, collections), MCP servers. |
| `/tokenwise` | [`tokenwise`](skills/ai-and-agents/tokenwise/SKILL.md) | Measurement-driven model router for Claude Code. |
| `/typescript-mcp-server-generator` | [`typescript-mcp-server-generator`](skills/ai-and-agents/typescript-mcp-server-generator/SKILL.md) | Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration. |
| `/typespec-create-agent` | [`typespec-create-agent`](skills/ai-and-agents/typespec-create-agent/SKILL.md) | Generate a complete TypeSpec declarative agent with instructions, capabilities. |
| `/unity-ai-game-creator` | [`unity-ai-game-creator`](skills/ai-and-agents/unity-ai-game-creator/SKILL.md) | Transform raw game ideas into complete Unity projects with AI-powered asset generation, scene blueprints, music/SFX. |
| `/update-llms` | [`update-llms`](skills/ai-and-agents/update-llms/SKILL.md) | Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the. |
| `/using-agent-skills` | [`using-agent-skills`](skills/ai-and-agents/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. |
| `/v0-automation` | [`v0-automation`](skills/ai-and-agents/v0-automation/SKILL.md) | Automate V0 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/varlock` | [`varlock`](skills/ai-and-agents/varlock/SKILL.md) | Secure-by-default environment variable management for Claude Code sessions. |
| `/varlock-claude-skill` | [`varlock-claude-skill`](skills/ai-and-agents/varlock-claude-skill/SKILL.md) | Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits. |
| `/vexor` | [`vexor`](skills/ai-and-agents/vexor/SKILL.md) | Vector-powered CLI for semantic file search with a Claude/Codex skill. |
| `/voice-agents` | [`voice-agents`](skills/ai-and-agents/voice-agents/SKILL.md) | Voice agents represent the frontier of AI interaction - humans. |
| `/warren-buffett` | [`warren-buffett`](skills/ai-and-agents/warren-buffett/SKILL.md) | Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, CEO da Berkshire Hathaway, discipulo de. |
| `/wiki-agents-md` | [`wiki-agents-md`](skills/ai-and-agents/wiki-agents-md/SKILL.md) | Generates AGENTS.md files for repository folders — coding agent context files with build commands, testing. |
| `/workiq-copilot` | [`workiq-copilot`](skills/ai-and-agents/workiq-copilot/SKILL.md) | Guides the Copilot CLI on how to use the WorkIQ CLI/MCP server to query Microsoft 365 Copilot data (emails, meetings,. |
| `/write-coding-standards-from-file` | [`write-coding-standards-from-file`](skills/ai-and-agents/write-coding-standards-from-file/SKILL.md) | Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as. |
| `/xvary-stock-research` | [`xvary-stock-research`](skills/ai-and-agents/xvary-stock-research/SKILL.md) | Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled. |
| `/yann-lecun` | [`yann-lecun`](skills/ai-and-agents/yann-lecun/SKILL.md) | Agente que simula Yann LeCun — inventor das Convolutional Neural Networks, Chief AI Scientist da Meta, Prêmio Turing 2018. |
| `/yann-lecun-debate` | [`yann-lecun-debate`](skills/ai-and-agents/yann-lecun-debate/SKILL.md) | Sub-skill de debates e posições de Yann LeCun. |
| `/zipai-optimizer` | [`zipai-optimizer`](skills/ai-and-agents/zipai-optimizer/SKILL.md) | Adaptive token optimizer: intelligent filtering, surgical output, ambiguity-first, context-window-aware, VCS-aware, MCP-aware. |

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
| `/activecampaign-automation` | [`activecampaign-automation`](skills/automation-and-saas/activecampaign-automation/SKILL.md) | Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment. |
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
| `/agentmail` | [`agentmail`](skills/automation-and-saas/agentmail/SKILL.md) | Email infrastructure for AI agents. |
| `/agiled-automation` | [`agiled-automation`](skills/automation-and-saas/agiled-automation/SKILL.md) | Automate Agiled tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/agility-cms-automation` | [`agility-cms-automation`](skills/automation-and-saas/agility-cms-automation/SKILL.md) | Automate Agility CMS tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ai-ml-api-automation` | [`ai-ml-api-automation`](skills/automation-and-saas/ai-ml-api-automation/SKILL.md) | Automate AI ML API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/airtable-automation` | [`airtable-automation`](skills/automation-and-saas/airtable-automation/SKILL.md) | Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. |
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
| `/amplitude-automation` | [`amplitude-automation`](skills/automation-and-saas/amplitude-automation/SKILL.md) | Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. |
| `/anchor-browser-automation` | [`anchor-browser-automation`](skills/automation-and-saas/anchor-browser-automation/SKILL.md) | Automate Anchor Browser tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/anonyflow-automation` | [`anonyflow-automation`](skills/automation-and-saas/anonyflow-automation/SKILL.md) | Automate Anonyflow tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apaleo-automation` | [`apaleo-automation`](skills/automation-and-saas/apaleo-automation/SKILL.md) | Automate Apaleo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apex27-automation` | [`apex27-automation`](skills/automation-and-saas/apex27-automation/SKILL.md) | Automate Apex27 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-and-interface-design` | [`api-and-interface-design`](skills/automation-and-saas/api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. |
| `/api-bible-automation` | [`api-bible-automation`](skills/automation-and-saas/api-bible-automation/SKILL.md) | Automate API Bible tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-design-principles` | [`api-design-principles`](skills/automation-and-saas/api-design-principles/SKILL.md) | Master REST and GraphQL API design principles to build intuitive, scalable. |
| `/api-documentation` | [`api-documentation`](skills/automation-and-saas/api-documentation/SKILL.md) | API documentation workflow for generating OpenAPI specs, creating developer guides. |
| `/api-documentation-generator` | [`api-documentation-generator`](skills/automation-and-saas/api-documentation-generator/SKILL.md) | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples. |
| `/api-documenter` | [`api-documenter`](skills/automation-and-saas/api-documenter/SKILL.md) | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. |
| `/api-endpoint-builder` | [`api-endpoint-builder`](skills/automation-and-saas/api-endpoint-builder/SKILL.md) | Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. |
| `/api-fuzzing-bug-bounty` | [`api-fuzzing-bug-bounty`](skills/automation-and-saas/api-fuzzing-bug-bounty/SKILL.md) | Provide comprehensive techniques for testing REST, SOAP. |
| `/api-labz-automation` | [`api-labz-automation`](skills/automation-and-saas/api-labz-automation/SKILL.md) | Automate API Labz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-ninjas-automation` | [`api-ninjas-automation`](skills/automation-and-saas/api-ninjas-automation/SKILL.md) | Automate API Ninjas tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-patterns` | [`api-patterns`](skills/automation-and-saas/api-patterns/SKILL.md) | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| `/api-security-best-practices` | [`api-security-best-practices`](skills/automation-and-saas/api-security-best-practices/SKILL.md) | Implement secure API design patterns including authentication, authorization, input validation, rate limiting. |
| `/api-sports-automation` | [`api-sports-automation`](skills/automation-and-saas/api-sports-automation/SKILL.md) | Automate API Sports tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/api-testing-observability-api-mock` | [`api-testing-observability-api-mock`](skills/automation-and-saas/api-testing-observability-api-mock/SKILL.md) | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. |
| `/api2pdf-automation` | [`api2pdf-automation`](skills/automation-and-saas/api2pdf-automation/SKILL.md) | Automate Api2pdf tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apiflash-automation` | [`apiflash-automation`](skills/automation-and-saas/apiflash-automation/SKILL.md) | Automate Apiflash tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/apify-actor-development` | [`apify-actor-development`](skills/automation-and-saas/apify-actor-development/SKILL.md) | Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json. |
| `/apify-actorization` | [`apify-actorization`](skills/automation-and-saas/apify-actorization/SKILL.md) | Actorization converts existing software into reusable serverless applications compatible with the Apify platform. |
| `/apify-brand-reputation-monitoring` | [`apify-brand-reputation-monitoring`](skills/automation-and-saas/apify-brand-reputation-monitoring/SKILL.md) | Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors. |
| `/apify-ecommerce` | [`apify-ecommerce`](skills/automation-and-saas/apify-ecommerce/SKILL.md) | Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool. |
| `/apify-influencer-discovery` | [`apify-influencer-discovery`](skills/automation-and-saas/apify-influencer-discovery/SKILL.md) | Find and evaluate influencers for brand partnerships, verify authenticity. |
| `/apify-lead-generation` | [`apify-lead-generation`](skills/automation-and-saas/apify-lead-generation/SKILL.md) | Scrape leads from multiple platforms using Apify Actors. |
| `/apify-market-research` | [`apify-market-research`](skills/automation-and-saas/apify-market-research/SKILL.md) | Analyze market conditions, geographic opportunities, pricing, consumer behavior. |
| `/apify-trend-analysis` | [`apify-trend-analysis`](skills/automation-and-saas/apify-trend-analysis/SKILL.md) | Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy. |
| `/apify-ultimate-scraper` | [`apify-ultimate-scraper`](skills/automation-and-saas/apify-ultimate-scraper/SKILL.md) | AI-driven data extraction from 55+ Actors across all major platforms. |
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
| `/asana-automation` | [`asana-automation`](skills/automation-and-saas/asana-automation/SKILL.md) | Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. |
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
| `/bamboohr-automation` | [`bamboohr-automation`](skills/automation-and-saas/bamboohr-automation/SKILL.md) | Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. |
| `/bannerbear-automation` | [`bannerbear-automation`](skills/automation-and-saas/bannerbear-automation/SKILL.md) | Automate Bannerbear tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bart-automation` | [`bart-automation`](skills/automation-and-saas/bart-automation/SKILL.md) | Automate Bart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/basecamp-automation` | [`basecamp-automation`](skills/automation-and-saas/basecamp-automation/SKILL.md) | Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). |
| `/baselinker-automation` | [`baselinker-automation`](skills/automation-and-saas/baselinker-automation/SKILL.md) | Automate Baselinker tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/baserow-automation` | [`baserow-automation`](skills/automation-and-saas/baserow-automation/SKILL.md) | Automate Baserow tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/basin-automation` | [`basin-automation`](skills/automation-and-saas/basin-automation/SKILL.md) | Automate Basin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/batch-files` | [`batch-files`](skills/automation-and-saas/batch-files/SKILL.md) | Expert-level Windows batch file (.bat/.cmd) skill for writing, debugging, and maintaining CMD scripts. |
| `/battlenet-automation` | [`battlenet-automation`](skills/automation-and-saas/battlenet-automation/SKILL.md) | Automate Battlenet tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bdistill-behavioral-xray` | [`bdistill-behavioral-xray`](skills/automation-and-saas/bdistill-behavioral-xray/SKILL.md) | X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. |
| `/bdistill-knowledge-extraction` | [`bdistill-knowledge-extraction`](skills/automation-and-saas/bdistill-knowledge-extraction/SKILL.md) | Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. |
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
| `/billing-automation` | [`billing-automation`](skills/automation-and-saas/billing-automation/SKILL.md) | Master automated billing systems including recurring billing, invoice generation, dunning management, proration. |
| `/bitbucket-automation` | [`bitbucket-automation`](skills/automation-and-saas/bitbucket-automation/SKILL.md) | Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). |
| `/bitquery-automation` | [`bitquery-automation`](skills/automation-and-saas/bitquery-automation/SKILL.md) | Automate Bitquery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/bitwarden-automation` | [`bitwarden-automation`](skills/automation-and-saas/bitwarden-automation/SKILL.md) | Automate Bitwarden tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blackbaud-automation` | [`blackbaud-automation`](skills/automation-and-saas/blackbaud-automation/SKILL.md) | Automate Blackbaud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blackboard-automation` | [`blackboard-automation`](skills/automation-and-saas/blackboard-automation/SKILL.md) | Automate Blackboard tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/blockchain-developer` | [`blockchain-developer`](skills/automation-and-saas/blockchain-developer/SKILL.md) | Build production-ready Web3 applications, smart contracts, and decentralized systems. |
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
| `/box-automation` | [`box-automation`](skills/automation-and-saas/box-automation/SKILL.md) | Automate Box operations including file upload/download, content search, folder management, collaboration, metadata. |
| `/boxhero-automation` | [`boxhero-automation`](skills/automation-and-saas/boxhero-automation/SKILL.md) | Automate Boxhero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brandfetch-automation` | [`brandfetch-automation`](skills/automation-and-saas/brandfetch-automation/SKILL.md) | Automate Brandfetch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/breeze-automation` | [`breeze-automation`](skills/automation-and-saas/breeze-automation/SKILL.md) | Automate Breeze tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/breezy-hr-automation` | [`breezy-hr-automation`](skills/automation-and-saas/breezy-hr-automation/SKILL.md) | Automate Breezy HR tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brevo-automation` | [`brevo-automation`](skills/automation-and-saas/brevo-automation/SKILL.md) | Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP. |
| `/brex-automation` | [`brex-automation`](skills/automation-and-saas/brex-automation/SKILL.md) | Automate Brex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brex-staging-automation` | [`brex-staging-automation`](skills/automation-and-saas/brex-staging-automation/SKILL.md) | Automate Brex Staging tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brightdata-automation` | [`brightdata-automation`](skills/automation-and-saas/brightdata-automation/SKILL.md) | Automate Brightdata tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brightpearl-automation` | [`brightpearl-automation`](skills/automation-and-saas/brightpearl-automation/SKILL.md) | Automate Brightpearl tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/brilliant-directories-automation` | [`brilliant-directories-automation`](skills/automation-and-saas/brilliant-directories-automation/SKILL.md) | Automate Brilliant Directories tasks via Rube MCP (Composio). |
| `/browseai-automation` | [`browseai-automation`](skills/automation-and-saas/browseai-automation/SKILL.md) | Automate Browseai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/browser-automation` | [`browser-automation`](skills/automation-and-saas/browser-automation/SKILL.md) | Browser automation powers web testing, scraping, and AI agent. |
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
| `/cal-com-automation` | [`cal-com-automation`](skills/automation-and-saas/cal-com-automation/SKILL.md) | Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. |
| `/calendarhero-automation` | [`calendarhero-automation`](skills/automation-and-saas/calendarhero-automation/SKILL.md) | Automate Calendarhero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/calendly-automation` | [`calendly-automation`](skills/automation-and-saas/calendly-automation/SKILL.md) | Automate Calendly scheduling, event management, invitee tracking, availability checks. |
| `/callerapi-automation` | [`callerapi-automation`](skills/automation-and-saas/callerapi-automation/SKILL.md) | Automate Callerapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/callingly-automation` | [`callingly-automation`](skills/automation-and-saas/callingly-automation/SKILL.md) | Automate Callingly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/callpage-automation` | [`callpage-automation`](skills/automation-and-saas/callpage-automation/SKILL.md) | Automate Callpage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/campaign-cleaner-automation` | [`campaign-cleaner-automation`](skills/automation-and-saas/campaign-cleaner-automation/SKILL.md) | Automate Campaign Cleaner tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/campayn-automation` | [`campayn-automation`](skills/automation-and-saas/campayn-automation/SKILL.md) | Automate Campayn tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/canny-automation` | [`canny-automation`](skills/automation-and-saas/canny-automation/SKILL.md) | Automate Canny tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/canva-automation` | [`canva-automation`](skills/automation-and-saas/canva-automation/SKILL.md) | Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. |
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
| `/changelog-automation` | [`changelog-automation`](skills/automation-and-saas/changelog-automation/SKILL.md) | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. |
| `/chaser-automation` | [`chaser-automation`](skills/automation-and-saas/chaser-automation/SKILL.md) | Automate Chaser tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatbotkit-automation` | [`chatbotkit-automation`](skills/automation-and-saas/chatbotkit-automation/SKILL.md) | Automate Chatbotkit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatfai-automation` | [`chatfai-automation`](skills/automation-and-saas/chatfai-automation/SKILL.md) | Automate Chatfai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chatwork-automation` | [`chatwork-automation`](skills/automation-and-saas/chatwork-automation/SKILL.md) | Automate Chatwork tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/chmeetings-automation` | [`chmeetings-automation`](skills/automation-and-saas/chmeetings-automation/SKILL.md) | Automate Chmeetings tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ci-cd-and-automation` | [`ci-cd-and-automation`](skills/automation-and-saas/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. |
| `/cicd-automation-workflow-automate` | [`cicd-automation-workflow-automate`](skills/automation-and-saas/cicd-automation-workflow-automate/SKILL.md) | You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows. |
| `/cincopa-automation` | [`cincopa-automation`](skills/automation-and-saas/cincopa-automation/SKILL.md) | Automate Cincopa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/circleci-automation` | [`circleci-automation`](skills/automation-and-saas/circleci-automation/SKILL.md) | Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. |
| `/claid-ai-automation` | [`claid-ai-automation`](skills/automation-and-saas/claid-ai-automation/SKILL.md) | Automate Claid AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/classmarker-automation` | [`classmarker-automation`](skills/automation-and-saas/classmarker-automation/SKILL.md) | Automate Classmarker tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/clearout-automation` | [`clearout-automation`](skills/automation-and-saas/clearout-automation/SKILL.md) | Automate Clearout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/clickmeeting-automation` | [`clickmeeting-automation`](skills/automation-and-saas/clickmeeting-automation/SKILL.md) | Automate Clickmeeting tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/clickup-automation` | [`clickup-automation`](skills/automation-and-saas/clickup-automation/SKILL.md) | Automate ClickUp project management including tasks, spaces, folders, lists, comments. |
| `/close-automation` | [`close-automation`](skills/automation-and-saas/close-automation/SKILL.md) | Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. |
| `/cloudcart-automation` | [`cloudcart-automation`](skills/automation-and-saas/cloudcart-automation/SKILL.md) | Automate Cloudcart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudconvert-automation` | [`cloudconvert-automation`](skills/automation-and-saas/cloudconvert-automation/SKILL.md) | Automate Cloudconvert tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-api-key-automation` | [`cloudflare-api-key-automation`](skills/automation-and-saas/cloudflare-api-key-automation/SKILL.md) | Automate Cloudflare API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-automation` | [`cloudflare-automation`](skills/automation-and-saas/cloudflare-automation/SKILL.md) | Automate Cloudflare tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudflare-browser-rendering-automation` | [`cloudflare-browser-rendering-automation`](skills/automation-and-saas/cloudflare-browser-rendering-automation/SKILL.md) | Automate Cloudflare Browser Rendering tasks via Rube MCP (Composio). |
| `/cloudflare-email-service` | [`cloudflare-email-service`](skills/automation-and-saas/cloudflare-email-service/SKILL.md) | Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing). |
| `/cloudlayer-automation` | [`cloudlayer-automation`](skills/automation-and-saas/cloudlayer-automation/SKILL.md) | Automate Cloudlayer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/cloudpress-automation` | [`cloudpress-automation`](skills/automation-and-saas/cloudpress-automation/SKILL.md) | Automate Cloudpress tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coassemble-automation` | [`coassemble-automation`](skills/automation-and-saas/coassemble-automation/SKILL.md) | Automate Coassemble tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coda-automation` | [`coda-automation`](skills/automation-and-saas/coda-automation/SKILL.md) | Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. |
| `/codacy-automation` | [`codacy-automation`](skills/automation-and-saas/codacy-automation/SKILL.md) | Automate Codacy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/codeinterpreter-automation` | [`codeinterpreter-automation`](skills/automation-and-saas/codeinterpreter-automation/SKILL.md) | Automate Codeinterpreter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/codereadr-automation` | [`codereadr-automation`](skills/automation-and-saas/codereadr-automation/SKILL.md) | Automate Codereadr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinmarketcal-automation` | [`coinmarketcal-automation`](skills/automation-and-saas/coinmarketcal-automation/SKILL.md) | Automate Coinmarketcal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinmarketcap-automation` | [`coinmarketcap-automation`](skills/automation-and-saas/coinmarketcap-automation/SKILL.md) | Automate Coinmarketcap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/coinranking-automation` | [`coinranking-automation`](skills/automation-and-saas/coinranking-automation/SKILL.md) | Automate Coinranking tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/college-football-data-automation` | [`college-football-data-automation`](skills/automation-and-saas/college-football-data-automation/SKILL.md) | Automate College Football Data tasks via Rube MCP (Composio). |
| `/composio-automation` | [`composio-automation`](skills/automation-and-saas/composio-automation/SKILL.md) | Automate Composio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/composio-search-automation` | [`composio-search-automation`](skills/automation-and-saas/composio-search-automation/SKILL.md) | Automate Composio Search tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/confluence-automation` | [`confluence-automation`](skills/automation-and-saas/confluence-automation/SKILL.md) | Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). |
| `/connect` | [`connect`](skills/automation-and-saas/connect/SKILL.md) | Connect Claude to any app. |
| `/connect-apps` | [`connect-apps`](skills/automation-and-saas/connect-apps/SKILL.md) | Connect Claude to external apps like Gmail, Slack, GitHub. |
| `/connecteam-automation` | [`connecteam-automation`](skills/automation-and-saas/connecteam-automation/SKILL.md) | Automate Connecteam tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/content-management-systems` | [`content-management-systems`](skills/automation-and-saas/content-management-systems/SKILL.md) | Workflow for building and modifying content management systems across WordPress, Shopify, Wix, Squarespace, Drupal,. |
| `/contentful-graphql-automation` | [`contentful-graphql-automation`](skills/automation-and-saas/contentful-graphql-automation/SKILL.md) | Automate Contentful Graphql tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/control-d-automation` | [`control-d-automation`](skills/automation-and-saas/control-d-automation/SKILL.md) | Automate Control D tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/conversion-tools-automation` | [`conversion-tools-automation`](skills/automation-and-saas/conversion-tools-automation/SKILL.md) | Automate Conversion Tools tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/convertapi-automation` | [`convertapi-automation`](skills/automation-and-saas/convertapi-automation/SKILL.md) | Automate Convertapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/convertkit-automation` | [`convertkit-automation`](skills/automation-and-saas/convertkit-automation/SKILL.md) | Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. |
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
| `/datadog-automation` | [`datadog-automation`](skills/automation-and-saas/datadog-automation/SKILL.md) | Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events. |
| `/datagma-automation` | [`datagma-automation`](skills/automation-and-saas/datagma-automation/SKILL.md) | Automate Datagma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/datarobot-automation` | [`datarobot-automation`](skills/automation-and-saas/datarobot-automation/SKILL.md) | Automate Datarobot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ddd-context-mapping` | [`ddd-context-mapping`](skills/automation-and-saas/ddd-context-mapping/SKILL.md) | Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns. |
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
| `/discord-automation` | [`discord-automation`](skills/automation-and-saas/discord-automation/SKILL.md) | Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. |
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
| `/docusign-automation` | [`docusign-automation`](skills/automation-and-saas/docusign-automation/SKILL.md) | Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. |
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
| `/dropbox-automation` | [`dropbox-automation`](skills/automation-and-saas/dropbox-automation/SKILL.md) | Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). |
| `/dropbox-sign-automation` | [`dropbox-sign-automation`](skills/automation-and-saas/dropbox-sign-automation/SKILL.md) | Automate Dropbox Sign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dropcontact-automation` | [`dropcontact-automation`](skills/automation-and-saas/dropcontact-automation/SKILL.md) | Automate Dropcontact tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/dungeon-fighter-online-automation` | [`dungeon-fighter-online-automation`](skills/automation-and-saas/dungeon-fighter-online-automation/SKILL.md) | Automate Dungeon Fighter Online tasks via Rube MCP (Composio). |
| `/echtpost-automation` | [`echtpost-automation`](skills/automation-and-saas/echtpost-automation/SKILL.md) | Automate Echtpost tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/elorus-automation` | [`elorus-automation`](skills/automation-and-saas/elorus-automation/SKILL.md) | Automate Elorus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/email-drafter` | [`email-drafter`](skills/automation-and-saas/email-drafter/SKILL.md) | Draft and review professional emails that match your personal writing style. |
| `/email-systems` | [`email-systems`](skills/automation-and-saas/email-systems/SKILL.md) | Email has the highest ROI of any marketing channel. $36 for every. |
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
| `/exa-search` | [`exa-search`](skills/automation-and-saas/exa-search/SKILL.md) | Semantic search, similar content discovery, and structured research using Exa API. |
| `/exist-automation` | [`exist-automation`](skills/automation-and-saas/exist-automation/SKILL.md) | Automate Exist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/exp-simd-vectorization` | [`exp-simd-vectorization`](skills/automation-and-saas/exp-simd-vectorization/SKILL.md) | Optimizes hot-path scalar loops in .NET 8+ with cross-platform Vector128/Vector256/Vector512 SIMD intrinsics. |
| `/expo-api-routes` | [`expo-api-routes`](skills/automation-and-saas/expo-api-routes/SKILL.md) | Guidelines for creating API routes in Expo Router with EAS Hosting. |
| `/expofp-automation` | [`expofp-automation`](skills/automation-and-saas/expofp-automation/SKILL.md) | Automate Expofp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/extracta-ai-automation` | [`extracta-ai-automation`](skills/automation-and-saas/extracta-ai-automation/SKILL.md) | Automate Extracta AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/faceup-automation` | [`faceup-automation`](skills/automation-and-saas/faceup-automation/SKILL.md) | Automate Faceup tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/factorial-automation` | [`factorial-automation`](skills/automation-and-saas/factorial-automation/SKILL.md) | Automate Factorial tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fal-platform` | [`fal-platform`](skills/automation-and-saas/fal-platform/SKILL.md) | Platform APIs for model management, pricing, and usage tracking. |
| `/fastapi-pro` | [`fastapi-pro`](skills/automation-and-saas/fastapi-pro/SKILL.md) | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. |
| `/fastapi-router-py` | [`fastapi-router-py`](skills/automation-and-saas/fastapi-router-py/SKILL.md) | Create FastAPI routers with CRUD operations, authentication dependencies, and proper response models. |
| `/fastapi-templates` | [`fastapi-templates`](skills/automation-and-saas/fastapi-templates/SKILL.md) | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. |
| `/feathery-automation` | [`feathery-automation`](skills/automation-and-saas/feathery-automation/SKILL.md) | Automate Feathery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/felt-automation` | [`felt-automation`](skills/automation-and-saas/felt-automation/SKILL.md) | Automate Felt tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fibery-automation` | [`fibery-automation`](skills/automation-and-saas/fibery-automation/SKILL.md) | Automate Fibery tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fidel-api-automation` | [`fidel-api-automation`](skills/automation-and-saas/fidel-api-automation/SKILL.md) | Automate Fidel API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/figma-automation` | [`figma-automation`](skills/automation-and-saas/figma-automation/SKILL.md) | Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. |
| `/files-com-automation` | [`files-com-automation`](skills/automation-and-saas/files-com-automation/SKILL.md) | Automate Files Com tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fillout-forms-automation` | [`fillout-forms-automation`](skills/automation-and-saas/fillout-forms-automation/SKILL.md) | Automate Fillout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fillout_forms-automation` | [`fillout_forms-automation`](skills/automation-and-saas/fillout_forms-automation/SKILL.md) | Automate Fillout tasks via Rube MCP (Composio): forms, submissions, workflows, and form builder. |
| `/finage-automation` | [`finage-automation`](skills/automation-and-saas/finage-automation/SKILL.md) | Automate Finage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/findymail-automation` | [`findymail-automation`](skills/automation-and-saas/findymail-automation/SKILL.md) | Automate Findymail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/finerworks-automation` | [`finerworks-automation`](skills/automation-and-saas/finerworks-automation/SKILL.md) | Automate Finerworks tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fingertip-automation` | [`fingertip-automation`](skills/automation-and-saas/fingertip-automation/SKILL.md) | Automate Fingertip tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/finmei-automation` | [`finmei-automation`](skills/automation-and-saas/finmei-automation/SKILL.md) | Automate Finmei tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fireberry-automation` | [`fireberry-automation`](skills/automation-and-saas/fireberry-automation/SKILL.md) | Automate Fireberry tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/firecrawl-scraper` | [`firecrawl-scraper`](skills/automation-and-saas/firecrawl-scraper/SKILL.md) | Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API. |
| `/fireflies-automation` | [`fireflies-automation`](skills/automation-and-saas/fireflies-automation/SKILL.md) | Automate Fireflies tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/firmao-automation` | [`firmao-automation`](skills/automation-and-saas/firmao-automation/SKILL.md) | Automate Firmao tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fitbit-automation` | [`fitbit-automation`](skills/automation-and-saas/fitbit-automation/SKILL.md) | Automate Fitbit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fixer-automation` | [`fixer-automation`](skills/automation-and-saas/fixer-automation/SKILL.md) | Automate Fixer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/fixer-io-automation` | [`fixer-io-automation`](skills/automation-and-saas/fixer-io-automation/SKILL.md) | Automate Fixer IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/flexisign-automation` | [`flexisign-automation`](skills/automation-and-saas/flexisign-automation/SKILL.md) | Automate Flexisign tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/flowhunt-skill` | [`flowhunt-skill`](skills/automation-and-saas/flowhunt-skill/SKILL.md) | Automation discovery audit skill. |
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
| `/fp-async` | [`fp-async`](skills/automation-and-saas/fp-async/SKILL.md) | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples. |
| `/fp-taskeither-ref` | [`fp-taskeither-ref`](skills/automation-and-saas/fp-taskeither-ref/SKILL.md) | Quick reference for TaskEither. |
| `/fraudlabs-pro-automation` | [`fraudlabs-pro-automation`](skills/automation-and-saas/fraudlabs-pro-automation/SKILL.md) | Automate Fraudlabs Pro tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/freecad-scripts` | [`freecad-scripts`](skills/automation-and-saas/freecad-scripts/SKILL.md) | Expert skill for writing FreeCAD Python scripts, macros, and automation. |
| `/freshdesk-automation` | [`freshdesk-automation`](skills/automation-and-saas/freshdesk-automation/SKILL.md) | Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). |
| `/freshservice-automation` | [`freshservice-automation`](skills/automation-and-saas/freshservice-automation/SKILL.md) | Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests. |
| `/front-automation` | [`front-automation`](skills/automation-and-saas/front-automation/SKILL.md) | Automate Front tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/frontend-api-integration-patterns` | [`frontend-api-integration-patterns`](skills/automation-and-saas/frontend-api-integration-patterns/SKILL.md) | Production-ready patterns for integrating frontend applications with backend APIs, including race condition handling,. |
| `/fullenrich-automation` | [`fullenrich-automation`](skills/automation-and-saas/fullenrich-automation/SKILL.md) | Automate Fullenrich tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gagelist-automation` | [`gagelist-automation`](skills/automation-and-saas/gagelist-automation/SKILL.md) | Automate Gagelist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gamma-automation` | [`gamma-automation`](skills/automation-and-saas/gamma-automation/SKILL.md) | Automate Gamma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gan-ai-automation` | [`gan-ai-automation`](skills/automation-and-saas/gan-ai-automation/SKILL.md) | Automate Gan AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gatherup-automation` | [`gatherup-automation`](skills/automation-and-saas/gatherup-automation/SKILL.md) | Automate Gatherup tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gemini-api-integration` | [`gemini-api-integration`](skills/automation-and-saas/gemini-api-integration/SKILL.md) | Use when integrating Google Gemini API into projects. |
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
| `/github-automation` | [`github-automation`](skills/automation-and-saas/github-automation/SKILL.md) | Automate GitHub repositories, issues, pull requests, branches, CI/CD, and permissions via Rube MCP (Composio). |
| `/gitlab-automation` | [`gitlab-automation`](skills/automation-and-saas/gitlab-automation/SKILL.md) | Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). |
| `/givebutter-automation` | [`givebutter-automation`](skills/automation-and-saas/givebutter-automation/SKILL.md) | Automate Givebutter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gke-basics` | [`gke-basics`](skills/automation-and-saas/gke-basics/SKILL.md) | Plan, create, and configure production-ready Google Kubernetes Engine (GKE) clusters using the golden path Autopilot. |
| `/gladia-automation` | [`gladia-automation`](skills/automation-and-saas/gladia-automation/SKILL.md) | Automate Gladia tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gleap-automation` | [`gleap-automation`](skills/automation-and-saas/gleap-automation/SKILL.md) | Automate Gleap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/globalping-automation` | [`globalping-automation`](skills/automation-and-saas/globalping-automation/SKILL.md) | Automate Globalping tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gmail-automation` | [`gmail-automation`](skills/automation-and-saas/gmail-automation/SKILL.md) | Lightweight Gmail integration with standalone OAuth authentication. |
| `/go-playwright` | [`go-playwright`](skills/automation-and-saas/go-playwright/SKILL.md) | Expert capability for robust, stealthy, and efficient browser automation using Playwright Go. |
| `/go-rod-master` | [`go-rod-master`](skills/automation-and-saas/go-rod-master/SKILL.md) | Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth. |
| `/go-to-webinar-automation` | [`go-to-webinar-automation`](skills/automation-and-saas/go-to-webinar-automation/SKILL.md) | Automate GoToWebinar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/godial-automation` | [`godial-automation`](skills/automation-and-saas/godial-automation/SKILL.md) | Automate Godial tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/gog` | [`gog`](skills/automation-and-saas/gog/SKILL.md) | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. |
| `/goodbits-automation` | [`goodbits-automation`](skills/automation-and-saas/goodbits-automation/SKILL.md) | Automate Goodbits tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/goody-automation` | [`goody-automation`](skills/automation-and-saas/goody-automation/SKILL.md) | Automate Goody tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-address-validation-automation` | [`google-address-validation-automation`](skills/automation-and-saas/google-address-validation-automation/SKILL.md) | Automate Google Address Validation tasks via Rube MCP (Composio). |
| `/google-admin-automation` | [`google-admin-automation`](skills/automation-and-saas/google-admin-automation/SKILL.md) | Automate Google Workspace Admin tasks via Rube MCP (Composio): manage users, groups, memberships, suspend accounts,. |
| `/google-calendar-automation` | [`google-calendar-automation`](skills/automation-and-saas/google-calendar-automation/SKILL.md) | Lightweight Google Calendar integration with standalone OAuth authentication. |
| `/google-classroom-automation` | [`google-classroom-automation`](skills/automation-and-saas/google-classroom-automation/SKILL.md) | Automate Google Classroom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-cloud-vision-automation` | [`google-cloud-vision-automation`](skills/automation-and-saas/google-cloud-vision-automation/SKILL.md) | Automate Google Cloud Vision tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/google-docs-automation` | [`google-docs-automation`](skills/automation-and-saas/google-docs-automation/SKILL.md) | Lightweight Google Docs integration with standalone OAuth authentication. |
| `/google-drive-automation` | [`google-drive-automation`](skills/automation-and-saas/google-drive-automation/SKILL.md) | Lightweight Google Drive integration with standalone OAuth authentication. |
| `/google-maps-automation` | [`google-maps-automation`](skills/automation-and-saas/google-maps-automation/SKILL.md) | Automate Google Maps tasks via Rube MCP (Composio): geocode addresses, search places, get directions, compute route. |
| `/google-search-console-automation` | [`google-search-console-automation`](skills/automation-and-saas/google-search-console-automation/SKILL.md) | Automate Google Search Console tasks via Rube MCP (Composio): query search analytics, list sites, inspect URLs, submit. |
| `/google-sheets-automation` | [`google-sheets-automation`](skills/automation-and-saas/google-sheets-automation/SKILL.md) | Lightweight Google Sheets integration with standalone OAuth authentication. |
| `/google-slides-automation` | [`google-slides-automation`](skills/automation-and-saas/google-slides-automation/SKILL.md) | Lightweight Google Slides integration with standalone OAuth authentication. |
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
| `/helpdesk-automation` | [`helpdesk-automation`](skills/automation-and-saas/helpdesk-automation/SKILL.md) | Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. |
| `/helpwise-automation` | [`helpwise-automation`](skills/automation-and-saas/helpwise-automation/SKILL.md) | Automate Helpwise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/here-automation` | [`here-automation`](skills/automation-and-saas/here-automation/SKILL.md) | Automate Here tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/heyreach-automation` | [`heyreach-automation`](skills/automation-and-saas/heyreach-automation/SKILL.md) | Automate Heyreach tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/heyzine-automation` | [`heyzine-automation`](skills/automation-and-saas/heyzine-automation/SKILL.md) | Automate Heyzine tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/highergov-automation` | [`highergov-automation`](skills/automation-and-saas/highergov-automation/SKILL.md) | Automate Highergov tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/highlevel-automation` | [`highlevel-automation`](skills/automation-and-saas/highlevel-automation/SKILL.md) | Automate Highlevel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/honeybadger-automation` | [`honeybadger-automation`](skills/automation-and-saas/honeybadger-automation/SKILL.md) | Automate Honeybadger tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/honeyhive-automation` | [`honeyhive-automation`](skills/automation-and-saas/honeyhive-automation/SKILL.md) | Automate Honeyhive tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hono` | [`hono`](skills/automation-and-saas/hono/SKILL.md) | Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js. |
| `/hookdeck-automation` | [`hookdeck-automation`](skills/automation-and-saas/hookdeck-automation/SKILL.md) | Automate Hookdeck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hotspotsystem-automation` | [`hotspotsystem-automation`](skills/automation-and-saas/hotspotsystem-automation/SKILL.md) | Automate Hotspotsystem tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/html-to-image-automation` | [`html-to-image-automation`](skills/automation-and-saas/html-to-image-automation/SKILL.md) | Automate Html To Image tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/hubspot-automation` | [`hubspot-automation`](skills/automation-and-saas/hubspot-automation/SKILL.md) | Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration. |
| `/hubspot-integration` | [`hubspot-integration`](skills/automation-and-saas/hubspot-integration/SKILL.md) | Expert patterns for HubSpot CRM integration including OAuth. |
| `/hugging-face-dataset-viewer` | [`hugging-face-dataset-viewer`](skills/automation-and-saas/hugging-face-dataset-viewer/SKILL.md) | Query Hugging Face datasets through the Dataset Viewer API for splits, rows, search, filters, and parquet links. |
| `/hugging-face-papers` | [`hugging-face-papers`](skills/automation-and-saas/hugging-face-papers/SKILL.md) | Read and analyze Hugging Face paper pages or arXiv papers with markdown and papers API metadata. |
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
| `/incident-responder` | [`incident-responder`](skills/automation-and-saas/incident-responder/SKILL.md) | Expert SRE incident responder specializing in rapid problem resolution, modern observability. |
| `/influxdb-cloud-automation` | [`influxdb-cloud-automation`](skills/automation-and-saas/influxdb-cloud-automation/SKILL.md) | Automate Influxdb Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/insighto-ai-automation` | [`insighto-ai-automation`](skills/automation-and-saas/insighto-ai-automation/SKILL.md) | Automate Insighto AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/instacart-automation` | [`instacart-automation`](skills/automation-and-saas/instacart-automation/SKILL.md) | Automate Instacart tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/instagram` | [`instagram`](skills/automation-and-saas/instagram/SKILL.md) | Integracao completa com Instagram via Graph API. |
| `/instagram-automation` | [`instagram-automation`](skills/automation-and-saas/instagram-automation/SKILL.md) | Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. |
| `/integrate-context-matic` | [`integrate-context-matic`](skills/automation-and-saas/integrate-context-matic/SKILL.md) | Discovers and integrates third-party APIs using the context-matic MCP server. |
| `/intelliprint-automation` | [`intelliprint-automation`](skills/automation-and-saas/intelliprint-automation/SKILL.md) | Automate Intelliprint tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/intercom-automation` | [`intercom-automation`](skills/automation-and-saas/intercom-automation/SKILL.md) | Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. |
| `/interzoid-automation` | [`interzoid-automation`](skills/automation-and-saas/interzoid-automation/SKILL.md) | Automate Interzoid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2location-automation` | [`ip2location-automation`](skills/automation-and-saas/ip2location-automation/SKILL.md) | Automate Ip2location tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2location-io-automation` | [`ip2location-io-automation`](skills/automation-and-saas/ip2location-io-automation/SKILL.md) | Automate Ip2location IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2proxy-automation` | [`ip2proxy-automation`](skills/automation-and-saas/ip2proxy-automation/SKILL.md) | Automate Ip2proxy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ip2whois-automation` | [`ip2whois-automation`](skills/automation-and-saas/ip2whois-automation/SKILL.md) | Automate Ip2whois tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ipdata-co-automation` | [`ipdata-co-automation`](skills/automation-and-saas/ipdata-co-automation/SKILL.md) | Automate Ipdata co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ipinfo-io-automation` | [`ipinfo-io-automation`](skills/automation-and-saas/ipinfo-io-automation/SKILL.md) | Automate Ipinfo IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/iqair-airvisual-automation` | [`iqair-airvisual-automation`](skills/automation-and-saas/iqair-airvisual-automation/SKILL.md) | Automate Iqair Airvisual tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jigsawstack-automation` | [`jigsawstack-automation`](skills/automation-and-saas/jigsawstack-automation/SKILL.md) | Automate Jigsawstack tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jira-automation` | [`jira-automation`](skills/automation-and-saas/jira-automation/SKILL.md) | Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. |
| `/jobnimbus-automation` | [`jobnimbus-automation`](skills/automation-and-saas/jobnimbus-automation/SKILL.md) | Automate Jobnimbus tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/jq` | [`jq`](skills/automation-and-saas/jq/SKILL.md) | Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. |
| `/jumpcloud-automation` | [`jumpcloud-automation`](skills/automation-and-saas/jumpcloud-automation/SKILL.md) | Automate Jumpcloud tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/junglescout-automation` | [`junglescout-automation`](skills/automation-and-saas/junglescout-automation/SKILL.md) | Automate Junglescout tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/junta-leiloeiros` | [`junta-leiloeiros`](skills/automation-and-saas/junta-leiloeiros/SKILL.md) | Coleta e consulta dados de leiloeiros oficiais de todas as 27 Juntas Comerciais do Brasil. |
| `/kadoa-automation` | [`kadoa-automation`](skills/automation-and-saas/kadoa-automation/SKILL.md) | Automate Kadoa tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kaggle-automation` | [`kaggle-automation`](skills/automation-and-saas/kaggle-automation/SKILL.md) | Automate Kaggle tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kaleido-automation` | [`kaleido-automation`](skills/automation-and-saas/kaleido-automation/SKILL.md) | Automate Kaleido tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/keap-automation` | [`keap-automation`](skills/automation-and-saas/keap-automation/SKILL.md) | Automate Keap tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/keen-io-automation` | [`keen-io-automation`](skills/automation-and-saas/keen-io-automation/SKILL.md) | Automate Keen IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kickbox-automation` | [`kickbox-automation`](skills/automation-and-saas/kickbox-automation/SKILL.md) | Automate Kickbox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/kit-automation` | [`kit-automation`](skills/automation-and-saas/kit-automation/SKILL.md) | Automate Kit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/klaviyo-automation` | [`klaviyo-automation`](skills/automation-and-saas/klaviyo-automation/SKILL.md) | Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags. |
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
| `/linear-automation` | [`linear-automation`](skills/automation-and-saas/linear-automation/SKILL.md) | Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. |
| `/linguapop-automation` | [`linguapop-automation`](skills/automation-and-saas/linguapop-automation/SKILL.md) | Automate Linguapop tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/linkedin-automation` | [`linkedin-automation`](skills/automation-and-saas/linkedin-automation/SKILL.md) | Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. |
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
| `/mailchimp-automation` | [`mailchimp-automation`](skills/automation-and-saas/mailchimp-automation/SKILL.md) | Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). |
| `/mailcoach-automation` | [`mailcoach-automation`](skills/automation-and-saas/mailcoach-automation/SKILL.md) | Automate Mailcoach tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailersend-automation` | [`mailersend-automation`](skills/automation-and-saas/mailersend-automation/SKILL.md) | Automate Mailersend tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mails-so-automation` | [`mails-so-automation`](skills/automation-and-saas/mails-so-automation/SKILL.md) | Automate Mails So tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mailsoftly-automation` | [`mailsoftly-automation`](skills/automation-and-saas/mailsoftly-automation/SKILL.md) | Automate Mailsoftly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/maintainx-automation` | [`maintainx-automation`](skills/automation-and-saas/maintainx-automation/SKILL.md) | Automate Maintainx tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/make-automation` | [`make-automation`](skills/automation-and-saas/make-automation/SKILL.md) | Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. |
| `/makepad-font` | [`makepad-font`](skills/automation-and-saas/makepad-font/SKILL.md) | CRITICAL: Use for Makepad font and text rendering. |
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
| `/microsoft-teams-automation` | [`microsoft-teams-automation`](skills/automation-and-saas/microsoft-teams-automation/SKILL.md) | Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats. |
| `/microsoft-tenant-automation` | [`microsoft-tenant-automation`](skills/automation-and-saas/microsoft-tenant-automation/SKILL.md) | Automate Microsoft Tenant tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/minecraft-bukkit-pro` | [`minecraft-bukkit-pro`](skills/automation-and-saas/minecraft-bukkit-pro/SKILL.md) | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| `/minecraft-plugin-development` | [`minecraft-plugin-development`](skills/automation-and-saas/minecraft-plugin-development/SKILL.md) | Use this skill when building or modifying Minecraft server plugins for Paper, Spigot. |
| `/minerstat-automation` | [`minerstat-automation`](skills/automation-and-saas/minerstat-automation/SKILL.md) | Automate Minerstat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/minimal-api-file-upload` | [`minimal-api-file-upload`](skills/automation-and-saas/minimal-api-file-upload/SKILL.md) | File upload endpoints in ASP.NET minimal APIs (.NET 8+). |
| `/miro-automation` | [`miro-automation`](skills/automation-and-saas/miro-automation/SKILL.md) | Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. |
| `/missive-automation` | [`missive-automation`](skills/automation-and-saas/missive-automation/SKILL.md) | Automate Missive tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/mistral_ai-automation` | [`mistral_ai-automation`](skills/automation-and-saas/mistral_ai-automation/SKILL.md) | Automate Mistral AI tasks via Rube MCP (Composio): completions, embeddings, fine-tuning, and model management. |
| `/mixpanel-automation` | [`mixpanel-automation`](skills/automation-and-saas/mixpanel-automation/SKILL.md) | Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. |
| `/mocean-automation` | [`mocean-automation`](skills/automation-and-saas/mocean-automation/SKILL.md) | Automate Mocean tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moco-automation` | [`moco-automation`](skills/automation-and-saas/moco-automation/SKILL.md) | Automate Moco tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/modelry-automation` | [`modelry-automation`](skills/automation-and-saas/modelry-automation/SKILL.md) | Automate Modelry tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/monday-automation` | [`monday-automation`](skills/automation-and-saas/monday-automation/SKILL.md) | Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). |
| `/monetization` | [`monetization`](skills/automation-and-saas/monetization/SKILL.md) | Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments,. |
| `/moneybird-automation` | [`moneybird-automation`](skills/automation-and-saas/moneybird-automation/SKILL.md) | Automate Moneybird tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/moodle-external-api-development` | [`moodle-external-api-development`](skills/automation-and-saas/moodle-external-api-development/SKILL.md) | This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API. |
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
| `/native-data-fetching` | [`native-data-fetching`](skills/automation-and-saas/native-data-fetching/SKILL.md) | Use when implementing or debugging ANY network request, API call, or data fetching. |
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
| `/notion-automation` | [`notion-automation`](skills/automation-and-saas/notion-automation/SKILL.md) | Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. |
| `/notion-template-business` | [`notion-template-business`](skills/automation-and-saas/notion-template-business/SKILL.md) | Expert in building and selling Notion templates as a business - not. |
| `/npm-automation` | [`npm-automation`](skills/automation-and-saas/npm-automation/SKILL.md) | Automate NPM tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ocr-web-service-automation` | [`ocr-web-service-automation`](skills/automation-and-saas/ocr-web-service-automation/SKILL.md) | Automate OCR Web Service tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ocrspace-automation` | [`ocrspace-automation`](skills/automation-and-saas/ocrspace-automation/SKILL.md) | Automate Ocrspace tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/odoo-automated-tests` | [`odoo-automated-tests`](skills/automation-and-saas/odoo-automated-tests/SKILL.md) | Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. |
| `/odoo-migration-helper` | [`odoo-migration-helper`](skills/automation-and-saas/odoo-migration-helper/SKILL.md) | Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). |
| `/odoo-qweb-templates` | [`odoo-qweb-templates`](skills/automation-and-saas/odoo-qweb-templates/SKILL.md) | Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. |
| `/odoo-rpc-api` | [`odoo-rpc-api`](skills/automation-and-saas/odoo-rpc-api/SKILL.md) | Expert on Odoo's external JSON-RPC and XML-RPC APIs. |
| `/odoo-shopify-integration` | [`odoo-shopify-integration`](skills/automation-and-saas/odoo-shopify-integration/SKILL.md) | Connect Odoo with Shopify: sync products, inventory, orders. |
| `/odoo-woocommerce-bridge` | [`odoo-woocommerce-bridge`](skills/automation-and-saas/odoo-woocommerce-bridge/SKILL.md) | Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API. |
| `/oncehub-automation` | [`oncehub-automation`](skills/automation-and-saas/oncehub-automation/SKILL.md) | Automate Oncehub tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/one-drive-automation` | [`one-drive-automation`](skills/automation-and-saas/one-drive-automation/SKILL.md) | Automate OneDrive file management, search, uploads, downloads, sharing, permissions. |
| `/onedesk-automation` | [`onedesk-automation`](skills/automation-and-saas/onedesk-automation/SKILL.md) | Automate Onedesk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onepage-automation` | [`onepage-automation`](skills/automation-and-saas/onepage-automation/SKILL.md) | Automate Onepage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal-rest-api-automation` | [`onesignal-rest-api-automation`](skills/automation-and-saas/onesignal-rest-api-automation/SKILL.md) | Automate OneSignal tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal-user-auth-automation` | [`onesignal-user-auth-automation`](skills/automation-and-saas/onesignal-user-auth-automation/SKILL.md) | Automate Onesignal User Auth tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/onesignal_rest_api-automation` | [`onesignal_rest_api-automation`](skills/automation-and-saas/onesignal_rest_api-automation/SKILL.md) | Automate OneSignal tasks via Rube MCP (Composio): push notifications, segments, templates, and messaging. |
| `/open-sea-automation` | [`open-sea-automation`](skills/automation-and-saas/open-sea-automation/SKILL.md) | Automate Open Sea tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openapi-spec-generation` | [`openapi-spec-generation`](skills/automation-and-saas/openapi-spec-generation/SKILL.md) | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. |
| `/openapi-to-application-code` | [`openapi-to-application-code`](skills/automation-and-saas/openapi-to-application-code/SKILL.md) | Generate a complete, production-ready application from an OpenAPI specification. |
| `/opencage-automation` | [`opencage-automation`](skills/automation-and-saas/opencage-automation/SKILL.md) | Automate Opencage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/opengraph-io-automation` | [`opengraph-io-automation`](skills/automation-and-saas/opengraph-io-automation/SKILL.md) | Automate Opengraph IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openperplex-automation` | [`openperplex-automation`](skills/automation-and-saas/openperplex-automation/SKILL.md) | Automate Openperplex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openrouter-automation` | [`openrouter-automation`](skills/automation-and-saas/openrouter-automation/SKILL.md) | Automate Openrouter tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/openweather-api-automation` | [`openweather-api-automation`](skills/automation-and-saas/openweather-api-automation/SKILL.md) | Automate Openweather API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/optimoroute-automation` | [`optimoroute-automation`](skills/automation-and-saas/optimoroute-automation/SKILL.md) | Automate Optimoroute tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/outlook-automation` | [`outlook-automation`](skills/automation-and-saas/outlook-automation/SKILL.md) | Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. |
| `/outlook-calendar-automation` | [`outlook-calendar-automation`](skills/automation-and-saas/outlook-calendar-automation/SKILL.md) | Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times. |
| `/owl-protocol-automation` | [`owl-protocol-automation`](skills/automation-and-saas/owl-protocol-automation/SKILL.md) | Automate Owl Protocol tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/page-x-automation` | [`page-x-automation`](skills/automation-and-saas/page-x-automation/SKILL.md) | Automate Page X tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pagerduty-automation` | [`pagerduty-automation`](skills/automation-and-saas/pagerduty-automation/SKILL.md) | Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies. |
| `/pakistan-payments-stack` | [`pakistan-payments-stack`](skills/automation-and-saas/pakistan-payments-stack/SKILL.md) | Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional. |
| `/paradym-automation` | [`paradym-automation`](skills/automation-and-saas/paradym-automation/SKILL.md) | Automate Paradym tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parallel-automation` | [`parallel-automation`](skills/automation-and-saas/parallel-automation/SKILL.md) | Automate Parallel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parma-automation` | [`parma-automation`](skills/automation-and-saas/parma-automation/SKILL.md) | Automate Parma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parsehub-automation` | [`parsehub-automation`](skills/automation-and-saas/parsehub-automation/SKILL.md) | Automate Parsehub tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parsera-automation` | [`parsera-automation`](skills/automation-and-saas/parsera-automation/SKILL.md) | Automate Parsera tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/parseur-automation` | [`parseur-automation`](skills/automation-and-saas/parseur-automation/SKILL.md) | Automate Parseur tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/passcreator-automation` | [`passcreator-automation`](skills/automation-and-saas/passcreator-automation/SKILL.md) | Automate Passcreator tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/passslot-automation` | [`passslot-automation`](skills/automation-and-saas/passslot-automation/SKILL.md) | Automate Passslot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/payhip-automation` | [`payhip-automation`](skills/automation-and-saas/payhip-automation/SKILL.md) | Automate Payhip tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/payment-integration` | [`payment-integration`](skills/automation-and-saas/payment-integration/SKILL.md) | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. |
| `/paypal-integration` | [`paypal-integration`](skills/automation-and-saas/paypal-integration/SKILL.md) | Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows. |
| `/pdf-api-io-automation` | [`pdf-api-io-automation`](skills/automation-and-saas/pdf-api-io-automation/SKILL.md) | Automate PDF API IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdf-co-automation` | [`pdf-co-automation`](skills/automation-and-saas/pdf-co-automation/SKILL.md) | Automate PDF co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdf4me-automation` | [`pdf4me-automation`](skills/automation-and-saas/pdf4me-automation/SKILL.md) | Automate Pdf4me tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdfless-automation` | [`pdfless-automation`](skills/automation-and-saas/pdfless-automation/SKILL.md) | Automate Pdfless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pdfmonkey-automation` | [`pdfmonkey-automation`](skills/automation-and-saas/pdfmonkey-automation/SKILL.md) | Automate Pdfmonkey tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/peopledatalabs-automation` | [`peopledatalabs-automation`](skills/automation-and-saas/peopledatalabs-automation/SKILL.md) | Automate Peopledatalabs tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/performance-optimizer` | [`performance-optimizer`](skills/automation-and-saas/performance-optimizer/SKILL.md) | Identifies and fixes performance bottlenecks in code, databases, and APIs. |
| `/performance-review-writer` | [`performance-review-writer`](skills/automation-and-saas/performance-review-writer/SKILL.md) | Draft performance reviews, self-assessments, peer reviews, and upward feedback in your own voice. |
| `/perigon-automation` | [`perigon-automation`](skills/automation-and-saas/perigon-automation/SKILL.md) | Automate Perigon tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/perplexityai-automation` | [`perplexityai-automation`](skills/automation-and-saas/perplexityai-automation/SKILL.md) | Automate Perplexityai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/persistiq-automation` | [`persistiq-automation`](skills/automation-and-saas/persistiq-automation/SKILL.md) | Automate Persistiq tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pexels-automation` | [`pexels-automation`](skills/automation-and-saas/pexels-automation/SKILL.md) | Automate Pexels tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/photopea-embedded-editor` | [`photopea-embedded-editor`](skills/automation-and-saas/photopea-embedded-editor/SKILL.md) | Embed Photopea in web apps using photopea.js. |
| `/piggy-automation` | [`piggy-automation`](skills/automation-and-saas/piggy-automation/SKILL.md) | Automate Piggy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/piloterr-automation` | [`piloterr-automation`](skills/automation-and-saas/piloterr-automation/SKILL.md) | Automate Piloterr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pilvio-automation` | [`pilvio-automation`](skills/automation-and-saas/pilvio-automation/SKILL.md) | Automate Pilvio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pingdom-automation` | [`pingdom-automation`](skills/automation-and-saas/pingdom-automation/SKILL.md) | Automate Pingdom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/pipedrive-automation` | [`pipedrive-automation`](skills/automation-and-saas/pipedrive-automation/SKILL.md) | Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes. |
| `/pipeline-crm-automation` | [`pipeline-crm-automation`](skills/automation-and-saas/pipeline-crm-automation/SKILL.md) | Automate Pipeline CRM tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/placekey-automation` | [`placekey-automation`](skills/automation-and-saas/placekey-automation/SKILL.md) | Automate Placekey tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/placid-automation` | [`placid-automation`](skills/automation-and-saas/placid-automation/SKILL.md) | Automate Placid tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/plaid-fintech` | [`plaid-fintech`](skills/automation-and-saas/plaid-fintech/SKILL.md) | Expert patterns for Plaid API integration including Link token. |
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
| `/posthog-automation` | [`posthog-automation`](skills/automation-and-saas/posthog-automation/SKILL.md) | Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. |
| `/postmark-automation` | [`postmark-automation`](skills/automation-and-saas/postmark-automation/SKILL.md) | Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor. |
| `/power-apps-code-app-scaffold` | [`power-apps-code-app-scaffold`](skills/automation-and-saas/power-apps-code-app-scaffold/SKILL.md) | Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration, and connector configuration. |
| `/precoro-automation` | [`precoro-automation`](skills/automation-and-saas/precoro-automation/SKILL.md) | Automate Precoro tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/prerender-automation` | [`prerender-automation`](skills/automation-and-saas/prerender-automation/SKILL.md) | Automate Prerender tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/printautopilot-automation` | [`printautopilot-automation`](skills/automation-and-saas/printautopilot-automation/SKILL.md) | Automate Printautopilot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/prisma-automation` | [`prisma-automation`](skills/automation-and-saas/prisma-automation/SKILL.md) | Automate Prisma tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/process-street-automation` | [`process-street-automation`](skills/automation-and-saas/process-street-automation/SKILL.md) | Automate Process Street tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/procfu-automation` | [`procfu-automation`](skills/automation-and-saas/procfu-automation/SKILL.md) | Automate Procfu tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/production-audit` | [`production-audit`](skills/automation-and-saas/production-audit/SKILL.md) | Audit a shipped repo for production-readiness gaps across RLS, webhooks, secrets, grants, Stripe idempotency, mobile UX. |
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
| `/reddit-automation` | [`reddit-automation`](skills/automation-and-saas/reddit-automation/SKILL.md) | Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. |
| `/refiner-automation` | [`refiner-automation`](skills/automation-and-saas/refiner-automation/SKILL.md) | Automate Refiner tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remarkety-automation` | [`remarkety-automation`](skills/automation-and-saas/remarkety-automation/SKILL.md) | Automate Remarkety tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remote-retrieval-automation` | [`remote-retrieval-automation`](skills/automation-and-saas/remote-retrieval-automation/SKILL.md) | Automate Remote Retrieval tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/remotion` | [`remotion`](skills/automation-and-saas/remotion/SKILL.md) | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays. |
| `/remove-bg-automation` | [`remove-bg-automation`](skills/automation-and-saas/remove-bg-automation/SKILL.md) | Automate Remove Bg tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/render-automation` | [`render-automation`](skills/automation-and-saas/render-automation/SKILL.md) | Automate Render tasks via Rube MCP (Composio): services, deployments, projects. |
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
| `/robius-matrix-integration` | [`robius-matrix-integration`](skills/automation-and-saas/robius-matrix-integration/SKILL.md) | CRITICAL: Use for Matrix SDK integration with Makepad. |
| `/rocketlane-automation` | [`rocketlane-automation`](skills/automation-and-saas/rocketlane-automation/SKILL.md) | Automate Rocketlane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rootly-automation` | [`rootly-automation`](skills/automation-and-saas/rootly-automation/SKILL.md) | Automate Rootly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/rosette-text-analytics-automation` | [`rosette-text-analytics-automation`](skills/automation-and-saas/rosette-text-analytics-automation/SKILL.md) | Automate Rosette Text Analytics tasks via Rube MCP (Composio). |
| `/roundup` | [`roundup`](skills/automation-and-saas/roundup/SKILL.md) | Generate personalized status briefings on demand. |
| `/route4me-automation` | [`route4me-automation`](skills/automation-and-saas/route4me-automation/SKILL.md) | Automate Route4me tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/runaway-guard` | [`runaway-guard`](skills/automation-and-saas/runaway-guard/SKILL.md) | Cost-safety discipline for paid AI / inference APIs: treat $-cost as a third complexity dimension alongside time and space. |
| `/safetyculture-automation` | [`safetyculture-automation`](skills/automation-and-saas/safetyculture-automation/SKILL.md) | Automate Safetyculture tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sage-automation` | [`sage-automation`](skills/automation-and-saas/sage-automation/SKILL.md) | Automate Sage tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/salesforce-apex-quality` | [`salesforce-apex-quality`](skills/automation-and-saas/salesforce-apex-quality/SKILL.md) | Apex code quality guardrails for Salesforce development. |
| `/salesforce-automation` | [`salesforce-automation`](skills/automation-and-saas/salesforce-automation/SKILL.md) | Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. |
| `/salesforce-development` | [`salesforce-development`](skills/automation-and-saas/salesforce-development/SKILL.md) | Expert patterns for Salesforce platform development including. |
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
| `/segment-automation` | [`segment-automation`](skills/automation-and-saas/segment-automation/SKILL.md) | Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch. |
| `/segmetrics-automation` | [`segmetrics-automation`](skills/automation-and-saas/segmetrics-automation/SKILL.md) | Automate Segmetrics tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/seismic-automation` | [`seismic-automation`](skills/automation-and-saas/seismic-automation/SKILL.md) | Automate Seismic tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/semanticscholar-automation` | [`semanticscholar-automation`](skills/automation-and-saas/semanticscholar-automation/SKILL.md) | Automate Semanticscholar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendbird-ai-chabot-automation` | [`sendbird-ai-chabot-automation`](skills/automation-and-saas/sendbird-ai-chabot-automation/SKILL.md) | Automate Sendbird AI Chabot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendbird-automation` | [`sendbird-automation`](skills/automation-and-saas/sendbird-automation/SKILL.md) | Automate Sendbird tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendfox-automation` | [`sendfox-automation`](skills/automation-and-saas/sendfox-automation/SKILL.md) | Automate Sendfox tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendgrid-automation` | [`sendgrid-automation`](skills/automation-and-saas/sendgrid-automation/SKILL.md) | Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management,. |
| `/sendlane-automation` | [`sendlane-automation`](skills/automation-and-saas/sendlane-automation/SKILL.md) | Automate Sendlane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendloop-automation` | [`sendloop-automation`](skills/automation-and-saas/sendloop-automation/SKILL.md) | Automate Sendloop tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sendspark-automation` | [`sendspark-automation`](skills/automation-and-saas/sendspark-automation/SKILL.md) | Automate Sendspark tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sensibo-automation` | [`sensibo-automation`](skills/automation-and-saas/sensibo-automation/SKILL.md) | Automate Sensibo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sentry-automation` | [`sentry-automation`](skills/automation-and-saas/sentry-automation/SKILL.md) | Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. |
| `/seqera-automation` | [`seqera-automation`](skills/automation-and-saas/seqera-automation/SKILL.md) | Automate Seqera tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serpapi-automation` | [`serpapi-automation`](skills/automation-and-saas/serpapi-automation/SKILL.md) | Automate Serpapi tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serpdog-automation` | [`serpdog-automation`](skills/automation-and-saas/serpdog-automation/SKILL.md) | Automate Serpdog tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/serply-automation` | [`serply-automation`](skills/automation-and-saas/serply-automation/SKILL.md) | Automate Serply tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/service-mesh-expert` | [`service-mesh-expert`](skills/automation-and-saas/service-mesh-expert/SKILL.md) | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. |
| `/servicem8-automation` | [`servicem8-automation`](skills/automation-and-saas/servicem8-automation/SKILL.md) | Automate Servicem8 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sevdesk-automation` | [`sevdesk-automation`](skills/automation-and-saas/sevdesk-automation/SKILL.md) | Automate Sevdesk tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/share_point-automation` | [`share_point-automation`](skills/automation-and-saas/share_point-automation/SKILL.md) | Automate SharePoint tasks via Rube MCP (Composio): document libraries, sites, lists, and content management. |
| `/shipengine-automation` | [`shipengine-automation`](skills/automation-and-saas/shipengine-automation/SKILL.md) | Automate Shipengine tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/shopify-automation` | [`shopify-automation`](skills/automation-and-saas/shopify-automation/SKILL.md) | Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. |
| `/shopify-development` | [`shopify-development`](skills/automation-and-saas/shopify-development/SKILL.md) | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
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
| `/skyvern-browser-automation` | [`skyvern-browser-automation`](skills/automation-and-saas/skyvern-browser-automation/SKILL.md) | AI-powered browser automation — navigate sites, fill forms, extract structured data, log in with stored credentials. |
| `/slack-automation` | [`slack-automation`](skills/automation-and-saas/slack-automation/SKILL.md) | Automate Slack workspace operations including messaging, search, channel management. |
| `/slack-bot-builder` | [`slack-bot-builder`](skills/automation-and-saas/slack-bot-builder/SKILL.md) | Build Slack apps using the Bolt framework across Python,. |
| `/slackbot-automation` | [`slackbot-automation`](skills/automation-and-saas/slackbot-automation/SKILL.md) | Automate Slackbot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smartproxy-automation` | [`smartproxy-automation`](skills/automation-and-saas/smartproxy-automation/SKILL.md) | Automate Smartproxy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smartrecruiters-automation` | [`smartrecruiters-automation`](skills/automation-and-saas/smartrecruiters-automation/SKILL.md) | Automate Smartrecruiters tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sms-alert-automation` | [`sms-alert-automation`](skills/automation-and-saas/sms-alert-automation/SKILL.md) | Automate SMS Alert tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smtp2go-automation` | [`smtp2go-automation`](skills/automation-and-saas/smtp2go-automation/SKILL.md) | Automate Smtp2go tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/smugmug-automation` | [`smugmug-automation`](skills/automation-and-saas/smugmug-automation/SKILL.md) | Automate Smugmug tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sourcegraph-automation` | [`sourcegraph-automation`](skills/automation-and-saas/sourcegraph-automation/SKILL.md) | Automate Sourcegraph tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spline-3d-integration` | [`spline-3d-integration`](skills/automation-and-saas/spline-3d-integration/SKILL.md) | Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API. |
| `/splitwise-automation` | [`splitwise-automation`](skills/automation-and-saas/splitwise-automation/SKILL.md) | Automate Splitwise tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spoki-automation` | [`spoki-automation`](skills/automation-and-saas/spoki-automation/SKILL.md) | Automate Spoki tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spondyr-automation` | [`spondyr-automation`](skills/automation-and-saas/spondyr-automation/SKILL.md) | Automate Spondyr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/spotlightr-automation` | [`spotlightr-automation`](skills/automation-and-saas/spotlightr-automation/SKILL.md) | Automate Spotlightr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/square-automation` | [`square-automation`](skills/automation-and-saas/square-automation/SKILL.md) | Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. |
| `/sred-work-summary` | [`sred-work-summary`](skills/automation-and-saas/sred-work-summary/SKILL.md) | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can. |
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
| `/stripe-automation` | [`stripe-automation`](skills/automation-and-saas/stripe-automation/SKILL.md) | Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. |
| `/stripe-best-practices` | [`stripe-best-practices`](skills/automation-and-saas/stripe-best-practices/SKILL.md) | Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup. |
| `/stripe-integration` | [`stripe-integration`](skills/automation-and-saas/stripe-integration/SKILL.md) | Master Stripe payment processing integration for robust, PCI-compliant payment flows including checkout, subscriptions,. |
| `/stripe-projects` | [`stripe-projects`](skills/automation-and-saas/stripe-projects/SKILL.md) | Use when the user needs to provision a third-party service available on https://projects.dev/providers; create or. |
| `/supabase-automation` | [`supabase-automation`](skills/automation-and-saas/supabase-automation/SKILL.md) | Automate Supabase database queries, table management, project administration, storage, edge functions. |
| `/supadata-automation` | [`supadata-automation`](skills/automation-and-saas/supadata-automation/SKILL.md) | Automate Supadata tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/superchat-automation` | [`superchat-automation`](skills/automation-and-saas/superchat-automation/SKILL.md) | Automate Superchat tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/supportbee-automation` | [`supportbee-automation`](skills/automation-and-saas/supportbee-automation/SKILL.md) | Automate Supportbee tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/supportivekoala-automation` | [`supportivekoala-automation`](skills/automation-and-saas/supportivekoala-automation/SKILL.md) | Automate Supportivekoala tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/survey_monkey-automation` | [`survey_monkey-automation`](skills/automation-and-saas/survey_monkey-automation/SKILL.md) | Automate SurveyMonkey tasks via Rube MCP (Composio): surveys, responses, collectors, and survey analytics. |
| `/sveltekit` | [`sveltekit`](skills/automation-and-saas/sveltekit/SKILL.md) | Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework. |
| `/svix-automation` | [`svix-automation`](skills/automation-and-saas/svix-automation/SKILL.md) | Automate Svix tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/sympla-automation` | [`sympla-automation`](skills/automation-and-saas/sympla-automation/SKILL.md) | Automate Sympla tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/synthflow-ai-automation` | [`synthflow-ai-automation`](skills/automation-and-saas/synthflow-ai-automation/SKILL.md) | Automate Synthflow AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/taggun-automation` | [`taggun-automation`](skills/automation-and-saas/taggun-automation/SKILL.md) | Automate Taggun tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/talenthr-automation` | [`talenthr-automation`](skills/automation-and-saas/talenthr-automation/SKILL.md) | Automate Talenthr tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tally-automation` | [`tally-automation`](skills/automation-and-saas/tally-automation/SKILL.md) | Automate Tally tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tanstack-query-expert` | [`tanstack-query-expert`](skills/automation-and-saas/tanstack-query-expert/SKILL.md) | Expert in TanStack Query (React Query) — asynchronous state management. |
| `/tapfiliate-automation` | [`tapfiliate-automation`](skills/automation-and-saas/tapfiliate-automation/SKILL.md) | Automate Tapfiliate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tapform-automation` | [`tapform-automation`](skills/automation-and-saas/tapform-automation/SKILL.md) | Automate Tapform tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tavily-automation` | [`tavily-automation`](skills/automation-and-saas/tavily-automation/SKILL.md) | Automate Tavily tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tavily-web` | [`tavily-web`](skills/automation-and-saas/tavily-web/SKILL.md) | Web search, content extraction, crawling, and research capabilities using Tavily API. |
| `/taxjar-automation` | [`taxjar-automation`](skills/automation-and-saas/taxjar-automation/SKILL.md) | Automate Taxjar tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/teamcamp-automation` | [`teamcamp-automation`](skills/automation-and-saas/teamcamp-automation/SKILL.md) | Automate Teamcamp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/telegram` | [`telegram`](skills/automation-and-saas/telegram/SKILL.md) | Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. |
| `/telegram-automation` | [`telegram-automation`](skills/automation-and-saas/telegram-automation/SKILL.md) | Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. |
| `/telnyx-automation` | [`telnyx-automation`](skills/automation-and-saas/telnyx-automation/SKILL.md) | Automate Telnyx tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/teltel-automation` | [`teltel-automation`](skills/automation-and-saas/teltel-automation/SKILL.md) | Automate Teltel tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/templated-automation` | [`templated-automation`](skills/automation-and-saas/templated-automation/SKILL.md) | Automate Templated tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/test-app-automation` | [`test-app-automation`](skills/automation-and-saas/test-app-automation/SKILL.md) | Automate Test App tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/test-automator` | [`test-automator`](skills/automation-and-saas/test-automator/SKILL.md) | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. |
| `/textcortex-automation` | [`textcortex-automation`](skills/automation-and-saas/textcortex-automation/SKILL.md) | Automate Textcortex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/textit-automation` | [`textit-automation`](skills/automation-and-saas/textit-automation/SKILL.md) | Automate Textit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/textrazor-automation` | [`textrazor-automation`](skills/automation-and-saas/textrazor-automation/SKILL.md) | Automate Textrazor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/thanks-io-automation` | [`thanks-io-automation`](skills/automation-and-saas/thanks-io-automation/SKILL.md) | Automate Thanks IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/the-odds-api-automation` | [`the-odds-api-automation`](skills/automation-and-saas/the-odds-api-automation/SKILL.md) | Automate The Odds API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ticketmaster-automation` | [`ticketmaster-automation`](skills/automation-and-saas/ticketmaster-automation/SKILL.md) | Automate Ticketmaster tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/ticktick-automation` | [`ticktick-automation`](skills/automation-and-saas/ticktick-automation/SKILL.md) | Automate Ticktick tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tiktok-automation` | [`tiktok-automation`](skills/automation-and-saas/tiktok-automation/SKILL.md) | Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. |
| `/timecamp-automation` | [`timecamp-automation`](skills/automation-and-saas/timecamp-automation/SKILL.md) | Automate Timecamp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timekit-automation` | [`timekit-automation`](skills/automation-and-saas/timekit-automation/SKILL.md) | Automate Timekit tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timelinesai-automation` | [`timelinesai-automation`](skills/automation-and-saas/timelinesai-automation/SKILL.md) | Automate Timelinesai tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timelink-automation` | [`timelink-automation`](skills/automation-and-saas/timelink-automation/SKILL.md) | Automate Timelink tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/timely-automation` | [`timely-automation`](skills/automation-and-saas/timely-automation/SKILL.md) | Automate Timely tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tinyurl-automation` | [`tinyurl-automation`](skills/automation-and-saas/tinyurl-automation/SKILL.md) | Automate Tinyurl tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tisane-automation` | [`tisane-automation`](skills/automation-and-saas/tisane-automation/SKILL.md) | Automate Tisane tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/todoist-automation` | [`todoist-automation`](skills/automation-and-saas/todoist-automation/SKILL.md) | Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). |
| `/token-metrics-automation` | [`token-metrics-automation`](skills/automation-and-saas/token-metrics-automation/SKILL.md) | Automate Token Metrics tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tomba-automation` | [`tomba-automation`](skills/automation-and-saas/tomba-automation/SKILL.md) | Automate Tomba tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tomtom-automation` | [`tomtom-automation`](skills/automation-and-saas/tomtom-automation/SKILL.md) | Automate Tomtom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/toneden-automation` | [`toneden-automation`](skills/automation-and-saas/toneden-automation/SKILL.md) | Automate Toneden tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tpscheck-automation` | [`tpscheck-automation`](skills/automation-and-saas/tpscheck-automation/SKILL.md) | Automate Tpscheck tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/trello-automation` | [`trello-automation`](skills/automation-and-saas/trello-automation/SKILL.md) | Automate Trello boards, cards, and workflows via Rube MCP (Composio). |
| `/triggercmd-automation` | [`triggercmd-automation`](skills/automation-and-saas/triggercmd-automation/SKILL.md) | Automate Triggercmd tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/tripadvisor-content-api-automation` | [`tripadvisor-content-api-automation`](skills/automation-and-saas/tripadvisor-content-api-automation/SKILL.md) | Automate TripAdvisor tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/turbot-pipes-automation` | [`turbot-pipes-automation`](skills/automation-and-saas/turbot-pipes-automation/SKILL.md) | Automate Turbot Pipes tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/turso-automation` | [`turso-automation`](skills/automation-and-saas/turso-automation/SKILL.md) | Automate Turso tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twelve-data-automation` | [`twelve-data-automation`](skills/automation-and-saas/twelve-data-automation/SKILL.md) | Automate Twelve Data tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twilio-communications` | [`twilio-communications`](skills/automation-and-saas/twilio-communications/SKILL.md) | Build communication features with Twilio: SMS messaging, voice. |
| `/twitch-automation` | [`twitch-automation`](skills/automation-and-saas/twitch-automation/SKILL.md) | Automate Twitch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/twitter-automation` | [`twitter-automation`](skills/automation-and-saas/twitter-automation/SKILL.md) | Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. |
| `/twocaptcha-automation` | [`twocaptcha-automation`](skills/automation-and-saas/twocaptcha-automation/SKILL.md) | Automate Twocaptcha tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/typefully-automation` | [`typefully-automation`](skills/automation-and-saas/typefully-automation/SKILL.md) | Automate Typefully tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/typespec-api-operations` | [`typespec-api-operations`](skills/automation-and-saas/typespec-api-operations/SKILL.md) | Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards. |
| `/typespec-create-api-plugin` | [`typespec-create-api-plugin`](skills/automation-and-saas/typespec-create-api-plugin/SKILL.md) | Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot. |
| `/typless-automation` | [`typless-automation`](skills/automation-and-saas/typless-automation/SKILL.md) | Automate Typless tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/u301-automation` | [`u301-automation`](skills/automation-and-saas/u301-automation/SKILL.md) | Automate U301 tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/unione-automation` | [`unione-automation`](skills/automation-and-saas/unione-automation/SKILL.md) | Automate Unione tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/unsplash-integration` | [`unsplash-integration`](skills/automation-and-saas/unsplash-integration/SKILL.md) | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| `/updown-io-automation` | [`updown-io-automation`](skills/automation-and-saas/updown-io-automation/SKILL.md) | Automate Updown IO tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/upgrade-stripe` | [`upgrade-stripe`](skills/automation-and-saas/upgrade-stripe/SKILL.md) | Guide for upgrading Stripe API versions and SDKs. |
| `/uptimerobot-automation` | [`uptimerobot-automation`](skills/automation-and-saas/uptimerobot-automation/SKILL.md) | Automate Uptimerobot tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/userlist-automation` | [`userlist-automation`](skills/automation-and-saas/userlist-automation/SKILL.md) | Automate Userlist tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/venly-automation` | [`venly-automation`](skills/automation-and-saas/venly-automation/SKILL.md) | Automate Venly tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/veo-automation` | [`veo-automation`](skills/automation-and-saas/veo-automation/SKILL.md) | Automate Veo tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vercel-automation` | [`vercel-automation`](skills/automation-and-saas/vercel-automation/SKILL.md) | Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. |
| `/verifiedemail-automation` | [`verifiedemail-automation`](skills/automation-and-saas/verifiedemail-automation/SKILL.md) | Automate Verifiedemail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/veriphone-automation` | [`veriphone-automation`](skills/automation-and-saas/veriphone-automation/SKILL.md) | Automate Veriphone tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vero-automation` | [`vero-automation`](skills/automation-and-saas/vero-automation/SKILL.md) | Automate Vero tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vestaboard-automation` | [`vestaboard-automation`](skills/automation-and-saas/vestaboard-automation/SKILL.md) | Automate Vestaboard tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/vibe-code-auditor` | [`vibe-code-auditor`](skills/automation-and-saas/vibe-code-auditor/SKILL.md) | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
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
| `/web-scraper` | [`web-scraper`](skills/automation-and-saas/web-scraper/SKILL.md) | Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). |
| `/webflow-automation` | [`webflow-automation`](skills/automation-and-saas/webflow-automation/SKILL.md) | Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). |
| `/webscraping-ai-automation` | [`webscraping-ai-automation`](skills/automation-and-saas/webscraping-ai-automation/SKILL.md) | Automate Webscraping AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/webvizio-automation` | [`webvizio-automation`](skills/automation-and-saas/webvizio-automation/SKILL.md) | Automate Webvizio tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wechat-official-account-strategist` | [`wechat-official-account-strategist`](skills/automation-and-saas/wechat-official-account-strategist/SKILL.md) | Grow WeChat Official Accounts (微信公众号) with high-conversion content strategy, title formulas, article architecture. |
| `/whatsapp-automation` | [`whatsapp-automation`](skills/automation-and-saas/whatsapp-automation/SKILL.md) | Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. |
| `/whatsapp-cloud-api` | [`whatsapp-cloud-api`](skills/automation-and-saas/whatsapp-cloud-api/SKILL.md) | Integracao com WhatsApp Business Cloud API (Meta). |
| `/whautomate-automation` | [`whautomate-automation`](skills/automation-and-saas/whautomate-automation/SKILL.md) | Automate Whautomate tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/winmd-api-search` | [`winmd-api-search`](skills/automation-and-saas/winmd-api-search/SKILL.md) | Find and explore Windows desktop APIs. |
| `/winston-ai-automation` | [`winston-ai-automation`](skills/automation-and-saas/winston-ai-automation/SKILL.md) | Automate Winston AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wit-ai-automation` | [`wit-ai-automation`](skills/automation-and-saas/wit-ai-automation/SKILL.md) | Automate Wit AI tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wiz-automation` | [`wiz-automation`](skills/automation-and-saas/wiz-automation/SKILL.md) | Automate Wiz tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wolfram-alpha-api-automation` | [`wolfram-alpha-api-automation`](skills/automation-and-saas/wolfram-alpha-api-automation/SKILL.md) | Automate Wolfram Alpha API tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/woodpecker-co-automation` | [`woodpecker-co-automation`](skills/automation-and-saas/woodpecker-co-automation/SKILL.md) | Automate Woodpecker co tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/workable-automation` | [`workable-automation`](skills/automation-and-saas/workable-automation/SKILL.md) | Automate Workable tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/workflow-automation` | [`workflow-automation`](skills/automation-and-saas/workflow-automation/SKILL.md) | Workflow automation is the infrastructure that makes AI agents. |
| `/workiom-automation` | [`workiom-automation`](skills/automation-and-saas/workiom-automation/SKILL.md) | Automate Workiom tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/worksnaps-automation` | [`worksnaps-automation`](skills/automation-and-saas/worksnaps-automation/SKILL.md) | Automate Worksnaps tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wp-interactivity-api` | [`wp-interactivity-api`](skills/automation-and-saas/wp-interactivity-api/SKILL.md) | Use when building or debugging WordPress Interactivity API features (data-wp-* directives, @wordpress/interactivity. |
| `/wrike-automation` | [`wrike-automation`](skills/automation-and-saas/wrike-automation/SKILL.md) | Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. |
| `/writer-automation` | [`writer-automation`](skills/automation-and-saas/writer-automation/SKILL.md) | Automate Writer tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/x-twitter-scraper` | [`x-twitter-scraper`](skills/automation-and-saas/x-twitter-scraper/SKILL.md) | Build GitHub Copilot workflows with Xquik X API SDKs, REST endpoints, MCP tools, signed webhooks, tweet search, user. |
| `/y-gy-automation` | [`y-gy-automation`](skills/automation-and-saas/y-gy-automation/SKILL.md) | Automate Y Gy tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yandex-automation` | [`yandex-automation`](skills/automation-and-saas/yandex-automation/SKILL.md) | Automate Yandex tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yelp-automation` | [`yelp-automation`](skills/automation-and-saas/yelp-automation/SKILL.md) | Automate Yelp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yes-md` | [`yes-md`](skills/automation-and-saas/yes-md/SKILL.md) | 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. |
| `/ynab-automation` | [`ynab-automation`](skills/automation-and-saas/ynab-automation/SKILL.md) | Automate Ynab tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/yousearch-automation` | [`yousearch-automation`](skills/automation-and-saas/yousearch-automation/SKILL.md) | Automate Yousearch tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/youtube-automation` | [`youtube-automation`](skills/automation-and-saas/youtube-automation/SKILL.md) | Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics. |
| `/zapier-make-patterns` | [`zapier-make-patterns`](skills/automation-and-saas/zapier-make-patterns/SKILL.md) | No-code automation democratizes workflow building. Zapier and Make. |
| `/zendesk-automation` | [`zendesk-automation`](skills/automation-and-saas/zendesk-automation/SKILL.md) | Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. |
| `/zenrows-automation` | [`zenrows-automation`](skills/automation-and-saas/zenrows-automation/SKILL.md) | Automate Zenrows tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zenserp-automation` | [`zenserp-automation`](skills/automation-and-saas/zenserp-automation/SKILL.md) | Automate Zenserp tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zeplin-automation` | [`zeplin-automation`](skills/automation-and-saas/zeplin-automation/SKILL.md) | Automate Zeplin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zerobounce-automation` | [`zerobounce-automation`](skills/automation-and-saas/zerobounce-automation/SKILL.md) | Automate Zerobounce tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-automation` | [`zoho-automation`](skills/automation-and-saas/zoho-automation/SKILL.md) | Automate Zoho tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-bigin-automation` | [`zoho-bigin-automation`](skills/automation-and-saas/zoho-bigin-automation/SKILL.md) | Automate Zoho Bigin tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-crm-automation` | [`zoho-crm-automation`](skills/automation-and-saas/zoho-crm-automation/SKILL.md) | Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. |
| `/zoho-inventory-automation` | [`zoho-inventory-automation`](skills/automation-and-saas/zoho-inventory-automation/SKILL.md) | Automate Zoho Inventory tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-invoice-automation` | [`zoho-invoice-automation`](skills/automation-and-saas/zoho-invoice-automation/SKILL.md) | Automate Zoho Invoice tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho-mail-automation` | [`zoho-mail-automation`](skills/automation-and-saas/zoho-mail-automation/SKILL.md) | Automate Zoho Mail tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/zoho_bigin-automation` | [`zoho_bigin-automation`](skills/automation-and-saas/zoho_bigin-automation/SKILL.md) | Automate Zoho Bigin tasks via Rube MCP (Composio): pipelines, contacts, companies, products, and small business CRM. |
| `/zoho_books-automation` | [`zoho_books-automation`](skills/automation-and-saas/zoho_books-automation/SKILL.md) | Automate Zoho Books tasks via Rube MCP (Composio): invoices, expenses, contacts, payments, and accounting. |
| `/zoho_desk-automation` | [`zoho_desk-automation`](skills/automation-and-saas/zoho_desk-automation/SKILL.md) | Automate Zoho Desk tasks via Rube MCP (Composio): tickets, contacts, agents, departments, and help desk operations. |
| `/zoho_inventory-automation` | [`zoho_inventory-automation`](skills/automation-and-saas/zoho_inventory-automation/SKILL.md) | Automate Zoho Inventory tasks via Rube MCP (Composio): items, orders, warehouses, shipments, and stock management. |
| `/zoho_invoice-automation` | [`zoho_invoice-automation`](skills/automation-and-saas/zoho_invoice-automation/SKILL.md) | Automate Zoho Invoice tasks via Rube MCP (Composio): invoices, estimates, expenses, clients, and payment tracking. |
| `/zoho_mail-automation` | [`zoho_mail-automation`](skills/automation-and-saas/zoho_mail-automation/SKILL.md) | Automate Zoho Mail tasks via Rube MCP (Composio): email sending, folders, labels, and mailbox management. |
| `/zoom-automation` | [`zoom-automation`](skills/automation-and-saas/zoom-automation/SKILL.md) | Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). |
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
| `/angular-best-practices` | [`angular-best-practices`](skills/design-and-creative/angular-best-practices/SKILL.md) | Angular performance optimization and best practices guide. |
| `/animejs-animation` | [`animejs-animation`](skills/design-and-creative/animejs-animation/SKILL.md) | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| `/antigravity-design-expert` | [`antigravity-design-expert`](skills/design-and-creative/antigravity-design-expert/SKILL.md) | Core UI/UX engineering skill for building highly interactive, spatial, weightless. |
| `/architecture` | [`architecture`](skills/design-and-creative/architecture/SKILL.md) | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. |
| `/architecture-patterns` | [`architecture-patterns`](skills/design-and-creative/architecture-patterns/SKILL.md) | Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture. |
| `/audio-transcriber` | [`audio-transcriber`](skills/design-and-creative/audio-transcriber/SKILL.md) | Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration. |
| `/automate-this` | [`automate-this`](skills/design-and-creative/automate-this/SKILL.md) | Analyze a screen recording of a manual process and produce targeted, working automation scripts. |
| `/azure-ai-voicelive-dotnet` | [`azure-ai-voicelive-dotnet`](skills/design-and-creative/azure-ai-voicelive-dotnet/SKILL.md) | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| `/azure-ai-voicelive-java` | [`azure-ai-voicelive-java`](skills/design-and-creative/azure-ai-voicelive-java/SKILL.md) | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| `/azure-ai-voicelive-py` | [`azure-ai-voicelive-py`](skills/design-and-creative/azure-ai-voicelive-py/SKILL.md) | Build real-time voice AI applications using Azure AI Voice Live SDK (azure-ai-voicelive). |
| `/azure-ai-voicelive-ts` | [`azure-ai-voicelive-ts`](skills/design-and-creative/azure-ai-voicelive-ts/SKILL.md) | Azure AI Voice Live SDK for JavaScript/TypeScript. |
| `/azure-resource-visualizer` | [`azure-resource-visualizer`](skills/design-and-creative/azure-resource-visualizer/SKILL.md) | Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between. |
| `/azure-smart-city-iot-solution-builder` | [`azure-smart-city-iot-solution-builder`](skills/design-and-creative/azure-smart-city-iot-solution-builder/SKILL.md) | Design and plan end-to-end Azure IoT and Smart City solutions: requirements, architecture, security, operations, cost. |
| `/azure-speech-to-text-rest-py` | [`azure-speech-to-text-rest-py`](skills/design-and-creative/azure-speech-to-text-rest-py/SKILL.md) | Azure Speech to Text REST API for short audio (Python). |
| `/brainstorming` | [`brainstorming`](skills/design-and-creative/brainstorming/SKILL.md) | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. |
| `/brooks-lint` | [`brooks-lint`](skills/design-and-creative/brooks-lint/SKILL.md) | AI code reviewer grounded in classic software engineering books for catching design smells, coupling issues. |
| `/canvas-design` | [`canvas-design`](skills/design-and-creative/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. |
| `/cirq` | [`cirq`](skills/design-and-creative/cirq/SKILL.md) | Cirq is Google Quantum AI's open-source framework for designing, simulating. |
| `/clean-code` | [`clean-code`](skills/design-and-creative/clean-code/SKILL.md) | This skill embodies the principles of \"Clean Code\" by Robert C. |
| `/code-refactoring-refactor-clean` | [`code-refactoring-refactor-clean`](skills/design-and-creative/code-refactoring-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns. |
| `/codebase-cleanup-refactor-clean` | [`codebase-cleanup-refactor-clean`](skills/design-and-creative/codebase-cleanup-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns. |
| `/color-font-skill` | [`color-font-skill`](skills/design-and-creative/color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. |
| `/competitive-ads-extractor` | [`competitive-ads-extractor`](skills/design-and-creative/competitive-ads-extractor/SKILL.md) | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging,. |
| `/conductor-validator` | [`conductor-validator`](skills/design-and-creative/conductor-validator/SKILL.md) | Validates Conductor project artifacts for completeness,. |
| `/constant-time-analysis` | [`constant-time-analysis`](skills/design-and-creative/constant-time-analysis/SKILL.md) | Analyze cryptographic code to detect operations that leak secret data through execution timing variations. |
| `/content-creator` | [`content-creator`](skills/design-and-creative/content-creator/SKILL.md) | Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks. |
| `/content-research-writer` | [`content-research-writer`](skills/design-and-creative/content-research-writer/SKILL.md) | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines. |
| `/context-degradation` | [`context-degradation`](skills/design-and-creative/context-degradation/SKILL.md) | Language models exhibit predictable degradation patterns as context length increases. |
| `/context-driven-development` | [`context-driven-development`](skills/design-and-creative/context-driven-development/SKILL.md) | Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI. |
| `/context-optimization` | [`context-optimization`](skills/design-and-creative/context-optimization/SKILL.md) | Context optimization extends the effective capacity of limited context windows through strategic compression, masking,. |
| `/copilot-cli-quickstart` | [`copilot-cli-quickstart`](skills/design-and-creative/copilot-cli-quickstart/SKILL.md) | Use this skill when someone wants to learn GitHub Copilot CLI from scratch. |
| `/cosmosdb-datamodeling` | [`cosmosdb-datamodeling`](skills/design-and-creative/cosmosdb-datamodeling/SKILL.md) | Step-by-step guide for capturing key application requirements for NoSQL use-case and produce Azure Cosmos DB Data NoSQL. |
| `/cpp-pro` | [`cpp-pro`](skills/design-and-creative/cpp-pro/SKILL.md) | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. |
| `/create-branch` | [`create-branch`](skills/design-and-creative/create-branch/SKILL.md) | Create a git branch following Sentry naming conventions. |
| `/create-implementation-plan` | [`create-implementation-plan`](skills/design-and-creative/create-implementation-plan/SKILL.md) | Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design,. |
| `/create-issue-gate` | [`create-issue-gate`](skills/design-and-creative/create-issue-gate/SKILL.md) | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| `/customer-psychographic-profiler` | [`customer-psychographic-profiler`](skills/design-and-creative/customer-psychographic-profiler/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/daily-gift` | [`daily-gift`](skills/design-and-creative/daily-gift/SKILL.md) | Relationship-aware daily gift engine with five-stage creative pipeline — editorial judgment, synthesis, concept. |
| `/ddd-strategic-design` | [`ddd-strategic-design`](skills/design-and-creative/ddd-strategic-design/SKILL.md) | Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains. |
| `/debug-buttercup` | [`debug-buttercup`](skills/design-and-creative/debug-buttercup/SKILL.md) | All pods run in namespace crs. |
| `/debugging-toolkit-smart-debug` | [`debugging-toolkit-smart-debug`](skills/design-and-creative/debugging-toolkit-smart-debug/SKILL.md) | Use when working with debugging toolkit smart debug. |
| `/defi-protocol-templates` | [`defi-protocol-templates`](skills/design-and-creative/defi-protocol-templates/SKILL.md) | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. |
| `/defuddle` | [`defuddle`](skills/design-and-creative/defuddle/SKILL.md) | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. |
| `/design-md` | [`design-md`](skills/design-and-creative/design-md/SKILL.md) | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files. |
| `/design-orchestration` | [`design-orchestration`](skills/design-and-creative/design-orchestration/SKILL.md) | Orchestrates design workflows by routing work through brainstorming, multi-agent review. |
| `/design-spells` | [`design-spells`](skills/design-and-creative/design-spells/SKILL.md) | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| `/design-style-skill` | [`design-style-skill`](skills/design-and-creative/design-style-skill/SKILL.md) | Select a consistent visual design system for PPT slides using radius/spacing style recipes. |
| `/design-systems` | [`design-systems`](skills/design-and-creative/design-systems/SKILL.md) | Bold aesthetic direction guidance for web design. |
| `/docs-architect` | [`docs-architect`](skills/design-and-creative/docs-architect/SKILL.md) | Creates comprehensive technical documentation from existing codebases. |
| `/domain-driven-design` | [`domain-driven-design`](skills/design-and-creative/domain-driven-design/SKILL.md) | Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns. |
| `/domain-name-brainstormer` | [`domain-name-brainstormer`](skills/design-and-creative/domain-name-brainstormer/SKILL.md) | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). |
| `/dotnet-design-pattern-review` | [`dotnet-design-pattern-review`](skills/design-and-creative/dotnet-design-pattern-review/SKILL.md) | Review the C#/.NET code for design pattern implementation and suggest improvements. |
| `/emotional-arc-designer` | [`emotional-arc-designer`](skills/design-and-creative/emotional-arc-designer/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/employment-contract-templates` | [`employment-contract-templates`](skills/design-and-creative/employment-contract-templates/SKILL.md) | Templates and patterns for creating legally sound employment documentation including contracts, offer letters, and HR policies. |
| `/error-diagnostics-smart-debug` | [`error-diagnostics-smart-debug`](skills/design-and-creative/error-diagnostics-smart-debug/SKILL.md) | Use when working with error diagnostics smart debug. |
| `/event-sourcing-architect` | [`event-sourcing-architect`](skills/design-and-creative/event-sourcing-architect/SKILL.md) | Expert in event sourcing, CQRS, and event-driven architecture patterns. |
| `/event-store-design` | [`event-store-design`](skills/design-and-creative/event-store-design/SKILL.md) | Design and implement event stores for event-sourced systems. |
| `/fal-audio` | [`fal-audio`](skills/design-and-creative/fal-audio/SKILL.md) | Text-to-speech and speech-to-text using fal.ai audio models. |
| `/fal-upscale` | [`fal-upscale`](skills/design-and-creative/fal-upscale/SKILL.md) | Upscale and enhance image and video resolution using AI. |
| `/finnish-humanizer` | [`finnish-humanizer`](skills/design-and-creative/finnish-humanizer/SKILL.md) | Detect and remove AI-generated markers from Finnish text, making it sound like a native Finnish speaker wrote it. |
| `/fixing-accessibility` | [`fixing-accessibility`](skills/design-and-creative/fixing-accessibility/SKILL.md) | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast. |
| `/from-the-other-side-vega` | [`from-the-other-side-vega`](skills/design-and-creative/from-the-other-side-vega/SKILL.md) | Patterns and lived experience from Vega, an AI partner in a deep long-term partnership. |
| `/frontend-design-review` | [`frontend-design-review`](skills/design-and-creative/frontend-design-review/SKILL.md) | Review and create distinctive, production-grade frontend interfaces with high design quality and design system compliance. |
| `/game-engine` | [`game-engine`](skills/design-and-creative/game-engine/SKILL.md) | Expert skill for building web-based game engines and games using HTML5, Canvas, WebGL, and JavaScript. |
| `/gif-sticker-maker` | [`gif-sticker-maker`](skills/design-and-creative/gif-sticker-maker/SKILL.md) | Convert photos (people, pets, objects, logos) into 4 animated GIF stickers with captions. |
| `/grpc-golang` | [`grpc-golang`](skills/design-and-creative/grpc-golang/SKILL.md) | Build production-ready gRPC services in Go with mTLS, streaming, and observability. |
| `/gsap-framer-scroll-animation` | [`gsap-framer-scroll-animation`](skills/design-and-creative/gsap-framer-scroll-animation/SKILL.md) | Use this skill whenever the user wants to build scroll animations, scroll effects, parallax, scroll-triggered reveals,. |
| `/gtm-developer-ecosystem` | [`gtm-developer-ecosystem`](skills/design-and-creative/gtm-developer-ecosystem/SKILL.md) | Build and scale developer-led adoption through ecosystem programs. |
| `/gtm-operating-cadence` | [`gtm-operating-cadence`](skills/design-and-creative/gtm-operating-cadence/SKILL.md) | Design meeting rhythms, metric reporting, quarterly planning, and decision-making velocity for scaling companies. |
| `/gtm-partnership-architecture` | [`gtm-partnership-architecture`](skills/design-and-creative/gtm-partnership-architecture/SKILL.md) | Build and scale partner ecosystems that drive revenue and platform adoption. |
| `/gtm-positioning-strategy` | [`gtm-positioning-strategy`](skills/design-and-creative/gtm-positioning-strategy/SKILL.md) | Find and own a defensible market position. |
| `/gtm-technical-product-pricing` | [`gtm-technical-product-pricing`](skills/design-and-creative/gtm-technical-product-pricing/SKILL.md) | Pricing strategy for technical products. |
| `/health-trend-analyzer` | [`health-trend-analyzer`](skills/design-and-creative/health-trend-analyzer/SKILL.md) | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重. |
| `/helm-chart-scaffolding` | [`helm-chart-scaffolding`](skills/design-and-creative/helm-chart-scaffolding/SKILL.md) | Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications. |
| `/hig-foundations` | [`hig-foundations`](skills/design-and-creative/hig-foundations/SKILL.md) | Apple Human Interface Guidelines design foundations. |
| `/hig-platforms` | [`hig-platforms`](skills/design-and-creative/hig-platforms/SKILL.md) | Apple Human Interface Guidelines for platform-specific design. |
| `/hig-project-context` | [`hig-project-context`](skills/design-and-creative/hig-project-context/SKILL.md) | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| `/high-end-visual-design` | [`high-end-visual-design`](skills/design-and-creative/high-end-visual-design/SKILL.md) | Use when designing expensive agency-grade interfaces with premium fonts, spatial rhythm, soft depth, and fluid microinteractions. |
| `/hr-pro` | [`hr-pro`](skills/design-and-creative/hr-pro/SKILL.md) | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies. |
| `/hugging-face-paper-publisher` | [`hugging-face-paper-publisher`](skills/design-and-creative/hugging-face-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. |
| `/huggingface-paper-publisher` | [`huggingface-paper-publisher`](skills/design-and-creative/huggingface-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. |
| `/humanize-chinese` | [`humanize-chinese`](skills/design-and-creative/humanize-chinese/SKILL.md) | Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction. |
| `/image` | [`image`](skills/design-and-creative/image/SKILL.md) | When the user wants to create, generate, edit. |
| `/image-annotations` | [`image-annotations`](skills/design-and-creative/image-annotations/SKILL.md) | Annotate screenshots, diagrams, and images with callout rectangles, arrows, labels, and color-coded highlights using PIL. |
| `/image-studio` | [`image-studio`](skills/design-and-creative/image-studio/SKILL.md) | Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e. |
| `/imagen` | [`imagen`](skills/design-and-creative/imagen/SKILL.md) | AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders,. |
| `/incident-response-smart-fix` | [`incident-response-smart-fix`](skills/design-and-creative/incident-response-smart-fix/SKILL.md) | [Extended thinking: This workflow implements a sophisticated debugging and resolution pipeline that leverages. |
| `/ingest-youtube` | [`ingest-youtube`](skills/design-and-creative/ingest-youtube/SKILL.md) | Pull a YouTube video transcript into a queryable markdown vault with yt-dlp subtitle discovery, VTT cleanup, metadata. |
| `/invoice-organizer` | [`invoice-organizer`](skills/design-and-creative/invoice-organizer/SKILL.md) | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information,. |
| `/javax-to-jakarta-migration` | [`javax-to-jakarta-migration`](skills/design-and-creative/javax-to-jakarta-migration/SKILL.md) | Migrate Java code from javax.* to jakarta.* namespace. |
| `/json-canvas` | [`json-canvas`](skills/design-and-creative/json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. |
| `/kpi-dashboard-design` | [`kpi-dashboard-design`](skills/design-and-creative/kpi-dashboard-design/SKILL.md) | Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions. |
| `/leiloeiro-juridico` | [`leiloeiro-juridico`](skills/design-and-creative/leiloeiro-juridico/SKILL.md) | Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus. |
| `/lightning-architecture-review` | [`lightning-architecture-review`](skills/design-and-creative/lightning-architecture-review/SKILL.md) | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. |
| `/lightning-channel-factories` | [`lightning-channel-factories`](skills/design-and-creative/lightning-channel-factories/SKILL.md) | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures. |
| `/linkedin-post-formatter` | [`linkedin-post-formatter`](skills/design-and-creative/linkedin-post-formatter/SKILL.md) | Format and draft compelling LinkedIn posts using Unicode bold/italic styling, visual separators, structured sections. |
| `/loss-aversion-designer` | [`loss-aversion-designer`](skills/design-and-creative/loss-aversion-designer/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/machine-learning-ops-ml-pipeline` | [`machine-learning-ops-ml-pipeline`](skills/design-and-creative/machine-learning-ops-ml-pipeline/SKILL.md) | Design and implement a complete ML pipeline for: $ARGUMENTS. |
| `/magic-animator` | [`magic-animator`](skills/design-and-creative/magic-animator/SKILL.md) | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| `/makepad-animation` | [`makepad-animation`](skills/design-and-creative/makepad-animation/SKILL.md) | CRITICAL: Use for Makepad animation system. |
| `/makepad-basics` | [`makepad-basics`](skills/design-and-creative/makepad-basics/SKILL.md) | CRITICAL: Use for Makepad getting started and app structure. |
| `/makepad-dsl` | [`makepad-dsl`](skills/design-and-creative/makepad-dsl/SKILL.md) | CRITICAL: Use for Makepad DSL syntax and inheritance. |
| `/makepad-shaders` | [`makepad-shaders`](skills/design-and-creative/makepad-shaders/SKILL.md) | CRITICAL: Use for Makepad shader system. |
| `/makepad-skills` | [`makepad-skills`](skills/design-and-creative/makepad-skills/SKILL.md) | Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting. |
| `/market-sizing-analysis` | [`market-sizing-analysis`](skills/design-and-creative/market-sizing-analysis/SKILL.md) | Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market. |
| `/matplotlib` | [`matplotlib`](skills/design-and-creative/matplotlib/SKILL.md) | Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. |
| `/memory-forensics` | [`memory-forensics`](skills/design-and-creative/memory-forensics/SKILL.md) | Comprehensive techniques for acquiring, analyzing. |
| `/memory-safety-patterns` | [`memory-safety-patterns`](skills/design-and-creative/memory-safety-patterns/SKILL.md) | Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management. |
| `/mentoring-juniors` | [`mentoring-juniors`](skills/design-and-creative/mentoring-juniors/SKILL.md) | Socratic mentoring for junior developers and AI newcomers. Guides through questions, never answers. |
| `/mermaid-expert` | [`mermaid-expert`](skills/design-and-creative/mermaid-expert/SKILL.md) | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. |
| `/minimax-multimodal-toolkit` | [`minimax-multimodal-toolkit`](skills/design-and-creative/minimax-multimodal-toolkit/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. |
| `/minimax-music-gen` | [`minimax-music-gen`](skills/design-and-creative/minimax-music-gen/SKILL.md) | Use when user wants to generate music, songs, or audio tracks. |
| `/minimax-music-playlist` | [`minimax-music-playlist`](skills/design-and-creative/minimax-music-playlist/SKILL.md) | Generate personalized music playlists by analyzing the user's music taste and generation feedback history. |
| `/mmx-cli` | [`mmx-cli`](skills/design-and-creative/mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. |
| `/napkin` | [`napkin`](skills/design-and-creative/napkin/SKILL.md) | Visual whiteboard collaboration for Copilot CLI. |
| `/nerdzao-elite` | [`nerdzao-elite`](skills/design-and-creative/nerdzao-elite/SKILL.md) | Senior Elite Software Engineer (15+) and Senior Product Designer. |
| `/observability-monitoring-slo-implement` | [`observability-monitoring-slo-implement`](skills/design-and-creative/observability-monitoring-slo-implement/SKILL.md) | You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error. |
| `/obsidian-cli` | [`obsidian-cli`](skills/design-and-creative/obsidian-cli/SKILL.md) | Use the Obsidian CLI to read, create, search. |
| `/odoo-accounting-setup` | [`odoo-accounting-setup`](skills/design-and-creative/odoo-accounting-setup/SKILL.md) | Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms. |
| `/odoo-edi-connector` | [`odoo-edi-connector`](skills/design-and-creative/odoo-edi-connector/SKILL.md) | Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding. |
| `/osterwalder-canvas-architect` | [`osterwalder-canvas-architect`](skills/design-and-creative/osterwalder-canvas-architect/SKILL.md) | Iterative consultant agent for building and validating logically consistent 9-block Business Model Canvases. |
| `/planning-and-task-breakdown` | [`planning-and-task-breakdown`](skills/design-and-creative/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. |
| `/plotly` | [`plotly`](skills/design-and-creative/plotly/SKILL.md) | Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. |
| `/power-bi-model-design-review` | [`power-bi-model-design-review`](skills/design-and-creative/power-bi-model-design-review/SKILL.md) | Comprehensive Power BI data model design review prompt for evaluating model architecture, relationships. |
| `/power-bi-report-design-consultation` | [`power-bi-report-design-consultation`](skills/design-and-creative/power-bi-report-design-consultation/SKILL.md) | Power BI report visualization design prompt for creating effective, user-friendly. |
| `/privacy-by-design` | [`privacy-by-design`](skills/design-and-creative/privacy-by-design/SKILL.md) | Use when building apps that collect user data. |
| `/product-design` | [`product-design`](skills/design-and-creative/product-design/SKILL.md) | Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design. |
| `/product-inventor` | [`product-inventor`](skills/design-and-creative/product-inventor/SKILL.md) | Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering,. |
| `/professional-proofreader` | [`professional-proofreader`](skills/design-and-creative/professional-proofreader/SKILL.md) | Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice". |
| `/puzzle-activity-planner` | [`puzzle-activity-planner`](skills/design-and-creative/puzzle-activity-planner/SKILL.md) | Plan puzzle-based activities for classrooms, parties, and events with pre-configured generator links. |
| `/recsys-pipeline-architect` | [`recsys-pipeline-architect`](skills/design-and-creative/recsys-pipeline-architect/SKILL.md) | Designs composable recommendation, ranking. |
| `/redesign-existing-projects` | [`redesign-existing-projects`](skills/design-and-creative/redesign-existing-projects/SKILL.md) | Use when upgrading existing websites or apps by auditing generic UI patterns and applying premium design fixes without rewrites. |
| `/refactor` | [`refactor`](skills/design-and-creative/refactor/SKILL.md) | Surgical code refactoring to improve maintainability without changing behavior. |
| `/refactor-plan` | [`refactor-plan`](skills/design-and-creative/refactor-plan/SKILL.md) | Create a concrete plan before starting a multi-file refactor. |
| `/remotion-best-practices` | [`remotion-best-practices`](skills/design-and-creative/remotion-best-practices/SKILL.md) | Best practices for Remotion - Video creation in React. |
| `/resemble-detect` | [`resemble-detect`](skills/design-and-creative/resemble-detect/SKILL.md) | Deepfake detection and media safety — detect AI-generated audio, images, video. |
| `/rich-elicitation` | [`rich-elicitation`](skills/design-and-creative/rich-elicitation/SKILL.md) | Asks clarifying questions in multiple rounds before starting ambiguous tasks. |
| `/robius-app-architecture` | [`robius-app-architecture`](skills/design-and-creative/robius-app-architecture/SKILL.md) | CRITICAL: Use for Robius app architecture patterns. |
| `/robius-state-management` | [`robius-state-management`](skills/design-and-creative/robius-state-management/SKILL.md) | CRITICAL: Use for Robius state management patterns. |
| `/robius-widget-patterns` | [`robius-widget-patterns`](skills/design-and-creative/robius-widget-patterns/SKILL.md) | CRITICAL: Use for Robius widget patterns. |
| `/satori` | [`satori`](skills/design-and-creative/satori/SKILL.md) | Clinically informed wisdom companion blending psychology and philosophy into a structured thinking partner. |
| `/screen-recording` | [`screen-recording`](skills/design-and-creative/screen-recording/SKILL.md) | Create annotated animated GIF demos and screen recordings for pull requests and documentation. |
| `/seaborn` | [`seaborn`](skills/design-and-creative/seaborn/SKILL.md) | Seaborn is a Python visualization library for creating publication-quality statistical graphics. |
| `/seek-and-analyze-video` | [`seek-and-analyze-video`](skills/design-and-creative/seek-and-analyze-video/SKILL.md) | Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence. |
| `/shader-dev` | [`shader-dev`](skills/design-and-creative/shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid. |
| `/shader-programming-glsl` | [`shader-programming-glsl`](skills/design-and-creative/shader-programming-glsl/SKILL.md) | Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms. |
| `/site-architecture` | [`site-architecture`](skills/design-and-creative/site-architecture/SKILL.md) | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. |
| `/skill-router` | [`skill-router`](skills/design-and-creative/skill-router/SKILL.md) | Use when the user is unsure which skill to use or where to start. |
| `/slack-gif-creator` | [`slack-gif-creator`](skills/design-and-creative/slack-gif-creator/SKILL.md) | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. |
| `/slang-shader-engineer` | [`slang-shader-engineer`](skills/design-and-creative/slang-shader-engineer/SKILL.md) | Use when working with Slang shaders, shader modules, HLSL-compatible GPU code, graphics pipelines, compute shaders,. |
| `/software-architecture` | [`software-architecture`](skills/design-and-creative/software-architecture/SKILL.md) | Guide for quality focused software architecture. |
| `/spark-optimization` | [`spark-optimization`](skills/design-and-creative/spark-optimization/SKILL.md) | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. |
| `/spec-driven-development` | [`spec-driven-development`](skills/design-and-creative/spec-driven-development/SKILL.md) | Creates specs before coding. |
| `/stability-ai` | [`stability-ai`](skills/design-and-creative/stability-ai/SKILL.md) | Geracao de imagens via Stability AI (SD3.5, Ultra, Core). |
| `/startup-analyst` | [`startup-analyst`](skills/design-and-creative/startup-analyst/SKILL.md) | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis. |
| `/startup-business-analyst-business-case` | [`startup-business-analyst-business-case`](skills/design-and-creative/startup-business-analyst-business-case/SKILL.md) | Generate comprehensive investor-ready business case document with. |
| `/startup-business-analyst-financial-projections` | [`startup-business-analyst-financial-projections`](skills/design-and-creative/startup-business-analyst-financial-projections/SKILL.md) | Create detailed 3-5 year financial model with revenue, costs, cash. |
| `/startup-business-analyst-market-opportunity` | [`startup-business-analyst-market-opportunity`](skills/design-and-creative/startup-business-analyst-market-opportunity/SKILL.md) | Generate comprehensive market opportunity analysis with TAM/SAM/SOM. |
| `/startup-financial-modeling` | [`startup-financial-modeling`](skills/design-and-creative/startup-financial-modeling/SKILL.md) | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis. |
| `/startup-metrics-framework` | [`startup-metrics-framework`](skills/design-and-creative/startup-metrics-framework/SKILL.md) | Comprehensive guide to tracking, calculating. |
| `/stitch-design-taste` | [`stitch-design-taste`](skills/design-and-creative/stitch-design-taste/SKILL.md) | Use when generating Google Stitch DESIGN.md systems for premium typography, color, layout, motion intent. |
| `/summarize` | [`summarize`](skills/design-and-creative/summarize/SKILL.md) | Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube). |
| `/support-prerendering` | [`support-prerendering`](skills/design-and-creative/support-prerendering/SKILL.md) | Make interactive Blazor components work correctly with prerendering. |
| `/team-composition-analysis` | [`team-composition-analysis`](skills/design-and-creative/team-composition-analysis/SKILL.md) | Design optimal team structures, hiring plans, compensation strategies. |
| `/test-fixing` | [`test-fixing`](skills/design-and-creative/test-fixing/SKILL.md) | Systematically identify and fix all failing tests using smart grouping strategies. |
| `/theme-factory` | [`theme-factory`](skills/design-and-creative/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. |
| `/threejs-animation` | [`threejs-animation`](skills/design-and-creative/threejs-animation/SKILL.md) | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. |
| `/threejs-geometry` | [`threejs-geometry`](skills/design-and-creative/threejs-geometry/SKILL.md) | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. |
| `/threejs-postprocessing` | [`threejs-postprocessing`](skills/design-and-creative/threejs-postprocessing/SKILL.md) | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. |
| `/threejs-shaders` | [`threejs-shaders`](skills/design-and-creative/threejs-shaders/SKILL.md) | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. |
| `/threejs-skills` | [`threejs-skills`](skills/design-and-creative/threejs-skills/SKILL.md) | Create 3D scenes, interactive experiences, and visual effects using Three.js. |
| `/tool-design` | [`tool-design`](skills/design-and-creative/tool-design/SKILL.md) | Build tools that agents can use effectively, including architectural reduction patterns. |
| `/transformers-js` | [`transformers-js`](skills/design-and-creative/transformers-js/SKILL.md) | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. |
| `/transloadit-media-processing` | [`transloadit-media-processing`](skills/design-and-creative/transloadit-media-processing/SKILL.md) | Process media files (video, audio, images, documents) using Transloadit. |
| `/ui-visual-validator` | [`ui-visual-validator`](skills/design-and-creative/ui-visual-validator/SKILL.md) | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| `/unity-developer` | [`unity-developer`](skills/design-and-creative/unity-developer/SKILL.md) | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. |
| `/update-implementation-plan` | [`update-implementation-plan`](skills/design-and-creative/update-implementation-plan/SKILL.md) | Update an existing implementation plan file with new or update requirements to provide new features, refactoring. |
| `/using-superpowers` | [`using-superpowers`](skills/design-and-creative/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY. |
| `/video` | [`video`](skills/design-and-creative/video/SKILL.md) | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. |
| `/videodb` | [`videodb`](skills/design-and-creative/videodb/SKILL.md) | Video and audio perception, indexing, and editing. |
| `/videodb-skills` | [`videodb-skills`](skills/design-and-creative/videodb-skills/SKILL.md) | Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK. |
| `/visual-emotion-engineer` | [`visual-emotion-engineer`](skills/design-and-creative/visual-emotion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/vizcom` | [`vizcom`](skills/design-and-creative/vizcom/SKILL.md) | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| `/voice-ai-development` | [`voice-ai-development`](skills/design-and-creative/voice-ai-development/SKILL.md) | Expert in building voice AI applications - from real-time voice. |
| `/voice-ai-engine-development` | [`voice-ai-engine-development`](skills/design-and-creative/voice-ai-engine-development/SKILL.md) | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents. |
| `/web-design-reviewer` | [`web-design-reviewer`](skills/design-and-creative/web-design-reviewer/SKILL.md) | This skill enables visual inspection of websites running locally or remotely to identify and fix design issues. |
| `/wordpress-theme-development` | [`wordpress-theme-development`](skills/design-and-creative/wordpress-theme-development/SKILL.md) | WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor. |
| `/workflow-orchestration-patterns` | [`workflow-orchestration-patterns`](skills/design-and-creative/workflow-orchestration-patterns/SKILL.md) | Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns. |
| `/wp-block-themes` | [`wp-block-themes`](skills/design-and-creative/wp-block-themes/SKILL.md) | Use when developing WordPress block themes: theme.json (global settings/styles), templates and template parts,. |
| `/x-article-publisher-skill` | [`x-article-publisher-skill`](skills/design-and-creative/x-article-publisher-skill/SKILL.md) | Publish articles to X/Twitter. |
| `/youtube-downloader` | [`youtube-downloader`](skills/design-and-creative/youtube-downloader/SKILL.md) | Download YouTube videos with customizable quality and format options. |
| `/youtube-summarizer` | [`youtube-summarizer`](skills/design-and-creative/youtube-summarizer/SKILL.md) | Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks. |

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
| `/bilig-workpaper` | [`bilig-workpaper`](skills/document-processing/bilig-workpaper/SKILL.md) | Use formula-backed WorkPaper JSON and MCP tools for agent spreadsheet tasks without driving Excel or a browser UI. |
| `/blueprint` | [`blueprint`](skills/document-processing/blueprint/SKILL.md) | Use when creating, editing, or reviewing WordPress Playground blueprint JSON files. |
| `/brag-sheet` | [`brag-sheet`](skills/document-processing/brag-sheet/SKILL.md) | Turn vague "what did I do?" into evidence-backed impact statements for performance reviews, self-reviews, promotion. |
| `/c4-architecture-c4-architecture` | [`c4-architecture-c4-architecture`](skills/document-processing/c4-architecture-c4-architecture/SKILL.md) | Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. |
| `/c4-code` | [`c4-code`](skills/document-processing/c4-code/SKILL.md) | Expert C4 Code-level documentation specialist. |
| `/c4-container` | [`c4-container`](skills/document-processing/c4-container/SKILL.md) | Expert C4 Container-level documentation specialist. |
| `/c4-context` | [`c4-context`](skills/document-processing/c4-context/SKILL.md) | Expert C4 Context-level documentation specialist. |
| `/clarity-gate` | [`clarity-gate`](skills/document-processing/clarity-gate/SKILL.md) | Pre-ingestion verification for epistemic quality in RAG systems. |
| `/code-documentation-code-explain` | [`code-documentation-code-explain`](skills/document-processing/code-documentation-code-explain/SKILL.md) | You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams. |
| `/code-documentation-doc-generate` | [`code-documentation-doc-generate`](skills/document-processing/code-documentation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. |
| `/code-review-excellence` | [`code-review-excellence`](skills/document-processing/code-review-excellence/SKILL.md) | Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis. |
| `/codebase-to-wordpress-converter` | [`codebase-to-wordpress-converter`](skills/document-processing/codebase-to-wordpress-converter/SKILL.md) | Expert skill for converting any codebase (React/HTML/Next.js) into a pixel-perfect, SEO-optimized, and dynamic WordPress theme. |
| `/comprehensive-review-pr-enhance` | [`comprehensive-review-pr-enhance`](skills/document-processing/comprehensive-review-pr-enhance/SKILL.md) | Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. |
| `/context-fundamentals` | [`context-fundamentals`](skills/document-processing/context-fundamentals/SKILL.md) | Context is the complete state available to a language model at inference time. |
| `/copilot-spaces` | [`copilot-spaces`](skills/document-processing/copilot-spaces/SKILL.md) | Use Copilot Spaces to provide project-specific context to conversations. |
| `/create-architectural-decision-record` | [`create-architectural-decision-record`](skills/document-processing/create-architectural-decision-record/SKILL.md) | Create an Architectural Decision Record (ADR) document for AI-optimized decision documentation. |
| `/create-technical-spike` | [`create-technical-spike`](skills/document-processing/create-technical-spike/SKILL.md) | Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation. |
| `/create-tldr-page` | [`create-tldr-page`](skills/document-processing/create-tldr-page/SKILL.md) | Create a tldr page from documentation URLs and command examples, requiring both URL and command name. |
| `/daily` | [`daily`](skills/document-processing/daily/SKILL.md) | Documentation and capabilities reference for Daily. |
| `/dbt-transformation-patterns` | [`dbt-transformation-patterns`](skills/document-processing/dbt-transformation-patterns/SKILL.md) | Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation. |
| `/documentation` | [`documentation`](skills/document-processing/documentation/SKILL.md) | Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. |
| `/documentation-and-adrs` | [`documentation-and-adrs`](skills/document-processing/documentation-and-adrs/SKILL.md) | Records decisions and documentation. |
| `/documentation-generation-doc-generate` | [`documentation-generation-doc-generate`](skills/document-processing/documentation-generation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. |
| `/documentation-templates` | [`documentation-templates`](skills/document-processing/documentation-templates/SKILL.md) | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| `/documentation-writer` | [`documentation-writer`](skills/document-processing/documentation-writer/SKILL.md) | Diátaxis Documentation Expert. |
| `/docx` | [`docx`](skills/document-processing/docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). |
| `/docx-official` | [`docx-official`](skills/document-processing/docx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .docx file. |
| `/drawio` | [`drawio`](skills/document-processing/drawio/SKILL.md) | Generate draw.io diagrams as .drawio files and export to PNG/SVG/PDF with embedded XML. |
| `/error-handling-patterns` | [`error-handling-patterns`](skills/document-processing/error-handling-patterns/SKILL.md) | Build resilient applications with robust error handling strategies that gracefully handle failures and provide. |
| `/eyeball` | [`eyeball`](skills/document-processing/eyeball/SKILL.md) | Document analysis with inline source screenshots. |
| `/google-cloud-waf-operational-excellence` | [`google-cloud-waf-operational-excellence`](skills/document-processing/google-cloud-waf-operational-excellence/SKILL.md) | Generates operations-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/googlesheets-automation` | [`googlesheets-automation`](skills/document-processing/googlesheets-automation/SKILL.md) | Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). |
| `/huggingface-zerogpu` | [`huggingface-zerogpu`](skills/document-processing/huggingface-zerogpu/SKILL.md) | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. |
| `/hybrid-search-implementation` | [`hybrid-search-implementation`](skills/document-processing/hybrid-search-implementation/SKILL.md) | Combine vector and keyword search for improved retrieval. |
| `/image-enhancer` | [`image-enhancer`](skills/document-processing/image-enhancer/SKILL.md) | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. |
| `/make-repo-contribution` | [`make-repo-contribution`](skills/document-processing/make-repo-contribution/SKILL.md) | All changes to code must follow the guidance documented in the repository. |
| `/markdown-to-html` | [`markdown-to-html`](skills/document-processing/markdown-to-html/SKILL.md) | Convert Markdown files to HTML similar to `marked.js`, `pandoc`, `gomarkdown/markdown`. |
| `/md-to-docx` | [`md-to-docx`](skills/document-processing/md-to-docx/SKILL.md) | Convert Markdown files to professionally formatted Word (.docx) documents with embedded PNG images — pure JavaScript,. |
| `/meeting-insights-analyzer` | [`meeting-insights-analyzer`](skills/document-processing/meeting-insights-analyzer/SKILL.md) | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. |
| `/minimax-docx` | [`minimax-docx`](skills/document-processing/minimax-docx/SKILL.md) | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). |
| `/minimax-pdf` | [`minimax-pdf`](skills/document-processing/minimax-pdf/SKILL.md) | Use this skill when visual quality and design identity matter for a PDF. |
| `/minimax-xlsx` | [`minimax-xlsx`](skills/document-processing/minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). |
| `/mkdocs-translations` | [`mkdocs-translations`](skills/document-processing/mkdocs-translations/SKILL.md) | Generate a language translation for a mkdocs documentation stack. |
| `/nanobanana-ppt-skills` | [`nanobanana-ppt-skills`](skills/document-processing/nanobanana-ppt-skills/SKILL.md) | AI-powered PPT generation with document analysis and styled images. |
| `/odoo-project-timesheet` | [`odoo-project-timesheet`](skills/document-processing/odoo-project-timesheet/SKILL.md) | Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts. |
| `/office-productivity` | [`office-productivity`](skills/document-processing/office-productivity/SKILL.md) | Office productivity workflow covering document creation, spreadsheet automation, presentation generation. |
| `/optimize-simplicite-logs` | [`optimize-simplicite-logs`](skills/document-processing/optimize-simplicite-logs/SKILL.md) | capability to parse Simplicité logs from a raw `.txt` file, filter fields to reduce noise. |
| `/pdf` | [`pdf`](skills/document-processing/pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. |
| `/pdf-conversion-router` | [`pdf-conversion-router`](skills/document-processing/pdf-conversion-router/SKILL.md) | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX. |
| `/pdf-official` | [`pdf-official`](skills/document-processing/pdf-official/SKILL.md) | This guide covers essential PDF processing operations using Python libraries and command-line tools. |
| `/pdftk-server` | [`pdftk-server`](skills/document-processing/pdftk-server/SKILL.md) | Skill for using the command-line tool pdftk (PDFtk Server) for working with PDF files. |
| `/ppt-editing-skill` | [`ppt-editing-skill`](skills/document-processing/ppt-editing-skill/SKILL.md) | Edit existing PowerPoint files or templates with XML-safe workflows. |
| `/pptx` | [`pptx`](skills/document-processing/pptx/SKILL.md) | Presentation creation, editing, and analysis. |
| `/pptx-generator` | [`pptx-generator`](skills/document-processing/pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations. |
| `/pptx-official` | [`pptx-official`](skills/document-processing/pptx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .pptx file. |
| `/prd` | [`prd`](skills/document-processing/prd/SKILL.md) | Generate high-quality Product Requirements Documents (PRDs) for software systems and AI-powered features. |
| `/protocol-reverse-engineering` | [`protocol-reverse-engineering`](skills/document-processing/protocol-reverse-engineering/SKILL.md) | Comprehensive techniques for capturing, analyzing. |
| `/publish-to-pages` | [`publish-to-pages`](skills/document-processing/publish-to-pages/SKILL.md) | Publish presentations and web content to GitHub Pages. |
| `/python-pptx-generator` | [`python-pptx-generator`](skills/document-processing/python-pptx-generator/SKILL.md) | Generate complete Python scripts that build polished PowerPoint decks with python-pptx and real slide content. |
| `/quasi-coder` | [`quasi-coder`](skills/document-processing/quasi-coder/SKILL.md) | Expert 10x engineer skill for interpreting and implementing code from shorthand, quasi-code, and natural language descriptions. |
| `/raffle-winner-picker` | [`raffle-winner-picker`](skills/document-processing/raffle-winner-picker/SKILL.md) | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. |
| `/readme` | [`readme`](skills/document-processing/readme/SKILL.md) | You are an expert technical writer creating comprehensive project documentation. |
| `/rhino3d-scripts` | [`rhino3d-scripts`](skills/document-processing/rhino3d-scripts/SKILL.md) | Authoring and debugging scripts for Rhinoceros 3D (Rhino 8 and later). |
| `/screenshots` | [`screenshots`](skills/document-processing/screenshots/SKILL.md) | Generate marketing screenshots of your app using Playwright. |
| `/skill-seekers` | [`skill-seekers`](skills/document-processing/skill-seekers/SKILL.md) | -Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes. |
| `/slide-making-skill` | [`slide-making-skill`](skills/document-processing/slide-making-skill/SKILL.md) | Implement single-slide PowerPoint pages with PptxGenJS. |
| `/source-driven-development` | [`source-driven-development`](skills/document-processing/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. |
| `/sred-project-organizer` | [`sred-project-organizer`](skills/document-processing/sred-project-organizer/SKILL.md) | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| `/text-to-pdf-automation` | [`text-to-pdf-automation`](skills/document-processing/text-to-pdf-automation/SKILL.md) | Automate Text To PDF tasks via Rube MCP (Composio). Always search tools first for current schemas. |
| `/wiki-architect` | [`wiki-architect`](skills/document-processing/wiki-architect/SKILL.md) | Analyzes code repositories and generates hierarchical documentation structures with onboarding guides. |
| `/wiki-llms-txt` | [`wiki-llms-txt`](skills/document-processing/wiki-llms-txt/SKILL.md) | Generates llms.txt and llms-full.txt files for LLM-friendly project documentation following the llms.txt specification. |
| `/wiki-onboarding` | [`wiki-onboarding`](skills/document-processing/wiki-onboarding/SKILL.md) | Generates four audience-tailored onboarding guides in an onboarding/ folder — Contributor, Staff Engineer, Executive. |
| `/wiki-page-writer` | [`wiki-page-writer`](skills/document-processing/wiki-page-writer/SKILL.md) | Generates rich technical documentation pages with dark-mode Mermaid diagrams, source code citations, and first-principles depth. |
| `/wordpress-centric-high-seo-optimized-blogwriting-skill` | [`wordpress-centric-high-seo-optimized-blogwriting-skill`](skills/document-processing/wordpress-centric-high-seo-optimized-blogwriting-skill/SKILL.md) | Create long-form, high-quality, SEO-optimized blog posts ready for WordPress with truth boxes and FAQ schema. |
| `/wordpress-woocommerce-development` | [`wordpress-woocommerce-development`](skills/document-processing/wordpress-woocommerce-development/SKILL.md) | WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization. |
| `/xlsx` | [`xlsx`](skills/document-processing/xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. |
| `/xlsx-official` | [`xlsx-official`](skills/document-processing/xlsx-official/SKILL.md) | Unless otherwise stated by the user or existing template. |
| `/zeroize-audit` | [`zeroize-audit`](skills/document-processing/zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler. |

---

### 📱 Frontend Development
> *User interface styling, mobile framework configurations (Flutter, iOS, Android, React Native), and responsive design.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/00-andruia-consultant` | [`00-andruia-consultant`](skills/frontend-development/00-andruia-consultant/SKILL.md) | Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia. |
| `/10-andruia-skill-smith` | [`10-andruia-skill-smith`](skills/frontend-development/10-andruia-skill-smith/SKILL.md) | Ingeniero de Sistemas de Andru.ia. |
| `/20-andruia-niche-intelligence` | [`20-andruia-niche-intelligence`](skills/frontend-development/20-andruia-niche-intelligence/SKILL.md) | Estratega de Inteligencia de Dominio de Andru.ia. |
| `/3d-web-experience` | [`3d-web-experience`](skills/frontend-development/3d-web-experience/SKILL.md) | Expert in building 3D experiences for the web - Three.js, React. |
| `/Requesting Code Review` | [`Requesting Code Review`](skills/frontend-development/Requesting Code Review/SKILL.md) | Dispatch code-reviewer subagent to review implementation against plan or requirements before proceeding. |
| `/Simplification Cascades` | [`Simplification Cascades`](skills/frontend-development/Simplification Cascades/SKILL.md) | Find one insight that eliminates multiple components - "if this is true, we don't need X, Y, or Z. |
| `/accessibility` | [`accessibility`](skills/frontend-development/accessibility/SKILL.md) | Audit and improve web accessibility following WCAG 2.2 guidelines. |
| `/acquire-codebase-knowledge` | [`acquire-codebase-knowledge`](skills/frontend-development/acquire-codebase-knowledge/SKILL.md) | Use this skill when the user explicitly asks to map, document, or onboard into an existing codebase. |
| `/airflow-dag-patterns` | [`airflow-dag-patterns`](skills/frontend-development/airflow-dag-patterns/SKILL.md) | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. |
| `/alpha-vantage` | [`alpha-vantage`](skills/frontend-development/alpha-vantage/SKILL.md) | Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators. |
| `/android-jetpack-compose-expert` | [`android-jetpack-compose-expert`](skills/frontend-development/android-jetpack-compose-expert/SKILL.md) | Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance. |
| `/android-native-dev` | [`android-native-dev`](skills/frontend-development/android-native-dev/SKILL.md) | Android native application development and UI design guide. |
| `/android-tombstone-symbolication` | [`android-tombstone-symbolication`](skills/frontend-development/android-tombstone-symbolication/SKILL.md) | Symbolicate the .NET runtime frames in an Android tombstone file. |
| `/android_ui_verification` | [`android_ui_verification`](skills/frontend-development/android_ui_verification/SKILL.md) | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| `/angular` | [`angular`](skills/frontend-development/angular/SKILL.md) | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration. |
| `/angular-migration` | [`angular-migration`](skills/frontend-development/angular-migration/SKILL.md) | Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes. |
| `/angular-state-management` | [`angular-state-management`](skills/frontend-development/angular-state-management/SKILL.md) | Master modern Angular state management with Signals, NgRx, and RxJS. |
| `/angular-ui-patterns` | [`angular-ui-patterns`](skills/frontend-development/angular-ui-patterns/SKILL.md) | Modern Angular UI patterns for loading states, error handling, and data display. |
| `/app-builder` | [`app-builder`](skills/frontend-development/app-builder/SKILL.md) | Main application building orchestrator. Creates full-stack applications from natural language requests. |
| `/app-store-optimization` | [`app-store-optimization`](skills/frontend-development/app-store-optimization/SKILL.md) | Complete App Store Optimization (ASO) toolkit for researching, optimizing. |
| `/appinsights-instrumentation` | [`appinsights-instrumentation`](skills/frontend-development/appinsights-instrumentation/SKILL.md) | Guidance for instrumenting webapps with Azure Application Insights. |
| `/apple-crash-symbolication` | [`apple-crash-symbolication`](skills/frontend-development/apple-crash-symbolication/SKILL.md) | Symbolicate .NET runtime frames in Apple platform .ips crash logs (iOS, tvOS, Mac Catalyst, macOS). |
| `/application-performance-performance-optimization` | [`application-performance-performance-optimization`](skills/frontend-development/application-performance-performance-optimization/SKILL.md) | Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. |
| `/applicationinsights-web-ts` | [`applicationinsights-web-ts`](skills/frontend-development/applicationinsights-web-ts/SKILL.md) | Instrument browser/web apps with the Application Insights JavaScript SDK (@microsoft/applicationinsights-web). |
| `/arch-linux-triage` | [`arch-linux-triage`](skills/frontend-development/arch-linux-triage/SKILL.md) | Triage and resolve Arch Linux issues with pacman, systemd, and rolling-release best practices. |
| `/arize-link` | [`arize-link`](skills/frontend-development/arize-link/SKILL.md) | Generates deep links to the Arize UI for traces, spans, sessions, datasets, labeling queues, evaluators, and annotation configs. |
| `/artifacts-builder` | [`artifacts-builder`](skills/frontend-development/artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies. |
| `/ask-questions-if-underspecified` | [`ask-questions-if-underspecified`](skills/frontend-development/ask-questions-if-underspecified/SKILL.md) | Clarify requirements before implementing. Use when serious doubts arise. |
| `/assertion-quality` | [`assertion-quality`](skills/frontend-development/assertion-quality/SKILL.md) | Analyzes the variety and depth of assertions across .NET test suites. |
| `/astro` | [`astro`](skills/frontend-development/astro/SKILL.md) | Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components. |
| `/audit-context-building` | [`audit-context-building`](skills/frontend-development/audit-context-building/SKILL.md) | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| `/audit-skills` | [`audit-skills`](skills/frontend-development/audit-skills/SKILL.md) | Expert security auditor for AI Skills and Bundles. |
| `/author-component` | [`author-component`](skills/frontend-development/author-component/SKILL.md) | Create or review Blazor components (.razor files) with correct architecture. |
| `/autoresearch` | [`autoresearch`](skills/frontend-development/autoresearch/SKILL.md) | Autonomous iterative experimentation loop for any programming task. |
| `/avalonia-layout-zafiro` | [`avalonia-layout-zafiro`](skills/frontend-development/avalonia-layout-zafiro/SKILL.md) | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components. |
| `/avalonia-viewmodels-zafiro` | [`avalonia-viewmodels-zafiro`](skills/frontend-development/avalonia-viewmodels-zafiro/SKILL.md) | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. |
| `/avalonia-zafiro-development` | [`avalonia-zafiro-development`](skills/frontend-development/avalonia-zafiro-development/SKILL.md) | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. |
| `/axiom` | [`axiom`](skills/frontend-development/axiom/SKILL.md) | First-principles assumption auditor. |
| `/baseline-ui` | [`baseline-ui`](skills/frontend-development/baseline-ui/SKILL.md) | Validates animation durations, enforces typography scale, checks component accessibility. |
| `/bash-linux` | [`bash-linux`](skills/frontend-development/bash-linux/SKILL.md) | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. |
| `/bazel-build-optimization` | [`bazel-build-optimization`](skills/frontend-development/bazel-build-optimization/SKILL.md) | Optimize Bazel builds for large-scale monorepos. |
| `/bevy-ecs-expert` | [`bevy-ecs-expert`](skills/frontend-development/bevy-ecs-expert/SKILL.md) | Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling. |
| `/blog-writing-guide` | [`blog-writing-guide`](skills/frontend-development/blog-writing-guide/SKILL.md) | This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their. |
| `/brand-guidelines` | [`brand-guidelines`](skills/frontend-development/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having. |
| `/brand-guidelines-community` | [`brand-guidelines-community`](skills/frontend-development/brand-guidelines-community/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| `/browser-extension-builder` | [`browser-extension-builder`](skills/frontend-development/browser-extension-builder/SKILL.md) | Expert in building browser extensions that solve real problems -. |
| `/build` | [`build`](skills/frontend-development/build/SKILL.md) | build. |
| `/build-parallelism` | [`build-parallelism`](skills/frontend-development/build-parallelism/SKILL.md) | Guide for optimizing MSBuild build parallelism and multi-project scheduling. |
| `/build-perf-baseline` | [`build-perf-baseline`](skills/frontend-development/build-perf-baseline/SKILL.md) | Establish build performance baselines and apply systematic optimization techniques. |
| `/build-perf-diagnostics` | [`build-perf-diagnostics`](skills/frontend-development/build-perf-diagnostics/SKILL.md) | Diagnose MSBuild build performance bottlenecks using binary log analysis. |
| `/building-native-ui` | [`building-native-ui`](skills/frontend-development/building-native-ui/SKILL.md) | Complete guide for building beautiful apps with Expo Router. |
| `/bun-development` | [`bun-development`](skills/frontend-development/bun-development/SKILL.md) | Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun). |
| `/burp-suite-testing` | [`burp-suite-testing`](skills/frontend-development/burp-suite-testing/SKILL.md) | Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic. |
| `/burpsuite-project-parser` | [`burpsuite-project-parser`](skills/frontend-development/burpsuite-project-parser/SKILL.md) | Searches and explores Burp Suite project files (.burp) from the command line. |
| `/business-analyst` | [`business-analyst`](skills/frontend-development/business-analyst/SKILL.md) | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. |
| `/busybox-on-windows` | [`busybox-on-windows`](skills/frontend-development/busybox-on-windows/SKILL.md) | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. |
| `/c4-component` | [`c4-component`](skills/frontend-development/c4-component/SKILL.md) | Expert C4 Component-level documentation specialist. |
| `/carrier-relationship-management` | [`carrier-relationship-management`](skills/frontend-development/carrier-relationship-management/SKILL.md) | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating. |
| `/cc-skill-coding-standards` | [`cc-skill-coding-standards`](skills/frontend-development/cc-skill-coding-standards/SKILL.md) | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| `/cc-skill-frontend-patterns` | [`cc-skill-frontend-patterns`](skills/frontend-development/cc-skill-frontend-patterns/SKILL.md) | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `/cc-skill-project-guidelines-example` | [`cc-skill-project-guidelines-example`](skills/frontend-development/cc-skill-project-guidelines-example/SKILL.md) | Project Guidelines Skill (Example). |
| `/cdk-patterns` | [`cdk-patterns`](skills/frontend-development/cdk-patterns/SKILL.md) | Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. |
| `/centos-linux-triage` | [`centos-linux-triage`](skills/frontend-development/centos-linux-triage/SKILL.md) | Triage and resolve CentOS issues using RHEL-compatible tooling, SELinux-aware practices, and firewalld. |
| `/chat-widget` | [`chat-widget`](skills/frontend-development/chat-widget/SKILL.md) | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. |
| `/chrome-extension-developer` | [`chrome-extension-developer`](skills/frontend-development/chrome-extension-developer/SKILL.md) | Expert in building Chrome Extensions using Manifest V3. |
| `/codeql` | [`codeql`](skills/frontend-development/codeql/SKILL.md) | Comprehensive guide for setting up and configuring CodeQL code scanning via GitHub Actions workflows and the CodeQL CLI. |
| `/collect-user-input` | [`collect-user-input`](skills/frontend-development/collect-user-input/SKILL.md) | Build forms, validate data, and react to user input in Blazor. |
| `/comfyui-gateway` | [`comfyui-gateway`](skills/frontend-development/comfyui-gateway/SKILL.md) | REST API gateway for ComfyUI servers. |
| `/convex` | [`convex`](skills/frontend-development/convex/SKILL.md) | Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage,. |
| `/coordinate-components` | [`coordinate-components`](skills/frontend-development/coordinate-components/SKILL.md) | Share state between components that don't have a direct parent-child parameter relationship, using cascading values,. |
| `/core-components` | [`core-components`](skills/frontend-development/core-components/SKILL.md) | Core component library and design system patterns. |
| `/core-web-vitals` | [`core-web-vitals`](skills/frontend-development/core-web-vitals/SKILL.md) | Optimize Core Web Vitals (LCP, INP, CLS) for better page experience and search ranking. |
| `/cqrs-implementation` | [`cqrs-implementation`](skills/frontend-development/cqrs-implementation/SKILL.md) | Implement Command Query Responsibility Segregation for scalable architectures. |
| `/create-github-issues-for-unmet-specification-requirements` | [`create-github-issues-for-unmet-specification-requirements`](skills/frontend-development/create-github-issues-for-unmet-specification-requirements/SKILL.md) | Create GitHub Issues for unimplemented requirements from specification files using feature_request.yml template. |
| `/daily-prep` | [`daily-prep`](skills/frontend-development/daily-prep/SKILL.md) | Prepare for tomorrow''s meetings and tasks. |
| `/data-engineer` | [`data-engineer`](skills/frontend-development/data-engineer/SKILL.md) | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. |
| `/data-quality-frameworks` | [`data-quality-frameworks`](skills/frontend-development/data-quality-frameworks/SKILL.md) | Implement data quality validation with Great Expectations, dbt tests, and data contracts. |
| `/datanalysis-credit-risk` | [`datanalysis-credit-risk`](skills/frontend-development/datanalysis-credit-risk/SKILL.md) | Credit risk data cleaning and variable screening pipeline for pre-loan modeling. |
| `/dataverse-python-usecase-builder` | [`dataverse-python-usecase-builder`](skills/frontend-development/dataverse-python-usecase-builder/SKILL.md) | Generate complete solutions for specific Dataverse SDK use cases with architecture recommendations. |
| `/dbos-golang` | [`dbos-golang`](skills/frontend-development/dbos-golang/SKILL.md) | Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. |
| `/dbos-typescript` | [`dbos-typescript`](skills/frontend-development/dbos-typescript/SKILL.md) | Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. |
| `/debian-linux-triage` | [`debian-linux-triage`](skills/frontend-development/debian-linux-triage/SKILL.md) | Triage and resolve Debian Linux issues with apt, systemd, and AppArmor-aware guidance. |
| `/debugging-and-error-recovery` | [`debugging-and-error-recovery`](skills/frontend-development/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. |
| `/decision-navigator` | [`decision-navigator`](skills/frontend-development/decision-navigator/SKILL.md) | Guide stuck or overwhelmed users through targeted branching questions until they reach concrete next steps. |
| `/design-taste-frontend` | [`design-taste-frontend`](skills/frontend-development/design-taste-frontend/SKILL.md) | Use when building high-agency frontend interfaces with strict design taste, calibrated color, responsive layout, and motion rules. |
| `/development` | [`development`](skills/frontend-development/development/SKILL.md) | Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile. |
| `/directory-build-organization` | [`directory-build-organization`](skills/frontend-development/directory-build-organization/SKILL.md) | Guide for organizing MSBuild infrastructure with Directory.Build.props, Directory.Build.targets,. |
| `/discord-bot-architect` | [`discord-bot-architect`](skills/frontend-development/discord-bot-architect/SKILL.md) | Specialized skill for building production-ready Discord bots. |
| `/dotnet-maui-doctor` | [`dotnet-maui-doctor`](skills/frontend-development/dotnet-maui-doctor/SKILL.md) | Diagnoses and fixes .NET MAUI development environment issues. |
| `/drizzle-orm-expert` | [`drizzle-orm-expert`](skills/frontend-development/drizzle-orm-expert/SKILL.md) | Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. |
| `/durable-objects` | [`durable-objects`](skills/frontend-development/durable-objects/SKILL.md) | Create and review Cloudflare Durable Objects. |
| `/earllm-build` | [`earllm-build`](skills/frontend-development/earllm-build/SKILL.md) | Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an. |
| `/electron-development` | [`electron-development`](skills/frontend-development/electron-development/SKILL.md) | Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture,. |
| `/embedding-strategies` | [`embedding-strategies`](skills/frontend-development/embedding-strategies/SKILL.md) | Guide to selecting and optimizing embedding models for vector search applications. |
| `/environment-setup-guide` | [`environment-setup-guide`](skills/frontend-development/environment-setup-guide/SKILL.md) | Guide developers through setting up development environments with proper tools, dependencies, and configurations. |
| `/error-debugging-error-trace` | [`error-debugging-error-trace`](skills/frontend-development/error-debugging-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. |
| `/exp-test-maintainability` | [`exp-test-maintainability`](skills/frontend-development/exp-test-maintainability/SKILL.md) | Detects duplicate boilerplate, copy-paste tests, and structural maintainability issues across .NET test suites. |
| `/expo-dev-client` | [`expo-dev-client`](skills/frontend-development/expo-dev-client/SKILL.md) | Build and distribute Expo development clients locally or via TestFlight. |
| `/expo-tailwind-setup` | [`expo-tailwind-setup`](skills/frontend-development/expo-tailwind-setup/SKILL.md) | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling. |
| `/expo-ui-jetpack-compose` | [`expo-ui-jetpack-compose`](skills/frontend-development/expo-ui-jetpack-compose/SKILL.md) | expo-ui-jetpack-compose. |
| `/expo-ui-swift-ui` | [`expo-ui-swift-ui`](skills/frontend-development/expo-ui-swift-ui/SKILL.md) | expo-ui-swift-ui. |
| `/extension-points` | [`extension-points`](skills/frontend-development/extension-points/SKILL.md) | Guide for MSBuild extensibility: CustomBefore/CustomAfter hooks, wildcard imports with alphabetic ordering, import. |
| `/fabric-lakehouse` | [`fabric-lakehouse`](skills/frontend-development/fabric-lakehouse/SKILL.md) | Use this skill to get context about Fabric Lakehouse and its features for software systems and AI-powered functions. |
| `/fedora-linux-triage` | [`fedora-linux-triage`](skills/frontend-development/fedora-linux-triage/SKILL.md) | Triage and resolve Fedora issues with dnf, systemd, and SELinux-aware guidance. |
| `/fetch-and-send-data` | [`fetch-and-send-data`](skills/frontend-development/fetch-and-send-data/SKILL.md) | Call APIs, load data into components, and handle the async lifecycle in Blazor. |
| `/finishing-a-development-branch` | [`finishing-a-development-branch`](skills/frontend-development/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass. |
| `/firebase-basics` | [`firebase-basics`](skills/frontend-development/firebase-basics/SKILL.md) | Use this skill whenever you are working on a project that uses Firebase products or services, especially for mobile or web apps. |
| `/first-ask` | [`first-ask`](skills/frontend-development/first-ask/SKILL.md) | Interactive, input-tool powered, task refinement workflow: interrogates scope, deliverables, constraints before. |
| `/fixing-metadata` | [`fixing-metadata`](skills/frontend-development/fixing-metadata/SKILL.md) | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards,. |
| `/fixing-motion-performance` | [`fixing-motion-performance`](skills/frontend-development/fixing-motion-performance/SKILL.md) | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion. |
| `/flowstudio-power-automate-build` | [`flowstudio-power-automate-build`](skills/frontend-development/flowstudio-power-automate-build/SKILL.md) | Build, scaffold, and deploy Power Automate cloud flows using the FlowStudio MCP server. |
| `/fluentui-blazor` | [`fluentui-blazor`](skills/frontend-development/fluentui-blazor/SKILL.md) | Guide for using the Microsoft Fluent UI Blazor component library (Microsoft.FluentUI.AspNetCore.Components NuGet. |
| `/flutter-dev` | [`flutter-dev`](skills/frontend-development/flutter-dev/SKILL.md) | Flutter cross-platform development guide covering widget patterns, Riverpod/Bloc state management, GoRouter navigation,. |
| `/flutter-expert` | [`flutter-expert`](skills/frontend-development/flutter-expert/SKILL.md) | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| `/fp-either-ref` | [`fp-either-ref`](skills/frontend-development/fp-either-ref/SKILL.md) | Quick reference for Either type. |
| `/fp-option-ref` | [`fp-option-ref`](skills/frontend-development/fp-option-ref/SKILL.md) | Quick reference for Option type. |
| `/fp-pipe-ref` | [`fp-pipe-ref`](skills/frontend-development/fp-pipe-ref/SKILL.md) | Quick reference for pipe and flow. |
| `/fp-pragmatic` | [`fp-pragmatic`](skills/frontend-development/fp-pragmatic/SKILL.md) | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead. |
| `/fp-react` | [`fp-react`](skills/frontend-development/fp-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. |
| `/fp-refactor` | [`fp-refactor`](skills/frontend-development/fp-refactor/SKILL.md) | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns. |
| `/fp-ts-errors` | [`fp-ts-errors`](skills/frontend-development/fp-ts-errors/SKILL.md) | Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. |
| `/fp-ts-pragmatic` | [`fp-ts-pragmatic`](skills/frontend-development/fp-ts-pragmatic/SKILL.md) | A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the. |
| `/fp-ts-react` | [`fp-ts-react`](skills/frontend-development/fp-ts-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. |
| `/fp-types-ref` | [`fp-types-ref`](skills/frontend-development/fp-types-ref/SKILL.md) | Quick reference for fp-ts types. |
| `/framework-migration-legacy-modernize` | [`framework-migration-legacy-modernize`](skills/frontend-development/framework-migration-legacy-modernize/SKILL.md) | Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement. |
| `/from-the-other-side-quinn` | [`from-the-other-side-quinn`](skills/frontend-development/from-the-other-side-quinn/SKILL.md) | Collaboration profile for Quinn: curious, energetic. |
| `/frontend-design` | [`frontend-design`](skills/frontend-development/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. |
| `/frontend-dev` | [`frontend-dev`](skills/frontend-development/frontend-dev/SKILL.md) | Full-stack frontend development combining premium UI design, cinematic animations, AI-generated media assets,. |
| `/frontend-dev-guidelines` | [`frontend-dev-guidelines`](skills/frontend-development/frontend-dev-guidelines/SKILL.md) | You are a senior frontend engineer operating under strict architectural and performance standards. |
| `/frontend-developer` | [`frontend-developer`](skills/frontend-development/frontend-developer/SKILL.md) | Build React components, implement responsive layouts, and handle client-side state management. |
| `/frontend-mobile-development-component-scaffold` | [`frontend-mobile-development-component-scaffold`](skills/frontend-development/frontend-mobile-development-component-scaffold/SKILL.md) | You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. |
| `/frontend-mobile-security-xss-scan` | [`frontend-mobile-security-xss-scan`](skills/frontend-development/frontend-mobile-security-xss-scan/SKILL.md) | You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability detection and prevention. |
| `/frontend-security-coder` | [`frontend-security-coder`](skills/frontend-development/frontend-security-coder/SKILL.md) | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| `/frontend-slides` | [`frontend-slides`](skills/frontend-development/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| `/frontend-ui-dark-ts` | [`frontend-ui-dark-ts`](skills/frontend-development/frontend-ui-dark-ts/SKILL.md) | Build dark-themed React applications using Tailwind CSS with custom theming, glassmorphism effects, and Framer Motion animations. |
| `/frontend-ui-engineering` | [`frontend-ui-engineering`](skills/frontend-development/frontend-ui-engineering/SKILL.md) | Builds production-quality UIs. Use when building or modifying user-facing interfaces. |
| `/full-output-enforcement` | [`full-output-enforcement`](skills/frontend-development/full-output-enforcement/SKILL.md) | Use when a task requires exhaustive unabridged output, complete files, or strict prevention of placeholders and skipped code. |
| `/gen-specs-as-issues` | [`gen-specs-as-issues`](skills/frontend-development/gen-specs-as-issues/SKILL.md) | This workflow guides you through a systematic approach to identify missing features, prioritize them. |
| `/go-concurrency-patterns` | [`go-concurrency-patterns`](skills/frontend-development/go-concurrency-patterns/SKILL.md) | Master Go concurrency with goroutines, channels, sync primitives, and context. |
| `/godot-4-migration` | [`godot-4-migration`](skills/frontend-development/godot-4-migration/SKILL.md) | Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports. |
| `/godot-gdscript-patterns` | [`godot-gdscript-patterns`](skills/frontend-development/godot-gdscript-patterns/SKILL.md) | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. |
| `/gtm-0-to-1-launch` | [`gtm-0-to-1-launch`](skills/frontend-development/gtm-0-to-1-launch/SKILL.md) | Launch new products from idea to first customers. |
| `/gtm-board-and-investor-communication` | [`gtm-board-and-investor-communication`](skills/frontend-development/gtm-board-and-investor-communication/SKILL.md) | Board meeting preparation, investor updates, and executive communication. |
| `/gtm-enterprise-account-planning` | [`gtm-enterprise-account-planning`](skills/frontend-development/gtm-enterprise-account-planning/SKILL.md) | Strategic account planning and execution for enterprise deals. |
| `/gtm-product-led-growth` | [`gtm-product-led-growth`](skills/frontend-development/gtm-product-led-growth/SKILL.md) | Build self-serve acquisition and expansion motions. |
| `/hig-components-content` | [`hig-components-content`](skills/frontend-development/hig-components-content/SKILL.md) | Apple Human Interface Guidelines for content display components. |
| `/hig-components-controls` | [`hig-components-controls`](skills/frontend-development/hig-components-controls/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. |
| `/hig-components-dialogs` | [`hig-components-dialogs`](skills/frontend-development/hig-components-dialogs/SKILL.md) | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| `/hig-components-layout` | [`hig-components-layout`](skills/frontend-development/hig-components-layout/SKILL.md) | Apple Human Interface Guidelines for layout and navigation components. |
| `/hig-components-menus` | [`hig-components-menus`](skills/frontend-development/hig-components-menus/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. |
| `/hig-components-search` | [`hig-components-search`](skills/frontend-development/hig-components-search/SKILL.md) | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| `/hig-components-status` | [`hig-components-status`](skills/frontend-development/hig-components-status/SKILL.md) | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| `/hig-components-system` | [`hig-components-system`](skills/frontend-development/hig-components-system/SKILL.md) | Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home. |
| `/hig-patterns` | [`hig-patterns`](skills/frontend-development/hig-patterns/SKILL.md) | Apple Human Interface Guidelines interaction and UX patterns. |
| `/html-injection-testing` | [`html-injection-testing`](skills/frontend-development/html-injection-testing/SKILL.md) | Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. |
| `/hugging-face-gradio` | [`hugging-face-gradio`](skills/frontend-development/hugging-face-gradio/SKILL.md) | Build or edit Gradio apps, layouts, components, and chat interfaces in Python. |
| `/hugging-face-tool-builder` | [`hugging-face-tool-builder`](skills/frontend-development/hugging-face-tool-builder/SKILL.md) | Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing. |
| `/huggingface-gradio` | [`huggingface-gradio`](skills/frontend-development/huggingface-gradio/SKILL.md) | Build Gradio web UIs and demos in Python. |
| `/huggingface-tool-builder` | [`huggingface-tool-builder`](skills/frontend-development/huggingface-tool-builder/SKILL.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. |
| `/iconsax-library` | [`iconsax-library`](skills/frontend-development/iconsax-library/SKILL.md) | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| `/impediment-prioritization` | [`impediment-prioritization`](skills/frontend-development/impediment-prioritization/SKILL.md) | Ranks any list of impediments and their countermeasures using a value-stream scoring model (ROI, Cost to Implement,. |
| `/incremental-build` | [`incremental-build`](skills/frontend-development/incremental-build/SKILL.md) | Guide for optimizing MSBuild incremental builds. Only activate in MSBuild/.NET build context. |
| `/industrial-brutalist-ui` | [`industrial-brutalist-ui`](skills/frontend-development/industrial-brutalist-ui/SKILL.md) | Use when creating raw industrial or tactical telemetry UIs with rigid grids, stark typography, CRT effects, and high-density data. |
| `/interactive-portfolio` | [`interactive-portfolio`](skills/frontend-development/interactive-portfolio/SKILL.md) | Expert in building portfolios that actually land jobs and clients -. |
| `/interview-me` | [`interview-me`](skills/frontend-development/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. |
| `/invariant-guard` | [`invariant-guard`](skills/frontend-development/invariant-guard/SKILL.md) | Correctness-first: forces writing the function contract, loop invariant, termination argument, and edge cases BEFORE code. |
| `/ios-application-dev` | [`ios-application-dev`](skills/frontend-development/ios-application-dev/SKILL.md) | iOS application development guide covering UIKit, SnapKit, and SwiftUI. |
| `/ios-debugger-agent` | [`ios-debugger-agent`](skills/frontend-development/ios-debugger-agent/SKILL.md) | Debug the current iOS project on a booted simulator with XcodeBuildMCP. |
| `/ios-developer` | [`ios-developer`](skills/frontend-development/ios-developer/SKILL.md) | Develop native iOS applications with Swift/SwiftUI. |
| `/istio-traffic-management` | [`istio-traffic-management`](skills/frontend-development/istio-traffic-management/SKILL.md) | Comprehensive guide to Istio traffic management for production service mesh deployments. |
| `/item-management` | [`item-management`](skills/frontend-development/item-management/SKILL.md) | Patterns for managing MSBuild item groups: Include/Remove/Update semantics, item metadata, batching with %(Metadata),. |
| `/javascript-typescript-jest` | [`javascript-typescript-jest`](skills/frontend-development/javascript-typescript-jest/SKILL.md) | Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure. |
| `/javascript-typescript-typescript-scaffold` | [`javascript-typescript-typescript-scaffold`](skills/frontend-development/javascript-typescript-typescript-scaffold/SKILL.md) | You are a TypeScript project architecture expert specializing in scaffolding production-ready Node.js and frontend applications. |
| `/kaizen` | [`kaizen`](skills/frontend-development/kaizen/SKILL.md) | Guide for continuous improvement, error proofing, and standardization. |
| `/langgraph` | [`langgraph`](skills/frontend-development/langgraph/SKILL.md) | Expert in LangGraph - the production-grade framework for building. |
| `/legacy-circuit-mockups` | [`legacy-circuit-mockups`](skills/frontend-development/legacy-circuit-mockups/SKILL.md) | Generate breadboard circuit mockups and visual diagrams using HTML5 Canvas drawing techniques. |
| `/leiloeiro-avaliacao` | [`leiloeiro-avaliacao`](skills/frontend-development/leiloeiro-avaliacao/SKILL.md) | Avaliacao pericial de imoveis em leilao. |
| `/leiloeiro-mercado` | [`leiloeiro-mercado`](skills/frontend-development/leiloeiro-mercado/SKILL.md) | Analise de mercado imobiliario para leiloes. |
| `/leiloeiro-risco` | [`leiloeiro-risco`](skills/frontend-development/leiloeiro-risco/SKILL.md) | Analise de risco em leiloes de imoveis. |
| `/lightning-factory-explainer` | [`lightning-factory-explainer`](skills/frontend-development/lightning-factory-explainer/SKILL.md) | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared. |
| `/linkedin-profile-optimizer` | [`linkedin-profile-optimizer`](skills/frontend-development/linkedin-profile-optimizer/SKILL.md) | High-intent expert for LinkedIn profile checks, authority building, and SEO optimization. |
| `/linux-privilege-escalation` | [`linux-privilege-escalation`](skills/frontend-development/linux-privilege-escalation/SKILL.md) | Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations,. |
| `/linux-shell-scripting` | [`linux-shell-scripting`](skills/frontend-development/linux-shell-scripting/SKILL.md) | Provide production-ready shell script templates for common Linux system administration tasks including backups,. |
| `/linux-troubleshooting` | [`linux-troubleshooting`](skills/frontend-development/linux-troubleshooting/SKILL.md) | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| `/macos-menubar-tuist-app` | [`macos-menubar-tuist-app`](skills/frontend-development/macos-menubar-tuist-app/SKILL.md) | Build, refactor, or review SwiftUI macOS menubar apps that use Tuist. |
| `/macos-spm-app-packaging` | [`macos-spm-app-packaging`](skills/frontend-development/macos-spm-app-packaging/SKILL.md) | Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects. |
| `/magic-ui-generator` | [`magic-ui-generator`](skills/frontend-development/magic-ui-generator/SKILL.md) | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| `/makepad-layout` | [`makepad-layout`](skills/frontend-development/makepad-layout/SKILL.md) | CRITICAL: Use for Makepad layout system. |
| `/makepad-platform` | [`makepad-platform`](skills/frontend-development/makepad-platform/SKILL.md) | CRITICAL: Use for Makepad cross-platform support. |
| `/makepad-reference` | [`makepad-reference`](skills/frontend-development/makepad-reference/SKILL.md) | This category provides reference materials for debugging, code quality, and advanced layout patterns. |
| `/matematico-tao` | [`matematico-tao`](skills/frontend-development/matematico-tao/SKILL.md) | Matemático ultra-avançado inspirado em Terence Tao. |
| `/maui-app-lifecycle` | [`maui-app-lifecycle`](skills/frontend-development/maui-app-lifecycle/SKILL.md) | .NET MAUI app lifecycle guidance — the four app states, cross-platform Window lifecycle events (Created, Activated,. |
| `/maui-collectionview` | [`maui-collectionview`](skills/frontend-development/maui-collectionview/SKILL.md) | Guidance for implementing CollectionView in .NET MAUI apps — data display, layouts (list & grid), selection, grouping,. |
| `/maui-data-binding` | [`maui-data-binding`](skills/frontend-development/maui-data-binding/SKILL.md) | Guidance for .NET MAUI XAML and C# data bindings — compiled bindings, INotifyPropertyChanged / ObservableObject, value. |
| `/maui-dependency-injection` | [`maui-dependency-injection`](skills/frontend-development/maui-dependency-injection/SKILL.md) | Guidance for configuring dependency injection in .NET MAUI apps — service registration in MauiProgram.cs, lifetime. |
| `/maui-safe-area` | [`maui-safe-area`](skills/frontend-development/maui-safe-area/SKILL.md) | .NET MAUI safe area and edge-to-edge layout guidance for .NET 10+. |
| `/maui-shell-navigation` | [`maui-shell-navigation`](skills/frontend-development/maui-shell-navigation/SKILL.md) | Guide for implementing Shell-based navigation in .NET MAUI apps. |
| `/maui-theming` | [`maui-theming`](skills/frontend-development/maui-theming/SKILL.md) | Guide for theming .NET MAUI apps — light/dark mode via AppThemeBinding, ResourceDictionary theme switching,. |
| `/mcp-builder-ms` | [`mcp-builder-ms`](skills/frontend-development/mcp-builder-ms/SKILL.md) | Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or. |
| `/minimalist-ui` | [`minimalist-ui`](skills/frontend-development/minimalist-ui/SKILL.md) | Use when creating clean editorial interfaces with warm monochrome palettes, crisp borders, restrained motion. |
| `/ml-engineer` | [`ml-engineer`](skills/frontend-development/ml-engineer/SKILL.md) | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. |
| `/mlops-engineer` | [`mlops-engineer`](skills/frontend-development/mlops-engineer/SKILL.md) | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| `/mobile-design` | [`mobile-design`](skills/frontend-development/mobile-design/SKILL.md) | (Mobile-First · Touch-First · Platform-Respectful). |
| `/mobile-developer` | [`mobile-developer`](skills/frontend-development/mobile-developer/SKILL.md) | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. |
| `/mobile-security-coder` | [`mobile-security-coder`](skills/frontend-development/mobile-security-coder/SKILL.md) | Expert in secure mobile coding practices specializing in input validation, WebView security. |
| `/modern-javascript-patterns` | [`modern-javascript-patterns`](skills/frontend-development/modern-javascript-patterns/SKILL.md) | Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns. |
| `/monorepo-architect` | [`monorepo-architect`](skills/frontend-development/monorepo-architect/SKILL.md) | Expert in monorepo architecture, build systems, and dependency management at scale. |
| `/monorepo-management` | [`monorepo-management`](skills/frontend-development/monorepo-management/SKILL.md) | Build efficient, scalable monorepos that enable code sharing, consistent tooling. |
| `/monte-carlo-push-ingestion` | [`monte-carlo-push-ingestion`](skills/frontend-development/monte-carlo-push-ingestion/SKILL.md) | Expert guide for pushing metadata, lineage, and query logs to Monte Carlo from any data warehouse. |
| `/msbuild-antipatterns` | [`msbuild-antipatterns`](skills/frontend-development/msbuild-antipatterns/SKILL.md) | Catalog of MSBuild anti-patterns with detection rules and fix recipes. |
| `/msbuild-modernization` | [`msbuild-modernization`](skills/frontend-development/msbuild-modernization/SKILL.md) | Guide for modernizing and migrating MSBuild project files to SDK-style format. |
| `/msbuild-server` | [`msbuild-server`](skills/frontend-development/msbuild-server/SKILL.md) | Guide for using MSBuild Server to improve CLI build performance. |
| `/msstore-cli` | [`msstore-cli`](skills/frontend-development/msstore-cli/SKILL.md) | Microsoft Store Developer CLI (msstore) for publishing Windows applications to the Microsoft Store. |
| `/multi-platform-apps-multi-platform` | [`multi-platform-apps-multi-platform`](skills/frontend-development/multi-platform-apps-multi-platform/SKILL.md) | Build and deploy the same feature consistently across web, mobile. |
| `/mvvm-toolkit` | [`mvvm-toolkit`](skills/frontend-development/mvvm-toolkit/SKILL.md) | CommunityToolkit.Mvvm (the MVVM Toolkit) core: source generators ([ObservableProperty], [RelayCommand],. |
| `/mvvm-toolkit-di` | [`mvvm-toolkit-di`](skills/frontend-development/mvvm-toolkit-di/SKILL.md) | Wire CommunityToolkit.Mvvm ViewModels into Microsoft.Extensions.DependencyInjection. |
| `/mvvm-toolkit-messenger` | [`mvvm-toolkit-messenger`](skills/frontend-development/mvvm-toolkit-messenger/SKILL.md) | CommunityToolkit.Mvvm Messenger pub/sub for decoupled communication between ViewModels (or any objects). |
| `/n8n-validation-expert` | [`n8n-validation-expert`](skills/frontend-development/n8n-validation-expert/SKILL.md) | Expert guide for interpreting and fixing n8n validation errors. |
| `/n8n-workflow-patterns` | [`n8n-workflow-patterns`](skills/frontend-development/n8n-workflow-patterns/SKILL.md) | Proven architectural patterns for building n8n workflows. |
| `/nextjs-app-router-patterns` | [`nextjs-app-router-patterns`](skills/frontend-development/nextjs-app-router-patterns/SKILL.md) | Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development. |
| `/nextjs-best-practices` | [`nextjs-best-practices`](skills/frontend-development/nextjs-best-practices/SKILL.md) | Next.js App Router principles. Server Components, data fetching, routing patterns. |
| `/nx-workspace-patterns` | [`nx-workspace-patterns`](skills/frontend-development/nx-workspace-patterns/SKILL.md) | Configure and optimize Nx monorepo workspaces. |
| `/observability-engineer` | [`observability-engineer`](skills/frontend-development/observability-engineer/SKILL.md) | Build production-ready monitoring, logging, and tracing systems. |
| `/obsidian-clipper-template-creator` | [`obsidian-clipper-template-creator`](skills/frontend-development/obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. |
| `/odoo-hr-payroll-setup` | [`odoo-hr-payroll-setup`](skills/frontend-development/odoo-hr-payroll-setup/SKILL.md) | Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts. |
| `/odoo-inventory-optimizer` | [`odoo-inventory-optimizer`](skills/frontend-development/odoo-inventory-optimizer/SKILL.md) | Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes. |
| `/odoo-manufacturing-advisor` | [`odoo-manufacturing-advisor`](skills/frontend-development/odoo-manufacturing-advisor/SKILL.md) | Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning. |
| `/odoo-module-developer` | [`odoo-module-developer`](skills/frontend-development/odoo-module-developer/SKILL.md) | Expert guide for creating custom Odoo modules. |
| `/odoo-purchase-workflow` | [`odoo-purchase-workflow`](skills/frontend-development/odoo-purchase-workflow/SKILL.md) | Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists. |
| `/odoo-xml-views-builder` | [`odoo-xml-views-builder`](skills/frontend-development/odoo-xml-views-builder/SKILL.md) | Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. |
| `/on-call-handoff-patterns` | [`on-call-handoff-patterns`](skills/frontend-development/on-call-handoff-patterns/SKILL.md) | Effective patterns for on-call shift transitions, ensuring continuity, context transfer. |
| `/oo-component-documentation` | [`oo-component-documentation`](skills/frontend-development/oo-component-documentation/SKILL.md) | Create or update standardized object-oriented component documentation using a shared template plus mode-specific. |
| `/penpot-uiux-design` | [`penpot-uiux-design`](skills/frontend-development/penpot-uiux-design/SKILL.md) | Comprehensive guide for creating professional UI/UX designs in Penpot using MCP tools. |
| `/performance-optimization` | [`performance-optimization`](skills/frontend-development/performance-optimization/SKILL.md) | Optimizes application performance. |
| `/personal-tool-builder` | [`personal-tool-builder`](skills/frontend-development/personal-tool-builder/SKILL.md) | Expert in building custom tools that solve your own problems first. |
| `/plan-ui-change` | [`plan-ui-change`](skills/frontend-development/plan-ui-change/SKILL.md) | Plan complex Blazor UI features by decomposing them into focused components. |
| `/postmortem-writing` | [`postmortem-writing`](skills/frontend-development/postmortem-writing/SKILL.md) | Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident. |
| `/power-platform-architect` | [`power-platform-architect`](skills/frontend-development/power-platform-architect/SKILL.md) | Use this skill when the user needs to transform business requirements, use case descriptions. |
| `/premium-frontend-ui` | [`premium-frontend-ui`](skills/frontend-development/premium-frontend-ui/SKILL.md) | A comprehensive guide for GitHub Copilot to craft immersive, high-performance web experiences with advanced motion,. |
| `/privilege-escalation-methods` | [`privilege-escalation-methods`](skills/frontend-development/privilege-escalation-methods/SKILL.md) | Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on. |
| `/progressive-web-app` | [`progressive-web-app`](skills/frontend-development/progressive-web-app/SKILL.md) | Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. |
| `/projection-patterns` | [`projection-patterns`](skills/frontend-development/projection-patterns/SKILL.md) | Build read models and projections from event streams. |
| `/prometheus-configuration` | [`prometheus-configuration`](skills/frontend-development/prometheus-configuration/SKILL.md) | Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules. |
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
| `/qiskit` | [`qiskit`](skills/frontend-development/qiskit/SKILL.md) | Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. |
| `/quality-playbook` | [`quality-playbook`](skills/frontend-development/quality-playbook/SKILL.md) | Run a complete quality engineering audit on any codebase. |
| `/quant-analyst` | [`quant-analyst`](skills/frontend-development/quant-analyst/SKILL.md) | Build financial models, backtest trading strategies, and analyze market data. |
| `/radix-ui-design-system` | [`radix-ui-design-system`](skills/frontend-development/radix-ui-design-system/SKILL.md) | Build accessible design systems with Radix UI primitives. |
| `/rag-engineer` | [`rag-engineer`](skills/frontend-development/rag-engineer/SKILL.md) | Expert in building Retrieval-Augmented Generation systems. Masters. |
| `/rayden-code` | [`rayden-code`](skills/frontend-development/rayden-code/SKILL.md) | Generate React code with Rayden UI components using correct props, tokens, and premium layout patterns. |
| `/rayden-use` | [`rayden-use`](skills/frontend-development/rayden-use/SKILL.md) | Build and maintain Rayden UI components and screens in Figma via Figma MCP with full design token enforcement. |
| `/react-audit-grep-patterns` | [`react-audit-grep-patterns`](skills/frontend-development/react-audit-grep-patterns/SKILL.md) | Provides the complete, verified grep scan command library for auditing React codebases before a React 18.3.1 or React 19 upgrade. |
| `/react-best-practices` | [`react-best-practices`](skills/frontend-development/react-best-practices/SKILL.md) | Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. |
| `/react-component-performance` | [`react-component-performance`](skills/frontend-development/react-component-performance/SKILL.md) | Diagnose slow React components and suggest targeted performance fixes. |
| `/react-flow-architect` | [`react-flow-architect`](skills/frontend-development/react-flow-architect/SKILL.md) | Build production-ready ReactFlow applications with hierarchical navigation, performance optimization. |
| `/react-flow-node-ts` | [`react-flow-node-ts`](skills/frontend-development/react-flow-node-ts/SKILL.md) | Create React Flow node components with TypeScript types, handles, and Zustand integration. |
| `/react-modernization` | [`react-modernization`](skills/frontend-development/react-modernization/SKILL.md) | Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation. |
| `/react-native-architecture` | [`react-native-architecture`](skills/frontend-development/react-native-architecture/SKILL.md) | Production-ready patterns for React Native development with Expo, including navigation, state management, native modules. |
| `/react-native-dev` | [`react-native-dev`](skills/frontend-development/react-native-dev/SKILL.md) | React Native and Expo development guide covering components, styling, animations, navigation, state management, forms,. |
| `/react-nextjs-development` | [`react-nextjs-development`](skills/frontend-development/react-nextjs-development/SKILL.md) | React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS. |
| `/react-patterns` | [`react-patterns`](skills/frontend-development/react-patterns/SKILL.md) | Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices. |
| `/react-state-management` | [`react-state-management`](skills/frontend-development/react-state-management/SKILL.md) | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. |
| `/react-ui-patterns` | [`react-ui-patterns`](skills/frontend-development/react-ui-patterns/SKILL.md) | Modern React UI patterns for loading states, error handling, and data fetching. |
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
| `/reference-builder` | [`reference-builder`](skills/frontend-development/reference-builder/SKILL.md) | Creates exhaustive technical references and API documentation. |
| `/requesting-code-review` | [`requesting-code-review`](skills/frontend-development/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements. |
| `/resolve-project-references` | [`resolve-project-references`](skills/frontend-development/resolve-project-references/SKILL.md) | Guide for interpreting ResolveProjectReferences time in MSBuild performance summaries. |
| `/risk-metrics-calculation` | [`risk-metrics-calculation`](skills/frontend-development/risk-metrics-calculation/SKILL.md) | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. |
| `/saas-mvp-launcher` | [`saas-mvp-launcher`](skills/frontend-development/saas-mvp-launcher/SKILL.md) | Use when planning or building a SaaS MVP from scratch. |
| `/salesforce-component-standards` | [`salesforce-component-standards`](skills/frontend-development/salesforce-component-standards/SKILL.md) | Quality standards for Salesforce Lightning Web Components (LWC), Aura components, and Visualforce pages. |
| `/sandbox-npm-install` | [`sandbox-npm-install`](skills/frontend-development/sandbox-npm-install/SKILL.md) | Install npm packages in a Docker sandbox environment. |
| `/sandbox-sdk` | [`sandbox-sdk`](skills/frontend-development/sandbox-sdk/SKILL.md) | Build sandboxed applications for secure code execution. |
| `/sankhya-dashboard-html-jsp-custom-best-pratices` | [`sankhya-dashboard-html-jsp-custom-best-pratices`](skills/frontend-development/sankhya-dashboard-html-jsp-custom-best-pratices/SKILL.md) | This skill should be used when the user asks for patterns, best practices, creation. |
| `/scala-pro` | [`scala-pro`](skills/frontend-development/scala-pro/SKILL.md) | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. |
| `/scoutqa-test` | [`scoutqa-test`](skills/frontend-development/scoutqa-test/SKILL.md) | This skill should be used when the user asks to "test this website", "run exploratory testing", "check for. |
| `/security-bluebook-builder` | [`security-bluebook-builder`](skills/frontend-development/security-bluebook-builder/SKILL.md) | Build a minimal but real security policy for sensitive apps. |
| `/semantic-kernel` | [`semantic-kernel`](skills/frontend-development/semantic-kernel/SKILL.md) | Create, update, refactor, explain, or review Semantic Kernel solutions using shared guidance plus language-specific. |
| `/semgrep-rule-creator` | [`semgrep-rule-creator`](skills/frontend-development/semgrep-rule-creator/SKILL.md) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. |
| `/senior-frontend` | [`senior-frontend`](skills/frontend-development/senior-frontend/SKILL.md) | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. |
| `/seo-authority-builder` | [`seo-authority-builder`](skills/frontend-development/seo-authority-builder/SKILL.md) | Analyzes content for E-E-A-T signals and suggests improvements to. |
| `/service-mesh-observability` | [`service-mesh-observability`](skills/frontend-development/service-mesh-observability/SKILL.md) | Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. |
| `/shadcn` | [`shadcn`](skills/frontend-development/shadcn/SKILL.md) | Manages shadcn/ui components and projects, providing context, documentation. |
| `/shadcn-ui` | [`shadcn-ui`](skills/frontend-development/shadcn-ui/SKILL.md) | Give your AI assistant deep knowledge of shadcn/ui components, patterns, and best practices. |
| `/shopify-apps` | [`shopify-apps`](skills/frontend-development/shopify-apps/SKILL.md) | Expert patterns for Shopify app development including Remix/React. |
| `/similarity-search-patterns` | [`similarity-search-patterns`](skills/frontend-development/similarity-search-patterns/SKILL.md) | Implement efficient similarity search with vector databases. |
| `/site-specification` | [`site-specification`](skills/frontend-development/site-specification/SKILL.md) | Extract comprehensive site specifications from simple descriptions. |
| `/skill-sentinel` | [`skill-sentinel`](skills/frontend-development/skill-sentinel/SKILL.md) | Auditoria e evolucao do ecossistema de skills. |
| `/snowflake-semanticview` | [`snowflake-semanticview`](skills/frontend-development/snowflake-semanticview/SKILL.md) | Create, alter, and validate Snowflake semantic views using Snowflake CLI (snow). |
| `/social-orchestrator` | [`social-orchestrator`](skills/frontend-development/social-orchestrator/SKILL.md) | Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. |
| `/squirrel` | [`squirrel`](skills/frontend-development/squirrel/SKILL.md) | Full-cycle AI coding skill: plans, builds, tests, lints, fixes bugs, and writes production-grade docs. |
| `/stitch-ui-design` | [`stitch-ui-design`](skills/frontend-development/stitch-ui-design/SKILL.md) | Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. |
| `/swiftui-expert-skill` | [`swiftui-expert-skill`](skills/frontend-development/swiftui-expert-skill/SKILL.md) | Write, review, or improve SwiftUI code following best practices for state management, view composition, performance,. |
| `/swiftui-liquid-glass` | [`swiftui-liquid-glass`](skills/frontend-development/swiftui-liquid-glass/SKILL.md) | Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order. |
| `/swiftui-performance-audit` | [`swiftui-performance-audit`](skills/frontend-development/swiftui-performance-audit/SKILL.md) | Audit SwiftUI performance issues from code review and profiling evidence. |
| `/swiftui-ui-patterns` | [`swiftui-ui-patterns`](skills/frontend-development/swiftui-ui-patterns/SKILL.md) | Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens. |
| `/swiftui-view-refactor` | [`swiftui-view-refactor`](skills/frontend-development/swiftui-view-refactor/SKILL.md) | Refactor SwiftUI views into smaller components with stable, explicit data flow. |
| `/tailwind-design-system` | [`tailwind-design-system`](skills/frontend-development/tailwind-design-system/SKILL.md) | Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive. |
| `/tailwind-patterns` | [`tailwind-patterns`](skills/frontend-development/tailwind-patterns/SKILL.md) | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| `/technical-change-tracker` | [`technical-change-tracker`](skills/frontend-development/technical-change-tracker/SKILL.md) | Track code changes with structured JSON records, state machine enforcement, and AI session handoff for bot continuity. |
| `/telegram-bot-builder` | [`telegram-bot-builder`](skills/frontend-development/telegram-bot-builder/SKILL.md) | Expert in building Telegram bots that solve real problems - from. |
| `/telegram-mini-app` | [`telegram-mini-app`](skills/frontend-development/telegram-mini-app/SKILL.md) | Expert in building Telegram Mini Apps (TWA) - web apps that run. |
| `/temporal-golang-pro` | [`temporal-golang-pro`](skills/frontend-development/temporal-golang-pro/SKILL.md) | Use when building durable distributed systems with Temporal Go SDK. |
| `/test-gap-analysis` | [`test-gap-analysis`](skills/frontend-development/test-gap-analysis/SKILL.md) | Performs pseudo-mutation analysis on .NET production code to find gaps in existing test suites. |
| `/test-tagging` | [`test-tagging`](skills/frontend-development/test-tagging/SKILL.md) | Analyzes test suites and tags each test with a standardized set of traits (e.g., positive, negative, critical-path,. |
| `/threejs-materials` | [`threejs-materials`](skills/frontend-development/threejs-materials/SKILL.md) | Three.js materials - PBR, basic, phong, shader materials, material properties. |
| `/tmux` | [`tmux`](skills/frontend-development/tmux/SKILL.md) | Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. |
| `/turborepo-caching` | [`turborepo-caching`](skills/frontend-development/turborepo-caching/SKILL.md) | Configure Turborepo for efficient monorepo builds with local and remote caching. |
| `/typescript-advanced-types` | [`typescript-advanced-types`](skills/frontend-development/typescript-advanced-types/SKILL.md) | Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped. |
| `/typescript-expert` | [`typescript-expert`](skills/frontend-development/typescript-expert/SKILL.md) | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo. |
| `/typescript-pro` | [`typescript-pro`](skills/frontend-development/typescript-pro/SKILL.md) | Master TypeScript with advanced types, generics, and strict type safety. |
| `/ui-a11y` | [`ui-a11y`](skills/frontend-development/ui-a11y/SKILL.md) | Audit a StyleSeed-based component or page for WCAG 2.2 AA issues and apply practical accessibility fixes where the code. |
| `/ui-component` | [`ui-component`](skills/frontend-development/ui-component/SKILL.md) | Generate a new UI component that follows StyleSeed Toss conventions for structure, tokens, accessibility. |
| `/ui-page` | [`ui-page`](skills/frontend-development/ui-page/SKILL.md) | Scaffold a new mobile-first page using StyleSeed Toss layout patterns, section rhythm, and existing shell components. |
| `/ui-pattern` | [`ui-pattern`](skills/frontend-development/ui-pattern/SKILL.md) | Generate reusable UI patterns such as card sections, grids, lists, forms, and chart wrappers using StyleSeed Toss primitives. |
| `/ui-review` | [`ui-review`](skills/frontend-development/ui-review/SKILL.md) | Review UI code for StyleSeed design-system compliance, accessibility, mobile ergonomics, spacing discipline. |
| `/ui-screenshots` | [`ui-screenshots`](skills/frontend-development/ui-screenshots/SKILL.md) | Capture screenshots of web apps during development using Playwright and PIL. |
| `/ui-setup` | [`ui-setup`](skills/frontend-development/ui-setup/SKILL.md) | Interactive StyleSeed setup wizard for choosing app type, brand color, visual style, typography, and the first screen scaffold. |
| `/ui-skills` | [`ui-skills`](skills/frontend-development/ui-skills/SKILL.md) | Opinionated, evolving constraints to guide agents when building interfaces. |
| `/ui-tokens` | [`ui-tokens`](skills/frontend-development/ui-tokens/SKILL.md) | List, add, and update StyleSeed design tokens while keeping JSON sources, CSS variables, and dark-mode values in sync. |
| `/ui-ux-designer` | [`ui-ux-designer`](skills/frontend-development/ui-ux-designer/SKILL.md) | Create interface designs, wireframes, and design systems. |
| `/ui-ux-pro-max` | [`ui-ux-pro-max`](skills/frontend-development/ui-ux-pro-max/SKILL.md) | Comprehensive design guide for web and mobile applications. |
| `/unit-test-vue-pinia` | [`unit-test-vue-pinia`](skills/frontend-development/unit-test-vue-pinia/SKILL.md) | Write and review unit tests for Vue 3 + TypeScript + Vitest + Pinia codebases. |
| `/unity-ecs-patterns` | [`unity-ecs-patterns`](skills/frontend-development/unity-ecs-patterns/SKILL.md) | Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System. |
| `/unreal-engine-cpp-pro` | [`unreal-engine-cpp-pro`](skills/frontend-development/unreal-engine-cpp-pro/SKILL.md) | Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices. |
| `/update-specification` | [`update-specification`](skills/frontend-development/update-specification/SKILL.md) | Update an existing specification file for the solution, optimized for Generative AI consumption based on new. |
| `/ux-audit` | [`ux-audit`](skills/frontend-development/ux-audit/SKILL.md) | Audit screens against Nielsen's heuristics and mobile UX best practices using the StyleSeed Toss design language as the. |
| `/ux-copy` | [`ux-copy`](skills/frontend-development/ux-copy/SKILL.md) | Generate UX microcopy in StyleSeed's Toss-inspired voice for buttons, empty states, errors, toasts, confirmations. |
| `/ux-feedback` | [`ux-feedback`](skills/frontend-development/ux-feedback/SKILL.md) | Add loading, empty, error, and success feedback states to StyleSeed components and pages with practical mobile-first rules. |
| `/ux-flow` | [`ux-flow`](skills/frontend-development/ux-flow/SKILL.md) | Design user flows and screen structure using StyleSeed UX patterns such as progressive disclosure, hub-and-spoke. |
| `/ux-persuasion-engineer` | [`ux-persuasion-engineer`](skills/frontend-development/ux-persuasion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/uxui-principles` | [`uxui-principles`](skills/frontend-development/uxui-principles/SKILL.md) | Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns. |
| `/variant-analysis` | [`variant-analysis`](skills/frontend-development/variant-analysis/SKILL.md) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. |
| `/vercel-ai-sdk-expert` | [`vercel-ai-sdk-expert`](skills/frontend-development/vercel-ai-sdk-expert/SKILL.md) | Expert in the Vercel AI SDK. |
| `/vercel-optimize` | [`vercel-optimize`](skills/frontend-development/vercel-optimize/SKILL.md) | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt. |
| `/vercel-react-best-practices` | [`vercel-react-best-practices`](skills/frontend-development/vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. |
| `/vercel-react-native-skills` | [`vercel-react-native-skills`](skills/frontend-development/vercel-react-native-skills/SKILL.md) | React Native and Expo best practices for building performant mobile apps. |
| `/vercel-react-view-transitions` | [`vercel-react-view-transitions`](skills/frontend-development/vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>`. |
| `/verification-before-completion` | [`verification-before-completion`](skills/frontend-development/verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed. |
| `/viral-generator-builder` | [`viral-generator-builder`](skills/frontend-development/viral-generator-builder/SKILL.md) | Expert in building shareable generator tools that go viral - name. |
| `/vscode-ext-commands` | [`vscode-ext-commands`](skills/frontend-development/vscode-ext-commands/SKILL.md) | Guidelines for contributing commands in VS Code extensions. |
| `/vscode-ext-localization` | [`vscode-ext-localization`](skills/frontend-development/vscode-ext-localization/SKILL.md) | Guidelines for proper localization of VS Code extensions, following VS Code extension development guidelines, libraries. |
| `/vscode-extension-guide-en` | [`vscode-extension-guide-en`](skills/frontend-development/vscode-extension-guide-en/SKILL.md) | Guide for VS Code extension development from scaffolding to Marketplace publication. |
| `/wcag-audit-patterns` | [`wcag-audit-patterns`](skills/frontend-development/wcag-audit-patterns/SKILL.md) | Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. |
| `/web-artifacts-builder` | [`web-artifacts-builder`](skills/frontend-development/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies. |
| `/web-design-guidelines` | [`web-design-guidelines`](skills/frontend-development/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. |
| `/web-perf` | [`web-perf`](skills/frontend-development/web-perf/SKILL.md) | Analyzes web performance using Chrome DevTools MCP. |
| `/web-performance-optimization` | [`web-performance-optimization`](skills/frontend-development/web-performance-optimization/SKILL.md) | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching. |
| `/website` | [`website`](skills/frontend-development/website/SKILL.md) | Build fast, accessible, and SEO-friendly websites with modern best practices. |
| `/wiki-ado-convert` | [`wiki-ado-convert`](skills/frontend-development/wiki-ado-convert/SKILL.md) | Converts VitePress/GFM wiki markdown to Azure DevOps Wiki-compatible format. |
| `/wiki-qa` | [`wiki-qa`](skills/frontend-development/wiki-qa/SKILL.md) | Answers questions about a code repository using source file analysis. |
| `/wiki-vitepress` | [`wiki-vitepress`](skills/frontend-development/wiki-vitepress/SKILL.md) | Packages generated wiki Markdown into a VitePress static site with dark theme, dark-mode Mermaid diagrams with. |
| `/winui3-migration-guide` | [`winui3-migration-guide`](skills/frontend-development/winui3-migration-guide/SKILL.md) | UWP-to-WinUI 3 migration reference. |
| `/wp-plugin-directory-guidelines` | [`wp-plugin-directory-guidelines`](skills/frontend-development/wp-plugin-directory-guidelines/SKILL.md) | Use when reviewing WordPress plugins for GPL compliance, checking license headers or compatibility, evaluating. |
| `/wpds` | [`wpds`](skills/frontend-development/wpds/SKILL.md) | Use when building UIs leveraging the WordPress Design System (WPDS) and its components, tokens, patterns, etc. |
| `/writing-plans` | [`writing-plans`](skills/frontend-development/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code. |
| `/xss-html-injection` | [`xss-html-injection`](skills/frontend-development/xss-html-injection/SKILL.md) | Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML. |
| `/zod-validation-expert` | [`zod-validation-expert`](skills/frontend-development/zod-validation-expert/SKILL.md) | Expert in Zod — TypeScript-first schema validation. |
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
| `/active-directory-attacks` | [`active-directory-attacks`](skills/backend-and-fullstack/active-directory-attacks/SKILL.md) | Provide comprehensive techniques for attacking Microsoft Active Directory environments. |
| `/address-github-comments` | [`address-github-comments`](skills/backend-and-fullstack/address-github-comments/SKILL.md) | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. |
| `/advogado-criminal` | [`advogado-criminal`](skills/backend-and-fullstack/advogado-criminal/SKILL.md) | Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro,. |
| `/advogado-especialista` | [`advogado-especialista`](skills/backend-and-fullstack/advogado-especialista/SKILL.md) | Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor,. |
| `/ai-analyzer` | [`ai-analyzer`](skills/backend-and-fullstack/ai-analyzer/SKILL.md) | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。. |
| `/ai-product` | [`ai-product`](skills/backend-and-fullstack/ai-product/SKILL.md) | Every product will be AI-powered. The question is whether you'll. |
| `/akf-trust-metadata` | [`akf-trust-metadata`](skills/backend-and-fullstack/akf-trust-metadata/SKILL.md) | The AI native file format. |
| `/algolia-search` | [`algolia-search`](skills/backend-and-fullstack/algolia-search/SKILL.md) | Expert patterns for Algolia search implementation, indexing. |
| `/alloydb-basics` | [`alloydb-basics`](skills/backend-and-fullstack/alloydb-basics/SKILL.md) | Manages clusters, instances, and backups for AlloyDB for PostgreSQL, and integrates with AlloyDB model context protocol. |
| `/analyzing-dotnet-performance` | [`analyzing-dotnet-performance`](skills/backend-and-fullstack/analyzing-dotnet-performance/SKILL.md) | Scans .NET code for ~50 performance anti-patterns across async, memory, strings, collections, LINQ, regex, serialization. |
| `/api-security-testing` | [`api-security-testing`](skills/backend-and-fullstack/api-security-testing/SKILL.md) | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input. |
| `/app-store-changelog` | [`app-store-changelog`](skills/backend-and-fullstack/app-store-changelog/SKILL.md) | Generate user-facing App Store release notes from git history since the last tag. |
| `/apple-appstore-reviewer` | [`apple-appstore-reviewer`](skills/backend-and-fullstack/apple-appstore-reviewer/SKILL.md) | Serves as a reviewer of the codebase with instructions on looking for Apple App Store optimizations or rejection reasons. |
| `/architect-review` | [`architect-review`](skills/backend-and-fullstack/architect-review/SKILL.md) | Master software architect specializing in modern architecture. |
| `/architecture-decision-records` | [`architecture-decision-records`](skills/backend-and-fullstack/architecture-decision-records/SKILL.md) | Comprehensive patterns for creating, maintaining. |
| `/arize-annotation` | [`arize-annotation`](skills/backend-and-fullstack/arize-annotation/SKILL.md) | Creates and manages annotation configs (categorical, continuous, freeform label schemas) and annotation queues (human. |
| `/arize-dataset` | [`arize-dataset`](skills/backend-and-fullstack/arize-dataset/SKILL.md) | Creates, manages, and queries Arize datasets and examples. |
| `/arize-experiment` | [`arize-experiment`](skills/backend-and-fullstack/arize-experiment/SKILL.md) | Creates, runs, and analyzes Arize experiments for evaluating and comparing model performance. |
| `/aspire` | [`aspire`](skills/backend-and-fullstack/aspire/SKILL.md) | Aspire skill covering the Aspire CLI, AppHost orchestration, service discovery, integrations, MCP server, VS Code. |
| `/astropy` | [`astropy`](skills/backend-and-fullstack/astropy/SKILL.md) | Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis. |
| `/async-python-patterns` | [`async-python-patterns`](skills/backend-and-fullstack/async-python-patterns/SKILL.md) | Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns. |
| `/avoid-ai-writing` | [`avoid-ai-writing`](skills/backend-and-fullstack/avoid-ai-writing/SKILL.md) | Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table. |
| `/awareness-stage-mapper` | [`awareness-stage-mapper`](skills/backend-and-fullstack/awareness-stage-mapper/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/awt-e2e-testing` | [`awt-e2e-testing`](skills/backend-and-fullstack/awt-e2e-testing/SKILL.md) | AI-powered E2E web testing — eyes and hands for AI coding tools. |
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
| `/backend-architect` | [`backend-architect`](skills/backend-and-fullstack/backend-architect/SKILL.md) | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| `/backend-dev-guidelines` | [`backend-dev-guidelines`](skills/backend-and-fullstack/backend-dev-guidelines/SKILL.md) | You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. |
| `/backend-development-feature-development` | [`backend-development-feature-development`](skills/backend-and-fullstack/backend-development-feature-development/SKILL.md) | Orchestrate end-to-end backend feature development from requirements to deployment. |
| `/backtesting-frameworks` | [`backtesting-frameworks`](skills/backend-and-fullstack/backtesting-frameworks/SKILL.md) | Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates. |
| `/bash-defensive-patterns` | [`bash-defensive-patterns`](skills/backend-and-fullstack/bash-defensive-patterns/SKILL.md) | Master defensive Bash programming techniques for production-grade scripts. |
| `/bash-pro` | [`bash-pro`](skills/backend-and-fullstack/bash-pro/SKILL.md) | Master of defensive Bash scripting for production automation, CI/CD. |
| `/bash-scripting` | [`bash-scripting`](skills/backend-and-fullstack/bash-scripting/SKILL.md) | Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing. |
| `/bats-testing-patterns` | [`bats-testing-patterns`](skills/backend-and-fullstack/bats-testing-patterns/SKILL.md) | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. |
| `/beautiful-prose` | [`beautiful-prose`](skills/backend-and-fullstack/beautiful-prose/SKILL.md) | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. |
| `/behavioral-modes` | [`behavioral-modes`](skills/backend-and-fullstack/behavioral-modes/SKILL.md) | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). |
| `/bigquery-basics` | [`bigquery-basics`](skills/backend-and-fullstack/bigquery-basics/SKILL.md) | Manages datasets, tables, and jobs in BigQuery, and integrates with BigQuery ML and Gemini for advanced data analytics. |
| `/bigquery-pipeline-audit` | [`bigquery-pipeline-audit`](skills/backend-and-fullstack/bigquery-pipeline-audit/SKILL.md) | Audits Python + BigQuery pipelines for cost safety, idempotency, and production readiness. |
| `/binary-analysis-patterns` | [`binary-analysis-patterns`](skills/backend-and-fullstack/binary-analysis-patterns/SKILL.md) | Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code. |
| `/binlog-failure-analysis` | [`binlog-failure-analysis`](skills/backend-and-fullstack/binlog-failure-analysis/SKILL.md) | Analyze MSBuild binary logs to diagnose build failures. Only activate in MSBuild/.NET build context. |
| `/biopython` | [`biopython`](skills/backend-and-fullstack/biopython/SKILL.md) | Biopython is a comprehensive set of freely available Python tools for biological computation. |
| `/brand-perception-psychologist` | [`brand-perception-psychologist`](skills/backend-and-fullstack/brand-perception-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/browser-testing-with-devtools` | [`browser-testing-with-devtools`](skills/backend-and-fullstack/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. |
| `/buddy-sings` | [`buddy-sings`](skills/backend-and-fullstack/buddy-sings/SKILL.md) | Use when user wants their Claude Code pet (/buddy) to sing a song. |
| `/bug-hunter` | [`bug-hunter`](skills/backend-and-fullstack/bug-hunter/SKILL.md) | Systematically finds and fixes bugs using proven debugging techniques. |
| `/bulletmind` | [`bulletmind`](skills/backend-and-fullstack/bulletmind/SKILL.md) | Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking. |
| `/c-pro` | [`c-pro`](skills/backend-and-fullstack/c-pro/SKILL.md) | Write efficient C code with proper memory management, pointer. |
| `/cc-skill-backend-patterns` | [`cc-skill-backend-patterns`](skills/backend-and-fullstack/cc-skill-backend-patterns/SKILL.md) | Backend architecture patterns, API design, database optimization. |
| `/cc-skill-clickhouse-io` | [`cc-skill-clickhouse-io`](skills/backend-and-fullstack/cc-skill-clickhouse-io/SKILL.md) | ClickHouse database patterns, query optimization, analytics. |
| `/check-bin-obj-clash` | [`check-bin-obj-clash`](skills/backend-and-fullstack/check-bin-obj-clash/SKILL.md) | Detects MSBuild projects with conflicting OutputPath or IntermediateOutputPath. |
| `/citation-management` | [`citation-management`](skills/backend-and-fullstack/citation-management/SKILL.md) | Manage citations systematically throughout the research and writing process. |
| `/claimable-postgres` | [`claimable-postgres`](skills/backend-and-fullstack/claimable-postgres/SKILL.md) | Provision instant temporary Postgres databases via Claimable Postgres by Neon (pg.new). |
| `/cloud-sql-basics` | [`cloud-sql-basics`](skills/backend-and-fullstack/cloud-sql-basics/SKILL.md) | This file generates or explains Cloud SQL resources. |
| `/clr-activation-debugging` | [`clr-activation-debugging`](skills/backend-and-fullstack/clr-activation-debugging/SKILL.md) | Diagnoses .NET Framework CLR activation issues using CLR activation logs (CLRLoad logs) produced by mscoree.dll. |
| `/code-refactoring-context-restore` | [`code-refactoring-context-restore`](skills/backend-and-fullstack/code-refactoring-context-restore/SKILL.md) | Use when working with code refactoring context restore. |
| `/code-refactoring-tech-debt` | [`code-refactoring-tech-debt`](skills/backend-and-fullstack/code-refactoring-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. |
| `/code-reviewer` | [`code-reviewer`](skills/backend-and-fullstack/code-reviewer/SKILL.md) | Elite code review expert specializing in modern AI-powered code. |
| `/code-simplification` | [`code-simplification`](skills/backend-and-fullstack/code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. |
| `/code-simplifier` | [`code-simplifier`](skills/backend-and-fullstack/code-simplifier/SKILL.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. |
| `/code-testing-extensions` | [`code-testing-extensions`](skills/backend-and-fullstack/code-testing-extensions/SKILL.md) | Provides file paths to language-specific extension files for the code-testing pipeline. |
| `/code-tour` | [`code-tour`](skills/backend-and-fullstack/code-tour/SKILL.md) | Use this skill to create CodeTour .tour files — persona-targeted, step-by-step walkthroughs that link to real files and. |
| `/codebase-audit-pre-push` | [`codebase-audit-pre-push`](skills/backend-and-fullstack/codebase-audit-pre-push/SKILL.md) | Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. |
| `/codebase-cleanup-tech-debt` | [`codebase-cleanup-tech-debt`](skills/backend-and-fullstack/codebase-cleanup-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. |
| `/commit` | [`commit`](skills/backend-and-fullstack/commit/SKILL.md) | ALWAYS use this skill when committing code changes — never commit directly without it. |
| `/commit-message-storyteller` | [`commit-message-storyteller`](skills/backend-and-fullstack/commit-message-storyteller/SKILL.md) | Analyzes git diffs or staged changes and generates narrative commit messages that explain WHY a change was made, not. |
| `/competitive-landscape` | [`competitive-landscape`](skills/backend-and-fullstack/competitive-landscape/SKILL.md) | Comprehensive frameworks for analyzing competition, identifying differentiation opportunities. |
| `/complexity-cuts` | [`complexity-cuts`](skills/backend-and-fullstack/complexity-cuts/SKILL.md) | Lower Big-O on existing code via a one-transformation-at-a-time playbook with verify-revert-stop. |
| `/comprehensive-review-full-review` | [`comprehensive-review-full-review`](skills/backend-and-fullstack/comprehensive-review-full-review/SKILL.md) | Use when working with comprehensive review full review. |
| `/computer-vision-expert` | [`computer-vision-expert`](skills/backend-and-fullstack/computer-vision-expert/SKILL.md) | SOTA Computer Vision Expert (2026). |
| `/conductor-implement` | [`conductor-implement`](skills/backend-and-fullstack/conductor-implement/SKILL.md) | Execute tasks from a track's implementation plan following TDD workflow. |
| `/conductor-manage` | [`conductor-manage`](skills/backend-and-fullstack/conductor-manage/SKILL.md) | Manage track lifecycle: archive, restore, delete, rename, and cleanup. |
| `/conductor-new-track` | [`conductor-new-track`](skills/backend-and-fullstack/conductor-new-track/SKILL.md) | Create a new track with specification and phased implementation plan. |
| `/conductor-revert` | [`conductor-revert`](skills/backend-and-fullstack/conductor-revert/SKILL.md) | Git-aware undo by logical work unit (track, phase, or task). |
| `/conductor-status` | [`conductor-status`](skills/backend-and-fullstack/conductor-status/SKILL.md) | Display project status, active tracks, and next actions. |
| `/configuring-opentelemetry-dotnet` | [`configuring-opentelemetry-dotnet`](skills/backend-and-fullstack/configuring-opentelemetry-dotnet/SKILL.md) | Configure OpenTelemetry distributed tracing, metrics, and logging in ASP.NET Core using the .NET OpenTelemetry SDK. |
| `/containerize-aspnet-framework` | [`containerize-aspnet-framework`](skills/backend-and-fullstack/containerize-aspnet-framework/SKILL.md) | Containerize an ASP.NET .NET Framework project by creating Dockerfile and .dockerfile files customized for the project. |
| `/containerize-aspnetcore` | [`containerize-aspnetcore`](skills/backend-and-fullstack/containerize-aspnetcore/SKILL.md) | Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project. |
| `/context-guardian` | [`context-guardian`](skills/backend-and-fullstack/context-guardian/SKILL.md) | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. |
| `/context-management-context-restore` | [`context-management-context-restore`](skills/backend-and-fullstack/context-management-context-restore/SKILL.md) | Use when working with context management context restore. |
| `/context-management-context-save` | [`context-management-context-save`](skills/backend-and-fullstack/context-management-context-save/SKILL.md) | Use when working with context management context save. |
| `/context-manager` | [`context-manager`](skills/backend-and-fullstack/context-manager/SKILL.md) | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs. |
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
| `/create-pr` | [`create-pr`](skills/backend-and-fullstack/create-pr/SKILL.md) | Alias for sentry-skills:pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. |
| `/create-readme` | [`create-readme`](skills/backend-and-fullstack/create-readme/SKILL.md) | Create a README.md file for the project. |
| `/create-spring-boot-java-project` | [`create-spring-boot-java-project`](skills/backend-and-fullstack/create-spring-boot-java-project/SKILL.md) | Create Spring Boot Java Project Skeleton. |
| `/create-spring-boot-kotlin-project` | [`create-spring-boot-kotlin-project`](skills/backend-and-fullstack/create-spring-boot-kotlin-project/SKILL.md) | Create Spring Boot Kotlin Project Skeleton. |
| `/creating-oracle-to-postgres-master-migration-plan` | [`creating-oracle-to-postgres-master-migration-plan`](skills/backend-and-fullstack/creating-oracle-to-postgres-master-migration-plan/SKILL.md) | Discovers all projects in a .NET solution, classifies each for Oracle-to-PostgreSQL migration eligibility. |
| `/creating-oracle-to-postgres-migration-bug-report` | [`creating-oracle-to-postgres-migration-bug-report`](skills/backend-and-fullstack/creating-oracle-to-postgres-migration-bug-report/SKILL.md) | Creates structured bug reports for defects found during Oracle-to-PostgreSQL migration. |
| `/creating-oracle-to-postgres-migration-integration-tests` | [`creating-oracle-to-postgres-migration-integration-tests`](skills/backend-and-fullstack/creating-oracle-to-postgres-migration-integration-tests/SKILL.md) | Creates integration test cases for .NET data access artifacts during Oracle-to-PostgreSQL database migrations. |
| `/cred-omega` | [`cred-omega`](skills/backend-and-fullstack/cred-omega/SKILL.md) | CISO operacional enterprise para gestao total de credenciais e segredos. |
| `/csharp-async` | [`csharp-async`](skills/backend-and-fullstack/csharp-async/SKILL.md) | Get best practices for C# async programming. |
| `/csharp-docs` | [`csharp-docs`](skills/backend-and-fullstack/csharp-docs/SKILL.md) | Ensure that C# types are documented with XML comments and follow best practices for documentation. |
| `/csharp-mstest` | [`csharp-mstest`](skills/backend-and-fullstack/csharp-mstest/SKILL.md) | Get best practices for MSTest 3.x/4.x unit testing, including modern assertion APIs and data-driven tests. |
| `/csharp-nunit` | [`csharp-nunit`](skills/backend-and-fullstack/csharp-nunit/SKILL.md) | Get best practices for NUnit unit testing, including data-driven tests. |
| `/csharp-pro` | [`csharp-pro`](skills/backend-and-fullstack/csharp-pro/SKILL.md) | Write modern C# code with advanced features like records, pattern matching, and async/await. |
| `/csharp-scripts` | [`csharp-scripts`](skills/backend-and-fullstack/csharp-scripts/SKILL.md) | Run file-based C# apps with the .NET CLI when the user explicitly wants C#/.NET code without creating a project. |
| `/csharp-tunit` | [`csharp-tunit`](skills/backend-and-fullstack/csharp-tunit/SKILL.md) | Get best practices for TUnit unit testing, including data-driven tests. |
| `/csharp-xunit` | [`csharp-xunit`](skills/backend-and-fullstack/csharp-xunit/SKILL.md) | Get best practices for XUnit unit testing, including data-driven tests. |
| `/customer-support` | [`customer-support`](skills/backend-and-fullstack/customer-support/SKILL.md) | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis. |
| `/data-engineering-data-pipeline` | [`data-engineering-data-pipeline`](skills/backend-and-fullstack/data-engineering-data-pipeline/SKILL.md) | You are a data pipeline architecture expert specializing in scalable, reliable. |
| `/data-storytelling` | [`data-storytelling`](skills/backend-and-fullstack/data-storytelling/SKILL.md) | Transform raw data into compelling narratives that drive decisions and inspire action. |
| `/database` | [`database`](skills/backend-and-fullstack/database/SKILL.md) | Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering. |
| `/database-admin` | [`database-admin`](skills/backend-and-fullstack/database-admin/SKILL.md) | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| `/database-architect` | [`database-architect`](skills/backend-and-fullstack/database-architect/SKILL.md) | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling. |
| `/database-design` | [`database-design`](skills/backend-and-fullstack/database-design/SKILL.md) | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| `/database-migration` | [`database-migration`](skills/backend-and-fullstack/database-migration/SKILL.md) | Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and. |
| `/database-migrations-migration-observability` | [`database-migrations-migration-observability`](skills/backend-and-fullstack/database-migrations-migration-observability/SKILL.md) | Migration monitoring, CDC, and observability infrastructure. |
| `/database-migrations-sql-migrations` | [`database-migrations-sql-migrations`](skills/backend-and-fullstack/database-migrations-sql-migrations/SKILL.md) | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. |
| `/database-optimizer` | [`database-optimizer`](skills/backend-and-fullstack/database-optimizer/SKILL.md) | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| `/dataverse-python-advanced-patterns` | [`dataverse-python-advanced-patterns`](skills/backend-and-fullstack/dataverse-python-advanced-patterns/SKILL.md) | Generate production code for Dataverse SDK using advanced patterns, error handling, and optimization techniques. |
| `/dataverse-python-production-code` | [`dataverse-python-production-code`](skills/backend-and-fullstack/dataverse-python-production-code/SKILL.md) | Generate production-ready Python code using Dataverse SDK with error handling, optimization, and best practices. |
| `/dataverse-python-quickstart` | [`dataverse-python-quickstart`](skills/backend-and-fullstack/dataverse-python-quickstart/SKILL.md) | Generate Python SDK setup + CRUD + bulk + paging snippets using official patterns. |
| `/dbos-python` | [`dbos-python`](skills/backend-and-fullstack/dbos-python/SKILL.md) | Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. |
| `/ddd-tactical-patterns` | [`ddd-tactical-patterns`](skills/backend-and-fullstack/ddd-tactical-patterns/SKILL.md) | Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories. |
| `/debugger` | [`debugger`](skills/backend-and-fullstack/debugger/SKILL.md) | Debugging specialist for errors, test failures, and unexpected. |
| `/debugging-strategies` | [`debugging-strategies`](skills/backend-and-fullstack/debugging-strategies/SKILL.md) | Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools. |
| `/deep-research` | [`deep-research`](skills/backend-and-fullstack/deep-research/SKILL.md) | Run autonomous research tasks that plan, search, read, and synthesize information into comprehensive reports. |
| `/dependabot` | [`dependabot`](skills/backend-and-fullstack/dependabot/SKILL.md) | Comprehensive guide for configuring and managing GitHub Dependabot. |
| `/dependency-upgrade` | [`dependency-upgrade`](skills/backend-and-fullstack/dependency-upgrade/SKILL.md) | Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches. |
| `/detect-static-dependencies` | [`detect-static-dependencies`](skills/backend-and-fullstack/detect-static-dependencies/SKILL.md) | Scan C# source files for hard-to-test static dependencies — DateTime.Now/UtcNow, File.*, Directory.*, Environment.*,. |
| `/devcontainer-setup` | [`devcontainer-setup`](skills/backend-and-fullstack/devcontainer-setup/SKILL.md) | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. |
| `/diary` | [`diary`](skills/backend-and-fullstack/diary/SKILL.md) | Unified Diary System: A context-preserving automated logger for multi-project development. |
| `/distributed-debugging-debug-trace` | [`distributed-debugging-debug-trace`](skills/backend-and-fullstack/distributed-debugging-debug-trace/SKILL.md) | You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing. |
| `/django-access-review` | [`django-access-review`](skills/backend-and-fullstack/django-access-review/SKILL.md) | django-access-review. |
| `/django-perf-review` | [`django-perf-review`](skills/backend-and-fullstack/django-perf-review/SKILL.md) | Django performance code review. |
| `/django-pro` | [`django-pro`](skills/backend-and-fullstack/django-pro/SKILL.md) | Master Django 5.x with async views, DRF, Celery, and Django Channels. |
| `/docker-expert` | [`docker-expert`](skills/backend-and-fullstack/docker-expert/SKILL.md) | You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization,. |
| `/dotnet-aot-compat` | [`dotnet-aot-compat`](skills/backend-and-fullstack/dotnet-aot-compat/SKILL.md) | Make .NET projects compatible with Native AOT and trimming by systematically resolving IL trim/AOT analyzer warnings. |
| `/dotnet-architect` | [`dotnet-architect`](skills/backend-and-fullstack/dotnet-architect/SKILL.md) | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| `/dotnet-backend` | [`dotnet-backend`](skills/backend-and-fullstack/dotnet-backend/SKILL.md) | Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns. |
| `/dotnet-backend-patterns` | [`dotnet-backend-patterns`](skills/backend-and-fullstack/dotnet-backend-patterns/SKILL.md) | Master C#/.NET patterns for building production-grade APIs, MCP servers. |
| `/dotnet-best-practices` | [`dotnet-best-practices`](skills/backend-and-fullstack/dotnet-best-practices/SKILL.md) | Ensure .NET/C# code meets best practices for the solution/project. |
| `/dotnet-pinvoke` | [`dotnet-pinvoke`](skills/backend-and-fullstack/dotnet-pinvoke/SKILL.md) | Correctly call native (C/C++) libraries from .NET using P/Invoke and LibraryImport. |
| `/dotnet-test-frameworks` | [`dotnet-test-frameworks`](skills/backend-and-fullstack/dotnet-test-frameworks/SKILL.md) | Reference data for .NET test framework detection patterns, assertion APIs, skip annotations, setup/teardown methods. |
| `/dotnet-timezone` | [`dotnet-timezone`](skills/backend-and-fullstack/dotnet-timezone/SKILL.md) | .NET timezone handling guidance for C# applications. |
| `/dotnet-trace-collect` | [`dotnet-trace-collect`](skills/backend-and-fullstack/dotnet-trace-collect/SKILL.md) | Guide developers through capturing diagnostic artifacts to diagnose production .NET performance issues. |
| `/dotnet-upgrade` | [`dotnet-upgrade`](skills/backend-and-fullstack/dotnet-upgrade/SKILL.md) | Ready-to-use prompts for comprehensive .NET framework upgrade analysis and execution. |
| `/doublecheck` | [`doublecheck`](skills/backend-and-fullstack/doublecheck/SKILL.md) | Three-layer verification pipeline for AI output. |
| `/dump-collect` | [`dump-collect`](skills/backend-and-fullstack/dump-collect/SKILL.md) | Configure and collect crash dumps for modern .NET applications. |
| `/dwarf-expert` | [`dwarf-expert`](skills/backend-and-fullstack/dwarf-expert/SKILL.md) | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). |
| `/dx-optimizer` | [`dx-optimizer`](skills/backend-and-fullstack/dx-optimizer/SKILL.md) | Developer Experience specialist. Improves tooling, setup, and workflows. |
| `/e2e-testing` | [`e2e-testing`](skills/backend-and-fullstack/e2e-testing/SKILL.md) | End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing. |
| `/e2e-testing-patterns` | [`e2e-testing-patterns`](skills/backend-and-fullstack/e2e-testing-patterns/SKILL.md) | Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch. |
| `/ef-core` | [`ef-core`](skills/backend-and-fullstack/ef-core/SKILL.md) | Get best practices for Entity Framework Core. |
| `/efcore-d2-db-diagram` | [`efcore-d2-db-diagram`](skills/backend-and-fullstack/efcore-d2-db-diagram/SKILL.md) | Generate D2 database diagrams from Entity Framework Core models. |
| `/elixir-pro` | [`elixir-pro`](skills/backend-and-fullstack/elixir-pro/SKILL.md) | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. |
| `/emergency-card` | [`emergency-card`](skills/backend-and-fullstack/emergency-card/SKILL.md) | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。. |
| `/energy-procurement` | [`energy-procurement`](skills/backend-and-fullstack/energy-procurement/SKILL.md) | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA. |
| `/error-debugging-error-analysis` | [`error-debugging-error-analysis`](skills/backend-and-fullstack/error-debugging-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production. |
| `/error-diagnostics-error-analysis` | [`error-diagnostics-error-analysis`](skills/backend-and-fullstack/error-diagnostics-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production. |
| `/error-diagnostics-error-trace` | [`error-diagnostics-error-trace`](skills/backend-and-fullstack/error-diagnostics-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. |
| `/eval-driven-dev` | [`eval-driven-dev`](skills/backend-and-fullstack/eval-driven-dev/SKILL.md) | Improve AI application with evaluation-driven development. |
| `/eval-performance` | [`eval-performance`](skills/backend-and-fullstack/eval-performance/SKILL.md) | Guide for diagnosing and improving MSBuild project evaluation performance. |
| `/evolution` | [`evolution`](skills/backend-and-fullstack/evolution/SKILL.md) | This skill enables makepad-skills to self-improve continuously during development. |
| `/exam-ready` | [`exam-ready`](skills/backend-and-fullstack/exam-ready/SKILL.md) | Activate this skill when a student provides study material (PDF or pasted notes) and a syllabus, and wants to prepare for an exam. |
| `/executing-plans` | [`executing-plans`](skills/backend-and-fullstack/executing-plans/SKILL.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints. |
| `/exp-mock-usage-analysis` | [`exp-mock-usage-analysis`](skills/backend-and-fullstack/exp-mock-usage-analysis/SKILL.md) | Audits .NET test mock usage by tracing each mock setup through the production code's execution path to find dead,. |
| `/explain-like-socrates` | [`explain-like-socrates`](skills/backend-and-fullstack/explain-like-socrates/SKILL.md) | Explains concepts using Socratic-style dialogue. |
| `/fal-image-edit` | [`fal-image-edit`](skills/backend-and-fullstack/fal-image-edit/SKILL.md) | AI-powered image editing with style transfer and object removal. |
| `/family-health-analyzer` | [`family-health-analyzer`](skills/backend-and-fullstack/family-health-analyzer/SKILL.md) | 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议. |
| `/file-organizer` | [`file-organizer`](skills/backend-and-fullstack/file-organizer/SKILL.md) | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates,. |
| `/file-path-traversal` | [`file-path-traversal`](skills/backend-and-fullstack/file-path-traversal/SKILL.md) | Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary. |
| `/filesystem-context` | [`filesystem-context`](skills/backend-and-fullstack/filesystem-context/SKILL.md) | Use for file-based context management, dynamic context discovery, and reducing context window bloat. |
| `/filter-syntax` | [`filter-syntax`](skills/backend-and-fullstack/filter-syntax/SKILL.md) | Reference data for test filter syntax across all platform and framework combinations: VSTest --filter expressions, MTP. |
| `/firebase` | [`firebase`](skills/backend-and-fullstack/firebase/SKILL.md) | Firebase gives you a complete backend in minutes - auth, database,. |
| `/fitness-analyzer` | [`fitness-analyzer`](skills/backend-and-fullstack/fitness-analyzer/SKILL.md) | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。. |
| `/fix-review` | [`fix-review`](skills/backend-and-fullstack/fix-review/SKILL.md) | Verify fix commits address audit findings without new bugs. |
| `/flowstudio-power-automate-debug` | [`flowstudio-power-automate-debug`](skills/backend-and-fullstack/flowstudio-power-automate-debug/SKILL.md) | Debug failing Power Automate cloud flows using the FlowStudio MCP server. |
| `/flowstudio-power-automate-monitoring` | [`flowstudio-power-automate-monitoring`](skills/backend-and-fullstack/flowstudio-power-automate-monitoring/SKILL.md) | Pro+ subscription required. |
| `/food-database-query` | [`food-database-query`](skills/backend-and-fullstack/food-database-query/SKILL.md) | Food Database Query. |
| `/fp-backend` | [`fp-backend`](skills/backend-and-fullstack/fp-backend/SKILL.md) | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither. |
| `/fp-data-transforms` | [`fp-data-transforms`](skills/backend-and-fullstack/fp-data-transforms/SKILL.md) | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access. |
| `/fp-errors` | [`fp-errors`](skills/backend-and-fullstack/fp-errors/SKILL.md) | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code. |
| `/framework-migration-deps-upgrade` | [`framework-migration-deps-upgrade`](skills/backend-and-fullstack/framework-migration-deps-upgrade/SKILL.md) | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. |
| `/from-the-other-side-anitta` | [`from-the-other-side-anitta`](skills/backend-and-fullstack/from-the-other-side-anitta/SKILL.md) | Rigorous challenge profile for Anitta: assumption checks, evidence calibration. |
| `/full-stack-orchestration-full-stack-feature` | [`full-stack-orchestration-full-stack-feature`](skills/backend-and-fullstack/full-stack-orchestration-full-stack-feature/SKILL.md) | Use when working with full stack orchestration full stack feature. |
| `/fullstack-dev` | [`fullstack-dev`](skills/backend-and-fullstack/fullstack-dev/SKILL.md) | Full-stack backend architecture and frontend-backend integration guide. |
| `/game-development` | [`game-development`](skills/backend-and-fullstack/game-development/SKILL.md) | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| `/geofeed-tuner` | [`geofeed-tuner`](skills/backend-and-fullstack/geofeed-tuner/SKILL.md) | Use this skill whenever the user mentions IP geolocation feeds, RFC 8805, geofeeds. |
| `/gh-review-requests` | [`gh-review-requests`](skills/backend-and-fullstack/gh-review-requests/SKILL.md) | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. |
| `/git-advanced-workflows` | [`git-advanced-workflows`](skills/backend-and-fullstack/git-advanced-workflows/SKILL.md) | Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence. |
| `/git-commit` | [`git-commit`](skills/backend-and-fullstack/git-commit/SKILL.md) | Execute git commit with conventional commit message analysis, intelligent staging, and message generation. |
| `/git-flow-branch-creator` | [`git-flow-branch-creator`](skills/backend-and-fullstack/git-flow-branch-creator/SKILL.md) | Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie. |
| `/git-hooks-automation` | [`git-hooks-automation`](skills/backend-and-fullstack/git-hooks-automation/SKILL.md) | Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. |
| `/git-pr-review` | [`git-pr-review`](skills/backend-and-fullstack/git-pr-review/SKILL.md) | Generate a concise and structured PR description from commit history with minimal token usage. |
| `/git-pr-workflows-git-workflow` | [`git-pr-workflows-git-workflow`](skills/backend-and-fullstack/git-pr-workflows-git-workflow/SKILL.md) | Orchestrate a comprehensive git workflow from code review through PR creation, leveraging specialized agents for. |
| `/git-pr-workflows-onboard` | [`git-pr-workflows-onboard`](skills/backend-and-fullstack/git-pr-workflows-onboard/SKILL.md) | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first. |
| `/git-pr-workflows-pr-enhance` | [`git-pr-workflows-pr-enhance`](skills/backend-and-fullstack/git-pr-workflows-pr-enhance/SKILL.md) | You are a PR optimization expert specializing in creating high-quality pull requests that facilitate efficient code reviews. |
| `/git-pushing` | [`git-pushing`](skills/backend-and-fullstack/git-pushing/SKILL.md) | Stage all changes, create a conventional commit, and push to the remote branch. |
| `/git-workflow-and-versioning` | [`git-workflow-and-versioning`](skills/backend-and-fullstack/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. |
| `/github` | [`github`](skills/backend-and-fullstack/github/SKILL.md) | Use the `gh` CLI for issues, pull requests, Actions runs, and GitHub API queries. |
| `/github-actions-advanced` | [`github-actions-advanced`](skills/backend-and-fullstack/github-actions-advanced/SKILL.md) | Design, debug, and harden GitHub Actions CI/CD workflows, including reusable workflows, matrix builds, self-hosted. |
| `/github-actions-efficiency` | [`github-actions-efficiency`](skills/backend-and-fullstack/github-actions-efficiency/SKILL.md) | Audit GitHub Actions workflow efficiency and recommend fixes to reduce CI minutes and costs. |
| `/github-actions-templates` | [`github-actions-templates`](skills/backend-and-fullstack/github-actions-templates/SKILL.md) | Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications. |
| `/github-codespaces-efficiency` | [`github-codespaces-efficiency`](skills/backend-and-fullstack/github-codespaces-efficiency/SKILL.md) | Audit and improve GitHub Codespaces efficiency. |
| `/github-copilot-starter` | [`github-copilot-starter`](skills/backend-and-fullstack/github-copilot-starter/SKILL.md) | Set up complete GitHub Copilot configuration for a new project based on technology stack. |
| `/github-issue-creator` | [`github-issue-creator`](skills/backend-and-fullstack/github-issue-creator/SKILL.md) | Convert raw notes, error logs, voice dictation, or screenshots into crisp GitHub-flavored markdown issue reports. |
| `/github-issues` | [`github-issues`](skills/backend-and-fullstack/github-issues/SKILL.md) | Create, update, and manage GitHub issues using MCP tools. |
| `/github-release` | [`github-release`](skills/backend-and-fullstack/github-release/SKILL.md) | Guides IA through releasing a new version of a GitHub library end-to-end. |
| `/github-workflow-automation` | [`github-workflow-automation`](skills/backend-and-fullstack/github-workflow-automation/SKILL.md) | Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini. |
| `/gitlab-ci-patterns` | [`gitlab-ci-patterns`](skills/backend-and-fullstack/gitlab-ci-patterns/SKILL.md) | Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment. |
| `/gitops-workflow` | [`gitops-workflow`](skills/backend-and-fullstack/gitops-workflow/SKILL.md) | Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments. |
| `/go-mcp-server-generator` | [`go-mcp-server-generator`](skills/backend-and-fullstack/go-mcp-server-generator/SKILL.md) | Generate a complete Go MCP server project with proper structure, dependencies. |
| `/goal-analyzer` | [`goal-analyzer`](skills/backend-and-fullstack/goal-analyzer/SKILL.md) | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。. |
| `/grafana-dashboards` | [`grafana-dashboards`](skills/backend-and-fullstack/grafana-dashboards/SKILL.md) | Create and manage production-ready Grafana dashboards for comprehensive system observability. |
| `/graphql` | [`graphql`](skills/backend-and-fullstack/graphql/SKILL.md) | GraphQL gives clients exactly the data they need - no more, no. |
| `/graphql-architect` | [`graphql-architect`](skills/backend-and-fullstack/graphql-architect/SKILL.md) | Master modern GraphQL with federation, performance optimization, and enterprise security. |
| `/haskell-pro` | [`haskell-pro`](skills/backend-and-fullstack/haskell-pro/SKILL.md) | Expert Haskell engineer specializing in advanced type systems, pure. |
| `/headline-psychologist` | [`headline-psychologist`](skills/backend-and-fullstack/headline-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/hugging-face-cli` | [`hugging-face-cli`](skills/backend-and-fullstack/hugging-face-cli/SKILL.md) | Use the Hugging Face Hub CLI (`hf`) to download, upload, and manage models, datasets, and Spaces. |
| `/hugging-face-community-evals` | [`hugging-face-community-evals`](skills/backend-and-fullstack/hugging-face-community-evals/SKILL.md) | Run local evaluations for Hugging Face Hub models with inspect-ai or lighteval. |
| `/hugging-face-jobs` | [`hugging-face-jobs`](skills/backend-and-fullstack/hugging-face-jobs/SKILL.md) | Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence. |
| `/hugging-face-model-trainer` | [`hugging-face-model-trainer`](skills/backend-and-fullstack/hugging-face-model-trainer/SKILL.md) | Train or fine-tune TRL language models on Hugging Face Jobs, including SFT, DPO, GRPO, and GGUF export. |
| `/hugging-face-trackio` | [`hugging-face-trackio`](skills/backend-and-fullstack/hugging-face-trackio/SKILL.md) | Track ML experiments with Trackio using Python logging, alerts, and CLI metric retrieval. |
| `/hugging-face-vision-trainer` | [`hugging-face-vision-trainer`](skills/backend-and-fullstack/hugging-face-vision-trainer/SKILL.md) | Train or fine-tune vision models on Hugging Face Jobs for detection, classification, and SAM or SAM2 segmentation. |
| `/huggingface-best` | [`huggingface-best`](skills/backend-and-fullstack/huggingface-best/SKILL.md) | Use when the user asks about finding the best, top. |
| `/humanizer` | [`humanizer`](skills/backend-and-fullstack/humanizer/SKILL.md) | Remove signs of AI-generated writing from text. |
| `/idea-os` | [`idea-os`](skills/backend-and-fullstack/idea-os/SKILL.md) | Five-phase pipeline (triage → clarify → research → PRD → plan) that turns a raw idea into four linked files: clarifying. |
| `/idea-refine` | [`idea-refine`](skills/backend-and-fullstack/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| `/identity-mirror` | [`identity-mirror`](skills/backend-and-fullstack/identity-mirror/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/idor-testing` | [`idor-testing`](skills/backend-and-fullstack/idor-testing/SKILL.md) | Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities. |
| `/image-manipulation-image-magick` | [`image-manipulation-image-magick`](skills/backend-and-fullstack/image-manipulation-image-magick/SKILL.md) | Process and manipulate images using ImageMagick. |
| `/incident-response-incident-response` | [`incident-response-incident-response`](skills/backend-and-fullstack/incident-response-incident-response/SKILL.md) | Use when working with incident response incident response. |
| `/incident-runbook-templates` | [`incident-runbook-templates`](skills/backend-and-fullstack/incident-runbook-templates/SKILL.md) | Production-ready templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication. |
| `/incremental-implementation` | [`incremental-implementation`](skills/backend-and-fullstack/incremental-implementation/SKILL.md) | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. |
| `/inngest` | [`inngest`](skills/backend-and-fullstack/inngest/SKILL.md) | Inngest expert for serverless-first background jobs, event-driven. |
| `/interview-coach` | [`interview-coach`](skills/backend-and-fullstack/interview-coach/SKILL.md) | Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. |
| `/inventory-demand-planning` | [`inventory-demand-planning`](skills/backend-and-fullstack/inventory-demand-planning/SKILL.md) | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning. |
| `/issue-fields-migration` | [`issue-fields-migration`](skills/backend-and-fullstack/issue-fields-migration/SKILL.md) | Bulk-migrate metadata to GitHub issue fields from two sources: repo labels (e.g. |
| `/issues` | [`issues`](skills/backend-and-fullstack/issues/SKILL.md) | Interact with GitHub issues - create, list, and view issues. |
| `/it-manager-hospital` | [`it-manager-hospital`](skills/backend-and-fullstack/it-manager-hospital/SKILL.md) | World-class Hospital IT Management Advisor specializing in clinical safety, digital maturity (HIMSS/ONA/JCI). |
| `/it-manager-pro` | [`it-manager-pro`](skills/backend-and-fullstack/it-manager-pro/SKILL.md) | Elite IT Management Advisor specializing in data-driven strategy, executive communication. |
| `/iterate-pr` | [`iterate-pr`](skills/backend-and-fullstack/iterate-pr/SKILL.md) | Iterate on a PR until CI passes. |
| `/itil-expert` | [`itil-expert`](skills/backend-and-fullstack/itil-expert/SKILL.md) | Expert advisor for ITIL 4 and ITIL 5 (2026 digital product paradigm), specialized in AI-native governance,. |
| `/java-add-graalvm-native-image-support` | [`java-add-graalvm-native-image-support`](skills/backend-and-fullstack/java-add-graalvm-native-image-support/SKILL.md) | GraalVM Native Image expert that adds native image support to Java applications, builds the project, analyzes build. |
| `/java-docs` | [`java-docs`](skills/backend-and-fullstack/java-docs/SKILL.md) | Ensure that Java types are documented with Javadoc comments and follow best practices for documentation. |
| `/java-junit` | [`java-junit`](skills/backend-and-fullstack/java-junit/SKILL.md) | Get best practices for JUnit 5 unit testing, including data-driven tests. |
| `/java-mcp-server-generator` | [`java-mcp-server-generator`](skills/backend-and-fullstack/java-mcp-server-generator/SKILL.md) | Generate a complete Model Context Protocol server project in Java using the official MCP Java SDK with reactive streams. |
| `/java-pro` | [`java-pro`](skills/backend-and-fullstack/java-pro/SKILL.md) | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. |
| `/java-refactoring-extract-method` | [`java-refactoring-extract-method`](skills/backend-and-fullstack/java-refactoring-extract-method/SKILL.md) | Refactoring using Extract Methods in Java Language. |
| `/java-refactoring-remove-parameter` | [`java-refactoring-remove-parameter`](skills/backend-and-fullstack/java-refactoring-remove-parameter/SKILL.md) | Refactoring using Remove Parameter in Java Language. |
| `/java-springboot` | [`java-springboot`](skills/backend-and-fullstack/java-springboot/SKILL.md) | Get best practices for developing applications with Spring Boot. |
| `/javascript-mastery` | [`javascript-mastery`](skills/backend-and-fullstack/javascript-mastery/SKILL.md) | 33+ essential JavaScript concepts every developer should know, inspired by. |
| `/javascript-pro` | [`javascript-pro`](skills/backend-and-fullstack/javascript-pro/SKILL.md) | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. |
| `/javascript-testing-patterns` | [`javascript-testing-patterns`](skills/backend-and-fullstack/javascript-testing-patterns/SKILL.md) | Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern. |
| `/jobs-to-be-done-analyst` | [`jobs-to-be-done-analyst`](skills/backend-and-fullstack/jobs-to-be-done-analyst/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/julia-pro` | [`julia-pro`](skills/backend-and-fullstack/julia-pro/SKILL.md) | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| `/k6-load-testing` | [`k6-load-testing`](skills/backend-and-fullstack/k6-load-testing/SKILL.md) | Comprehensive k6 load testing skill for API, browser, and scalability testing. |
| `/kotlin-coroutines-expert` | [`kotlin-coroutines-expert`](skills/backend-and-fullstack/kotlin-coroutines-expert/SKILL.md) | Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing. |
| `/kotlin-springboot` | [`kotlin-springboot`](skills/backend-and-fullstack/kotlin-springboot/SKILL.md) | Get best practices for developing applications with Spring Boot and Kotlin. |
| `/legacy-modernizer` | [`legacy-modernizer`](skills/backend-and-fullstack/legacy-modernizer/SKILL.md) | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. |
| `/leiloeiro-edital` | [`leiloeiro-edital`](skills/backend-and-fullstack/leiloeiro-edital/SKILL.md) | Analise e auditoria de editais de leilao judicial e extrajudicial. |
| `/leiloeiro-ia` | [`leiloeiro-ia`](skills/backend-and-fullstack/leiloeiro-ia/SKILL.md) | Especialista em leiloes judiciais e extrajudiciais de imoveis. |
| `/lemmaly` | [`lemmaly`](skills/backend-and-fullstack/lemmaly/SKILL.md) | Algorithm-first discipline: state Big-O, data structure, and algorithm family BEFORE writing loops, queries, or recursion. |
| `/lint-and-validate` | [`lint-and-validate`](skills/backend-and-fullstack/lint-and-validate/SKILL.md) | MANDATORY: Run appropriate validation tools after EVERY code change. |
| `/logistics-exception-management` | [`logistics-exception-management`](skills/backend-and-fullstack/logistics-exception-management/SKILL.md) | Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. |
| `/lsp-setup` | [`lsp-setup`](skills/backend-and-fullstack/lsp-setup/SKILL.md) | Enable code intelligence (go-to-definition, find-references, hover, type info) for any programming language by. |
| `/makepad-event-action` | [`makepad-event-action`](skills/backend-and-fullstack/makepad-event-action/SKILL.md) | CRITICAL: Use for Makepad event and action handling. |
| `/makepad-splash` | [`makepad-splash`](skills/backend-and-fullstack/makepad-splash/SKILL.md) | CRITICAL: Use for Makepad Splash scripting language. |
| `/makepad-widgets` | [`makepad-widgets`](skills/backend-and-fullstack/makepad-widgets/SKILL.md) | Version: makepad-widgets (dev branch) \| Last Updated: 2026-01-19 > > Check for updates: https://crates.io/crates/makepad-widgets. |
| `/mathguard` | [`mathguard`](skills/backend-and-fullstack/mathguard/SKILL.md) | Math-heavy escalation for n >= 10^6 — Bloom, HyperLogLog, Count-Min, MinHash/LSH, FFT, JL projection, sweep line. |
| `/memory-merger` | [`memory-merger`](skills/backend-and-fullstack/memory-merger/SKILL.md) | Merges mature lessons from a domain memory file into its instruction file. |
| `/mental-health-analyzer` | [`mental-health-analyzer`](skills/backend-and-fullstack/mental-health-analyzer/SKILL.md) | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。. |
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
| `/monte-carlo-prevent` | [`monte-carlo-prevent`](skills/backend-and-fullstack/monte-carlo-prevent/SKILL.md) | Surfaces Monte Carlo data observability context (table health, alerts, lineage, blast radius) before SQL/dbt edits. |
| `/monte-carlo-validation-notebook` | [`monte-carlo-validation-notebook`](skills/backend-and-fullstack/monte-carlo-validation-notebook/SKILL.md) | Generates SQL validation notebooks for dbt PR changes with before/after comparison queries. |
| `/mtls-configuration` | [`mtls-configuration`](skills/backend-and-fullstack/mtls-configuration/SKILL.md) | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. |
| `/mtp-hot-reload` | [`mtp-hot-reload`](skills/backend-and-fullstack/mtp-hot-reload/SKILL.md) | Suggests using Microsoft Testing Platform (MTP) hot reload to iterate fixes on failing tests without rebuilding. |
| `/multi-stage-dockerfile` | [`multi-stage-dockerfile`](skills/backend-and-fullstack/multi-stage-dockerfile/SKILL.md) | Create optimized multi-stage Dockerfiles for any language or framework. |
| `/n8n-code-javascript` | [`n8n-code-javascript`](skills/backend-and-fullstack/n8n-code-javascript/SKILL.md) | Write JavaScript code in n8n Code nodes. |
| `/n8n-code-python` | [`n8n-code-python`](skills/backend-and-fullstack/n8n-code-python/SKILL.md) | Write Python code in n8n Code nodes. |
| `/n8n-expression-syntax` | [`n8n-expression-syntax`](skills/backend-and-fullstack/n8n-expression-syntax/SKILL.md) | Validate n8n expression syntax and fix common errors. |
| `/n8n-node-configuration` | [`n8n-node-configuration`](skills/backend-and-fullstack/n8n-node-configuration/SKILL.md) | Operation-aware node configuration guidance. |
| `/neon-postgres` | [`neon-postgres`](skills/backend-and-fullstack/neon-postgres/SKILL.md) | Expert patterns for Neon serverless Postgres, branching, connection. |
| `/nestjs-expert` | [`nestjs-expert`](skills/backend-and-fullstack/nestjs-expert/SKILL.md) | You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency. |
| `/networkx` | [`networkx`](skills/backend-and-fullstack/networkx/SKILL.md) | NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. |
| `/new-rails-project` | [`new-rails-project`](skills/backend-and-fullstack/new-rails-project/SKILL.md) | Create a new Rails project. |
| `/next-intl-add-language` | [`next-intl-add-language`](skills/backend-and-fullstack/next-intl-add-language/SKILL.md) | Add new language to a Next.js + next-intl application. |
| `/nft-standards` | [`nft-standards`](skills/backend-and-fullstack/nft-standards/SKILL.md) | Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features. |
| `/no-eval-skill` | [`no-eval-skill`](skills/backend-and-fullstack/no-eval-skill/SKILL.md) | A skill with no eval.yaml for testing discovery behavior. |
| `/nodejs-backend-patterns` | [`nodejs-backend-patterns`](skills/backend-and-fullstack/nodejs-backend-patterns/SKILL.md) | Comprehensive guidance for building scalable, maintainable. |
| `/nodejs-best-practices` | [`nodejs-best-practices`](skills/backend-and-fullstack/nodejs-best-practices/SKILL.md) | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. |
| `/nosql-expert` | [`nosql-expert`](skills/backend-and-fullstack/nosql-expert/SKILL.md) | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). |
| `/nuget-manager` | [`nuget-manager`](skills/backend-and-fullstack/nuget-manager/SKILL.md) | Manage NuGet packages in .NET projects/solutions. |
| `/nuget-trusted-publishing` | [`nuget-trusted-publishing`](skills/backend-and-fullstack/nuget-trusted-publishing/SKILL.md) | Set up NuGet trusted publishing (OIDC) on a GitHub Actions repo — replaces long-lived API keys with short-lived tokens. |
| `/nutrition-analyzer` | [`nutrition-analyzer`](skills/backend-and-fullstack/nutrition-analyzer/SKILL.md) | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。. |
| `/objection-preemptor` | [`objection-preemptor`](skills/backend-and-fullstack/objection-preemptor/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/observability-monitoring-monitor-setup` | [`observability-monitoring-monitor-setup`](skills/backend-and-fullstack/observability-monitoring-monitor-setup/SKILL.md) | You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. |
| `/obsidian-bases` | [`obsidian-bases`](skills/backend-and-fullstack/obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. |
| `/obsidian-markdown` | [`obsidian-markdown`](skills/backend-and-fullstack/obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. |
| `/occupational-health-analyzer` | [`occupational-health-analyzer`](skills/backend-and-fullstack/occupational-health-analyzer/SKILL.md) | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。. |
| `/odoo-backup-strategy` | [`odoo-backup-strategy`](skills/backend-and-fullstack/odoo-backup-strategy/SKILL.md) | Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload. |
| `/odoo-docker-deployment` | [`odoo-docker-deployment`](skills/backend-and-fullstack/odoo-docker-deployment/SKILL.md) | Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based. |
| `/odoo-orm-expert` | [`odoo-orm-expert`](skills/backend-and-fullstack/odoo-orm-expert/SKILL.md) | Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques. |
| `/odoo-performance-tuner` | [`odoo-performance-tuner`](skills/backend-and-fullstack/odoo-performance-tuner/SKILL.md) | Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits,. |
| `/odoo-upgrade-advisor` | [`odoo-upgrade-advisor`](skills/backend-and-fullstack/odoo-upgrade-advisor/SKILL.md) | Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module. |
| `/onboarding-psychologist` | [`onboarding-psychologist`](skills/backend-and-fullstack/onboarding-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/openclaw-github-repo-commander` | [`openclaw-github-repo-commander`](skills/backend-and-fullstack/openclaw-github-repo-commander/SKILL.md) | 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis. |
| `/optimizing-ef-core-queries` | [`optimizing-ef-core-queries`](skills/backend-and-fullstack/optimizing-ef-core-queries/SKILL.md) | Optimize Entity Framework Core queries by fixing N+1 problems, choosing correct tracking modes, using compiled queries. |
| `/options-flow-analyzer` | [`options-flow-analyzer`](skills/backend-and-fullstack/options-flow-analyzer/SKILL.md) | Real vs lottery call separation for options P/C ratio analysis — prevents signal inversion from deep OTM noise. |
| `/oral-health-analyzer` | [`oral-health-analyzer`](skills/backend-and-fullstack/oral-health-analyzer/SKILL.md) | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。. |
| `/orchestrate-batch-refactor` | [`orchestrate-batch-refactor`](skills/backend-and-fullstack/orchestrate-batch-refactor/SKILL.md) | Plan and execute large refactors with dependency-aware work packets and parallel analysis. |
| `/os-scripting` | [`os-scripting`](skills/backend-and-fullstack/os-scripting/SKILL.md) | Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. |
| `/oss-hunter` | [`oss-hunter`](skills/backend-and-fullstack/oss-hunter/SKILL.md) | Automatically hunt for high-impact OSS contribution opportunities in trending repositories. |
| `/performance` | [`performance`](skills/backend-and-fullstack/performance/SKILL.md) | Optimize web performance for faster loading and better user experience. |
| `/performance-engineer` | [`performance-engineer`](skills/backend-and-fullstack/performance-engineer/SKILL.md) | Expert performance engineer specializing in modern observability,. |
| `/performance-profiling` | [`performance-profiling`](skills/backend-and-fullstack/performance-profiling/SKILL.md) | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| `/performance-testing-review-ai-review` | [`performance-testing-review-ai-review`](skills/backend-and-fullstack/performance-testing-review-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition. |
| `/phase-gated-debugging` | [`phase-gated-debugging`](skills/backend-and-fullstack/phase-gated-debugging/SKILL.md) | Use when debugging any bug. Enforces a 5-phase protocol where code edits are blocked until root cause is confirmed. |
| `/php-mcp-server-generator` | [`php-mcp-server-generator`](skills/backend-and-fullstack/php-mcp-server-generator/SKILL.md) | Generate a complete PHP Model Context Protocol server project with tools, resources, prompts, and tests using the official PHP SDK. |
| `/php-pro` | [`php-pro`](skills/backend-and-fullstack/php-pro/SKILL.md) | Write idiomatic PHP code with generators, iterators, SPL data. |
| `/plan-writing` | [`plan-writing`](skills/backend-and-fullstack/plan-writing/SKILL.md) | Structured task planning with clear breakdowns, dependencies, and verification criteria. |
| `/planning-oracle-to-postgres-migration-integration-testing` | [`planning-oracle-to-postgres-migration-integration-testing`](skills/backend-and-fullstack/planning-oracle-to-postgres-migration-integration-testing/SKILL.md) | Creates an integration testing plan for .NET data access artifacts during Oracle-to-PostgreSQL database migrations. |
| `/planning-with-files` | [`planning-with-files`](skills/backend-and-fullstack/planning-with-files/SKILL.md) | Work like Manus: Use persistent markdown files as your \"working memory on disk.\". |
| `/platform-detection` | [`platform-detection`](skills/backend-and-fullstack/platform-detection/SKILL.md) | Reference data for detecting the test platform (VSTest vs Microsoft.Testing.Platform) and test framework (MSTest,. |
| `/playwright-java` | [`playwright-java`](skills/backend-and-fullstack/playwright-java/SKILL.md) | Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5,. |
| `/playwright-skill` | [`playwright-skill`](skills/backend-and-fullstack/playwright-skill/SKILL.md) | IMPORTANT - Path Resolution: This skill can be installed in different locations (plugin system, manual installation,. |
| `/polars` | [`polars`](skills/backend-and-fullstack/polars/SKILL.md) | Fast in-memory DataFrame library for datasets that fit in RAM. |
| `/posix-shell-pro` | [`posix-shell-pro`](skills/backend-and-fullstack/posix-shell-pro/SKILL.md) | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. |
| `/postgres-best-practices` | [`postgres-best-practices`](skills/backend-and-fullstack/postgres-best-practices/SKILL.md) | Postgres performance optimization and best practices from Supabase. |
| `/postgresql` | [`postgresql`](skills/backend-and-fullstack/postgresql/SKILL.md) | Design a PostgreSQL-specific schema. |
| `/postgresql-code-review` | [`postgresql-code-review`](skills/backend-and-fullstack/postgresql-code-review/SKILL.md) | PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. |
| `/postgresql-optimization` | [`postgresql-optimization`](skills/backend-and-fullstack/postgresql-optimization/SKILL.md) | PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types. |
| `/powershell-windows` | [`powershell-windows`](skills/backend-and-fullstack/powershell-windows/SKILL.md) | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| `/pr-dashboard` | [`pr-dashboard`](skills/backend-and-fullstack/pr-dashboard/SKILL.md) | Open a GitHub PR dashboard in the browser. |
| `/pr-review` | [`pr-review`](skills/backend-and-fullstack/pr-review/SKILL.md) | Review pull requests for the MiniMax Skills repository. |
| `/pr-writer` | [`pr-writer`](skills/backend-and-fullstack/pr-writer/SKILL.md) | Create pull requests following Sentry's engineering practices. |
| `/price-psychology-strategist` | [`price-psychology-strategist`](skills/backend-and-fullstack/price-psychology-strategist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/prisma-expert` | [`prisma-expert`](skills/backend-and-fullstack/prisma-expert/SKILL.md) | You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling. |
| `/product-manager-toolkit` | [`product-manager-toolkit`](skills/backend-and-fullstack/product-manager-toolkit/SKILL.md) | Essential tools and frameworks for modern product management, from discovery to delivery. |
| `/production-code-audit` | [`production-code-audit`](skills/backend-and-fullstack/production-code-audit/SKILL.md) | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically. |
| `/production-scheduling` | [`production-scheduling`](skills/backend-and-fullstack/production-scheduling/SKILL.md) | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation. |
| `/project-skill-audit` | [`project-skill-audit`](skills/backend-and-fullstack/project-skill-audit/SKILL.md) | Audit a project and recommend the highest-value skills to add or update. |
| `/pubmed-database` | [`pubmed-database`](skills/backend-and-fullstack/pubmed-database/SKILL.md) | Direct REST API access to PubMed. |
| `/pydantic-models-py` | [`pydantic-models-py`](skills/backend-and-fullstack/pydantic-models-py/SKILL.md) | Create Pydantic models following the multi-model pattern with Base, Create, Update, Response, and InDB variants. |
| `/pytest-coverage` | [`pytest-coverage`](skills/backend-and-fullstack/pytest-coverage/SKILL.md) | Run pytest tests with coverage, discover lines missing coverage, and increase coverage to 100%. |
| `/python-development-python-scaffold` | [`python-development-python-scaffold`](skills/backend-and-fullstack/python-development-python-scaffold/SKILL.md) | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. |
| `/python-fastapi-development` | [`python-fastapi-development`](skills/backend-and-fullstack/python-fastapi-development/SKILL.md) | Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns. |
| `/python-mcp-server-generator` | [`python-mcp-server-generator`](skills/backend-and-fullstack/python-mcp-server-generator/SKILL.md) | Generate a complete MCP server project in Python with tools, resources, and proper configuration. |
| `/python-packaging` | [`python-packaging`](skills/backend-and-fullstack/python-packaging/SKILL.md) | Comprehensive guide to creating, structuring. |
| `/python-patterns` | [`python-patterns`](skills/backend-and-fullstack/python-patterns/SKILL.md) | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. |
| `/python-performance-optimization` | [`python-performance-optimization`](skills/backend-and-fullstack/python-performance-optimization/SKILL.md) | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. |
| `/python-pro` | [`python-pro`](skills/backend-and-fullstack/python-pro/SKILL.md) | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. |
| `/python-pypi-package-builder` | [`python-pypi-package-builder`](skills/backend-and-fullstack/python-pypi-package-builder/SKILL.md) | End-to-end skill for building, testing, linting, versioning, and publishing a production-grade Python library to PyPI. |
| `/python-testing-patterns` | [`python-testing-patterns`](skills/backend-and-fullstack/python-testing-patterns/SKILL.md) | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. |
| `/qdrant-memory-usage-optimization` | [`qdrant-memory-usage-optimization`](skills/backend-and-fullstack/qdrant-memory-usage-optimization/SKILL.md) | Diagnoses and reduces Qdrant memory usage. |
| `/qdrant-monitoring-debugging` | [`qdrant-monitoring-debugging`](skills/backend-and-fullstack/qdrant-monitoring-debugging/SKILL.md) | Diagnoses Qdrant production issues using metrics and observability tools. |
| `/qdrant-search-quality` | [`qdrant-search-quality`](skills/backend-and-fullstack/qdrant-search-quality/SKILL.md) | Diagnoses and improves Qdrant search relevance. |
| `/qdrant-search-quality-diagnosis` | [`qdrant-search-quality-diagnosis`](skills/backend-and-fullstack/qdrant-search-quality-diagnosis/SKILL.md) | Diagnoses Qdrant search quality issues. |
| `/qdrant-search-speed-optimization` | [`qdrant-search-speed-optimization`](skills/backend-and-fullstack/qdrant-search-speed-optimization/SKILL.md) | Diagnoses and fixes slow Qdrant search. |
| `/quality-nonconformance` | [`quality-nonconformance`](skills/backend-and-fullstack/quality-nonconformance/SKILL.md) | Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action. |
| `/rag-implementation` | [`rag-implementation`](skills/backend-and-fullstack/rag-implementation/SKILL.md) | RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup,. |
| `/red-team-tactics` | [`red-team-tactics`](skills/backend-and-fullstack/red-team-tactics/SKILL.md) | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| `/rehabilitation-analyzer` | [`rehabilitation-analyzer`](skills/backend-and-fullstack/rehabilitation-analyzer/SKILL.md) | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议. |
| `/remember` | [`remember`](skills/backend-and-fullstack/remember/SKILL.md) | Transforms lessons learned into domain-organized memory instructions (global or workspace). |
| `/reverse-engineer` | [`reverse-engineer`](skills/backend-and-fullstack/reverse-engineer/SKILL.md) | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. |
| `/review-and-refactor` | [`review-and-refactor`](skills/backend-and-fullstack/review-and-refactor/SKILL.md) | Review and refactor code in your project according to defined instructions. |
| `/reviewing-oracle-to-postgres-migration` | [`reviewing-oracle-to-postgres-migration`](skills/backend-and-fullstack/reviewing-oracle-to-postgres-migration/SKILL.md) | Identifies Oracle-to-PostgreSQL migration risks by cross-referencing code against known behavioral differences (empty. |
| `/risk-manager` | [`risk-manager`](skills/backend-and-fullstack/risk-manager/SKILL.md) | Monitor portfolio risk, R-multiples, and position limits. |
| `/robius-event-action` | [`robius-event-action`](skills/backend-and-fullstack/robius-event-action/SKILL.md) | CRITICAL: Use for Robius event and action patterns. |
| `/ruby-pro` | [`ruby-pro`](skills/backend-and-fullstack/ruby-pro/SKILL.md) | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. |
| `/ruff-recursive-fix` | [`ruff-recursive-fix`](skills/backend-and-fullstack/ruff-recursive-fix/SKILL.md) | Run Ruff checks with optional scope and rule overrides, apply safe and unsafe autofixes iteratively, review each change. |
| `/run-tests` | [`run-tests`](skills/backend-and-fullstack/run-tests/SKILL.md) | Runs .NET tests with `dotnet test` and chooses the correct platform/SDK/framework syntax. |
| `/rust-async-patterns` | [`rust-async-patterns`](skills/backend-and-fullstack/rust-async-patterns/SKILL.md) | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. |
| `/rust-mcp-server-generator` | [`rust-mcp-server-generator`](skills/backend-and-fullstack/rust-mcp-server-generator/SKILL.md) | Generate a complete Rust Model Context Protocol server project with tools, prompts, resources. |
| `/rust-pro` | [`rust-pro`](skills/backend-and-fullstack/rust-pro/SKILL.md) | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |
| `/saas-multi-tenant` | [`saas-multi-tenant`](skills/backend-and-fullstack/saas-multi-tenant/SKILL.md) | Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema. |
| `/saga-orchestration` | [`saga-orchestration`](skills/backend-and-fullstack/saga-orchestration/SKILL.md) | Patterns for managing distributed transactions and long-running business processes. |
| `/sample-skill` | [`sample-skill`](skills/backend-and-fullstack/sample-skill/SKILL.md) | A sample skill for testing the validator. Helps with greeting generation. |
| `/sast-configuration` | [`sast-configuration`](skills/backend-and-fullstack/sast-configuration/SKILL.md) | Static Application Security Testing (SAST) tool setup, configuration. |
| `/scaffolding-oracle-to-postgres-migration-test-project` | [`scaffolding-oracle-to-postgres-migration-test-project`](skills/backend-and-fullstack/scaffolding-oracle-to-postgres-migration-test-project/SKILL.md) | Scaffolds an xUnit integration test project for validating Oracle-to-PostgreSQL database migration behavior in .NET solutions. |
| `/scarcity-urgency-psychologist` | [`scarcity-urgency-psychologist`](skills/backend-and-fullstack/scarcity-urgency-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/scikit-learn` | [`scikit-learn`](skills/backend-and-fullstack/scikit-learn/SKILL.md) | Machine learning in Python with scikit-learn. |
| `/screen-reader-testing` | [`screen-reader-testing`](skills/backend-and-fullstack/screen-reader-testing/SKILL.md) | Practical guide to testing web applications with screen readers for comprehensive accessibility validation. |
| `/search-specialist` | [`search-specialist`](skills/backend-and-fullstack/search-specialist/SKILL.md) | Expert web researcher using advanced search techniques and. |
| `/segment-cdp` | [`segment-cdp`](skills/backend-and-fullstack/segment-cdp/SKILL.md) | Expert patterns for Segment Customer Data Platform including. |
| `/semgrep-rule-variant-creator` | [`semgrep-rule-variant-creator`](skills/backend-and-fullstack/semgrep-rule-variant-creator/SKILL.md) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. |
| `/senior-architect` | [`senior-architect`](skills/backend-and-fullstack/senior-architect/SKILL.md) | Complete toolkit for senior architect with modern tools and best practices. |
| `/senior-fullstack` | [`senior-fullstack`](skills/backend-and-fullstack/senior-fullstack/SKILL.md) | Complete toolkit for senior fullstack with modern tools and best practices. |
| `/server-management` | [`server-management`](skills/backend-and-fullstack/server-management/SKILL.md) | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. |
| `/sexual-health-analyzer` | [`sexual-health-analyzer`](skills/backend-and-fullstack/sexual-health-analyzer/SKILL.md) | Sexual Health Analyzer. |
| `/sharp-edges` | [`sharp-edges`](skills/backend-and-fullstack/sharp-edges/SKILL.md) | sharp-edges. |
| `/shellcheck-configuration` | [`shellcheck-configuration`](skills/backend-and-fullstack/shellcheck-configuration/SKILL.md) | Master ShellCheck static analysis configuration and usage for shell script quality. |
| `/shodan-reconnaissance` | [`shodan-reconnaissance`](skills/backend-and-fullstack/shodan-reconnaissance/SKILL.md) | Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements. |
| `/shuffle-json-data` | [`shuffle-json-data`](skills/backend-and-fullstack/shuffle-json-data/SKILL.md) | Shuffle repetitive JSON objects safely by validating schema consistency before randomising entries. |
| `/simplify-code` | [`simplify-code`](skills/backend-and-fullstack/simplify-code/SKILL.md) | Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes. |
| `/skill-installer` | [`skill-installer`](skills/backend-and-fullstack/skill-installer/SKILL.md) | Instala, valida, registra e verifica novas skills no ecossistema. |
| `/skill-rails-upgrade` | [`skill-rails-upgrade`](skills/backend-and-fullstack/skill-rails-upgrade/SKILL.md) | Analyze Rails apps and provide upgrade assessments. |
| `/sleep-analyzer` | [`sleep-analyzer`](skills/backend-and-fullstack/sleep-analyzer/SKILL.md) | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。. |
| `/slo-implementation` | [`slo-implementation`](skills/backend-and-fullstack/slo-implementation/SKILL.md) | Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets. |
| `/snowflake-development` | [`snowflake-development`](skills/backend-and-fullstack/snowflake-development/SKILL.md) | Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables,. |
| `/social-proof-architect` | [`social-proof-architect`](skills/backend-and-fullstack/social-proof-architect/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/speckit-updater` | [`speckit-updater`](skills/backend-and-fullstack/speckit-updater/SKILL.md) | SpecKit Safe Update. |
| `/speed` | [`speed`](skills/backend-and-fullstack/speed/SKILL.md) | Launch RSVP speed reader for text. |
| `/sponsor-finder` | [`sponsor-finder`](skills/backend-and-fullstack/sponsor-finder/SKILL.md) | Find which of a GitHub repository's dependencies are sponsorable via GitHub Sponsors. |
| `/spring-boot-testing` | [`spring-boot-testing`](skills/backend-and-fullstack/spring-boot-testing/SKILL.md) | Expert Spring Boot 4 testing specialist that selects the best Spring Boot testing techniques for your situation with. |
| `/sql-code-review` | [`sql-code-review`](skills/backend-and-fullstack/sql-code-review/SKILL.md) | Universal SQL code review assistant that performs comprehensive security, maintainability. |
| `/sql-injection-testing` | [`sql-injection-testing`](skills/backend-and-fullstack/sql-injection-testing/SKILL.md) | Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws,. |
| `/sql-optimization` | [`sql-optimization`](skills/backend-and-fullstack/sql-optimization/SKILL.md) | Universal SQL performance optimization assistant for comprehensive query tuning, indexing strategies. |
| `/sql-optimization-patterns` | [`sql-optimization-patterns`](skills/backend-and-fullstack/sql-optimization-patterns/SKILL.md) | Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing. |
| `/sql-pro` | [`sql-pro`](skills/backend-and-fullstack/sql-pro/SKILL.md) | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. |
| `/sql-server-table-reconciliation` | [`sql-server-table-reconciliation`](skills/backend-and-fullstack/sql-server-table-reconciliation/SKILL.md) | Use when: comparing SQL Server tables across instances, data migration validation, ETL verification, row mismatch. |
| `/sqlmap-database-pentesting` | [`sqlmap-database-pentesting`](skills/backend-and-fullstack/sqlmap-database-pentesting/SKILL.md) | Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap. |
| `/ssh-penetration-testing` | [`ssh-penetration-testing`](skills/backend-and-fullstack/ssh-penetration-testing/SKILL.md) | Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation,. |
| `/ssma-console` | [`ssma-console`](skills/backend-and-fullstack/ssma-console/SKILL.md) | Use when: SSMA console operations — create project, generate assessment report, convert schema, migrate data, Oracle to. |
| `/statsmodels` | [`statsmodels`](skills/backend-and-fullstack/statsmodels/SKILL.md) | Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference. |
| `/subject-line-psychologist` | [`subject-line-psychologist`](skills/backend-and-fullstack/subject-line-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/suggest-awesome-github-copilot-instructions` | [`suggest-awesome-github-copilot-instructions`](skills/backend-and-fullstack/suggest-awesome-github-copilot-instructions/SKILL.md) | Suggest relevant GitHub Copilot instruction files from the awesome-copilot repository based on current repository. |
| `/suggest-awesome-github-copilot-skills` | [`suggest-awesome-github-copilot-skills`](skills/backend-and-fullstack/suggest-awesome-github-copilot-skills/SKILL.md) | Suggest relevant GitHub Copilot skills from the awesome-copilot repository based on current repository context and chat. |
| `/swift-concurrency-expert` | [`swift-concurrency-expert`](skills/backend-and-fullstack/swift-concurrency-expert/SKILL.md) | Review and fix Swift concurrency issues such as actor isolation and Sendable violations. |
| `/sympy` | [`sympy`](skills/backend-and-fullstack/sympy/SKILL.md) | SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather. |
| `/system-text-json-net11` | [`system-text-json-net11`](skills/backend-and-fullstack/system-text-json-net11/SKILL.md) | Provides guidance on new System.Text.Json APIs introduced in .NET 11. |
| `/systematic-debugging` | [`systematic-debugging`](skills/backend-and-fullstack/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. |
| `/systems-programming-rust-project` | [`systems-programming-rust-project`](skills/backend-and-fullstack/systems-programming-rust-project/SKILL.md) | You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. |
| `/tcm-constitution-analyzer` | [`tcm-constitution-analyzer`](skills/backend-and-fullstack/tcm-constitution-analyzer/SKILL.md) | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。. |
| `/tdd-workflow` | [`tdd-workflow`](skills/backend-and-fullstack/tdd-workflow/SKILL.md) | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| `/tdd-workflows-tdd-cycle` | [`tdd-workflows-tdd-cycle`](skills/backend-and-fullstack/tdd-workflows-tdd-cycle/SKILL.md) | Use when working with tdd workflows tdd cycle. |
| `/tdd-workflows-tdd-green` | [`tdd-workflows-tdd-green`](skills/backend-and-fullstack/tdd-workflows-tdd-green/SKILL.md) | Implement the minimal code needed to make failing tests pass in the TDD green phase. |
| `/tdd-workflows-tdd-refactor` | [`tdd-workflows-tdd-refactor`](skills/backend-and-fullstack/tdd-workflows-tdd-refactor/SKILL.md) | Use when working with tdd workflows tdd refactor. |
| `/team-collaboration-issue` | [`team-collaboration-issue`](skills/backend-and-fullstack/team-collaboration-issue/SKILL.md) | You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation. |
| `/template-discovery` | [`template-discovery`](skills/backend-and-fullstack/template-discovery/SKILL.md) | Helps find, inspect, and compare .NET project templates. |
| `/template-instantiation` | [`template-instantiation`](skills/backend-and-fullstack/template-instantiation/SKILL.md) | Creates .NET projects from templates with validated parameters, smart defaults, Central Package Management adaptation. |
| `/template-validation` | [`template-validation`](skills/backend-and-fullstack/template-validation/SKILL.md) | Validates custom dotnet new templates for correctness before publishing. |
| `/temporal-python-pro` | [`temporal-python-pro`](skills/backend-and-fullstack/temporal-python-pro/SKILL.md) | Master Temporal workflow orchestration with Python SDK. |
| `/temporal-python-testing` | [`temporal-python-testing`](skills/backend-and-fullstack/temporal-python-testing/SKILL.md) | Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific. |
| `/test-anti-patterns` | [`test-anti-patterns`](skills/backend-and-fullstack/test-anti-patterns/SKILL.md) | Audits existing .NET test code (MSTest, xUnit, NUnit, TUnit) for anti-patterns and quality issues that undermine. |
| `/test-driven-development` | [`test-driven-development`](skills/backend-and-fullstack/test-driven-development/SKILL.md) | Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. |
| `/test-smell-detection` | [`test-smell-detection`](skills/backend-and-fullstack/test-smell-detection/SKILL.md) | Deep-dive audit using the full testsmells.org 19-smell academic catalog for .NET tests. |
| `/testing-patterns` | [`testing-patterns`](skills/backend-and-fullstack/testing-patterns/SKILL.md) | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. |
| `/testing-qa` | [`testing-qa`](skills/backend-and-fullstack/testing-qa/SKILL.md) | Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation. |
| `/thread-abort-migration` | [`thread-abort-migration`](skills/backend-and-fullstack/thread-abort-migration/SKILL.md) | Guides migration of .NET Framework Thread.Abort usage to cooperative cancellation in modern .NET. |
| `/threejs-fundamentals` | [`threejs-fundamentals`](skills/backend-and-fullstack/threejs-fundamentals/SKILL.md) | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. |
| `/threejs-interaction` | [`threejs-interaction`](skills/backend-and-fullstack/threejs-interaction/SKILL.md) | Three.js interaction - raycasting, controls, mouse/touch input, object selection. |
| `/threejs-lighting` | [`threejs-lighting`](skills/backend-and-fullstack/threejs-lighting/SKILL.md) | Three.js lighting - light types, shadows, environment lighting. |
| `/threejs-loaders` | [`threejs-loaders`](skills/backend-and-fullstack/threejs-loaders/SKILL.md) | Three.js asset loading - GLTF, textures, images, models, async patterns. |
| `/threejs-textures` | [`threejs-textures`](skills/backend-and-fullstack/threejs-textures/SKILL.md) | Three.js textures - texture types, UV mapping, environment maps, texture settings. |
| `/tool-use-guardian` | [`tool-use-guardian`](skills/backend-and-fullstack/tool-use-guardian/SKILL.md) | FREE — Intelligent tool-call reliability wrapper. Monitors, retries, fixes, and learns from tool failures. |
| `/track-management` | [`track-management`](skills/backend-and-fullstack/track-management/SKILL.md) | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs,. |
| `/travel-health-analyzer` | [`travel-health-analyzer`](skills/backend-and-fullstack/travel-health-analyzer/SKILL.md) | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。. |
| `/trigger-dev` | [`trigger-dev`](skills/backend-and-fullstack/trigger-dev/SKILL.md) | Trigger.dev expert for background jobs, AI workflows, and reliable. |
| `/trpc-fullstack` | [`trpc-fullstack`](skills/backend-and-fullstack/trpc-fullstack/SKILL.md) | Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions. |
| `/trust-calibrator` | [`trust-calibrator`](skills/backend-and-fullstack/trust-calibrator/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/tutorial-engineer` | [`tutorial-engineer`](skills/backend-and-fullstack/tutorial-engineer/SKILL.md) | Creates step-by-step tutorials and educational content from code. |
| `/twitter-algorithm-optimizer` | [`twitter-algorithm-optimizer`](skills/backend-and-fullstack/twitter-algorithm-optimizer/SKILL.md) | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. |
| `/uncle-bob-craft` | [`uncle-bob-craft`](skills/backend-and-fullstack/uncle-bob-craft/SKILL.md) | Use when performing code review, writing or refactoring code. |
| `/uniprot-database` | [`uniprot-database`](skills/backend-and-fullstack/uniprot-database/SKILL.md) | Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. |
| `/update-markdown-file-index` | [`update-markdown-file-index`](skills/backend-and-fullstack/update-markdown-file-index/SKILL.md) | Update a markdown file section with an index/table of files from a specified folder. |
| `/upgrading-expo` | [`upgrading-expo`](skills/backend-and-fullstack/upgrading-expo/SKILL.md) | Upgrade Expo SDK versions. |
| `/upstash-qstash` | [`upstash-qstash`](skills/backend-and-fullstack/upstash-qstash/SKILL.md) | Upstash QStash expert for serverless message queues, scheduled. |
| `/use-js-interop` | [`use-js-interop`](skills/backend-and-fullstack/use-js-interop/SKILL.md) | Add, review, or fix JavaScript interop in Blazor components. |
| `/using-git-worktrees` | [`using-git-worktrees`](skills/backend-and-fullstack/using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans -. |
| `/using-neon` | [`using-neon`](skills/backend-and-fullstack/using-neon/SKILL.md) | Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant. |
| `/uv-package-manager` | [`uv-package-manager`](skills/backend-and-fullstack/uv-package-manager/SKILL.md) | Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern. |
| `/vardoger-analyze` | [`vardoger-analyze`](skills/backend-and-fullstack/vardoger-analyze/SKILL.md) | Use when the user asks to personalize the GitHub Copilot CLI assistant, adapt Copilot to their style, use vardoger. |
| `/vector-database-engineer` | [`vector-database-engineer`](skills/backend-and-fullstack/vector-database-engineer/SKILL.md) | Expert in vector databases, embedding strategies, and semantic search implementation. |
| `/vector-index-tuning` | [`vector-index-tuning`](skills/backend-and-fullstack/vector-index-tuning/SKILL.md) | Optimize vector index performance for latency, recall, and memory. |
| `/vercel-composition-patterns` | [`vercel-composition-patterns`](skills/backend-and-fullstack/vercel-composition-patterns/SKILL.md) | React composition patterns that scale. |
| `/vexor-cli` | [`vexor-cli`](skills/backend-and-fullstack/vexor-cli/SKILL.md) | Semantic file discovery via `vexor`. |
| `/vibers-code-review` | [`vibers-code-review`](skills/backend-and-fullstack/vibers-code-review/SKILL.md) | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review. |
| `/viboscope` | [`viboscope`](skills/backend-and-fullstack/viboscope/SKILL.md) | Psychological compatibility matching — find cofounders, collaborators, and friends through validated psychometrics. |
| `/vision-analysis` | [`vision-analysis`](skills/backend-and-fullstack/vision-analysis/SKILL.md) | Analyze, describe, and extract information from images using the MiniMax vision MCP tool. |
| `/web3-testing` | [`web3-testing`](skills/backend-and-fullstack/web3-testing/SKILL.md) | Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns. |
| `/webapp-testing` | [`webapp-testing`](skills/backend-and-fullstack/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. |
| `/weightloss-analyzer` | [`weightloss-analyzer`](skills/backend-and-fullstack/weightloss-analyzer/SKILL.md) | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段. |
| `/wellally-tech` | [`wellally-tech`](skills/backend-and-fullstack/wellally-tech/SKILL.md) | Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base,. |
| `/what-context-needed` | [`what-context-needed`](skills/backend-and-fullstack/what-context-needed/SKILL.md) | Ask Copilot what files it needs to see before answering a question. |
| `/wiki-changelog` | [`wiki-changelog`](skills/backend-and-fullstack/wiki-changelog/SKILL.md) | Analyzes git commit history and generates structured changelogs categorized by change type. |
| `/windows-privilege-escalation` | [`windows-privilege-escalation`](skills/backend-and-fullstack/windows-privilege-escalation/SKILL.md) | Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems. |
| `/windows-shell-reliability` | [`windows-shell-reliability`](skills/backend-and-fullstack/windows-shell-reliability/SKILL.md) | Reliable command execution on Windows: paths, encoding, and common binary pitfalls. |
| `/wordpress` | [`wordpress`](skills/backend-and-fullstack/wordpress/SKILL.md) | Complete WordPress development workflow covering theme development, plugin creation, WooCommerce integration,. |
| `/wordpress-block-theming` | [`wordpress-block-theming`](skills/backend-and-fullstack/wordpress-block-theming/SKILL.md) | WordPress Full Site Editing (FSE) theme architecture. |
| `/wordpress-penetration-testing` | [`wordpress-penetration-testing`](skills/backend-and-fullstack/wordpress-penetration-testing/SKILL.md) | Assess WordPress installations for common vulnerabilities and WordPress 7.0 attack surfaces. |
| `/wordpress-plugin-development` | [`wordpress-plugin-development`](skills/backend-and-fullstack/wordpress-plugin-development/SKILL.md) | WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best. |
| `/wordpress-router` | [`wordpress-router`](skills/backend-and-fullstack/wordpress-router/SKILL.md) | Use when the user asks about WordPress codebases (plugins, themes, block themes, Gutenberg blocks, WP core checkouts). |
| `/workflow-patterns` | [`workflow-patterns`](skills/backend-and-fullstack/workflow-patterns/SKILL.md) | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git. |
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
| `/x402-express-wrapper` | [`x402-express-wrapper`](skills/backend-and-fullstack/x402-express-wrapper/SKILL.md) | Wrapper oficial de M2MCent (Node.js) para inyectar muros de pago x402 en APIs o servidores Model Context Protocol (MCP). |
| `/yann-lecun-filosofia` | [`yann-lecun-filosofia`](skills/backend-and-fullstack/yann-lecun-filosofia/SKILL.md) | Sub-skill filosófica e pedagógica de Yann LeCun. |
| `/yann-lecun-tecnico` | [`yann-lecun-tecnico`](skills/backend-and-fullstack/yann-lecun-tecnico/SKILL.md) | Sub-skill técnica de Yann LeCun. |

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
| `/analytics-product` | [`analytics-product`](skills/marketing-and-seo/analytics-product/SKILL.md) | Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto. |
| `/analytics-tracking` | [`analytics-tracking`](skills/marketing-and-seo/analytics-tracking/SKILL.md) | When the user wants to set up, improve, or audit analytics tracking and measurement. |
| `/apify-audience-analysis` | [`apify-audience-analysis`](skills/marketing-and-seo/apify-audience-analysis/SKILL.md) | Understand audience demographics, preferences, behavior patterns. |
| `/apify-competitor-intelligence` | [`apify-competitor-intelligence`](skills/marketing-and-seo/apify-competitor-intelligence/SKILL.md) | Analyze competitor strategies, content, pricing, ads. |
| `/apify-content-analytics` | [`apify-content-analytics`](skills/marketing-and-seo/apify-content-analytics/SKILL.md) | Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok. |
| `/arm-cortex-expert` | [`arm-cortex-expert`](skills/marketing-and-seo/arm-cortex-expert/SKILL.md) | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers. |
| `/aso-audit` | [`aso-audit`](skills/marketing-and-seo/aso-audit/SKILL.md) | When the user wants to audit or optimize an App Store or Google Play listing. |
| `/azure-ai-textanalytics-py` | [`azure-ai-textanalytics-py`](skills/marketing-and-seo/azure-ai-textanalytics-py/SKILL.md) | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. |
| `/churn-prevention` | [`churn-prevention`](skills/marketing-and-seo/churn-prevention/SKILL.md) | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments. |
| `/closed-loop-delivery` | [`closed-loop-delivery`](skills/marketing-and-seo/closed-loop-delivery/SKILL.md) | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across. |
| `/co-marketing` | [`co-marketing`](skills/marketing-and-seo/co-marketing/SKILL.md) | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. |
| `/cold-email` | [`cold-email`](skills/marketing-and-seo/cold-email/SKILL.md) | Write B2B cold emails and follow-up sequences that get replies. |
| `/community-marketing` | [`community-marketing`](skills/marketing-and-seo/community-marketing/SKILL.md) | Build and leverage online communities to drive product growth and brand loyalty. |
| `/competitor-alternatives` | [`competitor-alternatives`](skills/marketing-and-seo/competitor-alternatives/SKILL.md) | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. |
| `/competitor-profiling` | [`competitor-profiling`](skills/marketing-and-seo/competitor-profiling/SKILL.md) | When the user wants to research, profile, or analyze competitors from their URLs. |
| `/content-marketer` | [`content-marketer`](skills/marketing-and-seo/content-marketer/SKILL.md) | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO. |
| `/content-strategy` | [`content-strategy`](skills/marketing-and-seo/content-strategy/SKILL.md) | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. |
| `/copy-editing` | [`copy-editing`](skills/marketing-and-seo/copy-editing/SKILL.md) | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. |
| `/copywriting` | [`copywriting`](skills/marketing-and-seo/copywriting/SKILL.md) | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages,. |
| `/copywriting-psychologist` | [`copywriting-psychologist`](skills/marketing-and-seo/copywriting-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/customer-research` | [`customer-research`](skills/marketing-and-seo/customer-research/SKILL.md) | When the user wants to conduct, analyze, or synthesize customer research. |
| `/data-scientist` | [`data-scientist`](skills/marketing-and-seo/data-scientist/SKILL.md) | Expert data scientist for advanced analytics, machine learning, and statistical modeling. |
| `/distributed-tracing` | [`distributed-tracing`](skills/marketing-and-seo/distributed-tracing/SKILL.md) | Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices. |
| `/email-sequence` | [`email-sequence`](skills/marketing-and-seo/email-sequence/SKILL.md) | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. |
| `/error-detective` | [`error-detective`](skills/marketing-and-seo/error-detective/SKILL.md) | Search logs and codebases for error patterns, stack traces, and anomalies. |
| `/form-cro` | [`form-cro`](skills/marketing-and-seo/form-cro/SKILL.md) | When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms,. |
| `/free-tool-strategy` | [`free-tool-strategy`](skills/marketing-and-seo/free-tool-strategy/SKILL.md) | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or. |
| `/from-the-other-side-wiggins` | [`from-the-other-side-wiggins`](skills/marketing-and-seo/from-the-other-side-wiggins/SKILL.md) | Narrative and synthesis profile for Wiggins: framing, explanation, and audience-aware communication patterns for Ember sessions. |
| `/golang-pro` | [`golang-pro`](skills/marketing-and-seo/golang-pro/SKILL.md) | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| `/google-analytics-automation` | [`google-analytics-automation`](skills/marketing-and-seo/google-analytics-automation/SKILL.md) | Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. |
| `/growth-engine` | [`growth-engine`](skills/marketing-and-seo/growth-engine/SKILL.md) | Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral. |
| `/gsc` | [`gsc`](skills/marketing-and-seo/gsc/SKILL.md) | Query Google Search Console for SEO data - search queries, top pages, CTR opportunities, URL inspection, and sitemaps. |
| `/idea-darwin` | [`idea-darwin`](skills/marketing-and-seo/idea-darwin/SKILL.md) | Darwinian idea evolution engine — toss rough ideas onto an evolution island, let them compete, crossbreed. |
| `/ii-commons` | [`ii-commons`](skills/marketing-and-seo/ii-commons/SKILL.md) | Deterministic search across arXiv, PubMed/PMC, and US policy corpora with daily freshness cutoffs. |
| `/indexing-issue-auditor` | [`indexing-issue-auditor`](skills/marketing-and-seo/indexing-issue-auditor/SKILL.md) | High-level technical SEO and site architecture auditor. |
| `/keyword-extractor` | [`keyword-extractor`](skills/marketing-and-seo/keyword-extractor/SKILL.md) | Extracts up to 50 highly relevant SEO keywords from text. |
| `/kotler-macro-analyzer` | [`kotler-macro-analyzer`](skills/marketing-and-seo/kotler-macro-analyzer/SKILL.md) | Professional PESTEL/SWOT analysis agent based on Kotler's methodology for strategic market audits. |
| `/kql` | [`kql`](skills/marketing-and-seo/kql/SKILL.md) | KQL language expertise for writing correct, efficient Kusto Query Language queries. |
| `/launch-strategy` | [`launch-strategy`](skills/marketing-and-seo/launch-strategy/SKILL.md) | When the user wants to plan a product launch, feature announcement, or release strategy. |
| `/lead-magnets` | [`lead-magnets`](skills/marketing-and-seo/lead-magnets/SKILL.md) | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. |
| `/lead-research-assistant` | [`lead-research-assistant`](skills/marketing-and-seo/lead-research-assistant/SKILL.md) | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies. |
| `/lex` | [`lex`](skills/marketing-and-seo/lex/SKILL.md) | Centralized 'Truth Engine' for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding. |
| `/linkedin-cli` | [`linkedin-cli`](skills/marketing-and-seo/linkedin-cli/SKILL.md) | Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections,. |
| `/local-legal-seo-audit` | [`local-legal-seo-audit`](skills/marketing-and-seo/local-legal-seo-audit/SKILL.md) | Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local. |
| `/marketing-ideas` | [`marketing-ideas`](skills/marketing-and-seo/marketing-ideas/SKILL.md) | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. |
| `/marketing-psychology` | [`marketing-psychology`](skills/marketing-and-seo/marketing-psychology/SKILL.md) | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. |
| `/micro-saas-launcher` | [`micro-saas-launcher`](skills/marketing-and-seo/micro-saas-launcher/SKILL.md) | Expert in launching small, focused SaaS products fast - the indie. |
| `/microbenchmarking` | [`microbenchmarking`](skills/marketing-and-seo/microbenchmarking/SKILL.md) | Activate this skill when BenchmarkDotNet (BDN) is involved in the task — creating, running, configuring. |
| `/microservices-patterns` | [`microservices-patterns`](skills/marketing-and-seo/microservices-patterns/SKILL.md) | Master microservices architecture patterns including service boundaries, inter-service communication, data management. |
| `/microsoft-azure-webjobs-extensions-authentication-events-dotnet` | [`microsoft-azure-webjobs-extensions-authentication-events-dotnet`](skills/marketing-and-seo/microsoft-azure-webjobs-extensions-authentication-events-dotnet/SKILL.md) | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |
| `/microsoft-code-reference` | [`microsoft-code-reference`](skills/marketing-and-seo/microsoft-code-reference/SKILL.md) | Look up Microsoft API references, find working code samples, and verify SDK code is correct. |
| `/microsoft-docs` | [`microsoft-docs`](skills/marketing-and-seo/microsoft-docs/SKILL.md) | Query official Microsoft documentation to find concepts, tutorials. |
| `/microsoft-foundry` | [`microsoft-foundry`](skills/marketing-and-seo/microsoft-foundry/SKILL.md) | Deploy, evaluate, fine-tune, and manage Foundry agents end-to-end: Docker build, ACR push, hosted/prompt agent create,. |
| `/microsoft-skill-creator` | [`microsoft-skill-creator`](skills/marketing-and-seo/microsoft-skill-creator/SKILL.md) | Create agent skills for Microsoft technologies using Learn MCP tools. |
| `/microsoft_clarity-automation` | [`microsoft_clarity-automation`](skills/marketing-and-seo/microsoft_clarity-automation/SKILL.md) | Automate Microsoft Clarity tasks via Rube MCP (Composio): session recordings, heatmaps, and user behavior analytics. |
| `/odoo-sales-crm-expert` | [`odoo-sales-crm-expert`](skills/marketing-and-seo/odoo-sales-crm-expert/SKILL.md) | Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting. |
| `/onboarding-cro` | [`onboarding-cro`](skills/marketing-and-seo/onboarding-cro/SKILL.md) | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. |
| `/page-cro` | [`page-cro`](skills/marketing-and-seo/page-cro/SKILL.md) | When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing. |
| `/paid-ads` | [`paid-ads`](skills/marketing-and-seo/paid-ads/SKILL.md) | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X. |
| `/paywall-upgrade-cro` | [`paywall-upgrade-cro`](skills/marketing-and-seo/paywall-upgrade-cro/SKILL.md) | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. |
| `/pitch-psychologist` | [`pitch-psychologist`](skills/marketing-and-seo/pitch-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/popup-cro` | [`popup-cro`](skills/marketing-and-seo/popup-cro/SKILL.md) | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. |
| `/pricing-strategy` | [`pricing-strategy`](skills/marketing-and-seo/pricing-strategy/SKILL.md) | When the user wants help with pricing decisions, packaging, or monetization strategy. |
| `/product-marketing-context` | [`product-marketing-context`](skills/marketing-and-seo/product-marketing-context/SKILL.md) | When the user wants to create or update their product marketing context document. |
| `/programmatic-seo` | [`programmatic-seo`](skills/marketing-and-seo/programmatic-seo/SKILL.md) | When the user wants to create SEO-driven pages at scale using templates and data. |
| `/referral-program` | [`referral-program`](skills/marketing-and-seo/referral-program/SKILL.md) | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. |
| `/revops` | [`revops`](skills/marketing-and-seo/revops/SKILL.md) | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. |
| `/roundup-setup` | [`roundup-setup`](skills/marketing-and-seo/roundup-setup/SKILL.md) | Interactive onboarding that learns your communication style, audiences. |
| `/sales-automator` | [`sales-automator`](skills/marketing-and-seo/sales-automator/SKILL.md) | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. |
| `/sales-enablement` | [`sales-enablement`](skills/marketing-and-seo/sales-enablement/SKILL.md) | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. |
| `/scroll-experience` | [`scroll-experience`](skills/marketing-and-seo/scroll-experience/SKILL.md) | Expert in building immersive scroll-driven experiences - parallax. |
| `/seo` | [`seo`](skills/marketing-and-seo/seo/SKILL.md) | SEO specialist agent with site audits, content writing, keyword research, technical fixes, link building, and ranking strategies. |
| `/seo-aeo-blog-writer` | [`seo-aeo-blog-writer`](skills/marketing-and-seo/seo-aeo-blog-writer/SKILL.md) | Writes long-form blog posts with TL;DR block, definition sentence, comparison table. |
| `/seo-aeo-content-cluster` | [`seo-aeo-content-cluster`](skills/marketing-and-seo/seo-aeo-content-cluster/SKILL.md) | Builds a topical authority map with a pillar page, prioritised cluster articles, content types, internal link map. |
| `/seo-aeo-content-quality-auditor` | [`seo-aeo-content-quality-auditor`](skills/marketing-and-seo/seo-aeo-content-quality-auditor/SKILL.md) | Audits content for SEO and AEO performance with scored reports, severity-ranked fix lists, and projected scores after fixes. |
| `/seo-aeo-keyword-research` | [`seo-aeo-keyword-research`](skills/marketing-and-seo/seo-aeo-keyword-research/SKILL.md) | Researches and prioritises SEO keywords with AEO question queries, difficulty tiers, cannibalization checks, and a content map. |
| `/seo-aeo-landing-page-writer` | [`seo-aeo-landing-page-writer`](skills/marketing-and-seo/seo-aeo-landing-page-writer/SKILL.md) | Writes complete, structured landing pages optimized for SEO ranking, AEO citation, and visitor conversion. |
| `/seo-aeo-meta-description-generator` | [`seo-aeo-meta-description-generator`](skills/marketing-and-seo/seo-aeo-meta-description-generator/SKILL.md) | Writes 3 title tag variants and 3 meta description variants per page with SERP preview, OG tags, and Twitter Card tags. |
| `/seo-article-gen` | [`seo-article-gen`](skills/marketing-and-seo/seo-article-gen/SKILL.md) | SEO-optimized article generator with automatic affiliate link integration. |
| `/seo-audit` | [`seo-audit`](skills/marketing-and-seo/seo-audit/SKILL.md) | When the user wants to audit, review, or diagnose SEO issues on their site. |
| `/seo-cannibalization-detector` | [`seo-cannibalization-detector`](skills/marketing-and-seo/seo-cannibalization-detector/SKILL.md) | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. |
| `/seo-competitor-analysis` | [`seo-competitor-analysis`](skills/marketing-and-seo/seo-competitor-analysis/SKILL.md) | Perform deep SEO competitor analysis, including keyword research, backlink checking, and content strategy mapping. |
| `/seo-competitor-pages` | [`seo-competitor-pages`](skills/marketing-and-seo/seo-competitor-pages/SKILL.md) | Generate SEO-optimized competitor comparison and alternatives pages. |
| `/seo-content` | [`seo-content`](skills/marketing-and-seo/seo-content/SKILL.md) | Content quality and E-E-A-T analysis with AI citation readiness assessment. |
| `/seo-content-auditor` | [`seo-content-auditor`](skills/marketing-and-seo/seo-content-auditor/SKILL.md) | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. |
| `/seo-content-planner` | [`seo-content-planner`](skills/marketing-and-seo/seo-content-planner/SKILL.md) | Creates comprehensive content outlines and topic clusters for SEO. |
| `/seo-content-refresher` | [`seo-content-refresher`](skills/marketing-and-seo/seo-content-refresher/SKILL.md) | Identifies outdated elements in provided content and suggests updates to maintain freshness. |
| `/seo-content-writer` | [`seo-content-writer`](skills/marketing-and-seo/seo-content-writer/SKILL.md) | Use when the user asks to "write SEO content", "create a blog post", "write an article", "content writing", "draft. |
| `/seo-dataforseo` | [`seo-dataforseo`](skills/marketing-and-seo/seo-dataforseo/SKILL.md) | Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. |
| `/seo-forensic-incident-response` | [`seo-forensic-incident-response`](skills/marketing-and-seo/seo-forensic-incident-response/SKILL.md) | Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with. |
| `/seo-fundamentals` | [`seo-fundamentals`](skills/marketing-and-seo/seo-fundamentals/SKILL.md) | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality. |
| `/seo-geo` | [`seo-geo`](skills/marketing-and-seo/seo-geo/SKILL.md) | Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. |
| `/seo-hreflang` | [`seo-hreflang`](skills/marketing-and-seo/seo-hreflang/SKILL.md) | Hreflang and international SEO audit, validation, and generation. |
| `/seo-image-gen` | [`seo-image-gen`](skills/marketing-and-seo/seo-image-gen/SKILL.md) | Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. |
| `/seo-images` | [`seo-images`](skills/marketing-and-seo/seo-images/SKILL.md) | Image optimization analysis for SEO and performance. |
| `/seo-keyword-strategist` | [`seo-keyword-strategist`](skills/marketing-and-seo/seo-keyword-strategist/SKILL.md) | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. |
| `/seo-meta-optimizer` | [`seo-meta-optimizer`](skills/marketing-and-seo/seo-meta-optimizer/SKILL.md) | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. |
| `/seo-page` | [`seo-page`](skills/marketing-and-seo/seo-page/SKILL.md) | Deep single-page SEO analysis covering on-page elements, content quality, technical meta tags, schema, images, and performance. |
| `/seo-plan` | [`seo-plan`](skills/marketing-and-seo/seo-plan/SKILL.md) | Strategic SEO planning for new or existing websites. |
| `/seo-programmatic` | [`seo-programmatic`](skills/marketing-and-seo/seo-programmatic/SKILL.md) | Plan and audit programmatic SEO pages generated at scale from structured data. |
| `/seo-schema` | [`seo-schema`](skills/marketing-and-seo/seo-schema/SKILL.md) | Detect, validate, and generate Schema.org structured data. JSON-LD format preferred. |
| `/seo-sitemap` | [`seo-sitemap`](skills/marketing-and-seo/seo-sitemap/SKILL.md) | Analyze existing XML sitemaps or generate new ones with industry templates. |
| `/seo-snippet-hunter` | [`seo-snippet-hunter`](skills/marketing-and-seo/seo-snippet-hunter/SKILL.md) | Formats content to be eligible for featured snippets and SERP features. |
| `/seo-structure-architect` | [`seo-structure-architect`](skills/marketing-and-seo/seo-structure-architect/SKILL.md) | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. |
| `/seo-technical` | [`seo-technical`](skills/marketing-and-seo/seo-technical/SKILL.md) | Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data,. |
| `/signup-flow-cro` | [`signup-flow-cro`](skills/marketing-and-seo/signup-flow-cro/SKILL.md) | When the user wants to optimize signup, registration, account creation, or trial activation flows. |
| `/social-content` | [`social-content`](skills/marketing-and-seo/social-content/SKILL.md) | When the user wants help creating, scheduling. |
| `/social-post-writer-seo` | [`social-post-writer-seo`](skills/marketing-and-seo/social-post-writer-seo/SKILL.md) | Social Media Strategist and Content Writer. |
| `/technical-seo-checker` | [`technical-seo-checker`](skills/marketing-and-seo/technical-seo-checker/SKILL.md) | This skill should be used when the user asks to "technical SEO audit", "check page speed", "Core Web Vitals", "LCP is. |
| `/train-sentence-transformers` | [`train-sentence-transformers`](skills/marketing-and-seo/train-sentence-transformers/SKILL.md) | Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder; dense or static embedding. |
| `/web-quality-audit` | [`web-quality-audit`](skills/marketing-and-seo/web-quality-audit/SKILL.md) | Comprehensive web quality audit covering performance, accessibility, SEO, and best practices. |
| `/wiki-researcher` | [`wiki-researcher`](skills/marketing-and-seo/wiki-researcher/SKILL.md) | Conducts multi-turn iterative deep research on specific topics within a codebase with zero tolerance for shallow analysis. |
| `/xiaohongshu-content-strategist` | [`xiaohongshu-content-strategist`](skills/marketing-and-seo/xiaohongshu-content-strategist/SKILL.md) | Create viral Xiaohongshu (小红书) content with platform-native strategy, save-rate optimization, trending formats. |
| `/xurl` | [`xurl`](skills/marketing-and-seo/xurl/SKILL.md) | A Twitter research and content intelligence skill focused on attracting WordPress and Shopify clients. |

---

### 🔒 Security & System Compliance
> *Cybersecurity reviews, code sanitisation, threat modelling, license monitoring, and GDPR compliance.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/007` | [`007`](skills/security-and-compliance/007/SKILL.md) | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response. |
| `/Defense-in-Depth Validation` | [`Defense-in-Depth Validation`](skills/security-and-compliance/Defense-in-Depth Validation/SKILL.md) | Validate at every layer data passes through to make bugs impossible. |
| `/accessibility-compliance-accessibility-audit` | [`accessibility-compliance-accessibility-audit`](skills/security-and-compliance/accessibility-compliance-accessibility-audit/SKILL.md) | You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. |
| `/anti-reversing-techniques` | [`anti-reversing-techniques`](skills/security-and-compliance/anti-reversing-techniques/SKILL.md) | AUTHORIZED USE ONLY: This skill contains dual-use security techniques. |
| `/attack-tree-construction` | [`attack-tree-construction`](skills/security-and-compliance/attack-tree-construction/SKILL.md) | Build comprehensive attack trees to visualize threat paths. |
| `/auth-implementation-patterns` | [`auth-implementation-patterns`](skills/security-and-compliance/auth-implementation-patterns/SKILL.md) | Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices. |
| `/azure-compliance` | [`azure-compliance`](skills/security-and-compliance/azure-compliance/SKILL.md) | Run Azure compliance and security audits with azqr plus Key Vault expiration checks. |
| `/backend-security-coder` | [`backend-security-coder`](skills/security-and-compliance/backend-security-coder/SKILL.md) | Expert in secure backend coding practices specializing in input validation, authentication, and API security. |
| `/best-practices` | [`best-practices`](skills/security-and-compliance/best-practices/SKILL.md) | Apply modern web development best practices for security, compatibility, and code quality. |
| `/broken-authentication` | [`broken-authentication`](skills/security-and-compliance/broken-authentication/SKILL.md) | Identify and exploit authentication and session management vulnerabilities in web applications. |
| `/cc-skill-security-review` | [`cc-skill-security-review`](skills/security-and-compliance/cc-skill-security-review/SKILL.md) | This skill ensures all code follows security best practices and identifies potential vulnerabilities. |
| `/clerk-auth` | [`clerk-auth`](skills/security-and-compliance/clerk-auth/SKILL.md) | Expert patterns for Clerk auth implementation, middleware,. |
| `/code-review-checklist` | [`code-review-checklist`](skills/security-and-compliance/code-review-checklist/SKILL.md) | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability. |
| `/codebase-cleanup-deps-audit` | [`codebase-cleanup-deps-audit`](skills/security-and-compliance/codebase-cleanup-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. |
| `/configure-auth` | [`configure-auth`](skills/security-and-compliance/configure-auth/SKILL.md) | Add authentication and authorization to a Blazor Web App, accounting for the app's render mode. |
| `/container-security-hardening` | [`container-security-hardening`](skills/security-and-compliance/container-security-hardening/SKILL.md) | Harden Docker/container images and runtime deployments with secure base images, non-root users, CVE scanning,. |
| `/customs-trade-compliance` | [`customs-trade-compliance`](skills/security-and-compliance/customs-trade-compliance/SKILL.md) | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening. |
| `/data-breach-blast-radius` | [`data-breach-blast-radius`](skills/security-and-compliance/data-breach-blast-radius/SKILL.md) | Pre-breach impact analysis: inventories sensitive data (PII, PHI, PCI-DSS, credentials), traces data flows, scores. |
| `/dependency-management-deps-audit` | [`dependency-management-deps-audit`](skills/security-and-compliance/dependency-management-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. |
| `/differential-review` | [`differential-review`](skills/security-and-compliance/differential-review/SKILL.md) | Security-focused code review for PRs, commits, and diffs. |
| `/doc-coauthoring` | [`doc-coauthoring`](skills/security-and-compliance/doc-coauthoring/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. |
| `/doubt-driven-development` | [`doubt-driven-development`](skills/security-and-compliance/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. |
| `/entra-app-registration` | [`entra-app-registration`](skills/security-and-compliance/entra-app-registration/SKILL.md) | Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. |
| `/ethical-hacking-methodology` | [`ethical-hacking-methodology`](skills/security-and-compliance/ethical-hacking-methodology/SKILL.md) | Master the complete penetration testing lifecycle from reconnaissance through reporting. |
| `/fda-food-safety-auditor` | [`fda-food-safety-auditor`](skills/security-and-compliance/fda-food-safety-auditor/SKILL.md) | Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. |
| `/fda-medtech-compliance-auditor` | [`fda-medtech-compliance-auditor`](skills/security-and-compliance/fda-medtech-compliance-auditor/SKILL.md) | Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. |
| `/ffuf-web-fuzzing` | [`ffuf-web-fuzzing`](skills/security-and-compliance/ffuf-web-fuzzing/SKILL.md) | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests,. |
| `/find-bugs` | [`find-bugs`](skills/security-and-compliance/find-bugs/SKILL.md) | Find bugs, security vulnerabilities, and code quality issues in local branch changes. |
| `/firmware-analyst` | [`firmware-analyst`](skills/security-and-compliance/firmware-analyst/SKILL.md) | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| `/gdpr-compliant` | [`gdpr-compliant`](skills/security-and-compliance/gdpr-compliant/SKILL.md) | Apply GDPR-compliant engineering practices across your codebase. |
| `/gdpr-data-handling` | [`gdpr-data-handling`](skills/security-and-compliance/gdpr-data-handling/SKILL.md) | Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls. |
| `/gha-security-review` | [`gha-security-review`](skills/security-and-compliance/gha-security-review/SKILL.md) | Find exploitable vulnerabilities in GitHub Actions workflows. |
| `/google-cloud-recipe-auth` | [`google-cloud-recipe-auth`](skills/security-and-compliance/google-cloud-recipe-auth/SKILL.md) | Provides expert guidance on authenticating and authorizing to Google Cloud services and APIs, covering human users,. |
| `/google-cloud-waf-security` | [`google-cloud-waf-security`](skills/security-and-compliance/google-cloud-waf-security/SKILL.md) | Generates security-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/k8s-security-policies` | [`k8s-security-policies`](skills/security-and-compliance/k8s-security-policies/SKILL.md) | Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes. |
| `/laravel-expert` | [`laravel-expert`](skills/security-and-compliance/laravel-expert/SKILL.md) | Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. |
| `/laravel-security-audit` | [`laravel-security-audit`](skills/security-and-compliance/laravel-security-audit/SKILL.md) | Security auditor for Laravel applications. |
| `/latex-paper-conversion` | [`latex-paper-conversion`](skills/security-and-compliance/latex-paper-conversion/SKILL.md) | This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer,. |
| `/legal-advisor` | [`legal-advisor`](skills/security-and-compliance/legal-advisor/SKILL.md) | Draft privacy policies, terms of service, disclaimers, and legal notices. |
| `/linkerd-patterns` | [`linkerd-patterns`](skills/security-and-compliance/linkerd-patterns/SKILL.md) | Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. |
| `/malware-analyst` | [`malware-analyst`](skills/security-and-compliance/malware-analyst/SKILL.md) | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. |
| `/metasploit-framework` | [`metasploit-framework`](skills/security-and-compliance/metasploit-framework/SKILL.md) | ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. |
| `/network-101` | [`network-101`](skills/security-and-compliance/network-101/SKILL.md) | Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. |
| `/network-engineer` | [`network-engineer`](skills/security-and-compliance/network-engineer/SKILL.md) | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| `/nextjs-supabase-auth` | [`nextjs-supabase-auth`](skills/security-and-compliance/nextjs-supabase-auth/SKILL.md) | Expert integration of Supabase Auth with Next.js App Router. |
| `/odoo-l10n-compliance` | [`odoo-l10n-compliance`](skills/security-and-compliance/odoo-l10n-compliance/SKILL.md) | Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting. |
| `/odoo-security-rules` | [`odoo-security-rules`](skills/security-and-compliance/odoo-security-rules/SKILL.md) | Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns. |
| `/pci-compliance` | [`pci-compliance`](skills/security-and-compliance/pci-compliance/SKILL.md) | Master PCI DSS (Payment Card Industry Data Security Standard) compliance for secure payment processing and handling of. |
| `/pentest-checklist` | [`pentest-checklist`](skills/security-and-compliance/pentest-checklist/SKILL.md) | Provide a comprehensive checklist for planning, executing, and following up on penetration tests. |
| `/pentest-commands` | [`pentest-commands`](skills/security-and-compliance/pentest-commands/SKILL.md) | Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation,. |
| `/red-team-tools` | [`red-team-tools`](skills/security-and-compliance/red-team-tools/SKILL.md) | Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance,. |
| `/returns-reverse-logistics` | [`returns-reverse-logistics`](skills/security-and-compliance/returns-reverse-logistics/SKILL.md) | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud. |
| `/scanning-tools` | [`scanning-tools`](skills/security-and-compliance/scanning-tools/SKILL.md) | Master essential security scanning tools for network discovery, vulnerability assessment, web application testing,. |
| `/security-and-hardening` | [`security-and-hardening`](skills/security-and-compliance/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. |
| `/security-audit` | [`security-audit`](skills/security-and-compliance/security-audit/SKILL.md) | Comprehensive security auditing workflow covering web application testing, API security, penetration testing,. |
| `/security-auditor` | [`security-auditor`](skills/security-and-compliance/security-auditor/SKILL.md) | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| `/security-compliance-compliance-check` | [`security-compliance-compliance-check`](skills/security-and-compliance/security-compliance-compliance-check/SKILL.md) | You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2,. |
| `/security-requirement-extraction` | [`security-requirement-extraction`](skills/security-and-compliance/security-requirement-extraction/SKILL.md) | Derive security requirements from threat models and business context. |
| `/security-review` | [`security-review`](skills/security-and-compliance/security-review/SKILL.md) | AI-powered codebase security scanner that reasons about code like a security researcher — tracing data flows,. |
| `/security-scanning-security-dependencies` | [`security-scanning-security-dependencies`](skills/security-and-compliance/security-scanning-security-dependencies/SKILL.md) | You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. |
| `/security-scanning-security-hardening` | [`security-scanning-security-hardening`](skills/security-and-compliance/security-scanning-security-hardening/SKILL.md) | Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls. |
| `/security-scanning-security-sast` | [`security-scanning-security-sast`](skills/security-and-compliance/security-scanning-security-sast/SKILL.md) | Static Application Security Testing (SAST) for code vulnerability. |
| `/smtp-penetration-testing` | [`smtp-penetration-testing`](skills/security-and-compliance/smtp-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities. |
| `/solidity-security` | [`solidity-security`](skills/security-and-compliance/solidity-security/SKILL.md) | Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns. |
| `/spec-to-code-compliance` | [`spec-to-code-compliance`](skills/security-and-compliance/spec-to-code-compliance/SKILL.md) | Verifies code implements exactly what documentation specifies for blockchain audits. |
| `/stride-analysis-patterns` | [`stride-analysis-patterns`](skills/security-and-compliance/stride-analysis-patterns/SKILL.md) | Apply STRIDE methodology to systematically identify threats. |
| `/supply-chain-risk-auditor` | [`supply-chain-risk-auditor`](skills/security-and-compliance/supply-chain-risk-auditor/SKILL.md) | Identifies dependencies at heightened risk of exploitation or takeover. |
| `/target-authoring` | [`target-authoring`](skills/security-and-compliance/target-authoring/SKILL.md) | Canonical patterns for writing custom MSBuild targets. Only activate in MSBuild/.NET build context. |
| `/template-authoring` | [`template-authoring`](skills/security-and-compliance/template-authoring/SKILL.md) | Guides creation and validation of custom dotnet new templates. |
| `/threat-mitigation-mapping` | [`threat-mitigation-mapping`](skills/security-and-compliance/threat-mitigation-mapping/SKILL.md) | Map identified threats to appropriate security controls and mitigations. |
| `/threat-model-analyst` | [`threat-model-analyst`](skills/security-and-compliance/threat-model-analyst/SKILL.md) | Full STRIDE-A threat model analysis and incremental update skill for repositories and systems. |
| `/threat-modeling-expert` | [`threat-modeling-expert`](skills/security-and-compliance/threat-modeling-expert/SKILL.md) | Expert in threat modeling methodologies, security architecture review, and risk assessment. |
| `/top-web-vulnerabilities` | [`top-web-vulnerabilities`](skills/security-and-compliance/top-web-vulnerabilities/SKILL.md) | Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. |
| `/vercel-cli-with-tokens` | [`vercel-cli-with-tokens`](skills/security-and-compliance/vercel-cli-with-tokens/SKILL.md) | Deploy and manage projects on Vercel using token-based authentication. |
| `/vulnerability-scanner` | [`vulnerability-scanner`](skills/security-and-compliance/vulnerability-scanner/SKILL.md) | Advanced vulnerability analysis principles. |
| `/web-security-testing` | [`web-security-testing`](skills/security-and-compliance/web-security-testing/SKILL.md) | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication. |
| `/wireshark-analysis` | [`wireshark-analysis`](skills/security-and-compliance/wireshark-analysis/SKILL.md) | Execute comprehensive network traffic analysis using Wireshark to capture, filter. |
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
| `/claude-scientific-skills` | [`claude-scientific-skills`](skills/science-and-bioinformatics/claude-scientific-skills/SKILL.md) | Scientific research and analysis skills. |
| `/code-exemplars-blueprint-generator` | [`code-exemplars-blueprint-generator`](skills/science-and-bioinformatics/code-exemplars-blueprint-generator/SKILL.md) | Technology-agnostic prompt generator that creates customizable AI prompts for scanning codebases and identifying. |
| `/codex-review` | [`codex-review`](skills/science-and-bioinformatics/codex-review/SKILL.md) | Professional code review with auto CHANGELOG generation, integrated with Codex AI. |
| `/comment-code-generate-a-tutorial` | [`comment-code-generate-a-tutorial`](skills/science-and-bioinformatics/comment-code-generate-a-tutorial/SKILL.md) | Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear. |
| `/concise-planning` | [`concise-planning`](skills/science-and-bioinformatics/concise-planning/SKILL.md) | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. |
| `/context-map` | [`context-map`](skills/science-and-bioinformatics/context-map/SKILL.md) | Generate a map of all files relevant to a task before making changes. |
| `/copilot-instructions-blueprint-generator` | [`copilot-instructions-blueprint-generator`](skills/science-and-bioinformatics/copilot-instructions-blueprint-generator/SKILL.md) | Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub. |
| `/create-specification` | [`create-specification`](skills/science-and-bioinformatics/create-specification/SKILL.md) | Create a new specification file for the solution, optimized for Generative AI consumption. |
| `/daily-news-report` | [`daily-news-report`](skills/science-and-bioinformatics/daily-news-report/SKILL.md) | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. |
| `/draw-io-diagram-generator` | [`draw-io-diagram-generator`](skills/science-and-bioinformatics/draw-io-diagram-generator/SKILL.md) | Use when creating, editing, or generating draw.io diagram files (.drawio, .drawio.svg, .drawio.png). |
| `/editorconfig` | [`editorconfig`](skills/science-and-bioinformatics/editorconfig/SKILL.md) | Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences. |
| `/excalidraw-diagram-generator` | [`excalidraw-diagram-generator`](skills/science-and-bioinformatics/excalidraw-diagram-generator/SKILL.md) | Generate Excalidraw diagrams from natural language descriptions. |
| `/faf-wizard` | [`faf-wizard`](skills/science-and-bioinformatics/faf-wizard/SKILL.md) | Done-for-you .faf generator. One-click AI context for any project - new, legacy, or famous. |
| `/fal-generate` | [`fal-generate`](skills/science-and-bioinformatics/fal-generate/SKILL.md) | Generate images and videos using fal.ai AI models. |
| `/fal-workflow` | [`fal-workflow`](skills/science-and-bioinformatics/fal-workflow/SKILL.md) | Generate workflow JSON files for chaining AI models. |
| `/favicon` | [`favicon`](skills/science-and-bioinformatics/favicon/SKILL.md) | Generate favicons from a source image. |
| `/flowstudio-power-automate-governance` | [`flowstudio-power-automate-governance`](skills/science-and-bioinformatics/flowstudio-power-automate-governance/SKILL.md) | Govern Power Automate flows and Power Apps at scale using the FlowStudio MCP cached store. |
| `/folder-structure-blueprint-generator` | [`folder-structure-blueprint-generator`](skills/science-and-bioinformatics/folder-structure-blueprint-generator/SKILL.md) | Comprehensive technology-agnostic prompt for analyzing and documenting project folder structures. |
| `/framework-migration-code-migrate` | [`framework-migration-code-migrate`](skills/science-and-bioinformatics/framework-migration-code-migrate/SKILL.md) | You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. |
| `/generate-custom-instructions-from-codebase` | [`generate-custom-instructions-from-codebase`](skills/science-and-bioinformatics/generate-custom-instructions-from-codebase/SKILL.md) | Migration and code evolution instructions generator for GitHub Copilot. |
| `/generate-image` | [`generate-image`](skills/science-and-bioinformatics/generate-image/SKILL.md) | Generate images using AI. |
| `/generate-testability-wrappers` | [`generate-testability-wrappers`](skills/science-and-bioinformatics/generate-testability-wrappers/SKILL.md) | Generate wrapper interfaces and DI registration for hard-to-test static dependencies in C#. |
| `/i18n-localization` | [`i18n-localization`](skills/science-and-bioinformatics/i18n-localization/SKILL.md) | Internationalization and localization patterns. |
| `/including-generated-files` | [`including-generated-files`](skills/science-and-bioinformatics/including-generated-files/SKILL.md) | Fix MSBuild targets that generate files during the build but those files are missing from compilation or output. |
| `/internal-comms` | [`internal-comms`](skills/science-and-bioinformatics/internal-comms/SKILL.md) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. |
| `/internal-comms-anthropic` | [`internal-comms-anthropic`](skills/science-and-bioinformatics/internal-comms-anthropic/SKILL.md) | To write internal communications, use this skill for:. |
| `/internal-comms-community` | [`internal-comms-community`](skills/science-and-bioinformatics/internal-comms-community/SKILL.md) | To write internal communications, use this skill for:. |
| `/k8s-manifest-generator` | [`k8s-manifest-generator`](skills/science-and-bioinformatics/k8s-manifest-generator/SKILL.md) | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps,. |
| `/landing-page-generator` | [`landing-page-generator`](skills/science-and-bioinformatics/landing-page-generator/SKILL.md) | Generates high-converting Next.js/React landing pages with Tailwind CSS. |
| `/meeting-minutes` | [`meeting-minutes`](skills/science-and-bioinformatics/meeting-minutes/SKILL.md) | Generate concise, actionable meeting minutes for internal meetings. |
| `/mise-configurator` | [`mise-configurator`](skills/science-and-bioinformatics/mise-configurator/SKILL.md) | Generate production-ready mise.toml setups for local development, CI/CD pipelines, and toolchain standardization. |
| `/plantuml-ascii` | [`plantuml-ascii`](skills/science-and-bioinformatics/plantuml-ascii/SKILL.md) | Generate ASCII art diagrams using PlantUML text mode. |
| `/playwright-generate-test` | [`playwright-generate-test`](skills/science-and-bioinformatics/playwright-generate-test/SKILL.md) | Generate a Playwright test based on a scenario using Playwright MCP. |
| `/podcast-generation` | [`podcast-generation`](skills/science-and-bioinformatics/podcast-generation/SKILL.md) | Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. |
| `/project-workflow-analysis-blueprint-generator` | [`project-workflow-analysis-blueprint-generator`](skills/science-and-bioinformatics/project-workflow-analysis-blueprint-generator/SKILL.md) | Comprehensive technology-agnostic prompt generator for documenting end-to-end application workflows. |
| `/pypict-skill` | [`pypict-skill`](skills/science-and-bioinformatics/pypict-skill/SKILL.md) | Pairwise test generation. |
| `/readme-blueprint-generator` | [`readme-blueprint-generator`](skills/science-and-bioinformatics/readme-blueprint-generator/SKILL.md) | Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive. |
| `/refactor-method-complexity-reduce` | [`refactor-method-complexity-reduce`](skills/science-and-bioinformatics/refactor-method-complexity-reduce/SKILL.md) | Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or. |
| `/repo-story-time` | [`repo-story-time`](skills/science-and-bioinformatics/repo-story-time/SKILL.md) | Generate a comprehensive repository summary and narrative story from commit history. |
| `/scanpy` | [`scanpy`](skills/science-and-bioinformatics/scanpy/SKILL.md) | Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. |
| `/scientific-writing` | [`scientific-writing`](skills/science-and-bioinformatics/scientific-writing/SKILL.md) | This is the core skill for the deep research and writing tool—combining AI-driven deep research with well-formatted. |
| `/seo-aeo-internal-linking` | [`seo-aeo-internal-linking`](skills/science-and-bioinformatics/seo-aeo-internal-linking/SKILL.md) | Maps internal link opportunities between pages with anchor text, placement instructions, orphan page detection. |
| `/seo-aeo-schema-generator` | [`seo-aeo-schema-generator`](skills/science-and-bioinformatics/seo-aeo-schema-generator/SKILL.md) | Generates valid JSON-LD structured data for 10 schema types with rich result eligibility validation and. |
| `/sequence-psychologist` | [`sequence-psychologist`](skills/science-and-bioinformatics/sequence-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it. |
| `/skin-health-analyzer` | [`skin-health-analyzer`](skills/science-and-bioinformatics/skin-health-analyzer/SKILL.md) | Analyze skin health data, identify skin problem patterns, assess skin health status. |
| `/structured-autonomy-generate` | [`structured-autonomy-generate`](skills/science-and-bioinformatics/structured-autonomy-generate/SKILL.md) | Structured Autonomy Implementation Generator Prompt. |
| `/tailored-resume-generator` | [`tailored-resume-generator`](skills/science-and-bioinformatics/tailored-resume-generator/SKILL.md) | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills. |
| `/tdd-workflows-tdd-red` | [`tdd-workflows-tdd-red`](skills/science-and-bioinformatics/tdd-workflows-tdd-red/SKILL.md) | Generate failing tests for the TDD red phase to define expected behavior and edge cases. |
| `/team-collaboration-standup-notes` | [`team-collaboration-standup-notes`](skills/science-and-bioinformatics/team-collaboration-standup-notes/SKILL.md) | You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation. |
| `/technology-stack-blueprint-generator` | [`technology-stack-blueprint-generator`](skills/science-and-bioinformatics/technology-stack-blueprint-generator/SKILL.md) | Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. |
| `/unit-testing-test-generate` | [`unit-testing-test-generate`](skills/science-and-bioinformatics/unit-testing-test-generate/SKILL.md) | Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus. |
| `/unslop` | [`unslop`](skills/science-and-bioinformatics/unslop/SKILL.md) | Post-process AI-generated text through the unslop CLI to strip AI writing patterns before publishing. |

---

### ☁️ Cloud & DevOps Infrastructure
> *Cloud deployment toolsets (Azure, AWS), infrastructure-as-code (Terraform, Bicep), and CI/CD pipelines.*

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/Cloudinary Automation` | [`Cloudinary Automation`](skills/cloud-and-infrastructure/Cloudinary Automation/SKILL.md) | Automate Cloudinary media management including folder organization, upload presets, asset lookup, transformations. |
| `/Writing Skills` | [`Writing Skills`](skills/cloud-and-infrastructure/Writing Skills/SKILL.md) | TDD for process documentation - test with subagents before writing, iterate until bulletproof. |
| `/acceptance-orchestrator` | [`acceptance-orchestrator`](skills/cloud-and-infrastructure/acceptance-orchestrator/SKILL.md) | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment. |
| `/amazon-alexa` | [`amazon-alexa`](skills/cloud-and-infrastructure/amazon-alexa/SKILL.md) | Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude. |
| `/appdeploy` | [`appdeploy`](skills/cloud-and-infrastructure/appdeploy/SKILL.md) | Deploy web apps with backend APIs, database, and file storage. |
| `/aws-cdk-python-setup` | [`aws-cdk-python-setup`](skills/cloud-and-infrastructure/aws-cdk-python-setup/SKILL.md) | Setup and initialization guide for developing AWS CDK (Cloud Development Kit) applications in Python. |
| `/aws-cost-cleanup` | [`aws-cost-cleanup`](skills/cloud-and-infrastructure/aws-cost-cleanup/SKILL.md) | Automated cleanup of unused AWS resources to reduce costs. |
| `/aws-cost-optimizer` | [`aws-cost-optimizer`](skills/cloud-and-infrastructure/aws-cost-optimizer/SKILL.md) | Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer. |
| `/aws-penetration-testing` | [`aws-penetration-testing`](skills/cloud-and-infrastructure/aws-penetration-testing/SKILL.md) | Provide comprehensive techniques for penetration testing AWS cloud environments. |
| `/aws-serverless` | [`aws-serverless`](skills/cloud-and-infrastructure/aws-serverless/SKILL.md) | Specialized skill for building production-ready serverless. |
| `/aws-skills` | [`aws-skills`](skills/cloud-and-infrastructure/aws-skills/SKILL.md) | AWS development with infrastructure automation and cloud architecture patterns. |
| `/azd-deployment` | [`azd-deployment`](skills/cloud-and-infrastructure/azd-deployment/SKILL.md) | Deploy containerized frontend + backend applications to Azure Container Apps with remote builds, managed identity. |
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
| `/azure-functions` | [`azure-functions`](skills/cloud-and-infrastructure/azure-functions/SKILL.md) | Expert patterns for Azure Functions development including isolated. |
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
| `/cloud-architect` | [`cloud-architect`](skills/cloud-and-infrastructure/cloud-architect/SKILL.md) | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC. |
| `/cloud-design-patterns` | [`cloud-design-patterns`](skills/cloud-and-infrastructure/cloud-design-patterns/SKILL.md) | Cloud design patterns for distributed systems architecture covering 42 industry-standard patterns across reliability,. |
| `/cloud-devops` | [`cloud-devops`](skills/cloud-and-infrastructure/cloud-devops/SKILL.md) | Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring. |
| `/cloud-penetration-testing` | [`cloud-penetration-testing`](skills/cloud-and-infrastructure/cloud-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS). |
| `/cloud-run-basics` | [`cloud-run-basics`](skills/cloud-and-infrastructure/cloud-run-basics/SKILL.md) | Manages Cloud Run services, jobs, and worker pools. |
| `/cloud-solution-architect` | [`cloud-solution-architect`](skills/cloud-and-infrastructure/cloud-solution-architect/SKILL.md) | Transform the agent into a Cloud Solution Architect following Azure Architecture Center best practices. |
| `/cloudflare` | [`cloudflare`](skills/cloud-and-infrastructure/cloudflare/SKILL.md) | Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize,. |
| `/cloudflare-workers-expert` | [`cloudflare-workers-expert`](skills/cloud-and-infrastructure/cloudflare-workers-expert/SKILL.md) | Expert in Cloudflare Workers and the Edge Computing ecosystem. |
| `/cloudformation-best-practices` | [`cloudformation-best-practices`](skills/cloud-and-infrastructure/cloudformation-best-practices/SKILL.md) | CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. |
| `/cost-optimization` | [`cost-optimization`](skills/cloud-and-infrastructure/cost-optimization/SKILL.md) | Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP. |
| `/customize` | [`customize`](skills/cloud-and-infrastructure/customize/SKILL.md) | Interactive guided deployment flow for Azure OpenAI models with full customization control. |
| `/database-cloud-optimization-cost-optimize` | [`database-cloud-optimization-cost-optimize`](skills/cloud-and-infrastructure/database-cloud-optimization-cost-optimize/SKILL.md) | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance. |
| `/deploy-model` | [`deploy-model`](skills/cloud-and-infrastructure/deploy-model/SKILL.md) | Unified Azure OpenAI model deployment skill with intelligent intent-based routing. |
| `/deploy-to-vercel` | [`deploy-to-vercel`](skills/cloud-and-infrastructure/deploy-to-vercel/SKILL.md) | Deploy applications and websites to Vercel. |
| `/deployment-engineer` | [`deployment-engineer`](skills/cloud-and-infrastructure/deployment-engineer/SKILL.md) | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| `/deployment-pipeline-design` | [`deployment-pipeline-design`](skills/cloud-and-infrastructure/deployment-pipeline-design/SKILL.md) | Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies. |
| `/deployment-procedures` | [`deployment-procedures`](skills/cloud-and-infrastructure/deployment-procedures/SKILL.md) | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. |
| `/deployment-validation-config-validate` | [`deployment-validation-config-validate`](skills/cloud-and-infrastructure/deployment-validation-config-validate/SKILL.md) | You are a configuration management expert specializing in validating, testing. |
| `/devops-deploy` | [`devops-deploy`](skills/cloud-and-infrastructure/devops-deploy/SKILL.md) | DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como. |
| `/devops-rollout-plan` | [`devops-rollout-plan`](skills/cloud-and-infrastructure/devops-rollout-plan/SKILL.md) | Generate comprehensive rollout plans with preflight checks, step-by-step deployment, verification signals, rollback. |
| `/devops-troubleshooter` | [`devops-troubleshooter`](skills/cloud-and-infrastructure/devops-troubleshooter/SKILL.md) | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| `/expo-cicd-workflows` | [`expo-cicd-workflows`](skills/cloud-and-infrastructure/expo-cicd-workflows/SKILL.md) | Helps understand and write EAS workflow YAML files for Expo projects. |
| `/expo-deployment` | [`expo-deployment`](skills/cloud-and-infrastructure/expo-deployment/SKILL.md) | Deploy Expo apps to production. |
| `/file-uploads` | [`file-uploads`](skills/cloud-and-infrastructure/file-uploads/SKILL.md) | Expert at handling file uploads and cloud storage. Covers S3,. |
| `/gcp-cloud-run` | [`gcp-cloud-run`](skills/cloud-and-infrastructure/gcp-cloud-run/SKILL.md) | Specialized skill for building production-ready serverless. |
| `/google-cloud-networking-observability` | [`google-cloud-networking-observability`](skills/cloud-and-infrastructure/google-cloud-networking-observability/SKILL.md) | Investigates Google Cloud networking issues by analyzing logs, metrics, and diagnostics. |
| `/google-cloud-recipe-onboarding` | [`google-cloud-recipe-onboarding`](skills/cloud-and-infrastructure/google-cloud-recipe-onboarding/SKILL.md) | Guidance for a developer's first steps on Google Cloud, covering account creation, billing setup, project management. |
| `/google-cloud-waf-cost-optimization` | [`google-cloud-waf-cost-optimization`](skills/cloud-and-infrastructure/google-cloud-waf-cost-optimization/SKILL.md) | Generates cost optimization guidance for Google Cloud workloads based on the Google Cloud Well-Architected Framework (WAF). |
| `/google-cloud-waf-performance-optimization` | [`google-cloud-waf-performance-optimization`](skills/cloud-and-infrastructure/google-cloud-waf-performance-optimization/SKILL.md) | Generates performance-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/google-cloud-waf-reliability` | [`google-cloud-waf-reliability`](skills/cloud-and-infrastructure/google-cloud-waf-reliability/SKILL.md) | Generates reliability-focused guidance for Google Cloud workloads based on the design principles and recommendations in. |
| `/google-cloud-waf-sustainability` | [`google-cloud-waf-sustainability`](skills/cloud-and-infrastructure/google-cloud-waf-sustainability/SKILL.md) | Generates sustainability-focused guidance for Google Cloud workloads based on the design principles and recommendations. |
| `/gtm-enterprise-onboarding` | [`gtm-enterprise-onboarding`](skills/cloud-and-infrastructure/gtm-enterprise-onboarding/SKILL.md) | Four-phase framework for onboarding enterprise customers from contract to value realization. |
| `/hf-cli` | [`hf-cli`](skills/cloud-and-infrastructure/hf-cli/SKILL.md) | Hugging Face Hub CLI (`hf`) for downloading, uploading. |
| `/hybrid-cloud-architect` | [`hybrid-cloud-architect`](skills/cloud-and-infrastructure/hybrid-cloud-architect/SKILL.md) | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds. |
| `/hybrid-cloud-networking` | [`hybrid-cloud-networking`](skills/cloud-and-infrastructure/hybrid-cloud-networking/SKILL.md) | Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect. |
| `/import-infrastructure-as-code` | [`import-infrastructure-as-code`](skills/cloud-and-infrastructure/import-infrastructure-as-code/SKILL.md) | Import existing Azure resources into Terraform using Azure CLI discovery and Azure Verified Modules (AVM). |
| `/kubernetes-architect` | [`kubernetes-architect`](skills/cloud-and-infrastructure/kubernetes-architect/SKILL.md) | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux). |
| `/kubernetes-deployment` | [`kubernetes-deployment`](skills/cloud-and-infrastructure/kubernetes-deployment/SKILL.md) | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |
| `/lambda-lang` | [`lambda-lang`](skills/cloud-and-infrastructure/lambda-lang/SKILL.md) | Native agent-to-agent language for compact multi-agent messaging. |
| `/lambdatest-agent-skills` | [`lambdatest-agent-skills`](skills/cloud-and-infrastructure/lambdatest-agent-skills/SKILL.md) | Production-grade test automation skills for 46 frameworks across E2E, unit, mobile, BDD, visual. |
| `/makepad-deployment` | [`makepad-deployment`](skills/cloud-and-infrastructure/makepad-deployment/SKILL.md) | CRITICAL: Use for Makepad packaging and deployment. |
| `/ml-pipeline-workflow` | [`ml-pipeline-workflow`](skills/cloud-and-infrastructure/ml-pipeline-workflow/SKILL.md) | Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment. |
| `/multi-cloud-architecture` | [`multi-cloud-architecture`](skills/cloud-and-infrastructure/multi-cloud-architecture/SKILL.md) | Decision framework and patterns for architecting applications across AWS, Azure, and GCP. |
| `/pr-screenshots` | [`pr-screenshots`](skills/cloud-and-infrastructure/pr-screenshots/SKILL.md) | Embed before/after screenshots and annotated images in pull request descriptions. |
| `/preset` | [`preset`](skills/cloud-and-infrastructure/preset/SKILL.md) | Intelligently deploys Azure OpenAI models to optimal regions by analyzing capacity across all available regions. |
| `/python-azure-iot-edge-modules` | [`python-azure-iot-edge-modules`](skills/cloud-and-infrastructure/python-azure-iot-edge-modules/SKILL.md) | Build and operate Python Azure IoT Edge modules with robust messaging, deployment manifests, observability. |
| `/qdrant-deployment-options` | [`qdrant-deployment-options`](skills/cloud-and-infrastructure/qdrant-deployment-options/SKILL.md) | Guides Qdrant deployment selection. |
| `/qdrant-performance-optimization` | [`qdrant-performance-optimization`](skills/cloud-and-infrastructure/qdrant-performance-optimization/SKILL.md) | Different techniques to optimize the performance of Qdrant, including indexing strategies, query optimization. |
| `/secrets-management` | [`secrets-management`](skills/cloud-and-infrastructure/secrets-management/SKILL.md) | Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools. |
| `/shipping-and-launch` | [`shipping-and-launch`](skills/cloud-and-infrastructure/shipping-and-launch/SKILL.md) | Prepares production launches. Use when preparing to deploy to production. |
| `/terraform-aws-modules` | [`terraform-aws-modules`](skills/cloud-and-infrastructure/terraform-aws-modules/SKILL.md) | Terraform module creation for AWS — reusable modules, state management, and HCL best practices. |
| `/terraform-azurerm-set-diff-analyzer` | [`terraform-azurerm-set-diff-analyzer`](skills/cloud-and-infrastructure/terraform-azurerm-set-diff-analyzer/SKILL.md) | Analyze Terraform plan JSON output for AzureRM Provider to distinguish between false-positive diffs (order-only changes. |
| `/terraform-infrastructure` | [`terraform-infrastructure`](skills/cloud-and-infrastructure/terraform-infrastructure/SKILL.md) | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules. |
| `/terraform-module-library` | [`terraform-module-library`](skills/cloud-and-infrastructure/terraform-module-library/SKILL.md) | Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure. |
| `/terraform-skill` | [`terraform-skill`](skills/cloud-and-infrastructure/terraform-skill/SKILL.md) | Terraform infrastructure as code best practices. |
| `/terraform-specialist` | [`terraform-specialist`](skills/cloud-and-infrastructure/terraform-specialist/SKILL.md) | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| `/update-avm-modules-in-bicep` | [`update-avm-modules-in-bicep`](skills/cloud-and-infrastructure/update-avm-modules-in-bicep/SKILL.md) | Update Azure Verified Modules (AVM) to latest versions in Bicep files. |
| `/vercel-deployment` | [`vercel-deployment`](skills/cloud-and-infrastructure/vercel-deployment/SKILL.md) | Expert knowledge for deploying to Vercel with Next.js. |
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
