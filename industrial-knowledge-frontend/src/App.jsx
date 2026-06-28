import { useState } from 'react';
import UploadPanel from './components/UploadPanel';
import ChatWindow from './components/ChatWindow';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('chat');

  const handleUpload = (file) => {
    console.log('File selected:', file.name);
    // Day 2: send this file to Person B's backend
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Industrial Knowledge Intelligence</h1>
        <p>Unified Asset &amp; Operations Brain</p>
      </header>

      <nav className="tab-nav">
        <button
          className={activeTab === 'chat' ? 'tab-btn active' : 'tab-btn'}
          onClick={() => setActiveTab('chat')}
        >
          Knowledge Copilot
        </button>
        <button
          className={activeTab === 'dashboard' ? 'tab-btn active' : 'tab-btn'}
          onClick={() => setActiveTab('dashboard')}
        >
          Dashboard
        </button>
      </nav>

      <main className="app-main">
        {activeTab === 'chat' ? (
          <>
            <UploadPanel onUpload={handleUpload} />
            <ChatWindow />
          </>
        ) : (
          <Dashboard />
        )}
      </main>
    </div>
  );
}

export default App;