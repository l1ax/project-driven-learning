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
- Focus on projects that allow progressive learning and clear milestones

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

**Create a well-structured learning plan that includes:**

For the overall project:
- Project overview and what they'll build
- Complete list of concepts/skills they'll learn
- Prerequisites needed before starting

For each stage:
- **Goal**: Clear statement of what will be achieved
- **Prerequisites**: Knowledge needed for this stage
- **What you'll learn**: New concepts introduced
- **Implementation tasks**: Specific things to build
- **Acceptance criteria**: Measurable completion checklist
- **Learning resources**: Curated materials (2-3 focused resources)
- **Knowledge check**: Questions to verify understanding

Follow the stage structure template in `references/project_breakdown.md` for detailed guidance.

**Save the plan** to `./docs/plans/YYYY-MM-DD-{project-name}/plan.md` for future reference.

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

**Your response approach:**
1. Ask about their experience level with JavaScript and frameworks
2. Ask if they have a project idea or need suggestions
3. Clarify specific React concepts they want to focus on
4. Create a personalized learning plan following the workflow above
5. Save the plan to `./docs/plans/` directory

## Key Principles for Effective Learning Plans

- **Specific tasks**: Provide concrete, actionable tasks rather than vague instructions
- **Explain the why**: Help users understand the purpose behind each concept
- **Progressive complexity**: Don't overwhelm with too many new ideas at once
- **Objective criteria**: Users should be able to verify completion independently
- **Curated resources**: 2-3 focused, high-quality resources per stage
- **Encourage exploration**: Invite users to experiment beyond minimum requirements
- **Appropriate pacing**: Balance challenge with achievability

## References

- **Project breakdown strategies**: See `references/project_breakdown.md` for detailed guidelines on breaking projects into stages, stage templates, and common patterns
- **Resource recommendations**: See `references/learning_resources.md` for principles on selecting and recommending learning materials, and knowledge validation methods
