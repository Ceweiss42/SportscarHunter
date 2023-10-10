const express = require('express');
const fetch = require('node-fetch');
const app = express();
const port = 3000;

app.get('/proxyImage', async (req, res) => {
    const imageUrl = req.query.url;
    try {
        const response = await fetch(imageUrl);
        const buffer = await response.buffer();
        res.writeHead(200, { 'Content-Type': response.headers.get('content-type') });
        res.end(buffer, 'binary');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching image');
    }
});

app.listen(port, () => {
    console.log(`Proxy server is running on port ${port}`);
});

