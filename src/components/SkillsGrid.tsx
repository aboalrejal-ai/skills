export type Skill = {
  id: string;
  slug: string;
  name: string;
  source: string;
  installs: number;
  sourceType: string;
  installUrl: string;
  url: string;
  description?: string;
  category?: string;
};

export default function SkillsGrid({ skills, isLoading }: { skills: Skill[], isLoading: boolean }) {
  if (isLoading) {
    return (
      <section>
        <h2 className="section-title"><i className="fa-solid fa-dna"></i> Loading <span>Skills</span>...</h2>
        <div className="brands-grid">
           {/* Loader placeholder */}
        </div>
      </section>
    );
  }

  return (
    <section>
      <h2 className="section-title"><i className="fa-solid fa-dna"></i> Browse <span>Skills</span></h2>
      <div className="brands-grid">
        {skills.map((skill) => (
          <div key={skill.id} className="skill-card">
            <div className="skill-card-glow"></div>
            <div className="skill-header">
              <div>
                <div className="skill-category">{skill.category || 'Skill'}</div>
                <div className="skill-title">{skill.name}</div>
              </div>
            </div>
            <div className="skill-desc">{skill.description || 'No description provided.'}</div>
            <div className="skill-meta">
              <span className="meta-tag"><i className="fa-solid fa-download"></i> {skill.installs}</span>
              <span className="meta-tag"><i className="fa-solid fa-code"></i> {skill.source}</span>
            </div>
            <div className="card-footer">
              <div className="skill-id-badge">{skill.id}</div>
              <div className="card-action-row">
                <a href={skill.url} target="_blank" rel="noreferrer" className="btn btn-outline btn-card-action btn-sm">
                  <i className="fa-solid fa-bolt"></i> View Details
                </a>
              </div>
            </div>
          </div>
        ))}
        {skills.length === 0 && (
          <p style={{ color: 'var(--text-secondary)' }}>No skills found for your query.</p>
        )}
      </div>
    </section>
  );
}
