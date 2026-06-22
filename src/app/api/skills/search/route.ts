import { NextResponse } from 'next/server';
import { getVercelOidcToken } from '@vercel/oidc';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get('q') || '';

  try {
    let token = process.env.VERCEL_OIDC_TOKEN || '';
    try {
      const generated = await getVercelOidcToken();
      if (generated) token = generated;
    } catch (e) {
      console.log("No Vercel OIDC token generated, proceeding without token or using env fallback.");
    }

    const apiUrl = `https://skills.sh/api/v1/skills/search?q=${encodeURIComponent(q)}`;
    
    const headers: Record<string, string> = {};
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const res = await fetch(apiUrl, { headers });

    if (!res.ok) {
      return NextResponse.json({ error: 'Failed to fetch from skills.sh' }, { status: res.status });
    }

    const data = await res.json();
    
    let skillsArray = [];
    if (Array.isArray(data)) {
      skillsArray = data;
    } else if (data) {
      skillsArray = data.skills || data.items || data.data || data.results || [];
    }

    const normalized = skillsArray.map((skill: any) => ({
      id: skill.id || skill.slug || skill.name || skill.path || 'unknown',
      name: skill.name || skill.title || (skill.id ? String(skill.id).split('/').pop() : 'Skill'),
      category: skill.category || skill.group || skill.namespace || 'global-catalog',
      description: skill.description || skill.summary || skill.tagline || 'Modular agentic skill.',
      risk: skill.risk || 'unknown',
      source: skill.source || 'skills.sh',
      installs: skill.installs || 0,
      url: skill.url || `https://skills.sh/skill/${skill.id || skill.slug || ''}`
    }));

    return NextResponse.json({ data: normalized });
  } catch (err) {
    console.error("Proxy error", err);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
