### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is typically used for server-side development, scripting, and automation, while JavaScript is primarily used for client-side web development.
Python is a general-purpose language with a clear syntax, whereas JavaScript is designed for web development and has asynchronous capabilities.
Python uses indentation for code blocks, while JavaScript uses curly braces {}.
Python is an interpreted language, and JavaScript is often interpreted but can also be compiled.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
Use the get method: value = my_dict.get("c", default_value).
Use a conditional statement to check if the key exists:

if "c" in my_dict:
    value = my_dict["c"]
else:
    value = default_value


- What is a unit test?
A unit test is a type of software testing where individual units or components of a program are tested in isolation to ensure that they operate as intended. It focuses on validating that each unit of the software performs as designed.

- What is an integration test?
An integration test is a type of software testing that checks the combination of different parts or components of a system to verify their interactions. It ensures that integrated components work together correctly.

- What is the role of web application framework, like Flask?
Flask is a web application framework for Python. Its role is to provide a structure for building web applications, handling HTTP requests, managing routing, and enabling the development of dynamic web pages. Flask simplifies the process of building web applications by providing tools and abstractions.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
Use route parameters when the data is essential to the resource being requested.
Use query parameters when the data is optional or used for filtering.


- How do you collect data from a URL placeholder parameter using Flask?
Use the @app.route('/foods/<type>') decorator.
Access the data in the function as a parameter, e.g., def get_food(type):.

- How do you collect data from the query string using Flask?
Use request.args.get('param_name') to retrieve data from the query string.

- How do you collect data from the body of the request using Flask?
Use request.form.get('param_name') for form data in a POST request.
Use request.get_json() for JSON data.

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data stored on the client's machine.
Commonly used for session management, user preferences, and tracking.

- What is the session object in Flask?
In Flask, the session object is used to store user-specific information across requests.
It uses cookies to store a session ID on the client side.

- What does Flask's `jsonify()` do?
jsonify() in Flask converts a Python dictionary or other data types into a JSON response, making it suitable for use in APIs or AJAX applications. It sets the appropriate Content-Type header for JSON.
