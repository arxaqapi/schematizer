# schematizer
A sequence to sequence machine learning model to detect specific language patterns.

## What is schematizer?
Schematizer is a machine learning model that transforms comments, comming from a comment-oriented programming language, into specific language patterns similar to regular expressions. The output of the model is then used by the [schema](https://github.com/jdrprod/schema) parser generator.

## But how?
To do so, a sequence to sequence RNN is used.

## What does it look like?
let say we have the following comment:

> let **final_sum** be the **sum** of **a1** and **a2**.

The model should output the following sequence

> let **$var** be the **$op** of **$var** and **$var**.
