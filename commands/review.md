# Review Stage Implementation

Request a comprehensive review of your implementation for the current learning stage.

$ARGUMENTS

**Important:** Use the review agent defined in `./agents/review.md` to conduct this review.

The review agent will:
1. 🔍 Find your current progress and stage
2. 📋 Load acceptance criteria from the plan
3. 💻 Analyze your implementation code
4. ✅ Check against all requirements
5. 📝 Generate detailed feedback report
6. 💾 Save review to `./docs/plans/{project}/reviews/stage-{N}-review.md`

After the review, you'll get:
- Clear pass/fail/needs-improvement verdict
- Specific feedback on each acceptance criterion
- Code quality assessment
- Suggestions for improvement
- Next steps (fix issues or move forward)

---

**Usage:**
- `/review` - Review current stage
- `/review stage 2` - Review specific stage
- `/project:review` - Alias

**Before requesting review:**
- [ ] All TASKS.md items are implemented
- [ ] Code runs without critical errors
- [ ] You've tested the functionality yourself
- [ ] You believe acceptance criteria are met

**After review:**
- If ✅ Pass: Run `/project:complete` to mark done
- If ⚠️ Needs work: Fix issues and request `/review` again
- If ❌ Fail: Address critical issues before proceeding
