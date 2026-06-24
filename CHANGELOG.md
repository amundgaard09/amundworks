# DURENDAL CHANGELOG 2026

## ICARUS

### Sunday - 07.06.2026

- Fixed circular import bugs in Vanguard - result of UniCLI importing straight from DuraPy instead of absolute import
- Fixed general upimporting bugs in DuraPy
- Fixed paths in Vanguard (AmundWorks -> Durendal)
- Removed unneccesary console messages in the MDC Pipeline / Pagefinder script
- Added Matrix struct in DuraC
- Added ROADMAP, NOTES & CHANGELOG Markdown files
- Added `execution_engine.py` and `intent_engine` to the `engines` directory for Icarus

### Monday - 08.06.2026

- Added a Vosk speech model. Vosk will serve as an offline fallback for STT. Whisper will serve as the main STT, when ICARUS is ran online.
- Added `Icarus/core/__init__.py` complete with doc-string.
- Added `entrypoint.py` as the main entrypoint for ICARUS.
- Added functional STT and TTS capabilities for ICARUS. (`communicative_engine_rev3`). Icarus can now hear and speak.
- Added a simple `process()` function for processing the input text from the `communicative_engine`. This serves as a placeholder for future integration with the two other engines.
- Added `Icarus/skills` for SKILL.md files. Still need to figure out the architechture behind it.
- Added placeholder skills for future development (`calendar_lookup`, `web_search`)
- Added `skill_template.md`. It describes the structure of the skill folders for the intent/execution engines.
- Added individual GitHub projects for each Durendal project, instead of the DuraPy project serving as the singular project for the entirety of Durendal.
- Added XO Rev. IV. This will be optimalized to serve as the FFN/MLP as part of XO Rev. V, which will be a fully featured LLM, as part of the ICARUS complex.
- Added `Icarus`/`README.md`
- Added many new issues/TODOs in the ICARUS GitHub project.
- Changed (derivative) activation functions in UniCogni to take np/cp (xp) `ndarray`s instead of floats.
- Closed a lot of issues in all github projects.
- Made the `Article` class a dataclass.
- Started work on the MCP system for ICARUS.
- Made a `MCPTool` dataclass.
- Added functions for retriveing skills from the skills directory. Not complete yet, though.

### Tuesday - 09.06.2026

- Added and finished `mcp_tool.py`, `input_schema.py` and `mcp_property.py`, all of which are dataclasses.
- Added `mcp_server_kernel.py`.
- Added `Icarus`/`README.MD`.
- Added capabilities for exiting ICARUS by speech.
- Added capabilities for speaking to ICARUS indefinetly by adding a while-loop.
- Added `timeskill.py`, the first skill. It does not yet follow the standard skill template, but will be refactored.
- Added `pyproject.toml`, and plans to add a ICARUS startup script & CLI command.
- Added dynamic paths, and removed the old hardcoded ones, to enable much more streamlined cross-platform development.
- Added `skil_loaders.py`, with the `get_py_skill()` to load the `execute()` function for each python-based skill, following the future multi-language execute-file architecture.
- Moved the comms. kernel from `communicative_engine.py` to `entrypoint.py`. which will serve as the main entrypoint to ICARUS. This will also make combining the three engines much easier.

### Wednesday - 10.06.2026

- Stopped use of hardcoded paths for good - Only Path().parents[x] ... from now on.
- Fixed path in `communicative_engine.py`.
- Added `process()` back to `communicative_engine.py` for now.
- Added `Icarus`/`logs`, with `runtime_log.txt` & `debug_log.txt`.
- Added `Icarus`/`core`/`utilities`, with `decorators.py` & `txtfiletools.py`.
- Added `@logger` to `decorators.py` for logging a function's inputs, outputs and errors, as well as `log()`, a helper function for writing to a specified log txt file - defaults to `runtime_log.txt`.
- Implemented ColorMyText, that highlights failed functions in `runtime_log.txt` as red, and successful ones as green.
- Updated `pyproject.toml`.
- Finished `execution_engine.py` Rev. 1. Routing, skill finding and skill execution now works. Full modularity as well.
- Added methods for skipping pycache (dunder) folders, so that they don't get loaded as skills and crash the system.
- Removed `process()` from `communicative_engine.py` again, and added it to `execution_engine.py`.
- Added a testing environment. (just a simple test.py file, but positioned so that all imports work correctly)

### Thursday - 11.06.2026

- Added `DAY_DEV_PLAN.md` for noting daily development plans.
- Added `match_rev2()` and a new intent engine architecture for a score-based query classification system.

### Tuesday - 16.06.2026

- Added the start of the plans for the future `Scepter` Durendal programming language.
- Added error handling to `communicative_engine.py`, for `sounddevice`.`PortAudioError` errors.
- Added functionality to the `get_time` skill. `get_time`.`execute()` is no longer a placeholder.
- Optimized some dynamic path declarations in `utilities`/`txtfiletools.py`.
- Replaced `communicative_engine.py` with `feedback_engine.py` and `perception_engine.py`. Perception will be responsible for listening and taking in terminal text inputs and Feedback will be responsible for speaking and text printing in the terminal.
- Updated ICARUS top-level init file docstring.
- Started work on the new score intent routing system.
- Started working on the ICARUS README.

### Wednesday - 17.06.2026

- Restructured the `DuraPy` folder by removing the UniPy folder and instead adding everything to /src.
- Added `coordinate_systems.py` with cartesian (1, 2 and 3 dims), spherical, cylindrical and polar coordinate systems
- Added error handling for when ICARUS is run without internet. Because of the fact that ElevenLabs TTS is the only part that needs internet, an offline-mode with only text output needs to be added.
- Fixed a lot of bugs rooted in the use of "color_dtypes.color_text()" instead of just `color_text()`.

### Friday - 19.06.2026

- Developed a semi-functional score-based intent engine, instead of the first-match system.
- Fixed import errors in DuraPy.

### Saturday - 20.06.2026

- Fixed wrong paths in toplevel README.md.
- Started work on the CLI part of Vanguard.
- Added various init-files to the ICARUS complex.
- Added a better docstring to the `Icarus`/`Core`/`engines` directory.
- Added the `EmotionMatrix` class, to be used in the future for giving ICARUS a better way to understand the user.
- Added `Response` and `Query` classes for making dialouge-related development easier.
- Major architectural updates in the engines of ICARUS.

### Sunday - 21.06.2026

- Made the UX cleaner, added optional terminal notifications controlled by a `debug` bool flag.

### Monday - 22.06.2026

- Added correct type hints to errors in `exceptions.py`.

### Tuesday - 23.06.2026

- Rewrote DuraPy functions as per the snake_case naming convention.
- Made ICARUS a class: `IcarusInstance`, and added speak(), respond() and listen() as staticmethods.
- Cleaned up toplevel init upimports.
- Updated docs (README, DuraPy.md).
- Added dunders to `Response`, `Query` and `EmotionMatrix`.
- Added `IntentResult`.
- Added `__init__` files and filled pre-existing init files with `__all__` variables.

### Wednesday - 24.06.2026

- Huge changes for `mcp_server_kernel.py`. Added functional skill loaders and registry builders.
- Removed depecrated functions and boilerplate/bloat.
- Added `ARCHITECTURE.md`, a file explaining the data flow through ICARUS with a visualization.
- Added `PRINCIPLES.md`, a description of design principles and rules regarding ICARUS.
- Removed `skill_loaders.py`, moved functions to `mcp_server_kernel.py`
- Added `intent_spec` and `IntentSpec`, for the Intent Engine.

- Added functional MCP Server and went back to the old MCP types:
  - `MCPProperty`, represents a single argument.
  - `InputSchema`, represents all arguments to a tool call
  - `MCPTool`, represents a complete skill/tool
  - `ToolCall`, represents a tool call from IntentEngine to ExecutionEngine

- Added OpenAI API for conversations with ChatGPT via ICARUS.
- Added init files and fixed preexisting ones.
