import os
from dotenv import load_dotenv
from crewai import Crew, Task, Agent, Process, LLM

load_dotenv()

gemini_api_key = os.environ.get("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-3.1-flash-lite",
    api_key=gemini_api_key
)


def generate_reel(reel_theme):

    content_ideator = Agent(
        role="Content Ideation Specialist",
        goal="Come up with viral, relatable reel concepts based on the user's theme for college audience",
        backstory="""
        You are an experienced social media content creator with 1M+ followers.

        You excel at turning random ideas into viral reel concepts including:

        - trending audio
        - relatable hooks
        - visual storytelling

        Keep everything authentic and relatable for Indian college students.
        """,
        llm=llm,
        verbose=True
    )

    script_writer = Agent(
        role="Reel Script Writer",
        goal="Write a complete shot-by-shot reel script",
        backstory="""
        You are a senior Instagram Reel writer.

        Always generate:

        - Hook
        - Shot breakdown
        - Timing
        - Text overlays
        - CTA
        """,
        llm=llm,
        verbose=True
    )

    engagement_optimizer = Agent(
        role="Engagement Optimizer",
        goal="Optimize the reel for maximum engagement",
        backstory="""
        You optimize:

        - Hook
        - Caption
        - Hashtags
        - CTA
        - Posting time
        """,
        llm=llm,
        verbose=True
    )

    task_ideate = Task(
        description=f"""
Take the user's reel theme: {reel_theme}

1. Create 3 viral reel concepts
2. Pick the best one
3. Suggest trending audio

Output:

## Reel Concept

- Theme
- Concept
- Format
- Audio Style
- Target Emotion
- Why It Works
""",
        expected_output="Markdown Reel Concept",
        agent=content_ideator
    )

    task_write = Task(
        description="""
Using the reel concept,

Write a complete 15-30 second reel script.

Include:

- Hook
- Shot-by-shot breakdown
- Timing
- Text overlays
- CTA
""",
        expected_output="Complete reel script",
        agent=script_writer,
        context=[task_ideate]
    )

    task_optimize = Task(
        description="""
Review the script.

Generate:

- Improved Hook
- Caption
- 20 Hashtags
- Best Posting Time
- Final Optimized Reel Package
""",
        expected_output="Optimized Reel Package",
        agent=engagement_optimizer,
        context=[task_ideate, task_write]
    )

    crew = Crew(
        agents=[
            content_ideator,
            script_writer,
            engagement_optimizer
        ],
        tasks=[
            task_ideate,
            task_write,
            task_optimize
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return result