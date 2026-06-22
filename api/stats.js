const { getVercelOidcToken } = require('@vercel/oidc');

module.exports = async (req, res) => {
  try {
    const token = await getVercelOidcToken();
    const response = await fetch('https://skills.sh/api/v1/skills', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`skills.sh API error: ${response.statusText}`);
    }

    const data = await response.json();
    // The skills.sh API returns { skills: [], pagination: { total: X, ... } }
    res.status(200).json({
      total: data.pagination ? data.pagination.total : 0,
      skills: data.skills.slice(0, 10) // Return top 10 as trending
    });
  } catch (error) {
    console.error('Stats fetch error:', error);
    res.status(500).json({ error: error.message });
  }
};
