﻿#
# Copyright (c) 2015 Alexander Pruss
# L-system with turtle graphics
#

import collections
import random
from mcturtle import *

def playProgram(s, dictionary):
    for c in s:
        if c in dictionary:
            dictionary[c]()


def transform(c, t):
    if isinstance(t, str):
        return t
    else:
        r = random.random()
        for p,out in t:
            if r<p:
                 return out
            r -= p
        return c

def evolve(axiom, rules, levelCount):
    for i in range(levelCount):
        out = ""
        for c in axiom:
            if c in rules:
                out += transform(c, rules[c])
            else:
                out += c
        axiom = out
    return axiom


def lsystem(axiom, rules, dictionary, levelCount):
    out = evolve(axiom, rules, levelCount)
    playProgram(out, dictionary)

if __name__ == "__main__":
    t = Turtle()
    t.pendelay(0)
    t.penup()
    t.turtle(None)
    t.go(10)
    t.verticalangle(90)
    t.pendown()
    t.penblock(WOOD)

# a fairly simple example with rules from http://www.nbb.cornell.edu/neurobio/land/OldStudentProjects/cs490-94to95/hwchen/
#    rules = {'F':'F[-&<F][<++&F]||F[--&>F][+&F]'}
#
#    angle = 22.5
#
#    dictionary = {
#        '[': t.push,
#        ']': t.pop,
#        'F': lambda: t.go(5),
#        '-': lambda: t.yaw(-angle),
#        '+': lambda: t.yaw(angle),
#        '&': lambda: t.pitch(angle),
#        '^': lambda: t.pitch(-angle),
#        '<': lambda: t.roll(-angle),
#        '>': lambda: t.roll(angle),
#        '|': lambda: t.pitch(180)
#        }
#
#    lsystem('F', rules, dictionary, 3)


#
# A more complex example with
# rules based on http://www.geekyblogger.com/2008/04/tree-and-l-system.html
#
    rules = {'A': '^f[^^f>>>>>>A]>>>[^^f>>>>>>A]>>>>>[^^f>>>>>>A]'}

#randomized version:
#    rules = {'A': [(0.75,'^f[^^f>>>>>>A]>>>[^^f>>>>>>A]>>>>>[^^f>>>>>>A]'),
#          (0.25,'^f>>[^^f>>>>>>A]>>>[^^f>>>>>>A]')]}

    axiom = 'fA'
    angle = 15
    thickness = 8
    length = 15
    material = WOOD
    t.penwidth(thickness)
    t.penblock(material)

    stack = []
    def push():
        global length
        global thickness
        stack.append((length,thickness))
        t.push()
        thickness = thickness * 0.6
        length = length * 0.75
        if thickness < 1:
            thickness = 1
        if length <= 1:
            t.penblock(LEAVES_OAK_PERMANENT)
        t.penwidth(thickness)

    def pop():
        global length
        global thickness
        length,thickness = stack.pop()
        t.pop()

    dictionary = {
        '[': push,
        ']': pop,
        '^': lambda: t.pitch(angle),
        '>': lambda: t.roll(angle),
        'f': lambda: t.go(length)
    }

#    print evolve(axiom, rules, 11)
    lsystem(axiom, rules, dictionary, 11)