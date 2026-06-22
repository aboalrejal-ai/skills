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
  const [totalCount, setTotalCount] = useState<number | null>(null);

  useEffect(() => {
    const handler = setTimeout(() => {
      performSearch(query, source);
    }, 300);
    return () => clearTimeout(handler);
  }, [query, source]);

  const performSearch = async (q: string, s: string) => {
    setIsLoading(true);
    try {
      const apiUrl = s === 'skills.sh' ? `/api/skills/search?q=${encodeURIComponent(q)}` : `/api/skills/local?q=${encodeURIComponent(q)}`;
      const res = await fetch(apiUrl);
      if (res.ok) {
        const data = await res.json();
        setResults(data.data || []);
        if (s === 'default' && data.totalCount !== undefined) {
          setTotalCount(data.totalCount);
        }
      } else {
        setResults([]);
      }
    } catch (err) {
      console.error("Failed to fetch skills", err);
      setResults([]);
    } finally {
      setIsLoading(false);
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
          totalCount={totalCount || 3050}
        />
        <SkillsGrid skills={results} isLoading={isLoading} />
      </main>
      <Footer />
    </>
  );
}
