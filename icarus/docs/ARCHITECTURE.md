# ICARUS Complex Pipeline

## Classes

### Query

### Response

### EmotionMatrix

### IntentSpec

### IntentResult

## Responsibilities

### MCP Server & Skill Directory

- The MCPS and Skill Directory co-operate to manage the creation, storage, loading and utilization of skills.
- The MCPS loads the skills into two maps, the [IntentRegistry](#intentregistry) and the [ExecutionRegistry](#executionregistry).

### Perception Engine

- Captures real world data from microphones, sensors and cameras.
- Converts speech to text using `Vosk`.
- Converts text into [Query](#query) objects.
- Converts sensor data and camera data to ??? using ??? and OpenCV.
- The main function is `listen()`, which returns a Query-object.

### Intent Engine

- Processes [Query](#query) objects into [IntentResult](#intentresult) objects.

// Classifier System???

- Classifies the intent into: ????
  - Informational (Web Search + Vanguard + other skills)
  - Calculational (DuraPy + other skills)
  - Navigational (Skills)

### Execution Engine

- Uses [IntentResult](#intentresult) and the [ExecutionRegistry](#executionregistry) to execute a function.
- Returns a [Response](#response) object.

### Feedback Engine

- Uses [Response](#response) objects to return data to the user.
- Speaks via `ElevenLabs`.

### IntentRegistry

- A dict of skill names as keys and [IntentSpec](#intentspec) as values.

### ExecutionRegistry

- A dict of skill names as keys and Callables as values

## Complete Diagram

```markdown THIS IS WRONG! ! !! !!
Microphone──────►`listen()`  
                     ▼  
Vosk───────1.──┬─►STT Multiplexer  
Whisper─────2.─┤     ▼  
Fast-Whisper─3.┘  `Query` Intent Engine
                     │          ▼
┌─►`IntentRegistry`──┴─►`process(Query)`─►`ToolCall`─┐  
│                                                    ▼  
├─►`ExecutionRegistry`─────────────────►`respond(ToolCall)`────►`Response`─────►`speak(Response)`  
│                                                ▲                   ▲                  ▲  
└─`build_registries( )`                  Execution Engine   core/types/response  Feedback Engine  
                    ▲  
MCP Server Kernel───┤  
Skill Directory─────┘
```

│─
┌ ┐└ ┘
┬ ┴ ├ ┼ ┤
►▼▲◄  
