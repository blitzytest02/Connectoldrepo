# Connectoldrepo

A beginner-friendly Node.js tutorial demonstrating how to build a simple web server using Express.js with multiple endpoints.

## 📖 Project Overview

This tutorial project teaches the fundamentals of building a web server with Node.js and Express.js. You'll learn how to:

- Set up a Node.js project with npm
- Install and configure Express.js
- Create multiple HTTP endpoints
- Handle GET requests and send responses
- Run a local development server

The server implements two simple endpoints that return text responses, providing a foundation for understanding web server development.

## ✅ Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Node.js** (version 14.0.0 or higher, version 18+ recommended)
  - Check your version: `node --version`
  - Download from: [https://nodejs.org/](https://nodejs.org/)
- **npm** (Node Package Manager, comes with Node.js)
  - Check your version: `npm --version`
- **A text editor** (VS Code, Sublime Text, Atom, or any editor of your choice)
- **A terminal/command prompt** for running commands
- **A web browser** (Chrome, Firefox, Safari, or Edge)

Basic familiarity with the command line is helpful but not required.

## 📦 Installation

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Connectoldrepo
```

### 2. Install Dependencies

Run the following command to install Express.js and all required packages:

```bash
npm install
```

**Expected output:**
```
added 29 packages, and audited 30 packages in 3s

found 0 vulnerabilities
```

This command reads the `package.json` file and installs Express.js version 4.21.2 along with its dependencies into the `node_modules/` directory.

## 🚀 Running the Server

Once dependencies are installed, you can start the server:

```bash
npm start
```

**Expected console output:**
```
> connectoldrepo@1.0.0 start
> node server.js

Server running at http://localhost:3000
Try: http://localhost:3000/ for "Hello world"
Try: http://localhost:3000/evening for "Good evening"
```

The server is now running and listening for requests on port 3000. Keep this terminal window open while the server is running.

To stop the server, press `Ctrl + C` in the terminal.

## 🧪 Testing the Endpoints

The server provides two endpoints that you can test:

### Endpoint 1: Root Path

**URL:** `http://localhost:3000/`

**Response:** `Hello world`

**Test in browser:**
- Open your web browser and navigate to [http://localhost:3000/](http://localhost:3000/)
- You should see the text "Hello world" displayed

**Test with curl:**
```bash
curl http://localhost:3000/
```

**Expected output:**
```
Hello world
```

---

### Endpoint 2: Evening Path

**URL:** `http://localhost:3000/evening`

**Response:** `Good evening`

**Test in browser:**
- Open your web browser and navigate to [http://localhost:3000/evening](http://localhost:3000/evening)
- You should see the text "Good evening" displayed

**Test with curl:**
```bash
curl http://localhost:3000/evening
```

**Expected output:**
```
Good evening
```

## 📁 Project Structure

Here's an overview of the files in this project:

```
Connectoldrepo/
├── .gitignore           # Specifies files to exclude from version control
├── node_modules/        # Contains all installed npm packages (created by npm install)
├── package.json         # Project metadata and dependency declarations
├── package-lock.json    # Locks exact versions of all dependencies (created by npm install)
├── README.md           # This file - project documentation
└── server.js           # Main application file with Express.js server code
```

### File Descriptions

- **server.js**: The heart of the application. Contains the Express.js server code, route definitions, and server startup logic.
- **package.json**: Defines project metadata, dependencies (Express.js), and npm scripts like `npm start`.
- **.gitignore**: Tells Git which files to ignore (like `node_modules/`) to keep the repository clean.
- **node_modules/**: Directory where npm installs all package dependencies. This folder is not committed to version control.
- **package-lock.json**: Automatically generated file that locks the exact versions of dependencies for reproducible installations.

## 🔍 How It Works

### Express.js Framework

Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for building web servers and APIs. It simplifies the process of handling HTTP requests and responses.

### Route Handling

Routes define how the server responds to client requests to specific endpoints (URLs). In this project:

```javascript
app.get('/', (req, res) => {
  res.send('Hello world');
});
```

- **`app.get()`**: Registers a route handler for HTTP GET requests
- **First parameter (`'/'`)**: The URL path to match
- **Second parameter**: A callback function that executes when the route is accessed
  - `req`: Request object containing information about the HTTP request
  - `res`: Response object used to send data back to the client
- **`res.send()`**: Sends a response to the client (automatically sets appropriate headers)

### Server Initialization

The server starts listening for connections on a specific port:

```javascript
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

This binds the Express application to port 3000 and begins accepting incoming HTTP requests.

## 🎯 Next Steps

Now that you have a working Express.js server, here are some ideas to extend your learning:

### Add More Endpoints

Try creating additional routes:
```javascript
app.get('/morning', (req, res) => {
  res.send('Good morning');
});

app.get('/night', (req, res) => {
  res.send('Good night');
});
```

### Return JSON Responses

Instead of plain text, return JSON data:
```javascript
app.get('/api/status', (req, res) => {
  res.json({ status: 'success', message: 'Server is running' });
});
```

### Handle URL Parameters

Create dynamic routes that accept parameters:
```javascript
app.get('/greet/:name', (req, res) => {
  res.send(`Hello, ${req.params.name}!`);
});
```

### Add POST Endpoints

Accept data from clients:
```javascript
app.post('/message', (req, res) => {
  // Handle POST request
  res.json({ received: true });
});
```

## 📚 Learning Resources

- **Express.js Official Documentation**: [https://expressjs.com/](https://expressjs.com/)
- **Node.js Documentation**: [https://nodejs.org/docs/](https://nodejs.org/docs/)
- **MDN HTTP Methods**: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- **Express.js Routing Guide**: [https://expressjs.com/en/guide/routing.html](https://expressjs.com/en/guide/routing.html)

## 🐛 Troubleshooting

### Port Already in Use

**Error:** `EADDRINUSE: address already in use :::3000`

**Solution:** Another process is using port 3000. Either:
- Stop the other process
- Change the port in `server.js` (modify the `PORT` constant to a different number like 3001)

### Cannot Find Module 'express'

**Error:** `Cannot find module 'express'`

**Solution:** Express.js is not installed. Run:
```bash
npm install
```

### Permission Errors (npm install)

**Error:** `EACCES: permission denied`

**Solution:** You may need to fix npm permissions. See: [https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)

---

**Happy coding! 🚀**

Feel free to modify the code, experiment with different endpoints, and explore the Express.js documentation to learn more.