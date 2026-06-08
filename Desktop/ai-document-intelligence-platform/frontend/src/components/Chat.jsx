import { useState, useEffect } from "react";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const loadHistory = async () => {
    try {
      const response = await fetch(
        "/api/chat/history"
      );

      const data = await response.json();

      setHistory(data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const askQuestion = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "/api/chat/",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            question,
          }),
        }
      );

      const data =
        await response.json();

      setAnswer(data.answer);

      setQuestion("");

      await loadHistory();
    } catch (error) {
      console.error(error);

      setAnswer(
        "Something went wrong"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "50px auto",
        padding: "20px",
      }}
    >
      <h1>
        AI Document Intelligence Platform
      </h1>

      <input
        type="text"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        placeholder="Ask a question about your document..."
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "15px",
        }}
      />

      <button
        onClick={askQuestion}
        disabled={loading}
        style={{
          padding: "12px 20px",
          cursor: "pointer",
        }}
      >
        {loading
          ? "Thinking..."
          : "Ask"}
      </button>

      <div
        style={{
          marginTop: "25px",
          padding: "15px",
          border:
            "1px solid #ccc",
          borderRadius: "8px",
        }}
      >
        <h3>Latest Answer</h3>

        <p>{answer}</p>
      </div>

      <div
        style={{
          marginTop: "30px",
        }}
      >
        <h2>Chat History</h2>

        {history.length === 0 ? (
          <p>No chats yet</p>
        ) : (
          history.map((chat) => (
            <div
              key={chat.id}
              style={{
                border:
                  "1px solid #ddd",
                padding: "12px",
                marginBottom:
                  "10px",
                borderRadius:
                  "8px",
              }}
            >
              <strong>
                Question:
              </strong>

              <p>
                {chat.question}
              </p>

              <strong>
                Answer:
              </strong>

              <p>
                {chat.answer}
              </p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Chat;