import React, { useState } from 'react';
import type { ChangeEvent, FormEvent } from 'react';
import './App.css';

const App: React.FC = () => {
  const [fileName, setFileName] = useState<string | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string | null>(null);
  const [uploading, setUploading] = useState(false);

  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [fileUploaded, setFileUploaded] = useState(false);

  const handleFileChange = async (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file || file.type !== "application/pdf") {
      alert("Please upload a valid PDF file.");
      return;
    }

    setFileName(file.name);
    const formData = new FormData();
    formData.append('file', file);
    setUploading(true);
    setUploadStatus(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (response.ok) {
        setUploadStatus(`✅ File uploaded successfully. You can now ask your questions.`);
        setFileUploaded(true);
      } else {
        setUploadStatus(`❌ Upload failed: ${data.detail || 'Unknown error'}`);
        setFileUploaded(false);
      }
    } catch (error) {
      setUploadStatus('❌ Upload error: ' + (error as Error).message);
      setFileUploaded(false);
    } finally {
      setUploading(false);
    }
  };

  const handleQuestionSubmit = async (e: FormEvent) => {
  e.preventDefault();
  if (!question.trim()) return;

  setAnswer('🧠 Thinking...');

  const formData = new FormData();
  formData.append('question', question);

  try {
    const response = await fetch('http://127.0.0.1:8000/ask/', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    setAnswer(data.answer || 'No answer returned.');
  } catch (error) {
    setAnswer('❌ Error retrieving answer. Please try again.');
  }
};


 return (
    <div className="app-container">
      <h1 className="title">AskMyDoc</h1>
      <p className="subtitle">Upload a PDF and ask any question about its content.</p>

      <div style={{ textAlign: 'center' }}>
        <label htmlFor="file-upload" className="upload-label">
          📎 Upload PDF
          <input
            id="file-upload"
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            hidden
          />
        </label>
      </div>

      {fileName && <p className="file-name">📄 {fileName}</p>}

      {uploading && <div className="chat-bubble system">⏳ Uploading file...</div>}
      {uploadStatus && (
        <div className={`chat-bubble ${fileUploaded ? 'success' : 'error'}`}>
          {uploadStatus}
        </div>
      )}

      {fileUploaded && (
        <form className="question-form" onSubmit={handleQuestionSubmit}>
          <input
            type="text"
            placeholder="Ask a question about the PDF..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className="question-input"
            required
          />
          <button type="submit" className="ask-button">Ask</button>
        </form>
      )}

      {answer && (
        <div className="chat-bubble answer">
          <strong>Answer:</strong> {answer}
        </div>
      )}
    </div>
  );


};

export default App;
