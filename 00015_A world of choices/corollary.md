As you already guessed, **order matters** :exploding_head:.

Conditions `hour < 12` and `hour < 19` **are not** _mutually exclusive_, because the first is included in the latter.  In other words, if `hour < 19` is true, then `hour < 12` is true as well. When situations like this occur, we must be careful and properly order the conditions. :nerd: