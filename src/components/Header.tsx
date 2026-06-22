'use client';

export default function Header() {
  const toggleTheme = () => {
    const isLight = document.body.classList.contains('light-mode');
    if (isLight) {
      document.body.classList.replace('light-mode', 'dark-mode');
    } else {
      document.body.classList.replace('dark-mode', 'light-mode');
    }
  };

  return (
    <header className="site-header">
      <div className="header-container">
        <div className="logo-area" onClick={() => window.location.reload()}>
          <div className="logo-icon">
            <i className="fa-solid fa-brain"></i>
            <span className="status-dot" id="status-dot"></span>
          </div>
          <div className="logo-text">
            <h1>Abo Alrejal Skills</h1>
            <span>High-Performance AI Specs</span>
          </div>
        </div>

        <nav className="nav-links">
          <span className="curator-tag">
            <i className="fa-solid fa-user-check"></i> Curated by <strong>Mohammed Abo Alrejal</strong>
          </span>
          <a href="https://github.com/aboalrejal-ai/skills" target="_blank" rel="noreferrer" className="btn btn-outline btn-sm">
            <i className="fa-brands fa-github"></i> Star on GitHub
          </a>
          <button id="theme-toggle" className="theme-btn" aria-label="Toggle Theme" onClick={toggleTheme}>
            <i className="fa-solid fa-circle-half-stroke"></i>
          </button>
        </nav>
      </div>
    </header>
  );
}
