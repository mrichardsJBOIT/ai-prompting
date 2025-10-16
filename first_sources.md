# Sources

https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

https://docs.cline.bot/prompting/cline-memory-bank

https://docs.tessl.io/introduction-to-tessl/concepts



https://docs.x.ai/docs/guides/grok-code-prompt-engineering

https://medium.com/@TimSylvester/processes-for-better-agentic-coding-f452d4620ba8

https://github.com/tsylvester/paynless-framework/blob/main/docs/dev_plan.md

https://github.com/ruvnet/claude-flow/

## Spec Drive Dev Links
https://ruv.io/projects
https://kiro.dev/docs/specs/concepts/
https://github.com/github/spec-kit
https://tessl.io/about/


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


## From [John Hubbard](https://www.linkedin.com/posts/johubbard_after-6-months-of-using-ai-coding-tools-activity-7383606814086672384-vTW9)
1. Coding LLMs are working with *small context sizes* compared to the overall challenge space of keeping tens of thousands of lines of code working from commit to commit. You MUST have the AI write tests for everything it generates. You MUST tag every working checkpoint so that it (the AI) can compare working with non-working.
2. When you tell an AI tool to "plan", you are working a different part of the model - or even potentially a completely different model - when you are telling it to "execute". "Deep thinking" models are better at analyzing code and planning than they are at executing. Sometimes even "dumb" models are better at executing to a plan than the smart ones, and they are certainly CHEAPER.
3. You MUST break planning from execution, just like you would do if you were writing the code yourself, and you must have the AI write planning files that it can follow. If you or your devs are executing plans with the most expensive models, you're almost certainly just wasting money.
4. You must AUDIT the code for every feature cycle. My "flow" is basically:
* Plan (write this as a .md file, save in plans/ directory)
* Execute (write the code)
* Write tests
* Run tests
* Re-execute as necessary until tests pass
* Audit - check the code against Plan.md

You also don't need a lot of fancy prompts to do any of this. You can literally write out your high-level goals and then have the tool write the plan, then read the plan back to you, correct its assumptions, then proceed with steps 2-6.
