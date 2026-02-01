# {{PROJECT_NAME}}

## Project Overview

{{PROJECT_DESCRIPTION}}

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Access the API at `http://localhost:5000`

## Learning Stage: {{STAGE_NAME}}

### Goals
{{STAGE_GOALS}}

### Tasks
{{STAGE_TASKS}}

### Acceptance Criteria
{{ACCEPTANCE_CRITERIA}}

## Project Structure

```
app/
├── __init__.py    - App factory (provided)
├── routes.py      - Routes (YOUR IMPLEMENTATION)
└── models.py      - Data models (create as needed)
run.py             - Entry point (provided)
requirements.txt   - Dependencies (provided)
```

## What You Need to Implement

Check files with `TODO` and `USER IMPLEMENTATION REQUIRED` comments. Focus on implementing the routes and business logic in `app/routes.py`.

## Resources

{{LEARNING_RESOURCES}}

## Testing

You can test your API endpoints using:
- Browser for GET requests
- curl: `curl http://localhost:5000/your-endpoint`
- Postman or similar tools

## Getting Help

Review Flask documentation and make sure you understand routing, request handling, and response formatting before implementing your endpoints.
