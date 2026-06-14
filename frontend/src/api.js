import axios from "axios";

const API = "http://127.0.0.1:8000";

export const generateVideo = (data) =>
  axios.post(`${API}/generate`, data);

export const getProjects = () =>
  axios.get(`${API}/projects`);
