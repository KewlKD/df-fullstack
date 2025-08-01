import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Submit from './pages/Submit';

function App() {
  return (
    <Router>
      <nav style={{ padding: '10px' }}>
        <Link to="/" style={{ marginRight: '10px', color: 'white' }}>Home</Link>
        <Link to="/submit"style={{ marginRight: '10px', color: 'white' }}>Submit</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/submit" element={<Submit />} />
      </Routes>
    </Router>
  );
}

export default App;
