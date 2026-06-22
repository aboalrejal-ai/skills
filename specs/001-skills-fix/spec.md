# Feature Specification: Fix Skills App UI and API Integration

**Feature Branch**: `001-skills-fix`  
**Created**: 2026-06-22  
**Status**: Draft  

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Fix UI Layout for Search and Dropdown (Priority: P1)

Users should be able to clearly see and use the search bar and the source dropdown (default/skill.sh) without them overlapping or breaking the design. The dropdown should say "Default" instead of "Default: local" and "skills.sh" instead of having "local/global" terminology that confuses the design.

**Why this priority**: The broken UI is the first thing users see and prevents them from interacting with the app correctly.

**Independent Test**: Can be visually tested by loading the page and ensuring the search bar and dropdown don't overlap, and the dropdown options are correctly named.

**Acceptance Scenarios**:

1. **Given** the app is loaded, **When** the user views the search area, **Then** the search input and dropdown are visually separated and styled according to the brand theme.
2. **Given** the app is loaded, **When** the user opens the search source dropdown, **Then** the options are simply "Default" and "skills.sh".

---

### User Story 2 - Integrate skills.sh API Correctly (Priority: P1)

Users should be able to select "skills.sh" from the dropdown, type a query, and see real search results fetched from the official skills.sh API.

**Why this priority**: The app currently does not show any results when searching via skills.sh, making the primary feature of the site unusable.

**Independent Test**: Can be tested by selecting "skills.sh" in the dropdown, typing "React", and verifying that results are rendered on the screen from the API.

**Acceptance Scenarios**:

1. **Given** the user has selected "skills.sh" as the source, **When** they type a search query, **Then** a request is made to the skills.sh API.
2. **Given** a successful response from the skills.sh API, **When** the data is returned, **Then** it is rendered correctly in the UI grid.

---

### User Story 3 - Architectural Review and Update (Priority: P2)

The application should be able to securely query the API. Currently, it's a static HTML file which cannot securely hold or rotate the necessary authentication tokens required by the skills.sh API.

**Why this priority**: A backend or meta-framework is needed to securely proxy the requests and inject the required OIDC token for skills.sh API.

**Independent Test**: Can be tested by verifying that the app successfully proxies API requests through a secure server-side route.

**Acceptance Scenarios**:

1. **Given** the new architecture, **When** the frontend makes a search request to skills.sh, **Then** the backend attaches the necessary authentication token and forwards the request.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST render the search bar and dropdown without visual overlap.
- **FR-002**: System MUST label the default data source as "Default" and the remote one as "skills.sh", removing "local" and "global" labels.
- **FR-003**: System MUST fetch data from the remote API endpoint when "skills.sh" is selected.
- **FR-004**: System MUST handle authentication/OIDC token generation or proxying securely to access the API.
- **FR-005**: System MUST migrate the application to Next.js (React) to securely proxy API requests and manage state, and the entire application MUST be containerized with Docker for consistent deployment, while maintaining the exact existing UI design and CSS.
- **FR-006**: System MUST display the results from skills.sh matching the existing UI card design.

### Key Entities

- **Skill**: Represents an agent capability, containing id, slug, name, source, installs, installUrl.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: UI components no longer overlap and are visually distinct.
- **SC-002**: Selecting skills.sh and searching returns and renders results successfully.
- **SC-003**: No API CORS or authentication errors occur when fetching from skills.sh.

## Assumptions

- We assume the user has a Vercel project or can obtain the OIDC token if the API strictly requires it (as per the API docs). If the user does not want to use Vercel, we must determine if unauthenticated requests are allowed, or find an alternative auth method.
