export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-container">
        <div className="footer-left">
          <div className="footer-logo">
            <i className="fa-solid fa-palette"></i> Abo Alrejal Skills
          </div>
          <p>Curating modular agentic skills and prompt protocols for AI workflows.</p>
        </div>
        <div className="footer-right">
          <p className="copyright">&copy; 2026 Mohammed Abo Alrejal. Released under the MIT License.</p>
          <div className="footer-actions-row">
            <button className="footer-link-btn">
              <i className="fa-solid fa-terminal"></i> CLI Setup Guide
            </button>
          </div>
          <div className="social-icons">
            <a href="https://github.com/aboalrejal-ai" target="_blank" rel="noreferrer" aria-label="GitHub Profile">
              <i className="fa-brands fa-github"></i>
            </a>
            <a href="mailto:mohammed.abualrejal@gmail.com" aria-label="Contact Email">
              <i className="fa-solid fa-envelope"></i>
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
