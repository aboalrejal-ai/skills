'use client';

import { useState, useEffect } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import SearchBar from '@/components/SearchBar';
import SkillsGrid, { Skill } from '@/components/SkillsGrid';

export default function Home() {
  const [query, setQuery] = useState('');
  const [source, setSource] = useState('default');
  const [results, setResults] = useState<Skill[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const handler = setTimeout(() => {
      performSearch(query, source);
    }, 300);
    return () => clearTimeout(handler);
  }, [query, source]);

  const performSearch = async (q: string, s: string) => {
    if (s === 'skills.sh') {
      setIsLoading(true);
      try {
        const res = await fetch(`/api/skills/search?q=${encodeURIComponent(q)}`);
        if (res.ok) {
          const data = await res.json();
          setResults(data.data || []);
        } else {
          setResults([]);
        }
      } catch (err) {
        console.error("Failed to fetch skills", err);
        setResults([]);
      } finally {
        setIsLoading(false);
      }
    } else {
      setIsLoading(false);
      if (!q) {
        setResults([
          { id: 'vercel-labs/skills/find-skills', slug: 'find-skills', name: 'find-skills', source: 'vercel-labs/skills', installs: 24531, sourceType: 'github', installUrl: '', url: 'https://skills.sh', description: 'Find relevant skills for your AI agents' }
        ]);
      } else {
        setResults([]);
      }
    }
  };

  return (
    <>
      <Header />
      <main className="main-content">
        <SearchBar
          query={query}
          setQuery={setQuery}
          source={source}
          setSource={setSource}
          onSearch={() => performSearch(query, source)}
        />
        <SkillsGrid skills={results} isLoading={isLoading} />
      </main>
      <Footer />
    </>
  );
}
