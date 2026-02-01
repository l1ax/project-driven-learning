# Scaffold Learning Project

I want you to use the project-scaffold skill to set up the project structure for a learning stage.

$ARGUMENTS

Please follow these steps:

## 1. Check for Existing Progress
First, look for a `progress.json` file in the plan directory (same level as plan.md):
- **If progress.json exists**: Read it to get current stage, project location, and completion status
- **If it doesn't exist**: This is a new project, start from stage 1

Progress file format:
```json
{
  "project_name": "react-todo-app",
  "project_path": "./projects/react-todo-app",
  "plan_path": "./docs/plans/2026-02-01-react-todo-app/plan.md",
  "technology_stack": "react",
  "current_stage": 1,
  "stages": [
    {
      "stage_number": 1,
      "stage_name": "Setup & Basic Structure",
      "status": "in_progress",
      "started_at": "2026-02-01T10:30:00Z",
      "completed_at": null
    }
  ],
  "created_at": "2026-02-01T10:30:00Z",
  "updated_at": "2026-02-01T10:30:00Z"
}
```

## 2. Identify the Learning Plan
- If user provides path: use that plan
- If user mentions stage without path: look for most recent plan in ./docs/plans/
- Check the progress.json to understand which plan is being followed

## 3. Determine Target Stage
- If user specifies "stage 2" or "next stage": use that stage
- If no stage specified and progress exists: continue current stage or move to next
- If new project: start with stage 1

## 4. Parse the Plan
Extract from plan.md:
- Project name and description
- Target stage information (goals, tasks, criteria, resources)
- Technology stack (infer from keywords)

## 5. Create/Update Project Structure
- Create project in ./projects/{project-name}/
- Use appropriate template based on technology stack
- Generate boilerplate code and configuration files
- Mark areas for user implementation with TODO comments
- Create/update TASKS.md with implementation checklist

## 6. Update Progress File
Save/update `progress.json` in the plan directory (same level as plan.md):
- Update current_stage
- Add new stage entry if starting a new stage
- Update timestamps
- Set status to "in_progress" for current stage

Location: `./docs/plans/{date}-{project-name}/progress.json`

## 7. Provide Summary
Show the user:
- Current stage and progress
- Project location
- Next steps and setup instructions
- What files need to be implemented
- Acceptance criteria

---

**IMPORTANT Progress Tracking Rules:**
- Always check for progress.json FIRST before scaffolding
- Save progress.json in the same directory as plan.md
- Update progress.json after each scaffolding operation
- If user says "continue" or "next stage", increment stage based on progress.json
- If project already exists (check ./projects/), add to existing structure rather than overwriting

**Progress Status Values:**
- "not_started" - Stage hasn't been scaffolded yet
- "in_progress" - Stage has been scaffolded, user is implementing
- "completed" - User confirms stage is complete (via user confirmation)

Remember: Only provide project structure and boilerplate. Do NOT implement the core functionality - that's for the user to learn by doing.
