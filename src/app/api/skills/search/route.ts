import { NextResponse } from 'next/server';
import { getVercelOidcToken } from '@vercel/oidc';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get('q') || '';

  try {
    let token;
    try {
      token = await getVercelOidcToken();
    } catch (e) {
      token = process.env.VERCEL_OIDC_TOKEN;
      if (!token) {
        console.error("No OIDC token available.");
        return NextResponse.json({ error: 'Authentication failed: No Token' }, { status: 401 });
      }
    }

    const apiUrl = `https://skills.sh/api/v1/skills/search?q=${encodeURIComponent(q)}`;
    
    const res = await fetch(apiUrl, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!res.ok) {
      return NextResponse.json({ error: 'Failed to fetch from skills.sh' }, { status: res.status });
    }

    const data = await res.json();
    return NextResponse.json(data);
  } catch (err) {
    console.error("Proxy error", err);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
