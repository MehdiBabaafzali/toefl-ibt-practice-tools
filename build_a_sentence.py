import webbrowser
import os
import tempfile

def generate_build_sentence_html():
    """
    Generate an interactive drag-and-drop HTML exercise for the
    TOEFL iBT 'Build a Sentence' writing task.

    HOW TO ADD YOUR OWN QUESTIONS:
    - Edit the `questions` list below.
    - Each entry needs: id, context, template, and words.
    - Use [b] in the template for each blank (one per word/phrase).
    - The word bank should contain the correct words in shuffled order,
      plus optionally one distractor word/phrase to increase difficulty.
    - See ai_prompts.md for a prompt to generate new exercises with AI.
    """

    # ----------------------------------------------------------------
    # EDIT THIS LIST to add or replace exercises.
    # Correct answers are shown in the comments above each question.
    # ----------------------------------------------------------------
    questions = [
        {
            "id": 1,
            "context": "What was the highlight of your trip?",
            # Answer: The tour guides who showed us around the old city were fantastic.
            # Distractor: "was"
            "template": "The [b] [b] [b] [b] [b] [b] fantastic.",
            "words": ["were", "the", "was", "old city", "showed us around", "who", "tour guides"]
        },
        {
            "id": 2,
            "context": "I heard Anna got a promotion.",
            # Answer: Do you know if she will be moving to a different department?
            "template": "[b] [b] [b] [b] she will be [b] [b] ?",
            "words": ["a different department", "if", "moving to", "know", "do", "you"]
        },
        {
            "id": 3,
            "context": "We're planning a trip to the mountains next weekend.",
            # Answer: Can you tell me whether the cabins will be available?
            "template": "[b] [b] tell me [b] [b] [b] [b] ?",
            "words": ["the cabins", "available", "whether", "can", "will be", "you"]
        },
        {
            "id": 4,
            "context": "I'm looking forward to the concert this weekend.",
            # Answer: What time does it start?
            "template": "[b] [b] [b] [b] [b] ?",
            "words": ["does", "what", "time", "it", "start"]
        },
        {
            "id": 5,
            "context": "The museum exhibition opens next month.",
            # Answer: Do you know how much tickets will cost?
            "template": "[b] [b] [b] [b] [b] [b] [b] ?",
            "words": ["do", "you", "how", "know", "tickets", "will cost", "much"]
        }
    ]

    # Build the HTML block for each question
    questions_html = ""
    for q in questions:
        # Replace each [b] placeholder with an empty drop zone div
        sentence_html = q["template"].replace("[b]", '<div class="drop-zone"></div>')

        # Build a draggable box for each word in the bank
        words_html = ""
        for word in q["words"]:
            words_html += f'<div class="word-item" draggable="true">{word}</div>'

        questions_html += f"""
        <div class="question-container">
            <p class="context-sentence"><b>{q['id']}. {q['context']}</b></p>
            <div class="sentence-area">
                {sentence_html}
            </div>
            <div class="word-bank">
                {words_html}
            </div>
        </div>
        <hr>
        """

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TOEFL — Build a Sentence</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                padding: 40px;
                max-width: 900px;
                margin: 0 auto;
                background-color: #f9f9f9;
                color: #222;
            }}
            .main-container {{
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            }}
            h2 {{
                margin-top: 0;
                color: #1a1a2e;
            }}
            .instructions {{
                margin-bottom: 40px;
                color: #555;
                font-size: 15px;
                background: #f1f3f5;
                padding: 12px 18px;
                border-radius: 6px;
            }}
            .question-container {{
                margin-bottom: 30px;
            }}
            .context-sentence {{
                font-size: 18px;
                margin-bottom: 15px;
            }}
            .sentence-area {{
                display: flex;
                flex-wrap: wrap;
                align-items: center;
                gap: 8px;
                font-size: 18px;
                margin-bottom: 20px;
                line-height: 2.8;
            }}
            /* Empty blank — dashed underline */
            .drop-zone {{
                display: inline-flex;
                min-width: 70px;
                height: 36px;
                border-bottom: 2px dashed #999;
                background-color: #fafafa;
                align-items: center;
                justify-content: center;
                padding: 0 6px;
                transition: background-color 0.15s, border-color 0.15s;
                border-radius: 2px;
            }}
            /* Highlight while dragging over */
            .drop-zone.drag-over {{
                background-color: #dbeafe;
                border-bottom: 2px solid #2563eb;
            }}
            /* Word bank area */
            .word-bank {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                min-height: 52px;
                padding: 14px;
                background-color: #f1f3f5;
                border-radius: 6px;
                border: 1px solid #e0e0e0;
            }}
            /* Individual word chip */
            .word-item {{
                background-color: #fff;
                border: 1px solid #ccc;
                padding: 7px 14px;
                border-radius: 4px;
                cursor: grab;
                user-select: none;
                font-size: 16px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.07);
                transition: box-shadow 0.1s;
            }}
            .word-item:active {{
                cursor: grabbing;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            }}
            /* Word chip when placed inside a drop zone */
            .drop-zone .word-item {{
                border: none;
                box-shadow: none;
                padding: 2px 6px;
                background-color: transparent;
                border-bottom: 2px solid #111;
                border-radius: 0;
                font-weight: bold;
                cursor: pointer;  /* click to return to bank */
            }}
            hr {{
                border: 0;
                height: 1px;
                background: #eee;
                margin: 40px 0;
            }}
        </style>
    </head>
    <body>
        <div class="main-container">
            <h2>Build a Sentence — TOEFL Writing Practice</h2>
            <div class="instructions">
                Drag words into the blanks to build a grammatical sentence or question.
                <br>Click a word already in a blank to return it to the word bank.
            </div>

            {questions_html}

        </div>

        <script>
            let draggedItem = null;

            // Attach drag events to a word chip
            function setupDraggable(item) {{
                item.addEventListener('dragstart', function () {{
                    draggedItem = this;
                    setTimeout(() => this.style.opacity = '0.4', 0);
                }});

                item.addEventListener('dragend', function () {{
                    setTimeout(() => {{
                        this.style.opacity = '1';
                        draggedItem = null;
                    }}, 0);
                }});

                // Clicking a word that is already in a blank returns it to the bank
                item.addEventListener('click', function () {{
                    if (this.parentElement.classList.contains('drop-zone')) {{
                        const bank = this.closest('.question-container').querySelector('.word-bank');
                        bank.appendChild(this);
                    }}
                }});
            }}

            document.querySelectorAll('.word-item').forEach(setupDraggable);

            // Attach drop events to both blank slots and the word bank
            document.querySelectorAll('.drop-zone, .word-bank').forEach(zone => {{
                zone.addEventListener('dragover', e => e.preventDefault());

                zone.addEventListener('dragenter', function (e) {{
                    e.preventDefault();
                    if (this.classList.contains('drop-zone')) {{
                        this.classList.add('drag-over');
                    }}
                }});

                zone.addEventListener('dragleave', function () {{
                    this.classList.remove('drag-over');
                }});

                zone.addEventListener('drop', function (e) {{
                    e.preventDefault();
                    this.classList.remove('drag-over');

                    if (!draggedItem) return;

                    if (this.classList.contains('drop-zone')) {{
                        // If the blank is already occupied, send the existing word back to the bank
                        if (this.children.length > 0) {{
                            const existing = this.children[0];
                            const bank = this.closest('.question-container').querySelector('.word-bank');
                            bank.appendChild(existing);
                        }}
                        this.appendChild(draggedItem);
                    }} else if (this.classList.contains('word-bank')) {{
                        this.appendChild(draggedItem);
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """
    return html_template


# Generate HTML and open it in the default browser
html_output = generate_build_sentence_html()

fd, path = tempfile.mkstemp(suffix='.html')
with os.fdopen(fd, 'w', encoding='utf-8') as f:
    f.write(html_output)

webbrowser.open('file://' + os.path.realpath(path))
print("Opened:", os.path.realpath(path))
