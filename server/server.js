const express = require('express')

const app = express()
app.use(express.json())

app.get('/', (req, res) => {
  console.log('get')
  res.send('Hello World!1')
})

app.post('/', (req, res) => {
  console.log('post', req.body, req.params)
  res.send('Hello World!1')
})

app.listen(3000, () => {
  console.log(`Example app listening on port ${3000}`)
})
