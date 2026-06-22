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

    let skillsArray = [];
    let totalCount = 0;

    if (Array.isArray(data)) {
      skillsArray = data;
      totalCount = data.length;
    } else if (data) {
      skillsArray = data.skills || data.items || data.data || [];
      totalCount = data.pagination?.total || data.total || skillsArray.length;
    }

    res.status(200).json({
      total: totalCount,
      skills: skillsArray.slice(0, 10),
      debug_raw: data
    });
  } catch (error) {
    res.status(500).json({ error: error.message, stack: error.stack });
  }
};
