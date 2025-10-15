query = ""
original_language = "de"

prompt = f"""Translate this legal/construction question to ALL THREE languages: German, French, and Italian.
The input question is in {original_language}.
For the original language ({original_language}), keep the text mostly the same but only correct any spelling mistakes or minor grammatical errors.
For other languages, provide accurate translations while keeping legal terminology precise and maintaining the same meaning.

Examples:
- Input (de): "Welche Vorschriften gelten für Baustellen?" 
  → German: "Welche Vorschriften gelten für Baustellen?", French: "Quelles réglementations s'appliquent aux chantiers de construction ?", Italian: "Quali normative si applicano ai cantieri edili?"

- Input (fr): "Comment les compétences sont-elles réparties?"
  → German: "Wie sind die Zuständigkeiten verteilt?", French: "Comment les compétences sont-elles réparties ?", Italian: "Come sono distribuite le competenze?"

- Input (de): "Welche Vorschriftn gelten für Baustelen?" (with spelling errors)
  → German: "Welche Vorschriften gelten für Baustellen?", French: "Quelles réglementations s'appliquent aux chantiers de construction ?", Italian: "Quali normative si applicano ai cantieri edili?"

Original language: {original_language}
Question to translate: {query}"""


RESULTS_PER_LANGUAGE = 4
SUPPORTED_LANGUAGES = ["de", "fr", "it"]

"""
1. Translate into 3 languages
2. Query retriever (user hybric with semantic search)
3. Select top 4 from each language
4. Select top 4 from all 3 language
"""

LLM_MODEL = "gpt-4o"
