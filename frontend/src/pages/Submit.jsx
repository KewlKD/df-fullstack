import React, { useState } from 'react';
import axios from 'axios';

function Submit() {
  const [form, setForm] = useState({ name: '', email: '' });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/submit', form);
      alert(res.data.message);
    } catch (err) {
      console.error(err);
      alert('Error submitting data');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Submit Info</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" onChange={handleChange} /><br />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} /><br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Submit;
