const { getVercelOidcToken } = require('@vercel/oidc');

module.exports = async (req, res) => {
  const query = req.query.q || '';
  if (!query) {
    return res.status(200).json({ skills: [] });
  }

  try {
    const token = await getVercelOidcToken();
    // Search skills endpoint
    const response = await fetch(`https://skills.sh/api/v1/skills/search?q=${encodeURIComponent(query)}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`skills.sh API error: ${response.statusText}`);
    }

    const data = await response.json();

    let skillsArray = [];
    if (Array.isArray(data)) {
      skillsArray = data;
    } else if (data) {
      skillsArray = data.skills || data.items || data.data || [];
    }

    res.status(200).json({ 
      skills: skillsArray,
      debug_raw: data
    });
  } catch (error) {
    console.error('Search fetch error:', error);
    res.status(500).json({ error: error.message, stack: error.stack });
  }
};
