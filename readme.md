# Python
### Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability, using indentation and a clear syntax that allows developers to express concepts in fewer lines of code compared to other languages like C++ or Java.
![Python](https://www.dicsinnovatives.com/blog/wp-content/uploads/2023/08/python-blog-image.jpg)
<br>[link to image](https://www.dicsinnovatives.com/blog/wp-content/uploads/2023/08/python-blog-image.jpg)
## Advantages of Python:
1. Readability and Simplicity: Python’s clear syntax makes it easy to learn and understand, reducing maintenance costs.
2. Versatility: It’s used in diverse fields such as web development, data analysis, and automation.
3. Extensive Libraries: A rich ecosystem of libraries and frameworks accelerates development.
4. Cross-Platform: Python runs on all major operating systems.
5. Strong Community Support: Active community provides extensive resources and support.
## Disadvantages of Python:
1. Performance: Python is slower compared to compiled languages due to its interpreted nature.
2. Memory Consumption: Higher memory usage can be an issue for memory-intensive applications.
3. Weak in Mobile Computing: Less commonly used for mobile app development compared to other languages.
4. Global Interpreter Lock (GIL): Limits multi-threading performance, affecting parallel execution.
## Conclusion:
#### Python is an excellent choice for programming due to its readability, versatility, and extensive libraries. It is particularly well-suited for beginners and for tasks in data science, web development, and automation. However, its performance limitations and memory consumption should be considered when working on performance-critical applications.<br> For most use cases, Python’s advantages outweigh its disadvantages, especially for rapid development and prototyping. Its strong community support and wide adoption make it a valuable language to learn and use in various domains.
### Code Example:

```python
{
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Negative numbers not allowed.")
    else:
        print(f"Factorial of {num} is {factorial(num)}.")
except ValueError:
    print("Invalid input.")
}
