# Crystal MARK I

Version from Aug 25, 2022
Original Repo: [https://github.com/vatdut8994/Crystal3.0.git](https://github.com/vatdut8994/Crystal3.0.git)
Superseding Version: [https://github.com/vatsaldutt/CRYSTAL-Mark-I.git](https://github.com/vatsaldutt/CRYSTAL-Mark-I.git)

**Feature Showcase**

* Part 1: [https://youtu.be/E-cjXbukcfk](https://youtu.be/E-cjXbukcfk)
* Part 2: [https://youtu.be/1XxlWatTKJw](https://youtu.be/1XxlWatTKJw)

---

## Overview

**CRYSTAL MARK I** is the first **fully integrated** CRYSTAL system where perception, embodiment, multimodal interaction, and large-language reasoning operate as a single, continuously running agent.

Unlike CRYSTAL0 (chatbot-first) and CRYSTAL-R0 (hardware-first), **MARK I is an embodied, perceptual AI** that can:

* See (camera, face recognition, gaze / eye-state detection)
* Hear (continuous listening, wake-word detection, speaker recognition)
* Speak (multilingual TTS with personality switching)
* Act (robotic arm + smart devices)
* Reason (custom ML intent model + LLM completion)
* Remember (persistent conversational memory)
* Infer **who** is speaking, **who** is being addressed, and **whether** it should respond

This version marks the shift from *assistant* → **agent**.

---

## High-Level Architecture

CRYSTAL MARK I is **always-on, multi-threaded, and multimodal**. Core subsystems run concurrently and synchronize via shared state and lightweight file-based IPC:

* **Vision Thread**

  * Face recognition
  * Gaze / eye-state detection
  * Addressee inference (is the user looking at CRYSTAL?)
* **Audio Thread**

  * Continuous live speech transcription
  * Wake-word detection
  * Speaker diarisation & authorization
* **Reasoning Thread**

  * Custom neural intent classification
  * LLM-based response synthesis
  * Contextual memory retrieval
* **Embodiment Thread**

  * Robotic arm motion primitives
  * Physical execution of language outputs
* **UI Thread**

  * PyQt5 real-time dashboard (responses, vision feedback, weather, time)

---

## Key Innovations in MARK I

### Custom Real-Time Speech Transcription (Pre-Existing APIs Didn’t Exist)

At the time, **no usable free real-time speech-to-text systems existed online**. The only comparable option was AssemblyAI, which required **paid API access**.

CRYSTAL MARK I therefore implemented a **custom live speech transcription pipeline** by:

* Converting Google’s speech recognition library to support **true real-time streaming transcription**
* Running continuously (not clip-based or push-to-talk)
* Feeding partial and finalized transcripts directly into the reasoning loop

This system was later upgraded by **replacing Google Speech Recognition with a fully local pipeline using OpenAI’s Whisper**, eliminating external dependencies while preserving real-time behavior.

---

### Speaker Diarisation & Authorization

CRYSTAL does not blindly respond to sound.

* Voice identity is continuously tracked
* Only authorized speakers (e.g., *Vatsal Dutt*) can issue commands
* Unauthorized voices trigger security responses
* Voice identity is cross-validated with **face recognition**

This enables **identity-aware interaction**, not wake-word hacks.

---

### Addressee Detection via Gaze Tracking

CRYSTAL responds only when:

* A wake word is detected **or**
* The user is visually engaged (eye contact detected)

If you’re not looking at CRYSTAL, it often won’t respond—even if it hears speech. This creates **human-like turn-taking** and eliminates accidental activations.

---

### Gesture Control via MediaPipe (Vision-Based HCI)

Using **MediaPipe hand and body tracking**, CRYSTAL MARK I supports:

* Gesture-based computer control
* Vision-triggered commands
* Hands-free interaction without speech

This makes CRYSTAL a **vision-driven human–computer interface**, not just a voice assistant.

---

### Embodied Intelligence (Robotic Arm Integration)

CRYSTAL MARK I is physically embedded in a robotic arm. Language outputs map directly to motor actions:

| Language Output | Physical Action   |
| --------------- | ----------------- |
| “forward”       | Arm moves forward |
| “back”          | Arm retracts      |
| “arm up”        | Shoulder up       |
| “wrist down”    | Wrist rotation    |
| “open / close”  | Gripper control   |

The LLM is **instruction-constrained** so physical actions remain deterministic and safe.

---

### Hybrid Intelligence Stack

CRYSTAL MARK I combines **three intelligence layers**:

1. **Neural Intent Classifier**

   * Custom bag-of-words + tflearn model
   * Handles fast, deterministic commands (volume, lights, mode switching)
2. **Rule-Based Control Logic**

   * Safety enforcement
   * Authorization
   * Hardware execution
3. **LLM Reasoning**

   * Context-aware conversation
   * Personality-driven (Jarvis-like) responses
   * Persistent conversational memory
   * Dynamic prompt construction from past interactions

---

### Massive Custom Dataset Generation

MARK I includes **custom training pipelines** that:

* Scrape and normalize **terabytes of web text**
* Extract structured conversational patterns
* Append validated interactions to a growing memory store
* Continuously expand CRYSTAL’s conversational grounding

This was an early attempt at **local LLM training**, predating ChatGPT.

---

### Multilingual, Multimodal Assistant

CRYSTAL MARK I supports:

* Real-time language switching
* Multilingual speech recognition and TTS
* Contextual translation
* Language-aware reasoning

Language can be changed dynamically via voice:

> “Crystal, speak French.”

---

### Custom PyQt5 Control Interface

The UI provides:

* Live assistant responses
* Recognized speech
* Time, date, and day
* Real-time weather (scraped + icon-rendered)
* Animated assistant visuals
* Embedded terminal for system commands

It functions as both a **monitoring console** and **control surface**.

---

## Notable Capabilities

* Continuous listening (no push-to-talk)
* Wake-word variants with phonetic robustness
* Smart device control (desk lamp via local network)
* Email and notification checking
* Web search fallback for unknown queries
* Persistent memory injection into LLM prompts
* Assistant personality switching (“Crystal” ↔ “Krish”)
* Iron Man J.A.R.V.I.S.–inspired response style

---

## Historical Significance

CRYSTAL MARK I is where CRYSTAL stopped being:

> “a chatbot with features”

and became:

> **an always-on, perceptually grounded artificial agent**

It directly informed later CRYSTAL architectures focused on:

* Stronger memory systems
* Safer embodiment
* Cleaner agent loops
* Scalable reasoning frameworks

---

## Author

**Vatsal Dutt**
Creator of CRYSTAL

---

If you want, I can make an **even more aggressive résumé / portfolio cut** or a **paper-style version** with the same zero-loss constraint.
