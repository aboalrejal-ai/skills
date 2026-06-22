# Tasks: Fix Skills App UI and API Integration

**Input**: Design documents from `/specs/001-skills-fix/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/skills-api.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Next.js App Router project with TypeScript in the repository root.
- [x] T002 Install `@vercel/oidc` dependency for the API proxy.
- [x] T003 [P] Create `Dockerfile` at repository root for containerization.
- [x] T004 [P] Clear out default Next.js boilerplate from `src/app/page.tsx` and `src/app/layout.tsx`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Extract CSS from `index.html` and move it to `src/styles/globals.css` to maintain exact design.
- [x] T006 Copy existing `index.html` layout structure into the root `src/app/layout.tsx`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Fix UI Layout for Search and Dropdown (Priority: P1) 🎯 MVP

**Goal**: Extract the HTML into React components and fix the overlapping UI issue between the search bar and the source dropdown.

**Independent Test**: Can be visually tested by loading `http://localhost:3000` and ensuring the search bar and dropdown don't overlap, and the dropdown options are "Default" and "skills.sh".

### Implementation for User Story 1

- [x] T007 [P] [US1] Create `src/components/Header.tsx` to handle the top navigation and logo.
- [x] T008 [P] [US1] Create `src/components/SearchBar.tsx` to handle the search input and source dropdown UI correctly without overlap.
- [x] T009 [P] [US1] Create `src/components/SkillsGrid.tsx` for displaying empty state / default skills.
- [x] T010 [US1] Assemble `Header.tsx`, `SearchBar.tsx`, and `SkillsGrid.tsx` inside `src/app/page.tsx`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Integrate skills.sh API Correctly (Priority: P1)

**Goal**: Fetch real search results from the official skills.sh API when the user types a query.

**Independent Test**: Select "skills.sh" in the dropdown, type "React", and verify results are rendered on screen from the API without CORS or authentication errors.

### Implementation for User Story 2

- [x] T011 [P] [US2] Create API Proxy Endpoint at `src/app/api/skills/search/route.ts` using `@vercel/oidc` for authentication.
- [x] T012 [US2] Update `SearchBar.tsx` to manage local React state (`query`, `source`, `isLoading`, `results`).
- [x] T013 [US2] Add the `fetch()` logic inside a React `useEffect` or form submit handler in the client component to hit `/api/skills/search`.
- [x] T014 [US2] Update `SkillsGrid.tsx` to accept the fetched `results` array and dynamically render the skill cards.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T015 Verify the Docker container builds and runs successfully (`docker build -t skills-app . && docker run -p 3000:3000 skills-app`).
- [x] T016 Remove the legacy `index.html` file from the root directory.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - US1 and US2 can proceed sequentially in priority order (US1 then US2).
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Integrates with the components built in US1.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (Dockerfile creation, clearing boilerplate).
- Components in US1 (`Header.tsx`, `SearchBar.tsx`, `SkillsGrid.tsx`) marked [P] can be built in parallel.
- API Route creation (T011) can run in parallel with Frontend State management (T012).

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently to ensure the layout is fixed.

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (UI Fixed)
3. Add User Story 2 → Test independently → Deploy/Demo (API functional)
4. Dockerize and Polish → Final Delivery.
