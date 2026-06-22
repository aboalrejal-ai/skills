# Implementation Plan: Fix Skills App UI and API Integration

**Branch**: `001-skills-fix` | **Date**: 2026-06-22 | **Spec**: [spec.md](file:///c:/Users/Abo%20Alrejal/Desktop/skills/specs/001-skills-fix/spec.md)
**Input**: Feature specification from `/specs/001-skills-fix/spec.md`

## Summary

Migrate the static HTML site to Next.js (React) to securely proxy API requests to the `skills.sh` API using OIDC authentication, fix the overlapping search UI components, properly rename the source dropdown labels, and wrap the entire application in a Docker container for consistent deployment, all while retaining the exact premium design aesthetics.

## Technical Context

**Language/Version**: TypeScript / Node.js 20+  
**Primary Dependencies**: Next.js (App Router), React 18, @vercel/oidc  
**Storage**: N/A  
**Testing**: Jest / React Testing Library  
**Target Platform**: Docker container / Node environment
**Project Type**: Next.js Web Application  
**Performance Goals**: <2s response time for API searches  
**Constraints**: Keep existing CSS design pixel-perfect; hide API token on backend.  
**Scale/Scope**: Replace `index.html` with Next.js architecture; 1 main search page.

## Constitution Check

*GATE: Passed*
- **Test-First**: Will write component tests for the search bar and dropdown.
- **Simplicity**: Next.js App Router provides the simplest way to add backend proxy routes to a React app without setting up a completely separate Express server.

## Project Structure

### Documentation (this feature)

```text
specs/001-skills-fix/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (generated later)
```

### Source Code (repository root)

```text
# Next.js Application
./
├── src/
│   ├── app/
│   │   ├── api/skills/search/route.ts
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── SearchBar.tsx
│   │   ├── SkillsGrid.tsx
│   │   └── Header.tsx
│   └── styles/
│       └── globals.css
├── public/
├── Dockerfile
├── package.json
└── next.config.mjs
```

**Structure Decision**: A standard Next.js App Router structure will be used. The existing HTML will be broken into React components under `src/components/`, the CSS will go to `src/styles/globals.css`, and the backend API proxy will be at `src/app/api/skills/search/route.ts`. A Dockerfile will be added at the root.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
