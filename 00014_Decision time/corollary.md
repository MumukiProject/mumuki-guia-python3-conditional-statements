`if` is  called _a control structure_ because it allows you to control the _flow_ of execution: it executes one _statement_ or the other, depending on a _condition_. In particular, the previous example can be read as:

* _`if`_ the time is **less** than 19, then return _good morning_ followed by `name`;
* _`else`_, return _good evening_ followed  by `name`.

Because of that:

* when we greet Umi at 6:00 p.m., the statement `return "Good morning " + who` is executed;
* but when we greet Pun Pun at 7:00 p.m. (:warning: 19 **is not less than** 19) the statement `"Good evening " + who` is executed.
