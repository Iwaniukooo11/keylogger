const express = require('express')

const app = express()
app.use(express.json())

app.post('/', (req, res) => {
  console.log('recieved stolen data: ', req.body)
  res.status(201).json({
    status: 'OK',
  })
})

app.listen(3000, () => {
  console.log(`Example app listening on port ${3000}`)
})
