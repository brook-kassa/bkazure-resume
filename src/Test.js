import React from 'react';

function Test() {
    return (
      <div>
        <h1>Hello, World!</h1>
        <p>Welcome to Brook's CRC</p>
        
        {/* Navigation Bar */}
        <div className="nav-buttons">
          <a href="#Skills" className="nav-button">Skills</a>
          <a href="#Certifications" className="nav-button">Certifications</a>
          <a href="#Coursework" className="nav-button">Coursework</a>
          <a href="#Education" className="nav-button">Education</a>
          <a href="#Experience" className="nav-button">Experience</a>
          <a href="#Extracurriculars" className="nav-button">Extracurriculars</a>
        </div>
      </div>
    );
}

export default Test;