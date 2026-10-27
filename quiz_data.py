QUIZ_DATA = {
    "Python": {
        "Basics": [
            {
                "question": "What is the output of print(2 ** 3)?",
                "options": ["5", "6", "8", "9"],
                "answer": 2,
                "explanation": "2 ** 3 equals 8."
            },
            {
                "question": "Which keyword defines a function in Python?",
                "options": ["function", "def", "fun", "define"],
                "answer": 1,
                "explanation": "Python uses def to define a function."
            },
            {
                "question": "Which data type stores True or False?",
                "options": ["int", "str", "bool", "list"],
                "answer": 2,
                "explanation": "The bool type represents True and False."
            },
            {
                "question": "What does len([10, 20, 30]) return?",
                "options": ["2", "3", "10", "30"],
                "answer": 1,
                "explanation": "The list contains three elements."
            },
            {
                "question": "Which symbol starts a Python comment?",
                "options": ["//", "#", "/*", "--"],
                "answer": 1,
                "explanation": "A single-line Python comment starts with #."
            }
        ],
        "Loops and Conditions": [
            {
                "question": "What is the output of print(10 % 3)?",
                "options": ["1", "3", "3.33", "0"],
                "answer": 0,
                "explanation": "The modulo operator returns the remainder. 10 % 3 is 1."
            },
            {
                "question": "Which keyword is used to skip the current loop iteration?",
                "options": ["stop", "exit", "continue", "pass"],
                "answer": 2,
                "explanation": "continue skips the remaining statements in the current iteration."
            },
            {
                "question": "What is the output of print(bool(0))?",
                "options": ["True", "False", "0", "None"],
                "answer": 1,
                "explanation": "Zero is a falsy value in Python."
            },
            {
                "question": "Which loop is commonly used to iterate over a list?",
                "options": ["repeat", "for", "foreach only", "iterate"],
                "answer": 1,
                "explanation": "A for loop iterates over the elements of a list."
            },
            {
                "question": "What does range(3) generate?",
                "options": ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3 only"],
                "answer": 1,
                "explanation": "range(3) generates 0, 1, and 2."
            }
        ]
    },

    "Java": {
        "Basics": [
            {
                "question": "Which keyword is used to create an object in Java?",
                "options": ["class", "new", "this", "object"],
                "answer": 1,
                "explanation": "The new keyword creates an object."
            },
            {
                "question": "Which method is the usual entry point of a Java application?",
                "options": ["start()", "run()", "main()", "init()"],
                "answer": 2,
                "explanation": "Execution typically begins in public static void main(String[] args)."
            },
            {
                "question": "Which type stores a whole number such as 25?",
                "options": ["boolean", "int", "char", "String"],
                "answer": 1,
                "explanation": "The int type stores integer values."
            },
            {
                "question": "Which keyword is used to inherit a class in Java?",
                "options": ["implements", "inherits", "extends", "super"],
                "answer": 2,
                "explanation": "A class uses extends to inherit another class."
            },
            {
                "question": "Which symbol ends most Java statements?",
                "options": [":", ";", ".", ","],
                "answer": 1,
                "explanation": "Most Java statements end with a semicolon."
            }
        ],
        "OOP and Collections": [
            {
                "question": "Which concept allows one interface to have different implementations?",
                "options": ["Encapsulation", "Polymorphism", "Compilation", "Iteration"],
                "answer": 1,
                "explanation": "Polymorphism allows the same interface to represent different implementations."
            },
            {
                "question": "Which collection does not allow duplicate elements?",
                "options": ["List", "ArrayList", "Set", "LinkedList"],
                "answer": 2,
                "explanation": "A Set does not store duplicate elements."
            },
            {
                "question": "Which keyword refers to the current object?",
                "options": ["super", "this", "static", "final"],
                "answer": 1,
                "explanation": "this refers to the current object."
            },
            {
                "question": "Which access modifier makes a member accessible only within its class?",
                "options": ["public", "protected", "private", "default"],
                "answer": 2,
                "explanation": "private restricts access to the declaring class."
            },
            {
                "question": "Which block is commonly used to handle an exception?",
                "options": ["try-catch", "if-else", "for-while", "switch-case"],
                "answer": 0,
                "explanation": "try-catch is used to handle exceptions."
            }
        ]
    },

    "C": {
        "Basics": [
            {
                "question": "Which function displays formatted output in C?",
                "options": ["input()", "print()", "printf()", "display()"],
                "answer": 2,
                "explanation": "printf() displays formatted output."
            },
            {
                "question": "Which header is needed for printf()?",
                "options": ["stdlib.h", "stdio.h", "string.h", "math.h"],
                "answer": 1,
                "explanation": "stdio.h declares printf() and other standard input/output functions."
            },
            {
                "question": "Which operator obtains the address of a variable?",
                "options": ["*", "&", "%", "#"],
                "answer": 1,
                "explanation": "The unary & operator obtains a variable's address."
            },
            {
                "question": "Which format specifier is commonly used for an int in printf()?",
                "options": ["%c", "%s", "%d", "%f"],
                "answer": 2,
                "explanation": "%d is commonly used to print an int."
            },
            {
                "question": "Array indexing in C starts at which index?",
                "options": ["0", "1", "-1", "Depends on the array"],
                "answer": 0,
                "explanation": "The first element of a C array has index 0."
            }
        ]
    },

    "C++": {
        "Basics": [
            {
                "question": "Which stream is commonly used for output in C++?",
                "options": ["cin", "cout", "print", "output"],
                "answer": 1,
                "explanation": "cout is the standard output stream."
            },
            {
                "question": "Which operator is used with cout to send output?",
                "options": [">>", "<<", "==", "&&"],
                "answer": 1,
                "explanation": "The insertion operator << sends data to cout."
            },
            {
                "question": "Which feature allows functions to have the same name with different parameter lists?",
                "options": ["Overloading", "Inheritance", "Encapsulation", "Abstraction"],
                "answer": 0,
                "explanation": "Function overloading uses the same name with different parameter lists."
            },
            {
                "question": "Which keyword declares a class in C++?",
                "options": ["object", "define", "class", "structclass"],
                "answer": 2,
                "explanation": "The class keyword declares a class."
            },
            {
                "question": "Which operator accesses a member through an object pointer?",
                "options": [".", "::", "->", "&"],
                "answer": 2,
                "explanation": "The arrow operator -> accesses members through a pointer."
            }
        ]
    },

    "JavaScript": {
        "Basics": [
            {
                "question": "Which keyword declares a block-scoped variable that can be reassigned?",
                "options": ["const", "let", "fixed", "define"],
                "answer": 1,
                "explanation": "let declares a block-scoped variable that can be reassigned."
            },
            {
                "question": "Which operator checks both value and type equality?",
                "options": ["=", "==", "===", "!="],
                "answer": 2,
                "explanation": "=== checks strict equality without type coercion."
            },
            {
                "question": "Which method adds an element to the end of an array?",
                "options": ["push()", "pop()", "shift()", "unshift()"],
                "answer": 0,
                "explanation": "push() adds one or more elements to the end of an array."
            },
            {
                "question": "Which function converts a JSON string into a JavaScript value?",
                "options": ["JSON.stringify()", "JSON.parse()", "JSON.convert()", "JSON.read()"],
                "answer": 1,
                "explanation": "JSON.parse() parses a JSON string."
            },
            {
                "question": "Which keyword defines a function in an arrow-function expression?",
                "options": ["function =>", "->", "=>", "::"],
                "answer": 2,
                "explanation": "The => syntax defines an arrow function."
            }
        ]
    },

    "Data Structures & Algorithms": {
        "Basics": [
            {
                "question": "Which data structure follows FIFO order?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "answer": 1,
                "explanation": "FIFO means First In, First Out, which is the behavior of a queue."
            },
            {
                "question": "Which data structure follows LIFO order?",
                "options": ["Queue", "Array", "Stack", "Graph"],
                "answer": 2,
                "explanation": "LIFO means Last In, First Out, which is the behavior of a stack."
            },
            {
                "question": "What is the time complexity of binary search on a sorted array?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1) in every case"],
                "answer": 1,
                "explanation": "Binary search halves the remaining search interval each step."
            },
            {
                "question": "Which data structure uses nodes connected by links?",
                "options": ["Linked list", "Integer", "Boolean", "Character"],
                "answer": 0,
                "explanation": "A linked list consists of nodes connected through links or pointers."
            },
            {
                "question": "Which algorithm repeatedly selects the smallest remaining element?",
                "options": ["Merge sort", "Selection sort", "Binary search", "Breadth-first search"],
                "answer": 1,
                "explanation": "Selection sort repeatedly selects the smallest remaining element."
            }
        ],
        "Algorithms": [
            {
                "question": "What is the average time complexity of merge sort?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"],
                "answer": 2,
                "explanation": "Merge sort divides the input and merges sorted halves in O(n log n) time."
            },
            {
                "question": "Which traversal visits a node before its children?",
                "options": ["Preorder", "Postorder", "Inorder", "Reverse order"],
                "answer": 0,
                "explanation": "Preorder traversal processes the node before its children."
            },
            {
                "question": "Which technique is commonly used to solve maximum subarray sum in linear time?",
                "options": ["Dijkstra's algorithm", "Kadane's algorithm", "Binary search", "Prim's algorithm"],
                "answer": 1,
                "explanation": "Kadane's algorithm solves the maximum subarray sum problem in O(n) time."
            },
            {
                "question": "Which data structure is commonly used in breadth-first search?",
                "options": ["Stack", "Queue", "Heap only", "Hash function"],
                "answer": 1,
                "explanation": "Breadth-first search uses a queue to process nodes level by level."
            },
            {
                "question": "What is the worst-case time complexity of linear search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": 2,
                "explanation": "Linear search may inspect every element, giving O(n) worst-case time."
            }
        ]
    },

    "Object-Oriented Programming": {
        "Basics": [
            {
                "question": "Which OOP concept bundles data and methods together?",
                "options": ["Encapsulation", "Recursion", "Iteration", "Compilation"],
                "answer": 0,
                "explanation": "Encapsulation combines data and methods and controls access to them."
            },
            {
                "question": "Which OOP concept represents essential features while hiding implementation details?",
                "options": ["Abstraction", "Overloading", "Sorting", "Casting"],
                "answer": 0,
                "explanation": "Abstraction exposes essential behavior while hiding implementation details."
            },
            {
                "question": "What is inheritance mainly used for?",
                "options": ["Repeating code manually", "Reusing and extending class behavior", "Deleting objects", "Sorting arrays"],
                "answer": 1,
                "explanation": "Inheritance allows a class to reuse and extend another class's behavior."
            },
            {
                "question": "What is a constructor generally used for?",
                "options": ["Initializing an object", "Destroying every class", "Sorting a list", "Importing a package"],
                "answer": 0,
                "explanation": "A constructor initializes an object when it is created."
            },
            {
                "question": "Which concept allows the same operation to behave differently for different objects?",
                "options": ["Polymorphism", "Encapsulation", "Tokenization", "Normalization"],
                "answer": 0,
                "explanation": "Polymorphism allows different object types to provide different behavior through a common interface."
            }
        ]
    },

    "DBMS": {
        "Basics": [
            {
                "question": "What does DBMS stand for?",
                "options": ["Data Backup Management Software", "Database Management System", "Digital Base Machine System", "Database Memory Service"],
                "answer": 1,
                "explanation": "DBMS stands for Database Management System."
            },
            {
                "question": "Which key uniquely identifies each row in a table?",
                "options": ["Foreign key", "Primary key", "Duplicate key", "Secondary value"],
                "answer": 1,
                "explanation": "A primary key uniquely identifies each row in a table."
            },
            {
                "question": "Which SQL command retrieves data?",
                "options": ["SELECT", "UPDATE", "DELETE", "INSERT"],
                "answer": 0,
                "explanation": "SELECT retrieves data from one or more tables."
            },
            {
                "question": "What is the main purpose of normalization?",
                "options": ["Increase duplicate data", "Reduce redundancy and update anomalies", "Delete all keys", "Make every column identical"],
                "answer": 1,
                "explanation": "Normalization organizes data to reduce redundancy and update anomalies."
            },
            {
                "question": "Which property of a transaction means it is all completed or none is applied?",
                "options": ["Consistency", "Isolation", "Atomicity", "Durability"],
                "answer": 2,
                "explanation": "Atomicity ensures a transaction is treated as an all-or-nothing operation."
            }
        ]
    },

    "Operating Systems": {
        "Basics": [
            {
                "question": "Which component manages processes and system resources?",
                "options": ["Web browser", "Operating system", "Text editor", "Compiler only"],
                "answer": 1,
                "explanation": "The operating system manages processes, memory, files, and other resources."
            },
            {
                "question": "What is a process?",
                "options": ["A program in execution", "A file extension", "A keyboard shortcut", "A database table"],
                "answer": 0,
                "explanation": "A process is a program in execution."
            },
            {
                "question": "Which scheduling algorithm uses a fixed time quantum?",
                "options": ["FCFS", "Round Robin", "Shortest Job First only", "Non-preemptive priority only"],
                "answer": 1,
                "explanation": "Round Robin assigns each process a time quantum."
            },
            {
                "question": "Which condition describes two or more processes waiting indefinitely for resources held by one another?",
                "options": ["Paging", "Deadlock", "Compilation", "Fragmentation only"],
                "answer": 1,
                "explanation": "Deadlock can occur when processes wait indefinitely for resources held by each other."
            },
            {
                "question": "Which memory management technique divides memory into fixed-size blocks called pages?",
                "options": ["Paging", "Spooling", "Scheduling", "Linking"],
                "answer": 0,
                "explanation": "Paging divides logical memory into pages and physical memory into frames."
            }
        ]
    },

    "Computer Networks": {
        "Basics": [
            {
                "question": "Which protocol is commonly used to load web pages securely?",
                "options": ["FTP only", "HTTPS", "SMTP", "ARP only"],
                "answer": 1,
                "explanation": "HTTPS secures HTTP communication using TLS."
            },
            {
                "question": "Which device forwards packets between different networks?",
                "options": ["Router", "Keyboard", "Monitor", "Printer"],
                "answer": 0,
                "explanation": "A router forwards packets between networks."
            },
            {
                "question": "How many layers are in the OSI reference model?",
                "options": ["4", "5", "7", "8"],
                "answer": 2,
                "explanation": "The OSI reference model has seven layers."
            },
            {
                "question": "Which protocol provides reliable, connection-oriented transport?",
                "options": ["UDP", "TCP", "IP", "ARP"],
                "answer": 1,
                "explanation": "TCP provides reliable, connection-oriented transport."
            },
            {
                "question": "What does DNS primarily do?",
                "options": ["Encrypt every file", "Translate domain names into IP addresses", "Create web pages", "Assign CPU time"],
                "answer": 1,
                "explanation": "DNS resolves domain names to corresponding records, commonly IP addresses."
            }
        ]
    },

    "Software Engineering": {
        "Basics": [
            {
                "question": "What does SDLC stand for?",
                "options": ["Software Development Life Cycle", "System Data Link Control", "Software Design Level Code", "Structured Digital Logic Circuit"],
                "answer": 0,
                "explanation": "SDLC stands for Software Development Life Cycle."
            },
            {
                "question": "Which activity checks whether software meets specified requirements?",
                "options": ["Testing", "Typing", "Formatting", "Browsing"],
                "answer": 0,
                "explanation": "Testing evaluates software behavior against requirements and expected results."
            },
            {
                "question": "Which development approach organizes work into short, iterative cycles?",
                "options": ["Agile", "Waterfall only", "One-time coding", "Manual deployment only"],
                "answer": 0,
                "explanation": "Agile commonly delivers work through short, iterative cycles."
            },
            {
                "question": "What is the purpose of version control?",
                "options": ["Track and manage changes to files", "Increase monitor brightness", "Replace all testing", "Remove project history"],
                "answer": 0,
                "explanation": "Version control records changes and supports collaboration."
            },
            {
                "question": "Which testing level focuses on an individual function or component?",
                "options": ["System testing", "Acceptance testing", "Unit testing", "Load testing only"],
                "answer": 2,
                "explanation": "Unit testing checks individual functions or components."
            }
        ]
    },

    "HTML": {
        "Basics": [
            {
                "question": "What does HTML stand for?",
                "options": ["HyperText Markup Language", "HighText Machine Language", "Hyper Transfer Main Link", "Home Tool Markup Language"],
                "answer": 0,
                "explanation": "HTML stands for HyperText Markup Language."
            },
            {
                "question": "Which tag creates a hyperlink?",
                "options": ["<p>", "<a>", "<img>", "<table>"],
                "answer": 1,
                "explanation": "The <a> element creates a hyperlink."
            },
            {
                "question": "Which attribute specifies an image's source?",
                "options": ["href", "src", "alt", "target"],
                "answer": 1,
                "explanation": "The src attribute specifies the image resource."
            },
            {
                "question": "Which element represents the largest standard heading?",
                "options": ["<h6>", "<head>", "<h1>", "<heading>"],
                "answer": 2,
                "explanation": "<h1> is the highest-level standard HTML heading."
            },
            {
                "question": "Which element is used to create an unordered list?",
                "options": ["<ol>", "<ul>", "<li>", "<dl>"],
                "answer": 1,
                "explanation": "The <ul> element creates an unordered list."
            }
        ]
    },

    "CSS": {
        "Basics": [
            {
                "question": "What does CSS stand for?",
                "options": ["Computer Style System", "Cascading Style Sheets", "Creative Styling Software", "Colorful Sheet Syntax"],
                "answer": 1,
                "explanation": "CSS stands for Cascading Style Sheets."
            },
            {
                "question": "Which property changes the text color?",
                "options": ["font-style", "background", "color", "text-align"],
                "answer": 2,
                "explanation": "The color property sets the foreground color of text."
            },
            {
                "question": "Which selector targets an element with id=\"header\"?",
                "options": [".header", "#header", "header*", "@header"],
                "answer": 1,
                "explanation": "The # symbol selects an element by ID."
            },
            {
                "question": "Which property controls the space inside an element's border?",
                "options": ["margin", "padding", "outline", "gap only"],
                "answer": 1,
                "explanation": "Padding is the space between content and border."
            },
            {
                "question": "Which CSS layout system is designed for one-dimensional layouts?",
                "options": ["Flexbox", "Database", "SQL", "DOM"],
                "answer": 0,
                "explanation": "Flexbox is designed primarily for one-dimensional row or column layouts."
            }
        ]
    },

    "React": {
        "Basics": [
            {
                "question": "What is React primarily used for?",
                "options": ["Building user interfaces", "Managing database backups only", "Writing operating system kernels", "Replacing HTML entirely"],
                "answer": 0,
                "explanation": "React is a JavaScript library for building user interfaces."
            },
            {
                "question": "What is a React component?",
                "options": ["A reusable part of a user interface", "A SQL table", "A network cable", "A CSS file only"],
                "answer": 0,
                "explanation": "Components are reusable building blocks of React interfaces."
            },
            {
                "question": "Which Hook is commonly used to add state to a function component?",
                "options": ["useRoute", "useState", "useClass", "useHTML"],
                "answer": 1,
                "explanation": "useState adds state to a function component."
            },
            {
                "question": "What is the purpose of props?",
                "options": ["Pass data to components", "Automatically create databases", "Style every element globally", "Compile Java code"],
                "answer": 0,
                "explanation": "Props pass data from a parent component to a child component."
            },
            {
                "question": "Why should list items have stable keys?",
                "options": ["To help React identify items between renders", "To encrypt the list", "To sort every list alphabetically", "To create CSS files"],
                "answer": 0,
                "explanation": "Keys help React identify which list items have changed, moved, or been removed."
            }
        ]
    },

    "SQL": {
        "Basics": [
            {
                "question": "Which SQL command adds new rows to a table?",
                "options": ["INSERT", "SELECT", "ALTER", "DROP"],
                "answer": 0,
                "explanation": "INSERT adds new rows to a table."
            },
            {
                "question": "Which clause filters rows based on a condition?",
                "options": ["ORDER BY", "WHERE", "GROUP BY", "SELECT"],
                "answer": 1,
                "explanation": "WHERE filters rows based on a condition."
            },
            {
                "question": "Which clause sorts query results?",
                "options": ["SORT", "ORDER BY", "ARRANGE", "FILTER"],
                "answer": 1,
                "explanation": "ORDER BY sorts query results."
            },
            {
                "question": "Which function counts rows?",
                "options": ["SUM()", "AVG()", "COUNT()", "TOTALROWS()"],
                "answer": 2,
                "explanation": "COUNT() returns the number of rows or non-NULL values, depending on its argument."
            },
            {
                "question": "Which join returns rows with matching values in both tables?",
                "options": ["INNER JOIN", "CROSS JOIN", "FULL OUTER JOIN in all cases", "No join"],
                "answer": 0,
                "explanation": "INNER JOIN returns rows that satisfy the join condition in both tables."
            }
        ]
    },

    "Aptitude": {
        "Percentages": [
            {
                "question": "What is 20% of 250?",
                "options": ["25", "40", "50", "60"],
                "answer": 2,
                "explanation": "20% of 250 = 20/100 × 250 = 50."
            },
            {
                "question": "A value increases from 100 to 120. What is the percentage increase?",
                "options": ["10%", "15%", "20%", "25%"],
                "answer": 2,
                "explanation": "Increase = 20; percentage increase = 20/100 × 100 = 20%."
            },
            {
                "question": "A product costs ₹800 and has a 10% discount. What is its discounted price?",
                "options": ["₹700", "₹720", "₹740", "₹780"],
                "answer": 1,
                "explanation": "10% of ₹800 is ₹80; discounted price is ₹720."
            },
            {
                "question": "If 40% of a number is 80, what is the number?",
                "options": ["160", "180", "200", "240"],
                "answer": 2,
                "explanation": "Number = 80 ÷ 0.4 = 200."
            },
            {
                "question": "A number decreases from 200 to 150. What is the percentage decrease?",
                "options": ["20%", "25%", "30%", "50%"],
                "answer": 1,
                "explanation": "Decrease = 50; 50/200 × 100 = 25%."
            }
        ]
    },

    "Verbal Ability": {
        "Grammar": [
            {
                "question": "Choose the grammatically correct sentence.",
                "options": [
                    "She go to college every day.",
                    "She goes to college every day.",
                    "She going to college every day.",
                    "She gone to college every day."
                ],
                "answer": 1,
                "explanation": "In the simple present tense, a third-person singular subject takes the verb form goes."
            },
            {
                "question": "Choose the correct word: Neither of the answers _____ correct.",
                "options": ["are", "were", "is", "have"],
                "answer": 2,
                "explanation": "In standard formal English, neither is generally treated as singular in this sentence."
            },
            {
                "question": "Choose the correct word: She is interested _____ learning Java.",
                "options": ["on", "at", "in", "for"],
                "answer": 2,
                "explanation": "The correct expression is interested in."
            },
            {
                "question": "Choose the correctly spelled word.",
                "options": ["Accomodation", "Accommodation", "Acommodation", "Accommadation"],
                "answer": 1,
                "explanation": "Accommodation is spelled with double c and double m."
            },
            {
                "question": "Choose the antonym of 'ancient'.",
                "options": ["Old", "Historic", "Modern", "Traditional"],
                "answer": 2,
                "explanation": "Modern is the opposite of ancient."
            }
        ]
    },

    "Logical Reasoning": {
        "Number Series": [
            {
                "question": "Find the next number: 2, 4, 8, 16, __",
                "options": ["18", "24", "30", "32"],
                "answer": 3,
                "explanation": "Each number is multiplied by 2. The next number is 32."
            },
            {
                "question": "Find the next number: 3, 6, 9, 12, __",
                "options": ["13", "14", "15", "18"],
                "answer": 2,
                "explanation": "The sequence increases by 3 each time."
            },
            {
                "question": "Find the odd one out.",
                "options": ["Apple", "Mango", "Carrot", "Banana"],
                "answer": 2,
                "explanation": "Carrot is commonly classified as a vegetable; the others are fruits."
            },
            {
                "question": "If CAT is coded as DBU by shifting each letter one step forward, how is DOG coded?",
                "options": ["EPH", "EOG", "FPH", "DPH"],
                "answer": 0,
                "explanation": "D→E, O→P, and G→H, so DOG becomes EPH."
            },
            {
                "question": "A person faces north and turns right. Which direction are they facing now?",
                "options": ["South", "East", "West", "North"],
                "answer": 1,
                "explanation": "A right turn from north points east."
            }
        ]
    }
}