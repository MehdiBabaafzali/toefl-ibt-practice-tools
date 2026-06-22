import re
import webbrowser
import os
import tempfile


def generate_ctest_html(text):
    """
    Generate an interactive HTML C-Test exercise for the
    TOEFL iBT 'Complete the Words' reading task.

    Each underscore (_) in `text` becomes a single-character input box.
    The cursor auto-advances after each keystroke, and Backspace steps back.

    HOW TO FORMAT YOUR TEXT:
    - Keep the first sentence fully intact (no underscores).
    - From sentence 2 onward, delete the second half of every other word.
    - Mark each missing letter with one underscore: _
    - Use spaces between underscores for readability: "mi_ _ _" not "mi___"
    - Exactly 10 words should have missing letters (per real TOEFL format).
    - See ai_prompts.md for a prompt to generate formatted passages with AI.
    """

    def replace_underscores(match):
        # Count underscores in this run and create one input box per missing letter
        count = match.group(0).count('_')
        return ''.join(
            '<input type="text" maxlength="1" class="ctest-char">'
            for _ in range(count)
        )

    # Match one or more underscores (spaces between them are allowed)
    pattern = r'(?:_\s*)+'
    html_content = re.sub(pattern, replace_underscores, text)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TOEFL — Complete the Words (C-Test)</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 2.0;
                font-size: 18px;
                padding: 40px;
                max-width: 820px;
                margin: 0 auto;
                background-color: #f4f4f9;
                color: #333;
            }}
            .container {{
                background-color: #fff;
                padding: 36px 44px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.09);
            }}
            h2 {{
                font-size: 20px;
                margin-bottom: 8px;
                color: #1a1a2e;
            }}
            .subtitle {{
                font-size: 14px;
                color: #666;
                margin-bottom: 28px;
            }}
            /* Each single-letter input box */
            .ctest-char {{
                width: 1em;
                border: none;
                border-bottom: 2px solid #333;
                background-color: transparent;
                font-size: 18px;
                font-family: inherit;
                text-align: center;
                outline: none;
                padding: 0;
                margin: 0 2px;
                color: #1a1a2e;
                transition: border-color 0.15s;
            }}
            .ctest-char:focus {{
                border-bottom: 2px solid #2563eb;
                background-color: #eff6ff;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Complete the Words — TOEFL Reading Practice</h2>
            <p class="subtitle">
                Fill in the missing letters. Each blank represents one letter.
                Type a letter to move to the next blank automatically.
            </p>
            <p>{html_content}</p>
        </div>

        <script>
            const inputs = document.querySelectorAll('.ctest-char');

            inputs.forEach((input, index) => {{
                // Auto-advance to next box after typing a character
                input.addEventListener('input', function () {{
                    if (this.value.length === 1 && index < inputs.length - 1) {{
                        inputs[index + 1].focus();
                    }}
                }});

                // Backspace on an empty box moves focus to the previous box
                input.addEventListener('keydown', function (e) {{
                    if (e.key === 'Backspace' && this.value.length === 0 && index > 0) {{
                        inputs[index - 1].focus();
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """
    return html_template


# ---------------------------------------------------------------
# PASTE YOUR C-TEST PASSAGE BELOW.
#
# Rules for formatting:
#   - First sentence: complete, no underscores.
#   - Every other word from sentence 2 onward: second half replaced with underscores.
#   - One underscore per missing letter. Spaces between underscores are fine.
#   - Target: exactly 10 words with missing letters.
#
# Use Prompt 2 in ai_prompts.md to generate a new passage with AI,
# then replace the text below with the AI output.
# ---------------------------------------------------------------

sample_text = (
    "We know from drawings that have been preserved in caves for over 10,000 years "
    "that early humans performed dances as a group activity. "
    "We mi_ _ _ think th_ _ prehistoric peo_ _ _ concentrated on_ _ on ba_ _ _ survival. "
    "How_ _ _ _ _, it i_ clear fr_ _ the rec_ _ _ that dan_ _ _ _ was important to them. "
    "They recorded more drawings of dances than of any other group activity. "
    "Dances served various purposes, including ritualistic communication with the divine, "
    "storytelling, and social cohesion."
)

# Generate HTML and open it in the default browser
html_output = generate_ctest_html(sample_text)

fd, path = tempfile.mkstemp(suffix='.html')
with os.fdopen(fd, 'w', encoding='utf-8') as f:
    f.write(html_output)

webbrowser.open('file://' + os.path.realpath(path))
print("Opened:", os.path.realpath(path))
