Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> color('dark turqoise')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    color('dark turqoise')
  File "<string>", line 8, in color
  File "C:\Users\edway\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2215, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Users\edway\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2704, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\edway\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 1150, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: dark turqoise
>>> forward(200)
>>> left(90)
>>> color('pink')
>>> forward(200)
>>> left(90)
>>> color('brown')
>>> forward(200)
>>> left(90)
>>> color(blue)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    color(blue)
NameError: name 'blue' is not defined
>>> color('blue')
>>> forward(200)
