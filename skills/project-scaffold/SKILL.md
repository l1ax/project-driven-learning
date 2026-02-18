---
name: project-scaffold
description: Scaffold project structure for project-based learning stages. Use when users want to start a learning stage, set up a project, or say things like "scaffold stage 2", "set up the project for stage 1", "create project structure from this plan", or "start implementing stage X". Reads learning plans, detects technology stack, creates appropriate project structure with boilerplate code, marks files for user implementation, and generates task lists.
---

# Project Scaffold

## Overview

Scaffold project structures for project-based learning. Creates appropriate project setup based on learning plans, including boilerplate code, configuration files, and clear markers for user implementation.

## Workflow

### 1. Identify the Learning Plan

**If user provides a plan file path:**
```
"Scaffold the project from ./docs/plans/2026-02-01-react-todo/plan.md"
```
Read the plan file directly.

**If user mentions a stage without path:**
```
"Set up stage 2"
"Start implementing the first stage"
```
Look for the most recent plan in `./docs/plans/` directory.

**If context is unclear:**
Ask the user to clarify which plan and which stage they want to scaffold.

### 2. Parse the Learning Plan

Read the plan file and extract:
- Project name and description
- Target stage information:
  - Stage name and goals
  - Implementation tasks
  - Acceptance criteria
  - Prerequisites
  - Learning resources
- Technology stack (infer from keywords and context)

**Technology detection tips** (see `references/tech_stacks.md` for full details):
- Frontend: React, Vue, Angular, HTML/CSS/JS
- Backend: Node.js/Express, Flask, FastAPI
- Mobile: React Native
- CLI: Python CLI, Node.js CLI

### 3. Create Project Structure

**Project location:**
Create the project in `./projects/{project-name}/`

**Directory structure based on tech stack:**
Refer to `references/tech_stacks.md` for guidance on common patterns for different technologies.

**General approach:**
1. Analyze the detected technology stack and stage requirements
2. Create appropriate directory structure following best practices
3. Generate necessary configuration files (package.json, requirements.txt, etc.)
4. Create entry point files with basic boilerplate
5. Add clear TODO comments marking areas for user implementation

### 4. Mark User Implementation Areas

**Use two complementary approaches:**

**A. In-file TODO comments:**
Add clear, specific TODO/TASK/IMPLEMENT comments in code files to mark areas for user implementation.

**B. TASKS.md file at project root:**
Create a comprehensive task checklist that includes:
- Overview of the stage goals
- Numbered tasks with file locations and descriptions
- Implementation hints where helpful
- Acceptance criteria checklist
- Relevant learning resources

**What to mark for user implementation:**
- Core business logic and feature-specific code
- API endpoints, handlers, and data processing
- Component implementations and state management
- Data validation and custom utilities

**What to provide complete:**
- All project configuration (package.json, build configs, etc.)
- Entry points with basic structure
- Basic styling setup and README with instructions

### 5. Generate Output Summary

After scaffolding, provide the user with a clear, helpful summary:

**Include:**
- Project location and technology stack
- Stage number and name
- Next steps: navigation, dependency installation, starting dev server
- Brief summary of what they need to implement
- Key files to check with descriptions
- Acceptance criteria from the plan
- Encouragement and offer to help

Keep the summary concise and actionable, focusing on getting the user started quickly.

## Project Generation Principles

For any detected technology stack:

1. **Follow established conventions** - Use the community-standard directory structure and tooling
2. **Consult tech_stacks.md** - Reference patterns and best practices for the specific technology
3. **Create minimal boilerplate** - Provide only what's needed to get started
4. **Clear separation** - Distinguish between complete boilerplate and user implementation areas
5. **Configuration first** - Ensure all build tools, dependencies, and configs are properly set up

**Key files to always include:**
- Project configuration (package.json, requirements.txt, Cargo.toml, etc.)
- Entry point with basic structure
- README with setup and run instructions
- TASKS.md with clear implementation checklist

**Adapt dynamically** - If the technology isn't explicitly covered in tech_stacks.md, use your knowledge of that ecosystem's conventions and best practices to create an appropriate structure.

## Smart Scaffolding

**For Stage 1:**
- Provide complete project setup
- Minimal boilerplate to get started
- Focus on basic structure

**For Stage 2+:**
- Build on existing project (if it exists)
- Add new directories/files as needed
- Keep existing implementations
- Mark new areas for implementation

**Check if project already exists:**
```bash
# If ./projects/{project-name}/ exists
# Add to existing structure rather than overwriting
```

## Example Usage

**User:** "Scaffold the first stage of my React learning plan"

**Steps:**
1. Look for recent plan in `./docs/plans/`
2. Parse stage 1 information
3. Detect React as technology
4. Create `./projects/{project-name}/` with React + Vite structure
5. Generate appropriate configuration and boilerplate files
6. Generate TASKS.md with stage-specific tasks
7. Provide next steps to user

**User:** "Set up stage 2"

**Steps:**
1. Find the associated plan
2. Check if project exists in `./projects/`
3. If exists: add to existing structure
4. If not: create full scaffold
5. Update TASKS.md for stage 2
6. Guide user on what changed

## Important Guidelines

- **Never write implementation code** - Only provide structure and clear TODOs
- **Be specific in TODOs** - Help users understand what to implement
- **Test the basics** - Ensure the scaffolded project runs without errors
- **Clear instructions** - README should be comprehensive
- **Respect existing code** - Don't overwrite user's implementations

## References

- **Technology stack templates**: See `references/tech_stacks.md` for detailed structure and scaffolding patterns for different technologies
