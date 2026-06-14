# Small Scripts Worth Keeping

Some of the most valuable code in a technical workspace is not the flagship repository. It is the small script that saves an hour every week.

A plotting helper, a log converter, a benchmark wrapper, a deployment shortcut, a quick visualizer for a strange dataset: these are easy to dismiss because they look modest. But over time they become the glue between projects. They also show how someone thinks when no one is asking for a polished product.

## Why the small ones compound

A flagship project is used intensely for a while and then mostly maintained. A good utility is used a little, constantly, for years. The racecar benchmark only stayed honest because of unglamorous helpers around it: log matchers, trajectory plotters, session validators. None of those would headline a portfolio, and all of them were load-bearing.

The small tools also encode hard-won knowledge in a reusable form. A converter that handles the three weird edge cases in a log format is, in practice, a written record of every time that format bit me. Throwing it away means relearning those edge cases the next time.

## What makes one worth keeping

Not every one-off deserves to survive. The ones that do tend to share a few traits:

- they do **one** thing and have an obvious name,
- they run with no setup ritual,
- and they fail loudly instead of producing quietly wrong output.

A script with those properties graduates from "thing I wrote once" to "thing I reach for," and that is the whole difference.

I want this site to have room for those smaller pieces. Not every good engineering artifact is a startup-sized application. Sometimes the best code is the sharp little tool that keeps the rest of the work moving.
