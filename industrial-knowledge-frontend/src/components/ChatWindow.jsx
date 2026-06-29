import { useState } from 'react';

function ChatWindow() {
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hi! Upload a document and ask me any question about it.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: userMessage.text }),
      });

      if (!response.ok) {
        throw new Error('Backend returned an error');
      }

      const data = await response.json();

      const citationText = data.citations && data.citations.length > 0
        ? `Source: ${data.citations.map((c) => c.source).join(', ')}`
        : null;

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          text: data.answer || 'No answer received.',
          citation: citationText,
        },
      ]);
    } catch (error) {
      console.error('Query failed:', error);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          text: 'Could not reach the knowledge base right now. Please make sure the backend and AI service are running.',
        },
      ]);
    } finally {
      setLoading(false);
    }
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
        {loading && (
          <div className="chat-bubble assistant">
            <p>Thinking...</p>
          </div>
        )}
      </div>

      <div className="chat-input-row">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question here..."
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default ChatWindow;