import { useState } from 'react';

// Dummy data — will be replaced by real backend data later
const dummyDocuments = [
  { id: 1, name: 'CNC_Machine_Manual.pdf', type: 'Manual', date: '12-06-2026' },
  { id: 2, name: 'Maintenance_Log_Q1_2026.pdf', type: 'Maintenance Log', date: '14-03-2026' },
  { id: 3, name: 'Safety_Procedure_SOP.pdf', type: 'SOP', date: '01-02-2026' },
  { id: 4, name: 'Compressor_Inspection_Report.pdf', type: 'Inspection Report', date: '20-05-2026' },
  { id: 5, name: 'Incident_Report_E202.pdf', type: 'Incident Report', date: '10-06-2026' },
];

const dummyTopTopics = [
  { topic: 'Compressor pressure issues', count: 23 },
  { topic: 'Coolant refill procedure', count: 17 },
  { topic: 'Spindle alignment steps', count: 12 },
  { topic: 'Emergency stop protocol', count: 9 },
];

const dummyGaps = [
  'No SOP found for "hydraulic pump noise"',
  'No SOP found for "conveyor belt slippage"',
];

function Dashboard() {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterType, setFilterType] = useState('All');

  const documentTypes = ['All', 'Manual', 'SOP', 'Maintenance Log', 'Inspection Report', 'Incident Report'];

  const filteredDocs = dummyDocuments.filter((doc) => {
    const matchesSearch = doc.name.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesFilter = filterType === 'All' || doc.type === filterType;
    return matchesSearch && matchesFilter;
  });

  return (
    <div className="dashboard">
      {/* Search + Filter Bar */}
      <div className="dashboard-controls">
        <input
          type="text"
          placeholder="Search documents..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        <select
          value={filterType}
          onChange={(e) => setFilterType(e.target.value)}
          className="filter-select"
        >
          {documentTypes.map((type) => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
      </div>

      {/* Document List */}
      <div className="document-list">
        <h3>Knowledge Base ({filteredDocs.length} documents)</h3>
        {filteredDocs.length === 0 ? (
          <p className="empty-state">No documents match your search.</p>
        ) : (
          filteredDocs.map((doc) => (
            <div key={doc.id} className="document-card">
              <span className="doc-icon">📄</span>
              <div className="doc-info">
                <span className="doc-name">{doc.name}</span>
                <span className="doc-meta">{doc.type} · {doc.date}</span>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Analytics Panel */}
      <div className="analytics-panel">
        <div className="analytics-card">
          <h4>Top Searched Topics</h4>
          {dummyTopTopics.map((item, idx) => (
            <div key={idx} className="analytics-row">
              <span>{item.topic}</span>
              <span className="analytics-count">{item.count}</span>
            </div>
          ))}
        </div>

        <div className="analytics-card">
          <h4>Documentation Gaps</h4>
          {dummyGaps.map((gap, idx) => (
            <div key={idx} className="gap-row">⚠️ {gap}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;