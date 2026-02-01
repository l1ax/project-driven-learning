# Mark Stage Complete

Mark a learning stage as completed and optionally move to the next stage.

$ARGUMENTS

Please follow these steps:

## 1. Find the Progress File
Look for `progress.json` in the plan directory (./docs/plans/{date}-{project-name}/progress.json)

## 2. Validate Current Stage
- Check which stage is currently "in_progress"
- Ask user to confirm they've completed all acceptance criteria
- Review the TASKS.md in the project to verify completeness

## 3. Update Progress
Update the progress.json file:
- Set current stage status to "completed"
- Add completed_at timestamp
- If user wants to continue, increment current_stage

Example update:
```json
{
  "current_stage": 2,  // Moved to next stage
  "stages": [
    {
      "stage_number": 1,
      "stage_name": "Setup & Basic Structure",
      "status": "completed",  // ✅ Marked complete
      "started_at": "2026-02-01T10:30:00Z",
      "completed_at": "2026-02-01T15:45:00Z"  // ✅ Added timestamp
    },
    {
      "stage_number": 2,
      "stage_name": "Core Functionality",
      "status": "not_started",  // Ready for next
      "started_at": null,
      "completed_at": null
    }
  ],
  "updated_at": "2026-02-01T15:45:00Z"  // ✅ Updated
}
```

## 4. Provide Feedback
Show the user:
- Congratulations message
- Summary of what was accomplished in this stage
- Progress overview (X of Y stages completed)
- Suggestion to start next stage if available
- Command to scaffold next stage: `/project:scaffold stage {N+1}`

## 5. Optional: Auto-scaffold Next Stage
Ask user: "Would you like me to set up the next stage now?"
- If yes: Automatically trigger scaffold for next stage
- If no: Just mark current as complete

---

**Usage Examples:**
- `/project:complete` - Mark current stage as complete
- `/project:complete stage 1` - Mark specific stage as complete
- `/project:complete and continue` - Mark complete and scaffold next stage

**Validation Checks:**
Before marking complete, ask user to confirm:
- [ ] All tasks in TASKS.md are implemented
- [ ] Acceptance criteria are met
- [ ] Code runs without errors
- [ ] Ready to move to next stage
