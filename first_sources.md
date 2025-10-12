# Sources

https://docs.x.ai/docs/guides/grok-code-prompt-engineering

https://medium.com/@TimSylvester/processes-for-better-agentic-coding-f452d4620ba8

https://github.com/tsylvester/paynless-framework/blob/main/docs/dev_plan.md

# Development Plan & Guidelines

## Development Context

This application is designed to follow these principles:
- Full separation of concerns 
- API-first architecture
- Secure, safe, reliable, robust development practices
- No code duplication (DRY)
- Dependency inversion
- Dependency injection
- Interfaces 
- Well-structured code with proper documentation
- Event-driven architecture instead of delays or timeouts
- Comprehensive logging
- Proper TypeScript typing system
- Clear organization of types and interfaces

When implementing features:
- Use dependency inversion
- Use dependency injection
- Use interfaces
- Never duplicate or replicate existing functionality
- Create reusable components that can be used across the application
- Use separation of concerns to keep files focused and maintainable
- Document all code with clear, concise comments
- Use proper TypeScript types and interfaces
- Always implement full, production-ready features rather than placeholders or mock code
- Use logging for error handling and debugging
- Use events instead of timeouts for asynchronous operations
- Scan the codebase to prevent duplication of functionality
- Follow established patterns and conventions consistently

## Branch Hygiene

- Main is the prod branch
-- This deploys to paynless.app
-- This branch must always be fully tested, stable, and working
-- No broken or incomplete features or functions
-- Main has test-mode set to false
-- Main has logging set to Error
-- Main has all relevant API keys inserted & integrations working 

- Development is the development branch. 
-- This branch is in testing for feature addition, bug fixes, etc. 
-- May have broken or incomplete features or functions
-- Dev has test-mode set to true
-- Dev has logging configured to your local prefs 
-- Dev may be missing relevant API keys 

- For new features, bug fixes, etc
-- Branch development
-- Use a folder structure that identifies your work
-- e.g. development/feature/add-[feature_name]
-- Write all unit and integration tests and run them in your branch
-- Only merge to development once your tests pass locally
-- Once the work is merged to development with working tests, we'll do E2E testing
-- Once the work passes E2E we'll merge to main (prod) and it'll be deployed
