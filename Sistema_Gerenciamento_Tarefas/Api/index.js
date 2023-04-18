const express = require('express');


const app = express();

app.get('/', (req, res) => {
  res.send('Olá do microserviço de API!');
});

app.listen(8080, () => {
  console.log('Aplicativo ouvindo na porta 8080');
});
