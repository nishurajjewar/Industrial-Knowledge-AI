const express = require('express');
const cors = require('cors');
const multer = require('multer');
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json());

const upload = multer({ dest: 'uploads/' });
const AI_SERVICE_URL = 'http://localhost:8000';

app.get('/', (req, res) => {
  res.json({ message: 'Node backend is running' });
});

// Route 1: Upload document -> forward to Python AI service
app.post('/upload', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    const formData = new FormData();
    formData.append('file', fs.createReadStream(req.file.path), req.file.originalname);

    const response = await axios.post(`${AI_SERVICE_URL}/upload`, formData, {
      headers: formData.getHeaders(),
    });

    fs.unlink(req.file.path, () => {});
    res.json(response.data);
  } catch (error) {
    console.error('Upload error:', error.message);
    res.status(500).json({ error: 'Failed to process upload', details: error.message });
  }
});

// Route 2: Query -> forwards to Person A's /chat endpoint
// Person A's /chat expects { "question": "string" } and returns a plain string answer
app.post('/query', async (req, res) => {
  try {
    const { question } = req.body;

    if (!question) {
      return res.status(400).json({ error: 'Question is required' });
    }

    const response = await axios.post(`${AI_SERVICE_URL}/chat`, { question });

    // Person A's /chat currently returns a plain string (no citations yet)
    // Normalize it into the shape our frontend expects: { answer, citations }
    const rawAnswer = typeof response.data === 'string' ? response.data : response.data.answer;

    res.json({
      answer: rawAnswer || 'No answer received.',
      citations: response.data.citations || [],
    });
  } catch (error) {
    console.error('Query error:', error.message);
    res.status(500).json({ error: 'Failed to get answer', details: error.message });
  }
});

// Route 3: Summarize -> forward to Python AI service for document summary
app.post('/summarize', async (req, res) => {
  try {
    const { documentName } = req.body;

    if (!documentName) {
      return res.status(400).json({ error: 'documentName is required' });
    }

    const response = await axios.post(`${AI_SERVICE_URL}/summarize`, { documentName });
    res.json(response.data);
  } catch (error) {
    console.error('Summarize error:', error.message);
    res.status(500).json({ error: 'Failed to summarize document', details: error.message });
  }
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Node backend running on http://localhost:${PORT}`);
});