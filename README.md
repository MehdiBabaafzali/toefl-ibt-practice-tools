# toefl-ibt-practice-tools
Free, offline TOEFL iBT (2026 format) practice tools — interactive Build a Sentence and C-Test exercises with AI prompt templates for every task type. No account, no paywall.
# TOEFL iBT Practice Tools — Free & Open Source

Free, browser-based practice for the **TOEFL iBT (2026 format)**. No account, no paywall, works offline, and fully customizable. Use any AI assistant to generate unlimited new exercises.

---

## Tools Included

| File | TOEFL Task | Section |
|------|-----------|---------|
| `build_a_sentence.py` | Build a Sentence | Writing |
| `c_test.py` | Complete the Words (C-Test) | Reading |

---

## TOEFL iBT 2026 — Format Overview

The test is scored on a band scale of **1–6** per section, with an overall average. Reading and Listening are adaptive (two-stage); Writing and Speaking are linear.

| Section | Task Types | Scored Questions | Adaptive? |
|---------|-----------|-----------------|-----------|
| **Reading** | Complete the Words (C-Test); Read in Daily Life; Read an Academic Passage | 35 | Yes |
| **Listening** | Listen and Choose a Response; Listen to a Conversation; Listen to an Announcement; Listen to an Academic Talk | 35 | Yes |
| **Writing** | Build a Sentence (×10); Write an Email (×1); Write for an Academic Discussion (×1) | 12 | No |
| **Speaking** | Listen and Repeat (×7); Take an Interview (×4) | 11 | No |

> 📄 **Official Technical Manual (ETS, 2025):**
> Full test design, scoring rubrics, and validity evidence:
> **[Download PDF — TOEFL iBT Technical Manual RR-106](https://rr.ets.org/index.php/etsrr/article/view/28/17)**
> DOI: https://doi.org/10.64634/eje8f497

---

## Which Tasks Can You Simulate with AI?

The majority of TOEFL tasks can be replicated for free using any AI assistant (Claude, ChatGPT, Gemini, etc.). See `ai_prompts.md` for ready-to-copy prompts for every task type.

| Task | AI-Simulatable? | Notes |
|------|----------------|-------|
| Complete the Words (C-Test) | ✅ Yes — use `c_test.py` | Paste AI output into the script |
| Build a Sentence | ✅ Yes — use `build_a_sentence.py` | Paste AI output into the script |
| Read in Daily Life | ✅ Yes | AI generates text + multiple-choice questions |
| Read an Academic Passage | ✅ Yes | AI generates passage + 5 questions |
| Write an Email | ✅ Yes | AI gives scenario; you write; AI scores using rubric |
| Write for an Academic Discussion | ✅ Yes | AI role-plays professor + students; you contribute |
| Take an Interview | ✅ Yes | AI role-plays as the interviewer |
| Listen and Choose a Response | ⚠️ Partial | Use the text version; or paste into a TTS tool |
| Listen to a Conversation | ⚠️ Partial | AI generates script; use a TTS tool for audio |
| Listen to an Announcement | ⚠️ Partial | Same approach |
| Listen to an Academic Talk | ⚠️ Partial | Same approach |
| Listen and Repeat | ⚠️ Partial | Use TTS; record yourself and compare |

> **Free TTS tools for listening practice:** [Natural Reader](https://www.naturalreaders.com/online/), [TTSReader](https://ttsreader.com/), [Google Translate](https://translate.google.com) (paste text → click speaker icon)

---

## Requirements

- **Python 3.x** — no additional libraries needed (uses only built-in modules)
- A modern web browser (Chrome, Firefox, Safari, Edge)

---

## Quick Start

**Step 1** — Clone or download this repository.

python build_a_sentence.py
```

**Step 2** — Run either tool from your terminal:

```bash
```bash
python c_test.py
```

The script generates an HTML file and **opens it automatically in your browser**. No server needed — it runs completely offline.

---

## How to Customize — Build a Sentence

Open `build_a_sentence.py` and edit the `questions` list at the top of the file.

Each question needs three things:

```python
{
    "id": 1,
    # The context sentence shown in bold above the exercise
    "context": "I heard the lecture was really interesting.",
    # The target sentence with [b] in place of each word or phrase
    # Number of [b] = number of correct words in the bank (distractors are extra)
    "template": "[b] [b] [b] [b] [b] the topic [b] ?",
    # Word bank — shuffled; include one distractor to make it harder
    "words": ["do", "you", "know", "whether", "covered", "was", "will be"]
}
```

**Answer** for the example above: *Do you know whether the topic was covered?*
("will be" is the distractor.)

Use the prompts in `ai_prompts.md` → **Prompt 1** to generate new question sets with AI, then paste them directly into this list.

---

## How to Customize — C-Test (Complete the Words)

Open `c_test.py` and replace the `sample_text` string near the bottom of the file.

Mark each missing letter with a single underscore `_`. Use spaces between underscores for readability.

**Real TOEFL C-Test rules (from the Technical Manual):**
- The first sentence is always kept **fully intact**
- Starting from sentence 2, the **second half of every other word** is deleted
- Exactly **10 words** have missing letters per passage
- Each passage is self-contained with no required background knowledge

**Example format:**
