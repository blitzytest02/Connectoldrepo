// ===================================
// IMPORTS - Load dependencies
// ===================================
// Import Express.js framework for creating the web server
const express = require('express');

// ===================================
// CONFIGURATION - App setup
// ===================================
// Initialize Express application instance
const app = express();

// Define the port number the server will listen on
const PORT = 3000;

// ===================================
// ROUTES - Endpoint definitions
// ===================================

// Root endpoint - returns "Hello world"
// This demonstrates the simplest Express.js route handler
// Accessible at: http://localhost:3000/
app.get('/', (req, res) => {
  res.send('Hello world');
});

// Evening endpoint - returns "Good evening"
// This demonstrates how to create multiple endpoints in Express.js
// Accessible at: http://localhost:3000/evening
app.get('/evening', (req, res) => {
  res.send('Good evening');
});

// ===================================
// SERVER STARTUP - Begin listening
// ===================================
// Start the server and listen for incoming HTTP requests on the specified port
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log(`Try: http://localhost:${PORT}/ for "Hello world"`);
  console.log(`Try: http://localhost:${PORT}/evening for "Good evening"`);
});
