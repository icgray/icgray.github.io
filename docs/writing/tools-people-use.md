# Tools People Actually Use

An internal tool can be technically correct and still fail.

I have seen that in research labs and industry: the analysis is valid, but the interface is painful, the setup is unclear, or the workflow assumes too much patience from the next person. When that happens, the tool quietly dies and people go back to spreadsheets, screenshots, or manual workarounds.

## Adoption is a separate problem from correctness

A correct tool that nobody runs has the same practical value as a broken one. The places where tools die are almost never the math:

- **Setup cost.** If using the tool the first time means reading three READMEs and guessing at five config values, most people will try once and give up.
- **Unclear state.** When a user cannot tell whether the tool is working, stuck, or done, they stop trusting it and stop using it.
- **Owner-only ergonomics.** Tools built for the author often encode knowledge only the author has. The second user hits a wall the author never sees.

That is why I treat the front-end as part of the engineering, not as decoration on top of it. In the shot peening project, the GUI for non-ML users was not a nicety; it was the thing that let people who would never touch a training script actually benefit from the model.

## The unglamorous details that decide it

A cleaner plot, a sensible default, one less confusing configuration step, an error message that says what to do next: any of these can matter more than a marginal algorithm improvement if the goal is adoption. The work that makes a tool *get used* is rarely the work that looks impressive in a writeup, which is exactly why it gets skipped.

I would rather ship something slightly less clever that people reach for every week than something optimal that lives in a folder no one opens. A tool's real benchmark is whether it survives contact with the second user.
