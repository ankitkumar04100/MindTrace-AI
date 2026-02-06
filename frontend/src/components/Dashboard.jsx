import StressScore from "./StressScore";
import TrendsChart from "./TrendsChart";

function Dashboard({ data }) {
  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Assessment Results</h3>
      <StressScore score={data.score} />
      <p><strong>Risk Level:</strong> {data.insight.risk_level}</p>
      <p><strong>Recommendation:</strong> {data.insight.recommendation}</p>
      <TrendsChart />
    </div>
  );
}

export default Dashboard;
