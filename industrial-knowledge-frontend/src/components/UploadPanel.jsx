import { useState } from 'react';

function UploadPanel({ onUpload }) {
  const [fileName, setFileName] = useState('');

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
      // Day 2: this will call Person B's backend /upload route
      if (onUpload) onUpload(file);
    }
  };

  return (
    <div className="upload-panel">
      <h3>Upload Document</h3>
      <p className="upload-hint">Upload a PDF, manual, SOP, or maintenance log</p>

      <label className="upload-box">
        <input
          type="file"
          accept=".pdf,.docx,.txt"
          onChange={handleFileChange}
          hidden
        />
        {fileName ? (
          <span>📄 {fileName}</span>
        ) : (
          <span>+ Click to upload</span>
        )}
      </label>
    </div>
  );
}

export default UploadPanel;