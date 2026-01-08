# Crystal MARK I
Version from Aug 25, 2022\
Original Repo: https://github.com/vatdut8994/Crystal3.0.git \
Superceding version: https://github.com/vatsaldutt/CRYSTAL-Mark-I.git

**Feature Showcase**

* Part 1: [https://youtu.be/E-cjXbukcfk](https://youtu.be/E-cjXbukcfk)
* Part 2: [https://youtu.be/1XxlWatTKJw](https://youtu.be/1XxlWatTKJw)

---

## Overview

**CRYSTAL MARK I** is the first *truly integrated* version of CRYSTAL where perception, embodiment, multimodal interaction, and large-language reasoning converge into a single, continuously running system.

Unlike CRYSTAL0 and CRYSTAL-R0, which were either chatbot-first or hardware-first, **CRYSTAL MARK I is an embodied, perceptual AI system** designed to:

* See (camera + gaze detection)
* Hear (continuous listening + speaker recognition)
* Speak (TTS with personality switching)
* Act (robotic arm + smart devices)
* Reason (ML intent model + LLM completion)
* Remember (persistent conversational memory)
* Detect *who* is being spoken to and *whether* it should respond

This version represents the transition from *assistant* → *agent*.

---

## High-Level Architecture

CRYSTAL MARK I is **multi-threaded, multimodal, and always-on**.

Core subsystems run concurrently:

* **Vision Thread**

  * Face recognition
  * Gaze / eye-state detection
  * Addressee inference (is the user looking at CRYSTAL?)
* **Audio Thread**

  * Continuous speech recognition
  * Wake-word detection
  * Speaker diarisation & authorization
* **Reasoning Thread**

  * Intent classification (custom-trained neural model)
  * LLM-based response synthesis
  * Contextual memory retrieval
* **Embodiment Thread**

  * Robotic arm motion primitives
  * Physical execution of language outputs
* **UI Thread**

  * PyQt5 real-time dashboard
  * Weather, time, responses, vision feedback

All subsystems are synchronized through shared state and lightweight file-based IPC.

---

## Key Innovations in MARK I

### Speaker Diarisation & Authorization

CRYSTAL MARK I does not blindly respond to sound.

* Voice identity is continuously tracked
* Only authorized speakers (e.g. *Vatsal Dutt*) can issue commands
* Unauthorized voices trigger security responses
* Speaker identity is cross-referenced with **face recognition**

This enables **identity-aware interaction**, not just wake-word matching.

---

### Addressee Detection via Gaze Tracking

CRYSTAL responds only when:

* Wake word is detected **OR**
* The user is **visually engaged** (eye contact detected)

This eliminates accidental activations and creates **human-like conversational turn-taking**.

If you’re not looking at CRYSTAL, it often won’t respond — even if it hears speech.

---

### Gesture Control with MediaPipe (Computer Control)

Using **MediaPipe-based hand and body tracking**, CRYSTAL MARK I supports:

* Gesture-based computer control
* Vision-driven command triggering
* Hands-free interaction without speech

This allows CRYSTAL to act as a **vision-based human–computer interface**, not just a voice assistant.

---

### Embodied Intelligence (Robotic Arm Integration)

CRYSTAL MARK I is physically embedded in a robotic arm.

Language outputs can map directly to motor actions:

| Language Output | Physical Action   |
| --------------- | ----------------- |
| “forward”       | Arm moves forward |
| “back”          | Arm retracts      |
| “arm up”        | Shoulder up       |
| “wrist down”    | Wrist rotation    |
| “open / close”  | Gripper control   |

The LLM is **instruction-constrained** so that physical actions are deterministic and safe.

---

### Hybrid Intelligence Stack

CRYSTAL MARK I combines **three layers of intelligence**:

1. **Neural Intent Classifier**

   * Custom-trained model using bag-of-words + tflearn
   * Handles fast, deterministic commands (volume, lights, mode switching)

2. **Rule-Based Control Logic**

   * Safety checks
   * Authorization
   * Hardware execution

3. **Large Language Model (LLM) Reasoning**

   * Context-aware conversation
   * Personality-driven responses (Jarvis-like behavior)
   * Persistent conversational memory
   * Dynamic prompt construction from past interactions

---

### Massive Custom Dataset Generation

To support long-term intelligence growth, MARK I includes **custom training scripts** that:

* Scrape and normalize **terabytes of text data** from the web
* Extract structured conversational patterns
* Append validated interactions to a growing memory store
* Continuously expand CRYSTAL’s conversational grounding

This was an early attempt at **self-expanding knowledge pipelines**, predating modern RAG frameworks.

---

### Multilingual, Multimodal Assistant

CRYSTAL MARK I supports:

* Real-time language switching
* Speech recognition + TTS in multiple languages
* Contextual translation
* Language-aware reasoning

Language can be changed dynamically via voice:

> “Crystal, speak French.”

---

### Custom PyQt5 Control Interface

The MARK I UI displays:

* Live assistant responses
* Recognized speech
* Time, date, and day
* Real-time weather (scraped + icon-rendered)
* Animated assistant visuals
* Embedded terminal for system commands

This UI acts as both a **monitoring console** and **control surface**.

---

## Notable Capabilities

* Continuous listening (no push-to-talk)
* Wake-word variants & phonetic robustness
* Smart device control (desk lamp via local network)
* Email & notification checking
* Web search fallback for unknown queries
* Persistent memory injection into LLM prompts
* Assistant personality switching (“Crystal” ↔ “Krish”)
* Iron Man J.A.R.V.I.S.–inspired response style

---

## Historical Significance

CRYSTAL MARK I marks the moment where CRYSTAL stopped being:

> “a chatbot with features”

and became:

> **an always-on, perceptually grounded artificial agent**

This version directly influenced later CRYSTAL architectures that move toward:

* Better memory systems
* Safer embodiment
* Cleaner agent loops
* Scalable reasoning frameworks

---

## Author

**Vatsal Dutt**
Creator of CRYSTAL
