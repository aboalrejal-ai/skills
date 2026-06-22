# Phase 1: Data Model

## Entities

### `Skill`
Represents an agent capability fetched from the `skills.sh` API.
- **Fields**:
  - `id` (string): Unique identifier (e.g. `vercel-labs/skills/find-skills`)
  - `slug` (string): URL slug
  - `name` (string): Human-readable name
  - `source` (string): Repository owner/name
  - `installs` (number): Install count
  - `installUrl` (string): GitHub URL
  - `url` (string): skills.sh page URL
- **Relationships**: None

### `SearchState`
Represents the frontend state for the search feature.
- **Fields**:
  - `query` (string): The search input
  - `source` (enum: `'default'`, `'skills.sh'`): The selected data source
  - `results` (`Skill[]`): The fetched results
  - `isLoading` (boolean): Fetching state
  - `error` (string | null): Any error messages
