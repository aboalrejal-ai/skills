# Phase 0: Research & Decisions

## Decision 1: Next.js Architecture vs Node Proxy
**Decision**: Migrate to Next.js App Router.
**Rationale**: The user wants to securely proxy the `skills.sh` API, which requires the `@vercel/oidc` token. The user also wants to fix UI layout issues. Converting the static HTML to React components in Next.js allows us to use API Routes (`src/app/api/...`) to securely inject the token server-side, while taking advantage of React's component state to manage the UI correctly and avoid overlapping elements.
**Alternatives considered**: Express.js backend serving the static HTML. Rejected because managing complex UI state (dropdowns, search loading states) in vanilla JS is more brittle than React.

## Decision 2: API Proxying Implementation
**Decision**: Create a Next.js API route `/api/skills/search`.
**Rationale**: The route will use `getVercelOidcToken()` (or environment variable fallback) to securely authenticate with `https://skills.sh/api/v1/skills/search`. The client frontend will never see the token.

## Decision 3: Dockerization
**Decision**: Use official Node.js Alpine image for Docker.
**Rationale**: Provides a lightweight, secure container environment for running Next.js in production.
