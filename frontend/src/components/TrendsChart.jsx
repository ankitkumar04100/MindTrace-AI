import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

const data = [
  { day: "Mon", stress: 30 },
  { day: "Tue", stress: 40 },
  { day: "Wed", stress: 55 },
  { day: "Thu", stress: 60 },
  { day: "Fri", stress: 70 },
];

function TrendsChart() {
  return (
    <div>
      <h4>Weekly Stress Trend</h4>
      <LineChart width={300} height={200} data={data}>
        <XAxis dataKey="day" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="stress" />
      </LineChart>
    </div>
  );
}

export default TrendsChart;
