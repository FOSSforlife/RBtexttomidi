# RBtexttomidi - Convert text string to Rock Band MIDI notes

README updated 2017-02-25

This software will convert any text string into guitar and bass notes in REAPER for Rock Band customs. To add the script to your REAPER installation, download RBtexttomidi.py and open it using "Show Actions List" -> "Reascript - Load" (the same way you would add CAT). Make sure you have Python installed (if you've already used CAT, you're good).

Right now, it only works in REAPER 5, which I know isn't helpful for most people in the customs community. I'm working on making it compatible with REAPER 4 in the near future.

###How to write/format the text string:
It will read from left to right (just like the MIDI editor), with each digit representing one 16th note spot.
* 1 = Green note
* 2 = Red note
* 3 = Yellow note
* 4 = Blue note
* 5 = Orange note
* x = Rest
* "-" = Extend note (make sure this is followed with an x or another note)

For example, if I wanted one green, then one red, then a long yellow note:
123--x
(1 and 2 will be 16th notes, and 3 will be the duration of three 16th notes)

Another example, if I want an 8th note rhythm:
3x3x4x5x5x4x3x2x1x1x2x3x2x1x1

Quarter notes:
3xxx4xxx5xxx4xxx3xxx2xxx1xxx

Quarter notes, sustained:
3--x4--x5--x4--x3--x2--x1--x

### Reading text input

Right now the only way to input the text string is to edit the code and call the function addNotesFromStr(), as exemplified in the main function. Soon you will be able to input from a text file, and once I develop a GUI you will be able to just type it into REAPER.

### Upcoming features
- REAPER 4 compatibility
- File input
- Simultaneous notes (green-red, green-yellow, etc)
- GUI (with settngs configuration)
- Convert notes to text string (opposite of what it does now)
