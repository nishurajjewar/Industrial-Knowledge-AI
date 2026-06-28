import { useState } from 'react';

function ChatWindow() {
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hi! Upload a document and ask me any question about it.' }
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    // Day 2: this will call Person B's backend /query route
    // For now, showing a dummy response so the UI can be tested
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          text: 'This is a dummy answer — the real RAG response will appear here on Day 2.',
          citation: 'Source: sample_manual.pdf, Page 4'
        }
      ]);
    }, 600);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') handleSend();
  };

  return (
    <div className="chat-window">
      <h3>Ask the Knowledge Copilot</h3>

      <div className="chat-messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`chat-bubble ${msg.role}`}>
            <p>{msg.text}</p>
            {msg.citation && <span className="citation">{msg.citation}</span>}
          </div>
        ))}
      </div>

      <div className="chat-input-row">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question here..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default ChatWindow;