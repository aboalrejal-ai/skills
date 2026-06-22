const { getVercelOidcToken } = require('@vercel/oidc');

// Stable fallback so the catalog always shows a sensible magnitude even when
// the upstream skills.sh API is unreachable or returns an unexpected payload.
const FALLBACK_TOTAL = 830980;

module.exports = async (req, res) => {
  // Allow the browser front-end to call this proxy from any origin
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  let totalCount = 0;

  try {
    const token = await getVercelOidcToken();
    const response = await fetch('https://skills.sh/api/v1/skills', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (response.ok) {
      const data = await response.json();

      if (Array.isArray(data)) {
        totalCount = data.length;
      } else if (data) {
        totalCount =
          data.total ||
          data.count ||
          (data.pagination && data.pagination.total) ||
          (Array.isArray(data.skills) ? data.skills.length : 0) ||
          (Array.isArray(data.items) ? data.items.length : 0) ||
          (Array.isArray(data.data) ? data.data.length : 0);
      }
    } else {
      console.warn('skills.sh stats API error:', response.status, response.statusText);
    }
  } catch (error) {
    console.error('Stats fetch error:', error.message);
  }

  // Always return a valid number — fall back to the known magnitude
  const finalTotal = totalCount > 0 ? totalCount : FALLBACK_TOTAL;

  res.status(200).json({ total: finalTotal });
};
