function StressScore({ score }) {
  const percent = Math.round(score * 100);

  return (
    <div>
      <h4>Stress Score</h4>
      <div
        style={{
          width: "200px",
          height: "20px",
          background: "#eee",
          borderRadius: "10px",
        }}
      >
        <div
          style={{
            width: `${percent}%`,
            height: "100%",
            background: percent > 70 ? "red" : percent > 40 ? "orange" : "green",
            borderRadius: "10px",
          }}
        />
      </div>
      <p>{percent}%</p>
    </div>
  );
}

export default StressScore;
