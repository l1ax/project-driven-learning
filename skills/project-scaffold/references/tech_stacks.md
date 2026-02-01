# Technology Stack Templates

This document provides guidance on scaffolding projects for different technology stacks.

## Template Structure Guidelines

When scaffolding a project, consider:
1. **Core dependencies**: Essential packages and configuration
2. **Development setup**: Dev dependencies, scripts, tooling
3. **Project structure**: Directories, file organization
4. **Boilerplate code**: Minimal working examples
5. **User tasks**: Files that learners should implement themselves

## Common Technology Stacks

### Frontend Web

#### React
**Directory structure:**
```
project-name/
├── public/
│   └── index.html
├── src/
│   ├── App.jsx          # Basic component with TODO
│   ├── index.js         # Entry point (complete)
│   └── index.css        # Basic styles (complete)
├── package.json         # Dependencies (complete)
└── README.md           # Setup instructions (complete)
```

**Key files to provide:**
- `package.json`: Include react, react-dom, vite/webpack
- `index.html`: Basic HTML template
- `index.js`: ReactDOM.render boilerplate
- `App.jsx`: Simple component with TODO comments

**User implementation files:**
- Main application components
- State management
- API integration

#### Vue.js
**Directory structure:**
```
project-name/
├── public/
│   └── index.html
├── src/
│   ├── App.vue         # Basic component with TODO
│   ├── main.js         # Entry point (complete)
│   └── components/     # Component directory (empty)
├── package.json        # Dependencies (complete)
└── vite.config.js      # Build config (complete)
```

#### Vanilla JavaScript
**Directory structure:**
```
project-name/
├── index.html          # HTML structure with TODOs
├── style.css           # Basic styles (partial)
├── script.js           # JS file with TODOs
└── README.md          # Setup instructions
```

### Backend

#### Node.js + Express
**Directory structure:**
```
project-name/
├── src/
│   ├── index.js        # Server setup (complete)
│   ├── routes/         # Route files (structure only)
│   ├── controllers/    # Controllers (empty, for user)
│   ├── models/         # Models (empty, for user)
│   └── middleware/     # Middleware (empty, for user)
├── package.json        # Dependencies (complete)
└── README.md          # Setup instructions
```

**Key files to provide:**
- `package.json`: express, nodemon, etc.
- `index.js`: Basic Express server with TODO routes
- Route structure examples

#### Python Flask
**Directory structure:**
```
project-name/
├── app/
│   ├── __init__.py     # App factory (complete)
│   ├── routes.py       # Routes with TODOs
│   └── models.py       # Empty models file
├── requirements.txt    # Dependencies (complete)
├── run.py             # Entry point (complete)
└── README.md          # Setup instructions
```

#### Python FastAPI
**Directory structure:**
```
project-name/
├── app/
│   ├── main.py         # FastAPI app (basic setup)
│   ├── routes/         # Route modules (structure)
│   └── models/         # Pydantic models (empty)
├── requirements.txt    # Dependencies (complete)
└── README.md          # Setup instructions
```

### Full Stack

#### MERN Stack (MongoDB + Express + React + Node)
**Directory structure:**
```
project-name/
├── client/             # React app (see React structure)
├── server/             # Express app (see Express structure)
├── package.json        # Root scripts (complete)
└── README.md          # Full setup guide
```

### CLI Tools

#### Python CLI
**Directory structure:**
```
project-name/
├── src/
│   ├── __init__.py
│   ├── cli.py          # Click/argparse setup (basic)
│   └── commands/       # Command modules (empty)
├── requirements.txt    # Dependencies (complete)
├── setup.py           # Package setup (complete)
└── README.md          # Usage instructions
```

#### Node.js CLI
**Directory structure:**
```
project-name/
├── bin/
│   └── cli.js          # Entry point (basic)
├── src/
│   └── commands/       # Command modules (empty)
├── package.json        # With bin field (complete)
└── README.md          # Usage instructions
```

### Mobile

#### React Native
**Directory structure:**
```
project-name/
├── src/
│   ├── App.js          # Root component (basic)
│   ├── screens/        # Screen components (empty)
│   └── components/     # Reusable components (empty)
├── package.json        # Dependencies (complete)
└── README.md          # Setup instructions
```

## Determining What to Scaffold

### Stage 1: Always Provide
- Project initialization files (package.json, requirements.txt)
- Build/dev tool configuration
- Basic entry points
- Minimal working example
- README with setup instructions

### Stage 2+: Provide Structure
- Directory structure
- Config files
- Helper utilities
- Example patterns
- Files with TODO comments for implementation

### What Users Should Implement
- Core business logic
- Feature-specific components
- API route handlers
- Data models
- Complex state management
- Custom utilities

## File Marking Conventions

### TODO Comments
```javascript
// TODO: Implement user authentication logic
// TASK: Create a function that validates user input
// IMPLEMENT: Add error handling for API calls
```

### File-level markers
```javascript
/**
 * USER IMPLEMENTATION REQUIRED
 *
 * This file needs to be completed by the user.
 *
 * Tasks:
 * 1. Define the User model with required fields
 * 2. Implement validation methods
 * 3. Add database connection logic
 */
```

## Technology Detection

Use these indicators from the learning plan to determine tech stack:

**Frontend:**
- Keywords: React, Vue, Angular, Svelte, HTML/CSS/JavaScript
- Project types: "web app", "dashboard", "website"

**Backend:**
- Keywords: Node.js, Express, Flask, FastAPI, Django
- Project types: "API", "backend", "server"

**Database:**
- Keywords: MongoDB, PostgreSQL, MySQL, SQLite
- Mentioned in prerequisites or stage tasks

**Mobile:**
- Keywords: React Native, Flutter
- Project types: "mobile app", "iOS/Android"

**CLI:**
- Keywords: command-line, CLI tool
- Project types: "tool", "utility"
