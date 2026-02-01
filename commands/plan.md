# Project-Driven Learning Plan

I want you to use the project-driven-learning skill to help me create a structured learning plan.

$ARGUMENTS

Please follow these steps:
1. Ask me clarifying questions about my experience level, project preferences, and learning goals
2. Suggest appropriate project ideas if I don't have one
3. Break down the project into progressive learning stages (3-7 stages)
4. For each stage, provide:
   - Clear goals and objectives
   - Prerequisites and what I'll learn
   - Specific implementation tasks
   - Acceptance criteria
   - Curated learning resources
   - Knowledge check questions

**IMPORTANT**: After creating the learning plan, save it to:
`./docs/plans/{YYYY-MM-DD}-{learning-goal}/plan.md`

Where:
- {YYYY-MM-DD} is today's date (e.g., 2026-02-01)
- {learning-goal} is a short kebab-case description of what they're learning (e.g., "react-fundamentals", "python-web-scraping")

For example: `./docs/plans/2026-02-01-react-todo-app/plan.md`

**ALSO CREATE**: Initialize a `progress.json` file in the same directory to track learning progress:
`./docs/plans/{YYYY-MM-DD}-{learning-goal}/progress.json`

Progress file structure:
```json
{
  "project_name": "{project-name}",
  "project_path": "./projects/{project-name}",
  "plan_path": "./docs/plans/{YYYY-MM-DD}-{learning-goal}/plan.md",
  "technology_stack": "{detected-tech-stack}",
  "current_stage": 0,
  "total_stages": {number-of-stages},
  "stages": [
    {
      "stage_number": 1,
      "stage_name": "{Stage 1 name}",
      "status": "not_started",
      "started_at": null,
      "completed_at": null
    },
    {
      "stage_number": 2,
      "stage_name": "{Stage 2 name}",
      "status": "not_started",
      "started_at": null,
      "completed_at": null
    }
    // ... for all stages
  ],
  "created_at": "{ISO-8601-timestamp}",
  "updated_at": "{ISO-8601-timestamp}"
}
```

**After saving both files**, tell the user:
- Where the plan was saved
- How to start: `/project:scaffold stage 1` or `/project:scaffold`
- How to check progress: `/project:progress`

Remember: This is a learning journey, so guide me without writing the code for me. Help me understand concepts and verify my progress at each stage.
