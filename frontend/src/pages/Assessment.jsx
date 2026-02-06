import { useState } from "react";
import { submitAssessment, getInsights } from "../services/api";
import Dashboard from "../components/Dashboard";

function Assessment() {
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await submitAssessment({
      response_time: 2.5,
      error_rate: 0.3,
      consistency: 0.7,
    });

    const score = response.data.stress_prediction;
    const insight = await getInsights(score);

    setResult({ score, insight: insight.data });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Cognitive Assessment</h2>
      <button onClick={handleSubmit}>Run Assessment</button>

      {result && <Dashboard data={result} />}
    </div>
  );
}

export default Assessment;
