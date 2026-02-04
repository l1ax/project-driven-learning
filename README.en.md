# Project-Driven Learning Plugin for Claude Code

[English](README.en.md) | [中文](README.md)

A comprehensive Claude Code plugin that helps you learn programming through hands-on project implementation. This plugin provides a structured approach to learning: create learning plans, scaffold projects, track progress, and get code reviews - all within your development workflow.

## 🎯 What This Plugin Does

This plugin transforms Claude Code into your personal learning assistant that:

1. **Creates Structured Learning Plans** - Breaks down complex skills into progressive stages
2. **Scaffolds Projects** - Sets up project boilerplate with clear TODOs
3. **Tracks Your Progress** - Monitors which stages you've completed
4. **Reviews Your Code** - Provides detailed feedback on your implementations
5. **Guides Your Learning** - Offers resources, hints, and encouragement

## 📥 Installation

### Install from Marketplace

1. Add the marketplace:
```bash
/plugin marketplace add l1ax/project-driven-learning
```

2. Install the plugin:
```bash
/plugin install project-driven-learning@l1ax-plugin
```

### Verify Installation

After installation, verify the plugin is loaded:
```bash
/plugin list
```

You should see `project-driven-learning` in the list of installed plugins.

## ✨ Key Features

- 📚 **Project-Driven Learning Plans** - Multi-stage learning roadmaps with clear goals
- 🏗️ **Automatic Project Scaffolding** - Generates boilerplate for React, Python Flask, Vanilla JS, and more
- 📊 **Progress Tracking** - JSON-based progress files that track your learning journey
- 🔍 **Code Review Agent** - Automated reviews against acceptance criteria
- 📝 **Task Management** - Clear TASKS.md files marking what you need to implement
- 🎓 **Learning-Focused** - Provides structure without doing the work for you

## 📦 What's Included

### Skills
- **`project-driven-learning`** - Generates comprehensive learning plans
- **`project-scaffold`** - Scaffolds project structures with templates

### Commands
- `/project:plan` - Create a new learning plan
- `/project:scaffold` - Set up project structure for a stage
- `/project:progress` - Check your learning progress
- `/project:complete` - Mark a stage as completed
- `/project:review` - Request code review for your implementation

### Agents
- **`review.md`** - Intelligent code review agent that validates implementations

### Templates
Pre-built project templates for:
- React (with Vite)
- Python Flask
- Vanilla JavaScript/HTML/CSS

## 🚀 Quick Start

### 1. Create a Learning Plan

```bash
/project:plan I want to learn React by building a Todo app
```

This will:
- Ask about your experience level
- Generate a multi-stage learning plan
- Save to `./docs/plans/{date}-{project}/plan.md`
- Initialize progress tracking in `progress.json`

### 2. Start First Stage

```bash
/project:scaffold
```

This will:
- Read your learning plan
- Detect the technology stack
- Create project structure in `./projects/{project-name}/`
- Generate boilerplate code with TODO markers
- Create TASKS.md with implementation checklist

### 3. Implement the Code

Work on the tasks marked in:
- Files with `TODO` and `USER IMPLEMENTATION REQUIRED` comments
- `TASKS.md` checklist

### 4. Check Your Progress (Optional)

```bash
/project:progress
```

See which stages are completed, in progress, or not started.

### 5. Request Code Review

```bash
/project:review
```

The review agent will:
- Check your implementation against acceptance criteria
- Analyze code quality
- Provide detailed feedback
- Save review report to `./docs/plans/{project}/reviews/`

### 6. Mark Stage Complete

```bash
/project:complete
```

This updates your progress and optionally scaffolds the next stage.

### 7. Continue to Next Stage

```bash
/project:scaffold stage 2
```

Repeat steps 3-7 for each learning stage!

## 📁 Directory Structure

After using this plugin, your project will look like:

```
your-project/
├── docs/
│   └── plans/
│       └── 2026-02-02-react-todo-app/
│           ├── plan.md                 # Learning plan
│           ├── progress.json           # Progress tracking
│           └── reviews/                # Code review reports
│               ├── stage-1-review.md
│               └── stage-2-review.md
├── projects/
│   └── react-todo-app/                 # Your actual project
│       ├── TASKS.md                    # What to implement
│       ├── README.md                   # Setup instructions
│       ├── package.json                # Dependencies
│       └── src/
│           ├── App.jsx                 # Your implementation
│           └── ...
├── .claude-plugin/
│   └── plugin.json                     # Plugin metadata
├── commands/                           # Command definitions
│   ├── plan.md
│   ├── scaffold.md
│   ├── progress.md
│   ├── complete.md
│   └── review.md
├── agents/
│   └── review.md                       # Review agent
└── skills/
    ├── project-driven-learning/
    └── project-scaffold/
```

## 🎓 Learning Workflow Example

Let's say you want to learn React:

### Step 1: Plan
```
You: /project:plan I want to learn React by building a Todo app

Claude: I'll help you create a learning plan! Let me ask a few questions...
        [Creates structured 5-stage learning plan]

        ✅ Plan saved to: ./docs/plans/2026-02-02-react-todo-app/plan.md
```

### Step 2: Scaffold
```
You: /project:scaffold

Claude: ✅ Project scaffolded successfully!
        Location: ./projects/react-todo-app/
        Technology: React + Vite
        Stage: 1 - Setup & Basic Components

        Next steps:
        1. cd projects/react-todo-app
        2. npm install
        3. Review TASKS.md
        4. npm run dev
```

### Step 3: Implement
```
You: [Work on the code, implement TODO items]
```

### Step 4: Review
```
You: /project:review

Claude: # Stage 1 Review Report

        📊 Overall Assessment: ✅ Pass
        Completion Score: 8.5/10

        ✅ Acceptance Criteria Review
        1. ✅ Basic component structure created
        2. ✅ State management implemented
        3. ⚠️ Event handlers work but could be optimized

        [Detailed feedback and suggestions]

        🎯 Next Steps: Ready to proceed!
        Run /project:complete to mark this stage done.
```

### Step 5: Complete & Continue
```
You: /project:complete

Claude: 🎉 Congratulations! Stage 1 completed!
        Progress: 1 of 5 stages done (20%)
        Ready for Stage 2?

You: /project:scaffold stage 2

Claude: [Sets up structure for stage 2]
```

## 🛠️ Supported Technologies

Currently includes templates for:

- **Frontend**
  - React (with Vite)
  - Vue.js
  - Vanilla JavaScript/HTML/CSS

- **Backend**
  - Python Flask
  - Node.js/Express
  - Python FastAPI

- **Mobile**
  - React Native

- **CLI Tools**
  - Python CLI
  - Node.js CLI

Don't see your stack? The plugin can still create custom structures based on best practices!

## 📋 Progress Tracking

The `progress.json` file tracks your learning journey:

```json
{
  "project_name": "react-todo-app",
  "project_path": "./projects/react-todo-app",
  "current_stage": 2,
  "total_stages": 5,
  "stages": [
    {
      "stage_number": 1,
      "stage_name": "Setup & Basic Components",
      "status": "completed",
      "started_at": "2026-02-02T10:00:00Z",
      "completed_at": "2026-02-02T14:30:00Z"
    },
    {
      "stage_number": 2,
      "stage_name": "State Management",
      "status": "in_progress",
      "started_at": "2026-02-02T15:00:00Z",
      "completed_at": null
    }
  ]
}
```

## 🤖 Code Review Features

The review agent provides:

- **Acceptance Criteria Validation** - Checks all requirements are met
- **Code Quality Assessment** - Evaluates structure, naming, organization
- **Learning Objectives Check** - Verifies you understood the concepts
- **Constructive Feedback** - Specific, actionable suggestions
- **Bug Detection** - Identifies common issues and errors
- **Best Practices** - Highlights good patterns and anti-patterns
- **Next Steps** - Clear guidance on whether to proceed or improve

## 💡 Best Practices

1. **Read the Plan First** - Understand the full learning journey before starting
2. **One Stage at a Time** - Don't rush through stages
3. **Review Before Completing** - Use `/project:review` to validate your work
4. **Experiment Beyond Requirements** - The TODOs are minimums, explore more!
5. **Keep Code Organized** - Follow the structure the scaffold provides
6. **Check Progress Regularly** - Use `/project:progress` to stay motivated

## 🔧 Customization

### Adding New Templates

Add templates in `skills/project-scaffold/assets/templates/{tech-stack}/`:

```
templates/
└── your-tech/
    ├── package.json
    ├── README.md
    └── src/
        └── main.js
```

Update `references/tech_stacks.md` with scaffolding guidelines.

### Modifying Commands

Edit files in `commands/` to change command behavior or add new commands.

### Customizing Review Criteria

Edit `agents/review.md` to adjust review standards or add technology-specific checks.

## 📚 Example Projects

This plugin can help you learn by building:

- **React Todo App** - Learn components, state, events
- **Python Flask API** - Learn routing, request handling, JSON responses
- **Vanilla JS Calculator** - Learn DOM manipulation, event handling
- **React Weather Dashboard** - Learn API integration, async/await
- **Python CLI Tool** - Learn argument parsing, file I/O
- **Express REST API** - Learn CRUD operations, middleware

## ❓ FAQ

**Q: Does this write code for me?**
A: No! It provides structure, boilerplate, and TODOs. You implement the logic to learn.

**Q: Can I use this for advanced topics?**
A: Yes! Create plans for any complexity level - the plugin adapts to your goals.

**Q: What if my tech stack isn't supported?**
A: The plugin can still create structure following best practices. You can also add custom templates.

**Q: Can I skip stages?**
A: Not recommended for learning, but you can scaffold any stage number directly.

**Q: Is the review agent strict?**
A: It's learning-focused: constructive, educational, and encourages growth over perfection.

**Q: Can I use this for team learning?**
A: Yes! The progress files can be shared and reviewed by mentors or peers.

## 🤝 Contributing

Have ideas for improvements?
- Add new technology templates
- Improve review criteria
- Enhance command functionality
- Share example learning plans

## 📄 License

This plugin is provided as-is for educational purposes.

## 🎉 Happy Learning!

Remember: The goal isn't to finish quickly - it's to **learn deeply** through hands-on practice. Take your time, experiment, and enjoy the process!

---

**Created for:** Claude Code
**Version:** 1.0.0
**Author:** l1ax
