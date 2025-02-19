<details><summary>Prerequisites & Learning Objectives</summary>

# Prerequisites and Learning Objectives for the "Use Cases For LLM" topic

## Prerequisites

- LLMs

## Learning Objectives

After completing this module, associates should be able to:

- List some common use cases for LLM
</details>

<details><summary>Description</summary>

# Description for the "Use Cases for LLM" topic

Large Language Models (LLMs) are a powerful tool for solving a variety of problems. here is a non-exhaustive list of some of the use cases for LLMs:

- Chatbots - LLMs can be used to generate responses to user input
- Content Generation - LLMs can be used to generate content such as:
    - Learning Materials
    - Essays
    - News Articles
    - Blog Posts
    - Code
- Summarization - taking a lot of text and extracting the key points
- Translation - translating text from one language to another
- Question Answering - answering questions based on some context and a question

</details>

<details><summary>Real World Application</summary>

## Real-World Application for the Use Cases For LLM Topic

LLMs have countless real-world applications that will be examined in this document. However, it is important to note that the solutions produced by LLMs are not guaranteed to be correct. It is essential to verify the correctness of this generated content before using it in a real-world application. 

### Grammatical Error Correction

LLMs can be useful in correcting grammar and spelling mistakes in some text. To test this out, we can examine some text that has many errors:

```
Wuz a dark and stormi nite wen Sir Speling Eror set out on his grate quest. His nobel steed, Horseradish, munched on a hay-bale the size of a dragon's hoard, as Sir Speling Eror adjusted his knightly helmet, made of an old colander he found in the scullery.
```

We can use, for example, ChatGPT, to correct the text. 

#### Steps
1. Navigate to https://chat.openai.com/.
2. Sign up or log in.
3. You should be greeted with a chat interface. Send a message to the chat indicating that you would like to correct some text.
    - The following text has many spelling and grammatical errors, please correct them and return the original text: "{Given Text}"
4. The chatbot should respond with the corrected text.

Feel free to change the prompt and the given text to see different results. You can also experiment with other LLMs to see how they perform.
- [Google Bard](https://bard.google.com/chat)
- [Grammarly](https://www.grammarly.com/)
- [Claude](https://claude.ai/chats)

### Code Generation
LLMs can be used to generate code. Using the same tools from above, we can try the following prompts:
- Generate some Java code for a fully encapsulated "Student" class with name, age, grade, id, GPA, and list of classes.
- Generate some Python code for a function that finds the nth Fibonacci number recursively.
- Generate some C code for a function that takes in a string and returns the string reversed.

Try these prompts or some custom prompts and make sure to verify the correctness of the generated code. You can also experiment with multiple LLMs and compare the different outputs.

#### Mistakes in Generated Code
The following code was produced via the prompt "Generate some Java code for a fully encapsulated "Student" class with name, age, grade, id, GPA, and list of classes." using Google Bard:

```java
public class Student {
  private String name;
  private int age;
  private int grade;
  private String id;
  private double gpa;
  private List<String> classes;

  public Student(String name, int age, int grade, String id, double gpa, List<String> classes) {
    this.name = name;
    this.age = age;
    this.grade = grade;
    this.id = id;
    this.gpa = gpa;
    this.classes = classes;
  }

  /*
    Some Getters and Setters Removed for Brevity
  */


  public int getGrade() {
    return grade;
  }

  public void setGrade(int grade) {
    this.grade = grade;
  }

  public String toString() {
    return "Student{" +
      "name='" + name + '\'' +
      ", age=" + age +
      ", grade=" + grade +
      ", id='" + id + '\'' +
      ", gpa=" + gpa +
      ", classes=" + classes +
      '}';
  }

  public static void main(String[] args) {
    Student student1 = new Student("Alice", 16, 10, "12345", 3.8, Arrays.asList("Math", "Science", "English"));
    System.out.println(student1);

    List<Double> grades = Arrays.asList(4.0, 3.5, 4.5);
    student1.setGpa(grades);
    System.out.println(student1.getGpa());
  }
}
```

This code has a few mistakes/notes:
- The 'setGpa' method is meant to only take in a single double as a parameter, but the code in the main method takes in a list of doubles. 
- Imports are not included in the generated code. While this isn't necessarily a mistake on the LLM's part (the imports may be implied, depending on how the prompt is worded and what context is given), it is still important to keep in mind that the generated code won't immediately work without modifications/additions.
</details>


<details><summary>Summary</summary>

# Summary for the Use Cases of LLM topic

- LLMs have many use cases such as:
    - Chatbots
    - Content Generation
    - Summarization
    - Translation
    - Question Answering
- When using LLMs for real-world applications, it is important to verify the correctness of the generated content
    - Generated Code - inspect the code, run it, and test it with unit tests to ensure that the code is correct
    - Generated Text - read the text, check for grammatical errors, check for factual errors, check for plagiarism
- LLMs are a powerful tool that can be used to solve a variety of problems as long as proper care is taken to ensure the correctness of the generated content
</details>

