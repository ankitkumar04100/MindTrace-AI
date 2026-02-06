import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const submitAssessment = (data) =>
  API.post("/assessment/submit", data);

export const getInsights = (score) =>
  API.get(`/insights/result?score=${score}`);
