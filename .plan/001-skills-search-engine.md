---
goal: Build a Federated Search Engine integrating local skills and skills.sh API via Vercel Serverless
version: 1.0
date_created: 2026-06-22
status: 'Planned'
tags: [feature, architecture, search, vercel, frontend]
---

# Implementation Plan: Skills Search Engine

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

## Overview
**Current State:** The web application is a static Vite app that displays local skills only.
**Target State:** The web application acts as a Federated Search Engine deployed on Vercel, querying the local skills index AND fetching real-time data from the `skills.sh` API (using Vercel OIDC for authentication). It features a live skill counter, a real-time search bar, and displays the `SKILL.md` content inside a modal.

## 1. Requirements & Constraints
- **REQ-001**: Must integrate with `skills.sh` API using `@vercel/oidc`.
- **REQ-002**: Must migrate or configure the web application to run on Vercel (Next.js or Vite + Serverless Functions).
- **REQ-003**: The search engine must return mixed results (local + remote).
- **REQ-004**: Must display the total global skill count live.
- **REQ-005**: Must allow viewing `SKILL.md` content dynamically.
- **REQ-006**: Must provide a 1-click install command (`npx skills add ...`).
- **CON-001**: Must NOT use Hostinger or VPS. Everything must be deployed to Vercel.

## 2. Architecture & Alternatives
- Vercel Serverless Functions will be used as a secure proxy to fetch data from `skills.sh` to bypass CORS and authenticate using the automatically provided Vercel OIDC token.

## 2.1 No-Touch Zones
Files that MUST NOT be modified during this implementation:
- `AGENTS.md` — Agent context configuration.
- `plugins/aboalrejal-skills/` — The actual core skills stored locally must remain untouched.
- **ALT-001**: Direct client-side fetch to `skills.sh`. Rejected because Vercel OIDC tokens are only accessible securely from the backend serverless environment, and the API does not allow CORS for unauthenticated client requests.

## 3. Dependencies & Files
- **DEP-001**: `@vercel/oidc` for backend API authentication.
- **DEP-002**: `axios` or standard `fetch` API for network requests.
- **DEP-003**: A Markdown rendering library (e.g., `react-markdown` or `marked`) for previewing `SKILL.md` content.

| File Path | Change Type | Description / Dependencies |
|-----------|-------------|----------------------------|
| `package.json` | modify | Add Vercel and UI dependencies |
| `api/search.js` | create | Serverless function to proxy search requests to `skills.sh` |
| `api/stats.js` | create | Serverless function to fetch global skill stats |
| `api/skill-details.js` | create | Serverless function to fetch skill content |
| `apps/web-app/index.html` | modify | Add search bar and stat counters |
| `apps/web-app/main.js` | modify | Implement search logic and API calls |

## 4. Task Tracking & Phases

### Phase 1: Setup & Infrastructure
- **GOAL**: Configure Vercel deployment and install necessary backend dependencies.
- [x] TASK-001 [US1]: Initialize Vercel configuration and add `@vercel/oidc`

### Phase 2: Foundational (Backend APIs)
- **GOAL**: Create the serverless proxy functions to communicate securely with `skills.sh`.
- [x] TASK-002 [US1]: Create `api/stats.js` to fetch total skills count
- [x] TASK-003 [P] [US1]: Create `api/search.js` to query the search API
- [x] TASK-004 [P] [US1]: Create `api/skill-details.js` to fetch specific `SKILL.md` contents
- Checkpoint: Verify the APIs return valid JSON data locally using Vercel CLI.

### Phase 3: Frontend Search & UI
- **GOAL**: Update the web app to consume the backend APIs and display the Search Engine UI.
- [x] TASK-005 [US1]: Update the Home page to display the live global skill counter
- [x] TASK-006 [P] [US1]: Implement the dynamic search bar and result list
- [x] TASK-007 [US1]: Implement the Skill Details modal with Markdown rendering and copy command
- Checkpoint: Search flow works end-to-end. UI is polished and responsive.

## 5. Detailed Task Definitions

### TASK-001: Initialize Vercel configuration and add `@vercel/oidc`
**Description:** Configure the repository for Vercel deployment and install backend dependencies.
**Acceptance criteria:**
- [ ] `@vercel/oidc` is installed in `package.json`.
- [ ] A `vercel.json` file is added (if needed) for routing configuration.
**Verification:**
- [ ] Build succeeds: `npm run build`
**Dependencies:** None
**Files likely touched:**
- `package.json`
- `vercel.json`
**Estimated scope:** Small: 1-2 files

### TASK-002: Create `api/stats.js` to fetch total skills count
**Description:** Create a Vercel serverless function that uses `@vercel/oidc` to authenticate and fetch the total skill count from `skills.sh`.
**Acceptance criteria:**
- [ ] The endpoint `/api/stats` returns the total skill count from `skills.sh`.
- [ ] OIDC token is generated correctly.
**Verification:**
- [ ] Manual check: Hit `/api/stats` and verify numeric count response.
**Dependencies:** TASK-001
**Files likely touched:**
- `api/stats.js`
**Estimated scope:** Small: 1-2 files

### TASK-003: Create `api/search.js` to query the search API
**Description:** Create a serverless function that accepts a `q` parameter and fetches matching skills from `skills.sh`.
**Acceptance criteria:**
- [ ] The endpoint `/api/search?q=query` returns an array of skills.
- [ ] Handles empty queries gracefully.
**Verification:**
- [ ] Manual check: Hit `/api/search?q=react` and verify skill list.
**Dependencies:** TASK-001
**Files likely touched:**
- `api/search.js`
**Estimated scope:** Small: 1-2 files

### TASK-004: Create `api/skill-details.js` to fetch specific `SKILL.md` contents
**Description:** Create a serverless function that accepts a skill source and name, fetching the full `SKILL.md` content from the API.
**Acceptance criteria:**
- [ ] The endpoint `/api/skill-details?source=x&skill=y` returns the raw markdown.
**Verification:**
- [ ] Manual check: Hit `/api/skill-details?source=vercel-labs&skill=agent-skills` and verify markdown text.
**Dependencies:** TASK-001
**Files likely touched:**
- `api/skill-details.js`
**Estimated scope:** Small: 1-2 files

### TASK-005: Update the Home page to display the live global skill counter
**Description:** Update the frontend UI to fetch data from `/api/stats` and display a live skill counter.
**Acceptance criteria:**
- [ ] Counter shows global skills dynamically instead of static number.
**Verification:**
- [ ] Manual check: View UI and confirm number matches the API.
**Dependencies:** TASK-002
**Files likely touched:**
- `apps/web-app/index.html`
- `apps/web-app/main.js`
**Estimated scope:** Medium: 3-5 files

### TASK-006: Implement the dynamic search bar and result list
**Description:** Build the UI for searching and displaying skill cards using the `/api/search` endpoint.
**Acceptance criteria:**
- [ ] User can type and see results populating.
- [ ] Results show install count and author.
**Verification:**
- [ ] Manual check: Search for a skill and verify UI response.
**Dependencies:** TASK-003, TASK-005
**Files likely touched:**
- `apps/web-app/index.html`
- `apps/web-app/main.js`
**Estimated scope:** Medium: 3-5 files

### TASK-007: Implement the Skill Details modal with Markdown rendering and copy command
**Description:** When clicking a skill card, open a modal that fetches the full `SKILL.md` using `/api/skill-details` and renders it, showing a copy install command button.
**Acceptance criteria:**
- [ ] Modal opens quickly.
- [ ] Markdown is rendered safely and beautifully.
- [ ] Copy button copies `npx skills add <source>/<skill>` to clipboard.
**Verification:**
- [ ] Manual check: Open a skill, read docs, and click copy.
**Dependencies:** TASK-004, TASK-006
**Files likely touched:**
- `apps/web-app/index.html`
- `apps/web-app/main.js`
**Estimated scope:** Large: 5+ files

## 6. Risks and Assumptions
| ID | Risk / Assumption | Impact | Mitigation / Note |
|----|-------------------|--------|-------------------|
| RISK-001 | Vercel OIDC limits | Low | Verify rate limits on the free tier |
| ASM-001  | `skills.sh` API structure | - | Assuming the API endpoints exactly match the provided documentation. |

## 7. Open Questions
- هل تفضل أن نقوم بترقية تطبيقك الحالي المبني على Vite ليكون تطبيق Next.js لسهولة التعامل مع الـ APIs الخاصة بـ Vercel؟ أم نُبقيه كما هو ونضيف فقط مجلد الـ `api/` كما خططنا أعلاه؟

## 8. Rollback Plan
- Delete the `api/` folder and revert `apps/web-app/index.html` to the previous commit.
