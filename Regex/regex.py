"""

Literals: The most basic pattern, they match themselves.
Example: abc matches the string "abc".

Character Classes:

[abc]: Matches any one of the characters a, b, or c.

[a-z]: Matches any lowercase letter from a to z.

[^abc]: Matches any character that is not a, b, or c.

Predefined Character Classes:

.: Matches any single character (except newline in many engines).

\d: Matches a digit, equivalent to [0-9].

\D: Matches a non-digit, equivalent to [^0-9].

\w: Matches a word character (alphanumeric plus underscore), equivalent to [a-zA-Z0-9_].

\W: Matches a non-word character.

\s: Matches a whitespace character (space, tab, newline, etc.).

\S: Matches a non-whitespace character.

Anchors:

^: Matches the start of the string (or line in multi-line mode).

$: Matches the end of the string (or line in multi-line mode).

\b: Matches a word boundary (between a word character and a non-word character).

\B: Matches a non-word boundary.

Quantifiers:

*: Matches 0 or more of the preceding element.

+: Matches 1 or more of the preceding element.

?: Matches 0 or 1 of the preceding element (i.e., makes it optional).

{n}: Matches exactly n of the preceding element.

{n,}: Matches n or more of the preceding element.

{n,m}: Matches between n and m (inclusive) of the preceding element.

By default, quantifiers are greedy (they match as much as possible). Appending a ? makes them lazy (non-greedy), meaning they match as little as possible.

Groups and Capturing:

( ): Capturing group. Matches the pattern inside and remembers the match.

(?: ): Non-capturing group. Matches the pattern but does not remember the match.

(?<name> ): Named capturing group. Matches and stores the match under the given name.

Alternation:

|: Acts as an OR. For example, cat|dog matches "cat" or "dog".

Escape Special Characters:

Special characters like ., *, ?, etc., must be escaped with a backslash to be matched literally.

Lookaheads and Lookbehinds (Advanced):

(?= ): Positive lookahead. Asserts that the pattern inside must be ahead, but doesn't consume characters.

(?! ): Negative lookahead. Asserts that the pattern inside must not be ahead.

(?<= ): Positive lookbehind. Asserts that the pattern inside must be behind.

(?<! ): Negative lookbehind. Asserts that the pattern inside must not be behind.

Flags:

i: Case-insensitive matching.

g: Global matching (find all matches, not just the first).

m: Multi-line mode (^ and $ match start and end of each line).

s: Dotall mode (dot matches newline as well).
"""
