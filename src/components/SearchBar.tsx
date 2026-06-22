import { ChangeEvent } from 'react';

type SearchBarProps = {
  query: string;
  setQuery: (q: string) => void;
  source: string;
  setSource: (s: string) => void;
  onSearch: () => void;
  totalCount: number;
};

export default function SearchBar({ query, setQuery, source, setSource, onSearch, totalCount }: SearchBarProps) {
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      onSearch();
    }
  };

  return (
    <section className="hero-section">
      <div className="hero-badge">
        <span className="pulse-dot"></span> Open Source Visual Intelligence Catalog
      </div>
      <h2>Modular Agentic Skills <br /><span className="highlight">Tailored for AI Coding</span></h2>
      <p className="hero-desc">
        Explore and fetch <strong>{totalCount}+ production-grade modular skills</strong> for Claude Code, Cursor, Antigravity, and Gemini.
      </p>

      <div className="filter-box">
        <div className="search-wrapper" style={{ display: 'flex', alignItems: 'center', position: 'relative' }}>
          <i className="fa-solid fa-magnifying-glass search-icon" style={{ position: 'absolute', left: '16px' }}></i>
          <input
            type="text"
            className="search-input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search skills, triggers, platforms..."
            style={{ paddingLeft: '48px', paddingRight: '140px', width: '100%' }}
          />
          <select
            className="search-source-select"
            value={source}
            onChange={(e) => setSource(e.target.value)}
            style={{ position: 'absolute', right: '16px', top: '50%', transform: 'translateY(-50%)', maxWidth: '140px' }}
          >
            <option value="default">Default</option>
            <option value="skills.sh">skills.sh</option>
          </select>
        </div>
      </div>
      <div className="stats-row" style={{ marginTop: '24px' }}>
        <div className="stat-pill"><i className="fa-solid fa-folder-open"></i> <span>{totalCount}</span> Skills</div>
        <div className="stat-pill"><i className="fa-solid fa-code"></i> Offline Ready</div>
      </div>
    </section>
  );
}
