# Internal API Contract

## GET `/api/skills/search`

Proxies the request to the `skills.sh` API, attaching the required Vercel OIDC token.

**Query Parameters**:
- `q` (string): The search query.

**Response**:
```json
{
  "data": [
    {
      "id": "vercel-labs/skills/find-skills",
      "slug": "find-skills",
      "name": "find-skills",
      "source": "vercel-labs/skills",
      "installs": 24531,
      "sourceType": "github",
      "installUrl": "https://github.com/vercel-labs/skills",
      "url": "https://skills.sh/vercel-labs/skills/find-skills"
    }
  ],
  "query": "find skills",
  "searchType": "semantic",
  "count": 1
}
```
