# Technology Stack Reference

This document provides guidance on scaffolding projects for different technology stacks. Use these as **reference patterns**, not rigid templates. Adapt based on the specific learning plan requirements and modern best practices.

## Scaffolding Principles

When creating project structure:
1. **Follow ecosystem conventions** - Use community-standard patterns
2. **Minimal viable setup** - Include only what's needed to start
3. **Clear organization** - Logical directory structure
4. **Modern tooling** - Use current, recommended tools
5. **Learning-focused** - Mark implementation areas clearly

## Reference Patterns by Technology

The following are **reference patterns** to guide project setup. Adapt them based on:
- Current best practices in the ecosystem
- Specific learning plan requirements
- Stage complexity and user experience level
- Modern tooling updates

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

## Scaffolding Decision Guidelines

### For Stage 1
**Provide complete setup:**
- All configuration files needed to run the project
- Build/dev tool setup with proper scripts
- Entry points with minimal boilerplate
- A working "hello world" or minimal example
- Comprehensive README with setup and running instructions
- Clear markers (TODOs) for where user implements features

### For Stage 2+
**Build incrementally:**
- Add new directories/files as needed for new features
- Preserve existing user implementations
- Provide new boilerplate only for new concepts
- Update README if new setup steps are needed
- Add stage-specific TODOs

### Implementation vs. Boilerplate

**Users should implement (mark with TODOs):**
- All business logic specific to the project
- Feature implementations described in stage tasks
- API route handlers and their logic
- Data models and schemas
- State management logic
- Custom validation and utilities

**Provide complete boilerplate:**
- Configuration files (package.json, tsconfig.json, etc.)
- Build tool setup (Vite, Webpack configs)
- Basic entry points and app initialization
- Development server setup
- Basic styling structure
- Testing framework setup (if stage requires it)

## Implementation Marking Best Practices

**In-code markers:**
Use clear, specific TODO comments that explain what needs to be implemented and why:
- `TODO:` for implementation tasks
- `TASK:` for specific sub-tasks
- `IMPLEMENT:` for core logic to be added

Be specific about what needs to be done, not just "implement this function."

**File-level documentation:**
For files that are mostly user implementation, add a header comment block explaining:
- What this file is for
- What the user needs to implement
- Key tasks or components to complete
- Any hints or important considerations

## Technology Detection Guidelines

Analyze the learning plan to identify the technology stack:

**Look for explicit mentions:**
- Technology names in project title or description
- Specific frameworks, libraries, or tools mentioned
- Prerequisites that indicate the stack (e.g., "knowledge of Flask")

**Infer from project type:**
- "Web app", "dashboard", "website" → likely frontend framework
- "API", "backend", "server" → backend framework
- "Mobile app" → mobile framework
- "CLI tool", "command-line" → CLI framework

**Consider context clues:**
- Database mentions → backend project likely needed
- UI/UX focus → frontend project
- Real-time features → may need WebSockets/specific backend

**When multiple technologies apply:**
- Prioritize what the user wants to learn (from learning plan)
- Consider stage requirements
- Choose appropriate architecture (monolith vs. separated frontend/backend)

If uncertain, prefer simpler stack for beginners, more complete stack for advanced learners.
