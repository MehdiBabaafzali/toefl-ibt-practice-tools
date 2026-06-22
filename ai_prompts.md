# AI Prompts for TOEFL iBT Practice

Copy any prompt below into Claude, ChatGPT, Gemini, or any AI assistant to generate exercises you can use directly with the tools in this repo or practice on your own.

> The official TOEFL iBT Technical Manual (ETS, 2025) describes every task type in full detail:
> **[Download PDF](https://rr.ets.org/index.php/etsrr/article/view/28/17)**

---

## Prompt 1 — Build a Sentence (for `build_a_sentence.py`)
Generate 5 TOEFL "Build a Sentence" exercises.
For each exercise, provide:

context: one short sentence that sets the scene (e.g., a piece of news or a situation)
answer: the complete correct target sentence
template: the answer sentence, but with every word or phrase replaced by [b]
words: all words/phrases from the template in SHUFFLED order, plus ONE extra distractor word/phrase that does not fit grammatically

Rules:

Each exercise should test a different structure: embedded question (if/whether), relative clause (who/that/which), passive voice, reported speech, or conditional
Include a mix of function words (do, you, if, whether, will) and content phrases (e.g., "the conference room", "has been scheduled")
Word bank size: 5 to 8 items per exercise
Topics: everyday campus or workplace life

Output format (Python list, ready to paste into build_a_sentence.py):
questions = [

{

"id": 1,

"context": "...",

"template": "[b] [b] [b] [b] ?",

"words": ["word1", "word2", "phrase1", "word3", "distractor"]

},

...

]
Include the correct answer as a comment above each entry.

---

## Prompt 2 — C-Test / Complete the Words (for `c_test.py`)
Write a TOEFL "Complete the Words" (C-Test) passage on the topic of: [INSERT TOPIC].
Formatting rules — follow these exactly:

The passage should be 4–6 sentences and approximately 80–100 words.
The first sentence must be completely intact — no deletions at all.
From the second sentence onward, delete the second half of every other word (words 2, 4, 6, 8 … in each sentence, counting from 1).

"second half" means: from the middle character onward
For odd-length words, delete the larger half: "people" (6 letters) → "peo_ _ _"
For 2-letter words: delete the last letter: "is" → "i_"
For 3-letter words: delete the last letter: "the" → "th_"


Mark each missing letter with exactly one underscore: _
Put a space between consecutive underscores for readability: "mi_ _ " not "mi__"
Exactly 10 words must have missing letters across the full passage.
Topic must be general knowledge — no technical jargon, no specialized field required.

Example of correctly formatted output:

"We know from drawings that have been preserved in caves for over 10,000 years that early humans performed dances as a group activity. We mi_ _ _ think th_ _ prehistoric peo_ _ _ concentrated on_ _ on ba_ _ _ survival. How_ _ _ _ , it i clear fr_ _ the rec_ _ _ that dan_ _ _ _ was important to them."
Output only the formatted passage text — nothing else. It should be ready to paste into the sample_text variable in c_test.py.

**Good topics to try:** urban farming, bioluminescence, the history of coffee, migratory birds, ancient trade routes, public libraries, the science of sleep, coral reefs, the invention of the printing press, citizen science.

---

## Prompt 3 — Read in Daily Life (multiple-choice practice)
Create one TOEFL "Read in Daily Life" exercise.
Provide:

A short text (30–120 words) that could realistically appear in one of these formats:

a social media post, an email, a campus notice, a menu, a schedule, a chain of text messages, a receipt, a flyer, or an advertisement


Two or three multiple-choice questions (A / B / C / D), each with one correct answer

Question types to include (pick 2–3):

What is the main purpose of this [text type]?
According to the [text], what must someone do to...?
What does the phrase "..." most likely mean?
What can be inferred from this [text]?
What information is NOT mentioned?

Format:

TEXT TYPE: [e.g., Campus Notice]
[text here]
QUESTIONS:

...

A) ...  B) ...  C) ...  D) ...

Answer: X — Explanation: ...
...


---

## Prompt 4 — Read an Academic Passage (multiple-choice practice)
Create one TOEFL "Read an Academic Passage" exercise.
Provide:

A short expository passage (approximately 200 words) on a topic from one of these fields: history, art and music, business and economics, life science, physical science, or social science.

No specialized background knowledge should be needed to understand it.
Write in clear, formal academic English.


Five multiple-choice questions (A / B / C / D) — one of each type:

Main idea
Factual detail
Vocabulary in context (ask what a word in the passage "most nearly means")
Inference (something implied but not directly stated)
Rhetorical purpose (why did the author include a particular sentence or example?)



Format:

PASSAGE:

[text]
QUESTIONS:

[Main idea] ...

A) ... B) ... C) ... D) ...

Answer: X
[Detail] ...

...


---

## Prompt 5 — Write an Email (practice + AI scoring)
Give me one TOEFL "Write an Email" task scenario.
The scenario should:

Describe a realistic academic or everyday situation in 2–3 sentences
State a clear writing goal: for example, making a complaint, requesting information, extending an invitation, proposing a solution, making a recommendation, or declining a request
Include any necessary context (a name, an event, a deadline) so I know exactly what to write

After you give me the scenario, I will write my email. Then I will ask you to score it.
When scoring, evaluate on these five dimensions (each out of 5, with a brief comment):

Content & elaboration — does the email clearly achieve the communicative goal?
Social conventions — is the tone, register, and politeness appropriate?
Grammar accuracy — are structures used correctly?
Vocabulary range — is word choice precise and varied?
Mechanical accuracy — spelling, punctuation, capitalization

Give an overall band score (0–5) based on the official TOEFL Write an Email rubric.

---

## Prompt 6 — Write for an Academic Discussion (practice + AI scoring)
Simulate one TOEFL "Write for an Academic Discussion" task.
Set up the scenario as follows:

Professor's post: 2–3 sentences introducing a debatable topic and ending with a direct question for students
Student A post (give a name): 3–4 sentences arguing one position clearly
Student B post (give a different name): 3–4 sentences arguing a different position clearly

Topics should be accessible and arguable, for example:

Whether universities should require students to study abroad
Whether social media should be taught as a subject in schools
Whether remote work benefits or harms career development
Whether cities should charge fees for driving in congested areas

After displaying the three posts, tell me: "Now write your contribution to the discussion."
When I submit my response, score it 0–5 using the TOEFL rubric:

Relevance and elaboration of argument
Grammar and vocabulary range
Clarity and cohesion
Mechanical accuracy

Give an overall band score with 2–3 sentences of specific feedback.


---

## Prompt 7 — Take an Interview (speaking practice via text)
Simulate a TOEFL "Take an Interview" speaking task. You are a prerecorded interviewer.
Choose a realistic scenario from one of these:

Applying for a university scholarship
Participating in a campus research study on student life
Applying for a study abroad program
Being interviewed for a student podcast on lifelong learning

Structure the interview as the real TOEFL does:

Questions 1–2: factual and personal (easy — about current habits or past experience)
Questions 3–4: opinion-based (harder — ask me to argue a position or evaluate a viewpoint)

After each of my responses (which I will type), briefly evaluate:

Did I answer the question directly?
Was my response elaborated enough?
One specific grammar or vocabulary suggestion

Then ask the next question. Start the interview now with a brief introduction of the scenario.

---

## Prompt 8 — Listen and Choose a Response (text-based)
Create 5 TOEFL "Listen and Choose a Response" exercises.
For each item:

Write a short spoken statement or question (1–2 sentences) that someone might say in a daily life or campus context
Provide four response options (A, B, C, D):

One is clearly the most appropriate response
Three are plausible but wrong (off-topic, socially inappropriate, or misunderstand the implied meaning)


State the correct answer and explain in one sentence why it is correct and why the others are not

Test a variety of communicative functions:

Responding to an invitation or suggestion
Responding to a complaint or apology
Understanding implied or indirect meaning
Recognizing appropriate social conventions
Responding to a factual question with an implied follow-up

Format:

Statement: "..."

A) ...  B) ...  C) ...  D) ...

Answer: X — Explanation: ...


**To add audio:** paste the statement text into [Natural Reader](https://www.naturalreaders.com/online/) or [TTSReader](https://ttsreader.com/) and listen before looking at the options.

---

## Prompt 9 — Listen to a Conversation (script + questions)
Write one TOEFL "Listen to a Conversation" exercise.
Provide:

A realistic dialogue script (10–14 exchanges) between two people in a university or campus setting — for example: a student and a librarian, two classmates planning a project, a student and a housing advisor, two friends discussing a lecture
Four or five multiple-choice questions (A / B / C / D) about the conversation

Question types to include:

What is the conversation mainly about?
What will [Speaker] most likely do next?
Why does [Speaker] say "..."?
What does [Speaker] imply when she/he says "..."?
According to the conversation, what is the problem / solution / requirement?

Format:

NARRATOR: Listen to a conversation.
...
QUESTIONS:

...

A) ... B) ... C) ... D) ...

Answer: X

Note: use a text-to-speech tool to convert the script to audio for realistic listening practice.

---

## Prompt 10 — Listen to an Academic Talk (script + questions)
Write one TOEFL "Listen to an Academic Talk" exercise.
Provide:

A short talk script (175–250 words) by an expert or educator. The topic should come from one of these fields: history, art and music, life science, physical science, business and economics, or social science. No specialized background knowledge should be needed.
Four or five multiple-choice questions (A / B / C / D)

Question types to include:

What is the main idea of the talk?
According to the speaker, what is the difference between X and Y?
What does the speaker imply about...?
Why does the speaker mention [example]?
What can be inferred from the talk about...?

Format:

NARRATOR: Listen to a talk on [context — e.g., a podcast, a lecture, a radio program].
SPEAKER: [script]
QUESTIONS:

...

A) ... B) ... C) ... D) ...

Answer: X

Tip: paste the script into a free TTS tool for audio — Natural Reader, TTSReader, or Google Translate (speaker icon).

---

## General Scoring Prompt (use after any writing task)
Score my response below using the official TOEFL scoring rubric for [Write an Email / Write for an Academic Discussion].
The rubric awards 0–5 points based on:

Content: does the response fully and clearly achieve the communicative goal?
Language: range and accuracy of grammar and vocabulary
Conventions: appropriate register, politeness, and organization
Mechanics: spelling, punctuation, capitalization

For each criterion, give a score and one sentence of specific feedback. Then give an overall band score and two concrete suggestions for improvement.
My response:

[PASTE YOUR WRITING HERE]
