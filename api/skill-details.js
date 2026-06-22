const { getVercelOidcToken } = require('@vercel/oidc');

module.exports = async (req, res) => {
  const { source, skill } = req.query;

  if (!source || !skill) {
    return res.status(400).json({ error: 'Missing source or skill parameter' });
  }

  try {
    const token = await getVercelOidcToken();
    const response = await fetch(`https://skills.sh/api/v1/skills/${encodeURIComponent(source)}/${encodeURIComponent(skill)}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`skills.sh API error: ${response.statusText}`);
    }

    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    console.error('Skill details fetch error:', error);
    res.status(500).json({ error: error.message });
  }
};
