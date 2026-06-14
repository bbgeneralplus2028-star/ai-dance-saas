import React, { useState } from "react";
import { generateVideo, getProjects } from "./api";

export default function App() {
  const [result, setResult] = useState(null);
  const [projects, setProjects] = useState([]);

  const [form, setForm] = useState({
    style: "hip hop",
    expression: "happy",
    background: "neon city",
    effects: ["rain"],
    camera: "orbit",
    aspect_ratio: "9:16"
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submit = async () => {
    const res = await generateVideo(form);
    setResult(res.data);
  };

  const loadProjects = async () => {
    const res = await getProjects();
    setProjects(res.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🎬 AI Dance SaaS</h1>

      <h3>Controls</h3>

      <input name="style" onChange={handleChange} placeholder="Style" />
      <input name="expression" onChange={handleChange} placeholder="Expression" />
      <input name="background" onChange={handleChange} placeholder="Background" />
      <input name="camera" onChange={handleChange} placeholder="Camera" />

      <br /><br />

      <button onClick={submit}>Generate Video</button>
      <button onClick={loadProjects}>Load Projects</button>

      {result && (
        <div>
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      <h3>Projects</h3>
      <pre>{JSON.stringify(projects, null, 2)}</pre>
    </div>
  );
}
