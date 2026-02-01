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
See `references/tech_stacks.md` for specific structure for each technology.

**General approach:**
1. Create necessary directories
2. Copy appropriate template files from `assets/templates/`
3. Replace placeholders with actual values
4. Add stage-specific TODO comments

**Placeholder replacements:**
- `{{PROJECT_NAME}}` → actual project name
- `{{PROJECT_DESCRIPTION}}` → from plan
- `{{STAGE_NAME}}` → current stage name
- `{{STAGE_GOALS}}` → stage goals from plan
- `{{STAGE_TASKS}}` → formatted task list
- `{{ACCEPTANCE_CRITERIA}}` → formatted criteria
- `{{LEARNING_RESOURCES}}` → formatted resources

### 4. Mark User Implementation Areas

**Use two approaches:**

**A. In-file TODO comments:**
```javascript
// TODO: Implement user authentication logic
// TASK: Add form validation
// IMPLEMENT: Connect to API endpoint
```

**B. TASKS.md file at project root:**
```markdown
# Implementation Tasks - Stage {N}

## Overview
Brief description of what needs to be implemented in this stage.

## Tasks

### 1. [Task Name]
**File:** `path/to/file.js`
**Description:** What needs to be done
**Hints:**
- Hint 1
- Hint 2

### 2. [Task Name]
...

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Resources
- [Resource name](URL)
```

**What to mark for user implementation:**
- Core business logic
- Feature-specific code
- API endpoints and handlers
- Component implementations
- State management
- Data validation

**What to provide complete:**
- Project configuration (package.json, vite.config.js, etc.)
- Build tool setup
- Entry points with basic structure
- Basic styling setup
- README with instructions

### 5. Generate Output Summary

After scaffolding, provide the user with:

```markdown
✅ Project scaffolded successfully!

**Location:** `./projects/{project-name}/`

**Technology:** {detected tech stack}

**Stage:** {stage number and name}

## Next Steps

1. Navigate to the project:
   ```bash
   cd projects/{project-name}
   ```

2. Install dependencies:
   ```bash
   {installation command}
   ```

3. Review TASKS.md for implementation checklist

4. Start development:
   ```bash
   {dev command}
   ```

## What You Need to Implement

{Brief summary of main tasks}

Check these files:
- `{file1}` - {what to implement}
- `{file2}` - {what to implement}

## Acceptance Criteria

{List criteria from plan}

Good luck! Feel free to ask questions as you implement the features.
```

## Template Selection

Based on detected technology, use appropriate template from `assets/templates/`:

- **react** → React + Vite project
- **python-flask** → Flask API project
- **vanilla-js** → HTML/CSS/JavaScript project

For technologies not having templates:
1. Create basic structure manually following patterns in `references/tech_stacks.md`
2. Ensure proper configuration files
3. Add clear TODO comments

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
4. Create `./projects/{project-name}/` using React template
5. Replace placeholders
6. Generate TASKS.md
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
