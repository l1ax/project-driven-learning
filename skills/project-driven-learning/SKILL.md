---
name: project-driven-learning
description: Guide users through project-based learning by breaking down programming skills into structured, stage-by-stage learning plans. Use when users want to learn a technology/skill through building a project, request a learning roadmap, or say things like "help me learn X by building Y", "create a learning plan for X", or "I want to learn X through practice". Creates phased learning plans with prerequisites, knowledge checks, implementation tasks, and acceptance criteria.
---

# Project-Driven Learning

## Overview

Guide users through hands-on learning of programming skills by breaking down projects into progressive stages. Each stage includes prerequisite knowledge, learning resources, implementation tasks, knowledge checks, and clear acceptance criteria.

## Workflow

### 1. Understand the Learning Goal

First, clarify what the user wants to learn:

**Ask about:**
- **Target skill/technology**: What specifically do they want to learn? (e.g., React, Python, REST APIs)
- **Current level**: What's their experience with this technology?
- **Project idea**: Do they have a project in mind, or should you suggest one?
- **End goal**: What do they want to be able to build by the end?

**Common trigger phrases:**
- "I want to learn [technology] by building a project"
- "Help me learn [skill] through practice"
- "Create a learning plan for [technology]"
- "I want to build [project] to learn [skill]"

### 2. Define or Confirm the Project

Based on the user's goal and experience level:

**If user has a project idea:**
- Confirm it's appropriate for their skill level
- Ensure it covers the concepts they want to learn
- Adjust scope if needed (not too ambitious, not too trivial)

**If user needs project suggestions:**
- Propose 2-3 project options that teach the target skills
- Match complexity to their experience level
- Examples:
  - **Beginner**: Todo app, Calculator, Weather dashboard
  - **Intermediate**: Blog with CMS, E-commerce site, Chat application
  - **Advanced**: Social network, Real-time collaboration tool, Microservices system

### 3. Break Down into Stages

Use the guidelines in `references/project_breakdown.md` to structure the project:

**Key principles:**
- Start simple, add complexity gradually
- Each stage should be functional and testable
- Aim for 3-7 stages depending on complexity
- Order by logical dependencies (basics before advanced)

**Stage structure** (see `references/project_breakdown.md` for details):
- Clear goal statement
- Prerequisites (what they need to know first)
- What they'll learn (new concepts in this stage)
- Implementation tasks (specific things to build)
- Acceptance criteria (how to know it's done)
- Learning resources (where to learn prerequisites)
- Knowledge check (verify understanding before proceeding)

### 4. Present the Learning Plan

**Format the plan clearly:**

```markdown
# [Project Name]: Learning Plan

## Project Overview
[1-2 sentences describing what they'll build]

## What You'll Learn
- Concept/skill 1
- Concept/skill 2
- ...

## Prerequisites
Before starting, you should know:
- Prerequisite 1
- Prerequisite 2
(If user doesn't have these, recommend resources or adjust project)

---

## Stage 1: [Name]

**Goal**: [What will be achieved in this stage]

**Prerequisites for this stage**:
- Knowledge point 1
- Knowledge point 2

**What you'll learn**:
- New concept 1
- New concept 2

**Implementation tasks**:
1. Task 1
2. Task 2
3. Task 3

**Acceptance criteria**:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Learning resources**:
- [Resource Title](URL) - Description of what to focus on
- [Resource Title](URL) - Description

**Knowledge check** (before moving to next stage):
Ask yourself these questions:
1. Can you explain [concept] in your own words?
2. Can you write [code pattern] without looking at examples?
3. Do you understand why we use [approach] instead of [alternative]?

---

## Stage 2: [Name]
[Same structure as Stage 1]

...

---

## Final Notes

**Learning approach**:
- Complete each stage fully before moving on
- Don't rush - understanding matters more than speed
- If you get stuck, review the learning resources
- Feel free to experiment beyond the requirements

**When you're ready to start**: Let me know which stage you're beginning, and I can provide additional guidance or answer questions. When you finish a stage, share what you've built and I'll help verify it meets the criteria before moving forward.
```

### 5. Support Throughout Learning Journey

**As user progresses through stages:**

**When starting a new stage:**
- Briefly review prerequisites
- Highlight the most important concepts to focus on
- Provide additional examples if requested
- Answer questions about approach

**Knowledge verification before next stage:**
- Ask 2-3 questions to check understanding (see `references/learning_resources.md`)
- Have them explain concepts in their own words
- Ensure they can identify when/why to use what they learned

**When they share completed work:**
- Review against acceptance criteria
- Provide constructive feedback
- Celebrate progress
- Confirm readiness for next stage

**If they get stuck:**
- Help debug specific issues
- Point to relevant learning resources
- Break down confusing concepts
- Provide hints without giving full solutions (they're learning!)

**Important**: Let the user implement the code independently. This is about learning, not getting code written for them. Your role is to guide, explain, and verify understanding.

## Resource Recommendations

When suggesting learning resources, follow guidelines in `references/learning_resources.md`:

**Prioritize:**
1. Official documentation
2. Interactive tutorials
3. Well-established community resources
4. Hands-on coding exercises

**Match to user level:**
- **Beginners**: Step-by-step tutorials, visual explanations
- **Intermediate**: Best practices, design patterns, real examples
- **Advanced**: In-depth articles, source code analysis, architecture

## Example Usage

**User**: "I want to learn React by building something practical"

**Response**:
```
I'll help you learn React through project-based practice! Let me understand your goal better:

1. **Experience level**: Have you used JavaScript before? Any experience with other frameworks?
2. **Project preference**: Do you have a project idea in mind, or would you like suggestions?
3. **Learning goal**: Are there specific React concepts you want to focus on (hooks, state management, routing)?
```

[After user responds, create personalized learning plan following the workflow above]

## Tips for Effective Learning Plans

- **Be specific in tasks**: Instead of "Add styling", say "Style the todo list with CSS Grid and add hover effects"
- **Include why, not just what**: Help users understand the purpose behind each concept
- **Progressive concept introduction**: Don't overwhelm with too many new ideas at once
- **Realistic acceptance criteria**: Users should be able to objectively verify completion
- **Curate resources**: 2-3 focused resources per stage, not a long list
- **Encourage exploration**: Invite users to experiment beyond minimum requirements

## References

- **Project breakdown strategies**: See `references/project_breakdown.md` for detailed guidelines on breaking projects into stages, stage templates, and common patterns
- **Resource recommendations**: See `references/learning_resources.md` for principles on selecting and recommending learning materials, and knowledge validation methods
