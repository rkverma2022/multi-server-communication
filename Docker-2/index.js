const express = require('express');
const app = express();
const port = 3000;

app.get('/multiply', (req, res) => {
  const a = parseFloat(req.query.a);
  const b = parseFloat(req.query.b);

  if (isNaN(a) || isNaN(b)) {
    return res.status(400).json({ error: 'Please provide valid numbers for a and b' });
  }
 
  const result = a * b;
  res.json({ result });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
