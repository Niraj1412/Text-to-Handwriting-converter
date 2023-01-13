import pywhatkit as pw

txt="""Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances."""

pw.text_to_handwriting(txt, "handwriting.png",[0,0,138])
print(" END ")