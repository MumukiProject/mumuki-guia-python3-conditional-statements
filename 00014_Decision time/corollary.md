`if` is  called _a control structure_ because it allows you to control the _flow_ of execution: it executes one _statement_ or the other, depending on a _condition_. In particular, the previous example can be read as:

* _`if`_ the time is **less** than 19, then return _good morning_ followed by `who`;
* _`else`_, return _good evening_ followed  by `who`.

Because of that:

* when we greet Umi at 18:00, the statement `return "Good morning " + who` is executed;
* but when we greet Pun Pun at 19:00 (:warning: 19 **is not less than** 19) the statement `"Good evening " + who` is executed.
