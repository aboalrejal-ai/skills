import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get('q')?.toLowerCase() || '';

  try {
    const indexPath = path.join(process.cwd(), 'skills_index.json');
    if (!fs.existsSync(indexPath)) {
      return NextResponse.json({ data: [] });
    }

    const fileContent = fs.readFileSync(indexPath, 'utf-8');
    const skills = JSON.parse(fileContent);

    let filtered = skills;
    if (q) {
      filtered = skills.filter((s: any) => 
        (s.name && s.name.toLowerCase().includes(q)) ||
        (s.description && s.description.toLowerCase().includes(q)) ||
        (s.category && s.category.toLowerCase().includes(q))
      );
    } else {
      // If no query, return first 50 to avoid massive payload
      filtered = skills.slice(0, 50);
    }

    const normalized = filtered.map((skill: any) => ({
      id: skill.id || skill.slug || skill.name || skill.path || 'unknown',
      name: skill.name || skill.title || (skill.id ? String(skill.id).split('/').pop() : 'Skill'),
      category: skill.category || skill.group || skill.namespace || 'global-catalog',
      description: skill.description || skill.summary || skill.tagline || 'Modular agentic skill.',
      risk: skill.risk || 'unknown',
      source: skill.source || 'local',
      installs: skill.installs || 0,
      url: skill.url || `https://github.com/aboalrejal-ai/skills/tree/main/${skill.path || ''}`
    }));

    return NextResponse.json({ data: normalized, totalCount: skills.length });
  } catch (err) {
    console.error("Local search error", err);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
