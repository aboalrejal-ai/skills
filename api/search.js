const { getVercelOidcToken } = require('@vercel/oidc');

module.exports = async (req, res) => {
  // Allow the browser front-end to call this proxy from any origin
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const query = (req.query.q || '').toString().trim();
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
      throw new Error(`skills.sh API error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();

    let skillsArray = [];
    if (Array.isArray(data)) {
      skillsArray = data;
    } else if (data) {
      skillsArray = data.skills || data.items || data.data || data.results || [];
    }

    // Normalize the shape so the front-end always sees {id, name, category, description, risk}
    const normalized = skillsArray.map(skill => ({
      id: skill.id || skill.slug || skill.name || skill.path || 'unknown',
      name: skill.name || skill.title || (skill.id ? String(skill.id).split('/').pop() : 'Skill'),
      category: skill.category || skill.group || skill.namespace || 'global-catalog',
      description: skill.description || skill.summary || skill.tagline || 'Modular agentic skill.',
      risk: skill.risk || 'unknown',
      source: skill.source || 'skills.sh'
    }));

    res.status(200).json({ skills: normalized });
  } catch (error) {
    console.error('Search fetch error:', error);
    // Return an empty (but valid) result set so the UI keeps working gracefully
    res.status(200).json({ skills: [], error: error.message });
  }
};
