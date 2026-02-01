# Check Learning Progress

Display the current progress of your learning project.

$ARGUMENTS

Please follow these steps:

## 1. Locate Progress File
Look for `progress.json` in the plan directory:
- If user specifies a project: use that project's progress.json
- If no project specified: find the most recent progress.json in ./docs/plans/
- If no progress file exists: inform user no active learning project found

## 2. Read and Parse Progress
Load the progress.json and extract:
- Project name and path
- Technology stack
- Total stages and current stage
- Status of each stage
- Timestamps (when started, when last updated)

## 3. Display Progress Overview

Format the output like this:

```markdown
# Learning Progress: {Project Name}

**Technology:** {tech_stack}
**Project Path:** {project_path}
**Plan:** {plan_path}

## Progress Overview
Stage {current_stage} of {total_stages} • {completion_percentage}% Complete

## Stages

### ✅ Stage 1: {stage_name}
**Status:** Completed
**Started:** {started_at}
**Completed:** {completed_at}
**Duration:** {duration}

### 🔄 Stage 2: {stage_name}
**Status:** In Progress
**Started:** {started_at}
**Tasks:** See ./projects/{project-name}/TASKS.md

### ⏸️ Stage 3: {stage_name}
**Status:** Not Started

### ⏸️ Stage 4: {stage_name}
**Status:** Not Started

---

## Next Steps

{If in progress:}
Continue working on Stage {N}:
- Review TASKS.md for implementation checklist
- Check acceptance criteria in the plan
- When done: `/project:complete`

{If last stage completed:}
🎉 Congratulations! You've completed all stages of this learning project!

{If ready for next stage:}
Ready to start Stage {N+1}?
Run: `/project:scaffold stage {N+1}`
```

## 4. Show Statistics
Provide helpful statistics:
- Total time spent (if available)
- Stages completed / total stages
- Estimated progress percentage
- Days since project started

## 5. Quick Actions
Suggest relevant commands:
- Continue current stage: Review TASKS.md
- Mark stage complete: `/project:complete`
- Start next stage: `/project:scaffold next`
- View plan details: Open plan.md

---

**Usage Examples:**
- `/project:progress` - Show progress for most recent project
- `/project:progress react-todo-app` - Show progress for specific project
- `/project:status` - Alias for progress

**Status Indicators:**
- ✅ Completed stages
- 🔄 Current/in-progress stage
- ⏸️ Not started stages
